#this file is used to build nural networks, and to process information within them.
from matrix_handling import create_matrix

def build_network(layer_list):
    network = {}
    for i in range(len(layer_list)):
        layer = create_matrix(layer_list[i], 2)
        network[i] = layer
    return network

def create_weight_matricies(network):
    weights = {}
    for i in range(len(network)-1):
        weights[i] = create_matrix(len(network.get(i)), len(network.get(i+1)))
    return weights

def save_network_to_file(file):
    pass

layers = [8,7,6,5,4,3,2,1]
network = build_network(layers)
print(create_weight_matricies(network))
