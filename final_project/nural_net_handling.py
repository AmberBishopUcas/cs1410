#this file is used to build nural networks, and to process information within them.
from matrix_handling import create_matrix, get_file_path
import os

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
            ValueError("You cannot calculate the first layer, it takes inputs")
        elif layer_number < 0:
            ValueError("You cannot calculate a layer below 1")
    layer = 0
    for i in range(len(network[layer_number])):
        for j in range(len(network[layer_number-1])):
            layer += (network[layer_number-1][j][0]*weights[j][i])
        layer += network[layer_number][i][1]
        network[layer_number][i][0] = layer
    return network

def calculate_network(network, weights):
    for layer in network:
        calculate_layer(len(layer), weights)
    return network


if __name__ == "__main__":
    layers = [8, 7, 6, 5, 4, 3, 2, 1]
    network = build_network(layers)
    #print(create_weight_matricies(network))
    print((network[1][1][1]))
    print((network[1][1]))
    print((network[1]))