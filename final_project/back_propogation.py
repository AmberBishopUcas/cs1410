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
                g[i][j] = 1
    return g

def get_output_error(network, expected_token):
    output_layer = softmax(network)
    expected_output_layer = []
    error = []
    for i in range(len(output_layer)):
        if i == expected_token:
            expected_output_layer.append(1)
        else:
            expected_output_layer.append(0)
    for i in range(len(output_layer)):
        error.append(output_layer[i] - expected_output_layer[i])
    return error

def find_layers_errors(network, weights, expected_token):
    matrix_mask = get_g(network)
    error = {
    }
    get_output_error(network, expected_token)
    error[len(network)-1] = get_output_error(network, expected_token)
    for i in range(len(network) - 1, 0, -1):
        error[i] = hadamard(multiply(transpose(weights[i + 1]), error[i + 1]), matrix_mask[i])
    return error


#Before `find_layers_errors` can compute backprop deltas, fix these issues:

1. #**Make the backward loop actually count downward.** 
#`range(len(network) - 1, -1)` uses the default positive 
# step, so the loop never runs.
2. #**Use one layer-index convention.** Store the output 
#delta at the actual output layer index, `len(network) - 1`, 
# then calculate earlier layer deltas from there. `len(network)` 
# is past the last layer.
3. #**Index the connection weights correctly.** `weights[k]` 
#connects layer `k` to layer `k + 1`. For a delta at layer `k`, 
# multiply `transpose(weights[k])` by the delta at layer `k + 1`. 
# The current `weights[i] + 1` expression is not valid indexing.
4. #**Use the mask for the layer being calculated.** `get_g(network)` 
#returns a dictionary of masks, so use the mask for that specific 
# layer rather than the whole dictionary.
5. #**Fix how `get_g` fills each mask.** Each mask entry is a 
#one-cell row, but `g[i][j] = 1` replaces that row with a number. 
#Set the value inside the row instead, so the mask remains a 2D 
# column matrix.
6. #**Keep the dimensions consistent.** `get_output_error` 
#returns a 1D list, but your multiplication and Hadamard 
# helpers expect 2D matrices. Represent each layer’s delta 
# and mask as a column matrix with one row per neuron.
7. #**Choose where the input layer stops.** Usually you calculate 
#deltas for hidden layers, not the input layer, because inputs have 
# no activation derivative in this network.
8. #**Account for the output activation.** Your forward pass applies 
#ReLU to the final layer before softmax. Either include that ReLU 
# derivative in the output delta, or remove ReLU from the final layer 
# and use its values as logits.

#Also validate that `expected_token` is a valid output index. 
# The output delta calculation itself is reasonable for softmax 
# with cross-entropy; most of the work is getting `find_layers_errors`’ 
# indexing, masks, and matrix shapes consistent.