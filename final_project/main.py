#welcome, and be amazed. this is a small 
# LLM made entirely from scratch! Zero imports* 

#*by imports i mean no pip installs, importing 
# from other files, and internal python modules 
# like os and random are fine, but no external 
# libraries like numpy or pandas.
from matrix_handling import create_matrix, randomise_matrix, save_matrix, load_matrix, hadamard_product, matrix_multiplication
from byte_pair_encoding import main as bpe_main

#bpe_main()  # Run the byte pair encoding process to update the vocabulary