# Backpropagation is the training method used to adjust weights based on the
# error between a model's output and the target answer.
# In a neural network, each weight is nudged in the direction that reduces loss,
# which lets the model learn from examples over time.
# The formula below reflects the general idea behind the gradient calculation:
# (W^T_next × Error_next) ⊙ g'(z)
# This is a core concept for training large language models and other neural nets.
from matrix_handling import matrix_transpose as transpose, create_matrix
