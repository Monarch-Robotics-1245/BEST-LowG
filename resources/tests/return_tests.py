import random

import pytest
import itertools

import src.main

def test_remaining_return():
    zero_params = []
    for i in range(48):
        zero_params.append(0)
    zero_params = tuple(zero_params)


    # Define the range of values
    values = range(-127, 128)  # from -127 to 127, inclusive

    sample_size = 1000000  # Adjust this to any reasonable number for sampling

    for _ in range(sample_size):
        # Generate a random combination of 8 parameters
        combination = tuple(random.randint(-127, 127) for _ in range(8))

        result = src.main.robot(*combination, *zero_params)
        result = list(result)
        for i in range(len(result)):
            if i > 7:
                result.pop(8)
        result = tuple(result)


        # Check if the expected condition holds true for the specific spot
        # For example, let's check if the first value in the result is equal to 0
        if combination[0] == 0:
            assert result[0] == 0  # Adjust this condition as needed
