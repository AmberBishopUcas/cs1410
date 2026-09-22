#this file is used to build nural networks, and to process information within them.
from matrix_handling import create_matrix, get_file_path, randomise_matrix
import os
from math import exp as e

def build_network(layer_list):
    network = {}
    for i in range(len(layer_list)):
        layer = create_matrix(layer_list[i], 2)
        network[i] = layer
    return network


def create_weight_matricies(network):
    weights = {}
    for i in range(len(network) - 1):
        weights[i] = create_matrix(len(network.get(i)), len(network.get(i + 1)))
    return weights


def save_network_to_file(network, filename):
    with open(get_file_path(filename), "w") as file:
        for layer_index, matrix in network.items():
            file.write(f"layer {layer_index}\n")
            for row in matrix:
                file.write("[" + ", ".join(str(value) for value in row) + "]\n")
            file.write("\n")


def load_network_from_file(filename):
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
    if layer_number <= 0:
        if layer_number == 0: 
            raise ValueError("You cannot calculate the first layer, it takes inputs")
        elif layer_number < 0:
            raise ValueError("You cannot calculate a layer below 1")
    for i in range(len(network[layer_number])):
        layer = 0
        for j in range(len(network[layer_number-1])):
            layer += (network[layer_number-1][j][0]*weights[j][i])
        layer += network[layer_number][i][1]
        if layer < 0 and layer_number < len(network):
            layer = 0
        network[layer_number][i][0] = layer
    return network

def softmax(network):
    final_layer = len(network)-1
    outputs = []
    for i in range(len(network[final_layer])):
        outputs.append(network[final_layer][i][0])
    for nuron in outputs:
        nuron = e(nuron)
    for nuron in outputs:
        output = 0
        nuron/sum(outputs)
        if nuron/sum(outputs) > output:
            output = nuron
    return outputs.index(nuron)



def calculate_network(network, weights):
    for layer_number in range(1, len(network)):
        calculate_layer(layer_number, network, weights[layer_number - 1])
    output_nuron = softmax(network)
    return network, output_nuron



def test_network():
    print("Starting network test")

    network = build_network([2, 3, 1])
    print("Built network:", network)

    weights = create_weight_matricies(network)
    print("Created weight matrices:", weights)

    for layer_number, layer in network.items():
        randomise_matrix(layer)
        print(f"Randomized network layer {layer_number}: {layer}")
        assert all(-0.1 <= value <= 0.1 for row in layer for value in row)
        print(f"Layer {layer_number} values are in range")

    for weight_number, weight_matrix in weights.items():
        randomise_matrix(weight_matrix)
        print(f"Randomized weight matrix {weight_number}: {weight_matrix}")
        assert all(-0.1 <= value <= 0.1 for row in weight_matrix for value in row)
        print(f"Weight matrix {weight_number} values are in range")

    print("Checking network dimensions")
    assert [len(layer) for layer in network.values()] == [2, 3, 1]
    assert [len(weight_matrix) for weight_matrix in weights.values()] == [2, 3]
    assert [len(weight_matrix[0]) for weight_matrix in weights.values()] == [3, 1]
    print("Network dimensions are correct")

    test_network_data = {
        0: [[2, 0], [3, 0]],
        1: [[0, 1], [0, 2]],
    }
    test_weights = {0: [[4, 5], [6, 7]]}
    print("Deterministic network before calculation:", test_network_data)
    print("Deterministic weights:", test_weights)
    calculate_layer(1, test_network_data, test_weights[0])
    print("Deterministic network after calculation:", test_network_data)
    assert test_network_data[1] == [[27, 1], [33, 2]]
    print("Forward calculation is correct")

    softmax_network = {
        0: [[0, 0]],
        1: [[1, 0], [2, 0], [3, 0]],
    }
    print("Softmax logits before calculation:", softmax_network[1])
    selected_nuron = softmax(softmax_network)
    probabilities = [neuron[0] for neuron in softmax_network[1]]
    print("Softmax probabilities:", probabilities)
    print("Selected output neuron:", selected_nuron)
    assert all(probability >= 0 for probability in probabilities)
    assert abs(sum(probabilities) - 1) < 1e-9
    assert selected_nuron == 2
    assert probabilities[0] < probabilities[1] < probabilities[2]
    print("Softmax calculation is correct")

    return True


if __name__ == "__main__":
    test_network()
    print("Network test passed")
