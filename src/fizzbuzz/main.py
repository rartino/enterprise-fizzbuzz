import sys

from .factory import FizzBuzzHandlerFactory
from .registry import register_handler
from .handlers import FizzHandler, BuzzHandler

# Registering Fizz and Buzz handlers
@register_handler
class RegisteredFizzHandler(FizzHandler):
    """
    Registered handler for Fizz (numbers divisible by 3).
    """
    pass

@register_handler
class RegisteredBuzzHandler(BuzzHandler):
    """
    Registered handler for Buzz (numbers divisible by 5).
    """
    pass

def generate_fizzbuzz_sequence(n: int):
    """
    Generates a FizzBuzz sequence from 1 to n.
    
    Parameters
    ----------
    n : int
        The upper limit of the sequence (inclusive).
    
    Returns
    -------
    list
        A list containing the FizzBuzz results for numbers from 1 to n.
    """
    composite_handler = FizzBuzzHandlerFactory.create_composite_handler()
    return [composite_handler.handle(i) for i in range(1, n + 1)]

# CLI for FizzBuzz without external dependency
def fizzbuzz_cli():
    """
    Command Line Interface for generating and printing a FizzBuzz sequence.
    
    The CLI takes an argument from the command line and prints the FizzBuzz sequence.
    """
    if len(sys.argv) != 2:
        print("Usage: python -m fizzbuzz <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: n must be an integer.")
        sys.exit(1)

    fizzbuzz_sequence = generate_fizzbuzz_sequence(n)
    for line in fizzbuzz_sequence:
        print(line)

if __name__ == "__main__":
    fizzbuzz_cli()
