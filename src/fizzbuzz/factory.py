from .handlers import FizzHandler, BuzzHandler, FizzBuzzCompositeHandler
from .registry import FizzBuzzHandlerRegistry

class FizzBuzzHandlerFactory:
    """
    Factory class for creating FizzBuzz handlers.
    
    Methods
    -------
    create_fizz_handler() -> FizzHandler
        Creates an instance of FizzHandler.
    create_buzz_handler() -> BuzzHandler
        Creates an instance of BuzzHandler.
    create_composite_handler() -> FizzBuzzCompositeHandler
        Creates an instance of FizzBuzzCompositeHandler using all registered handlers.
    """
    @staticmethod
    def create_fizz_handler():
        """
        Creates an instance of FizzHandler.
        
        Returns
        -------
        FizzHandler
            An instance of FizzHandler.
        """
        return FizzHandler()

    @staticmethod
    def create_buzz_handler():
        """
        Creates an instance of BuzzHandler.
        
        Returns
        -------
        BuzzHandler
            An instance of BuzzHandler.
        """        
        return BuzzHandler()

    @staticmethod
    def create_composite_handler():
        """
        Creates an instance of FizzBuzzCompositeHandler using all registered handlers.
        
        Returns
        -------
        FizzBuzzCompositeHandler
            An instance of FizzBuzzCompositeHandler.
        """        
        registry = FizzBuzzHandlerRegistry()
        return FizzBuzzCompositeHandler(registry.get_handlers())
