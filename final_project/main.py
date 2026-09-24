# Project entry point for the neural language-model experiment.
# This file is intended to coordinate token processing, network construction,
# and future training runs, but the implementation is still in progress.
import os

from csv_handling import csv_to_list
from matrix_handling import randomise_matrix
from nural_net_handling import build_network, calculate_network, create_weight_matricies
from token_handling import chunk_to_sentence, chunk_to_tokens, sentence_to_chunks, token_to_chunk


def main():
    """Placeholder main routine showing the intended project flow."""
    nurons = [5, 2, 5, 7, 8, 5, 5]
    # define the size of each layer in the network: input -> hidden -> output
    network = build_network(nurons)
    # create the matrix of weights that connects every layer to the next one
    create_weight_matricies(network)
    # this loop is a placeholder for the future training and token-processing workflow
    for i in range(len(nurons)):
        pass


if __name__ == "__main__":
    main()
