# Project entry point for the neural language-model experiment.
# This file is intended to coordinate token processing, network construction,
# and future training runs, but the implementation is still in progress.

from math import isclose

from back_propogation import find_layers_errors, get_g, get_output_error


def test_back_propogation():
	network = {
		0: [[1, 0], [0, 0]],
		1: [[2, 0], [0, 0]],
		2: [[0, 0], [0, 0]],
	}
	weights = {
		0: [[0.1, 0.2], [0.3, 0.4]],
		1: [[0.2, 0.4], [0.5, 0.6]],
	}

	activation_mask = get_g(network)
	assert activation_mask[1] == [[1], [0]]

	output_error = get_output_error(network, expected_token=1)
	assert all(isclose(actual, expected) for actual, expected in zip(
		[row[0] for row in output_error], [0.5, -0.5]
	))

	layer_errors = find_layers_errors(network, weights, expected_token=1)
	assert all(isclose(actual, expected) for actual, expected in zip(
		[row[0] for row in layer_errors[1]], [-0.1, 0]
	))
	assert layer_errors[2] == output_error

	print("Backpropagation tests passed.")


if __name__ == "__main__":
	test_back_propogation()
