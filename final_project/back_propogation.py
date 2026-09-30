# Backpropagation is the training method used to adjust weights based on the
# error between a model's output and the target answer.
# In a neural network, each weight is nudged in the direction that reduces loss,
# which lets the model learn from examples over time.
# The formula below reflects the general idea behind the gradient calculation:
# (W^T_next × Error_next) ⊙ g'(z)
# This is a core concept for training large language models and other neural nets.
from matrix_handling import matrix_transpose as transpose, matrix_multiplication as multiply, hadamard_product as hadamard, create_matrix
from nural_net_handling import softmax

def get_g(network):
    g = {
    }
    for i in range(len(network)):
        #network is all layers of the network
        g[i] = create_matrix(len(network[i]), 1)
        #network[i] is all the nurons on layer i
        for j in range(len(network[i])):
            if network[i][j][0] != 0:
                #network[i][j][0] is nuron j on layer i, 0 means its the weight, 1 means its the bias
                g[i][j][0] = 1
    return g

def get_output_error(network, expected_token):
    output_layer = softmax(network)
    error = create_matrix(len(output_layer), 1)

    for i, output in enumerate(output_layer):
        target = 1 if i == expected_token else 0
        error[i][0] = output - target

    return error

def find_layers_errors(network, weights, expected_token):
    matrix_mask = get_g(network)
    error = {}
    output_index = len(network) - 1
    error[output_index] = get_output_error(network, expected_token)
    for i in range(output_index -1, 0, -1):
        error[i] = hadamard(
            multiply(weights[i], error[i + 1]), 
            matrix_mask[i],
        )
        
    return error