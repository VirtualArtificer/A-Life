from typing import DefaultDict
from collections import defaultdict

#Vector = DefaultDict[int, int]

class Vector:
    """
    Custom Vector class for sparsely populated vectors.

    Supports initialization from iterable, efficient indexing,
    and additional features for the project.
    """

    def __init__(self, iterable=None):
        """
        Initializes a Vector object.

        Args:
            iterable: An optional iterable object used to populate the vector.
        """
        self.data = defaultdict(int)  # stores values with index as key
        self.max_index = -1  # tracks the highest populated index

        if iterable is not None:
            for index, value in enumerate(iterable):
                self.__setitem__(index, value)

    def __getitem__(self, index):
        """
        Retrieves the value at a specific index.

        Args:
            index: The index of the element to retrieve.

        Returns:
            The element value at the specified index.
            If the index is not populated, returns 0.
        """
        if index > self.max_index:
            return 0
        return self.data[index]

    def __setitem__(self, index, value):
        """
        Sets the value at a specific index.

        Args:
            index: The index of the element to set.
            value: The value to assign to the element.
        """
        self.data[index] = value
        self.max_index = max(self.max_index, index)

    def __len__(self):
        """
        Returns the logical size of the vector.

        Returns:
            The highest populated index + 1.
        """
        return self.max_index + 1

    # Additional features for the project

    def to_bytes(self):
        """
        Converts the vector data to a byte stream.

        Returns:
            A byte array representing the vector data.
        """
        # ... implement logic to convert vector data to bytes
        # consider using pickle or other serialization library
        # ...
        return bytes

    def from_bytes(self, data):
        """
        Reconstructs the vector from a byte stream.

        Args:
            data: A byte array containing the vector data.
        """
        # ... implement logic to reconstruct vector data from bytes
        # consider using pickle or other deserialization library
        # ...
        pass

    def get_non_zero_indices(self):
        """
        Returns a list of all non-zero indices in the vector.

        Returns:
            A list of integers representing the non-zero indices.
        """
        return list(self.data.keys())

    def apply_function(self, func):
        """
        Applies a function to all elements of the vector.

        Args:
            func: A function that takes a single element as input and returns a new value.
        """
        for index, value in self.data.items():
            self.data[index] = func(value)

    # ... add other relevant methods as needed ...
