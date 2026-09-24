# Neural-network layer utilities used to build and evaluate a small model.
# Each layer is stored as a matrix-like structure so the project can apply simple
# feed-forward computations in a compact, matrix-based way.
from matrix_handling import create_matrix, get_file_path, randomise_matrix
from math import exp as e


def build_network(layer_list):
    """Create a network dictionary where each layer is represented as a matrix."""
    network = {}
    for i in range(len(layer_list)):
        # each layer stores one value and one bias-style slot per neuron
        layer = create_matrix(layer_list[i], 2)
        network[i] = layer
    return network


def create_weight_matricies(network):
    """Initialize one weight matrix between each pair of adjacent layers."""
    weights = {}
    for i in range(len(network) - 1):
        # weight matrix connects layer i to the next layer
        weights[i] = create_matrix(len(network.get(i)), len(network.get(i + 1)))
    return weights


def save_network_to_file(network, filename):
    """Write a network structure to disk in a human-readable layer-by-layer format."""
    with open(get_file_path(filename), "w") as file:
        for layer_index, matrix in network.items():
            file.write(f"layer {layer_index}\n")
            for row in matrix:
                file.write("[" + ", ".join(str(value) for value in row) + "]\n")
            file.write("\n")


def load_network_from_file(filename):
    """Reconstruct a saved network from the text format written by save_network_to_file."""
    network = {}
    with open(get_file_path(filename), "r") as file:
        current_index = None
        current_layer = None

        for line in file:
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("layer "):
                if current_index is not None and current_layer is not None:
                    network[current_index] = current_layer
                current_index = int(stripped.split()[1])
                current_layer = []
                continue

            if stripped.startswith("[") and stripped.endswith("]"):
                row = [float(value.strip()) for value in stripped.strip("[]").split(",") if value.strip()]
                current_layer.append(row)

        if current_index is not None and current_layer is not None:
            network[current_index] = current_layer

    return network


def calculate_layer(layer_number, network, weights):
    """Compute one layer's activations from the previous layer and the weight matrix."""
    if layer_number <= 0:
        if layer_number == 0:
            raise ValueError("You cannot calculate the first layer, it takes inputs")
        elif layer_number < 0:
            raise ValueError("You cannot calculate a layer below 1")
    for i in range(len(network[layer_number])):
        layer = 0
        for j in range(len(network[layer_number - 1])):
            # combine each previous neuron's value with the matching weight for this neuron
            layer += (network[layer_number - 1][j][0] * weights[j][i])
        # add the bias term for this neuron before activation
        layer += network[layer_number][i][1]
        if layer < 0 and layer_number < len(network):
            # simple ReLU-style clamp to keep negative values from propagating
            layer = 0
        network[layer_number][i][0] = layer
    return network


def softmax(network):
    """Convert the final layer values into a probability distribution."""
    final_layer = len(network) - 1
    network_outputs = []
    softmax_result = []
    for i in range(len(network[final_layer])):
        # store the raw score from each output neuron
        network_outputs.append(network[final_layer][i][0])
    for i in range(len(network_outputs)):
        # exponentiate to turn scores into positive values for probability-style weighting
        network_outputs[i] = e(network_outputs[i])
    total_output = sum(network_outputs)
    for nuron in network_outputs:
        # normalize so all outputs sum to 1 and represent likelihoods
        softmax_result.append(nuron / total_output)
    return softmax_result


def calculate_network(network, weights, inputs):
    """Run one full forward pass through the network using the provided input values."""
    if len(inputs) > len(network[0]):
        print("warning inputs exceed amount of input nurons...\ncutting off excess inputs")
    for i in range(len(network[0])):
        # place the input values into the first layer of neurons
        network[0][i][0] = input[i]
    for layer_number in range(1, len(network)):
        # move forward one layer at a time using the weight matrix from the previous layer
        calculate_layer(layer_number, network, weights[layer_number - 1])
    output_nuron = softmax(network)
    return network, output_nuron