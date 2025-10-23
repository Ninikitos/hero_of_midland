import random


class Randomizer():
    """Singleton class for generating random numbers and boolean values."""

    def __new__(cls):
        """Create or return the existing instance of the Randomizer class."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Randomizer, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Initialize the random number generator."""
        self.random_num = random.Random()

    def get_random_int(self, start: int, end: int) -> int:
        """
        Generate a random integer within a given range.

        Args:
            start (int): The lower bound of the range.
            end (int): The upper bound of the range.

        Returns:
            int: A random integer between 'start' and 'end'.
        """
        return int(self.random_num.randint(start, end))

    def roll(self) -> bool:
        """
        Randomly return either True or False.

        Returns:
            bool: A randomly chosen boolean value.
        """
        return self.random_num.choice([True, False])
