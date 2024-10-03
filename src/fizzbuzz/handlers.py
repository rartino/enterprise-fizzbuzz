from abc import ABC, abstractmethod

# Abstract Base Class for FizzBuzz Handlers
class FizzBuzzHandler(ABC):
    """
    Abstract base class for FizzBuzz handlers.
    
    Methods
    -------
    handle(number: int) -> str
        Abstract method to handle the processing of a number.
    """
    @abstractmethod
    def handle(self, number: int) -> str:
        pass

# Concrete Handlers for Fizz, Buzz, and FizzBuzz
class FizzHandler(FizzBuzzHandler):
    """
    Handler for processing numbers divisible by 3.
    
    Methods
    -------
    handle(number: int) -> str
        Returns "Fizz" if the number is divisible by 3, otherwise returns an empty string.
    """
    def handle(self, number: int) -> str:
        return "Fizz" if number % 3 == 0 else ""

class BuzzHandler(FizzBuzzHandler):
    """
    Handler for processing numbers divisible by 5.
    
    Methods
    -------
    handle(number: int) -> str
        Returns "Buzz" if the number is divisible by 5, otherwise returns an empty string.
    """
    def handle(self, number: int) -> str:
        return "Buzz" if number % 5 == 0 else ""

class FizzBuzzCompositeHandler(FizzBuzzHandler):
    """
    Composite handler for aggregating multiple FizzBuzz handlers.
    
    Attributes
    ----------
    handlers : list
        A list of FizzBuzzHandler objects used for processing numbers.
    
    Methods
    -------
    handle(number: int) -> str
        Processes the number using all registered handlers and returns the appropriate result.
    """
    def __init__(self, handlers):
        """
        Parameters
        ----------
        handlers : list
            A list of FizzBuzzHandler objects.
        """
        self.handlers = handlers

    def handle(self, number: int) -> str:
        """
        Processes the given number by applying all handlers in sequence.
        
        Parameters
        ----------
        number : int
            The number to be processed.
        
        Returns
        -------
        str
            The result after processing the number. Returns "Fizz", "Buzz", "FizzBuzz", or the number as a string.
        """        
        result = ''.join(handler.handle(number) for handler in self.handlers)
        return result if result else str(number)
