
import pytest
import unittest
import sys
from practice import pizza_box, get_output_from_pizza_box, get_input

class TestPizzaBox(unittest.TestCase):
    def test_pizza_box(self):
        capacity, pizza_types = get_input("a_example.in")
        print("input:\n{}\n{}".format(capacity, pizza_types))
        actual_number_of_pizza_types, actual_types_to_order = get_output_from_pizza_box(
            capacity,
            pizza_types,
            pizza_box(capacity, pizza_types)
        )
        expected_number_of_pizza_types, expected_types_to_order = get_expected_output("a_example.out")

        print("\noutput:\n{}\n{}".format(actual_number_of_pizza_types, actual_types_to_order))
        print("\nexpected:\n{}\n{}".format(expected_number_of_pizza_types, expected_types_to_order))

        assert actual_number_of_pizza_types == expected_number_of_pizza_types
        assert actual_types_to_order == expected_types_to_order

def get_expected_output(file_name):
    number_of_pizza_types = None
    types_to_order = None
    with open(file_name) as descriptor:
        line = descriptor.readline().split(" ")
        number_of_pizza_types = int(line[0])
        types_to_order = descriptor.readline().split(" ")
        types_to_order = [int(item) for item in types_to_order]
    return number_of_pizza_types, types_to_order

if __name__ == "__main__":
    sys.exit(pytest.main(["--color=yes", "-s"]))
    # sys.exit(unittest.main())