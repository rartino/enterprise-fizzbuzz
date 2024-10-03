class SingletonMeta(type):
    """
    Metaclass for creating singleton classes.
    
    This ensures that only one instance of a class exists.
    
    Attributes
    ----------
    _instances : dict
        A dictionary storing the single instances of classes.
    
    Methods
    -------
    __call__(*args, **kwargs)
        Returns the single instance of the class, creating it if it does not exist.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class FizzBuzzHandlerRegistry(metaclass=SingletonMeta):
    """
    Registry for storing and managing FizzBuzz handlers.
    
    Attributes
    ----------
    handlers : list
        A list of registered FizzBuzzHandler objects.
    
    Methods
    -------
    register_handler(handler: FizzBuzzHandler)
        Registers a new handler in the registry.
    get_handlers() -> list
        Returns the list of registered handlers.
    """
    def __init__(self):
        self.handlers = []

    def register_handler(self, handler):
        self.handlers.append(handler)

    def get_handlers(self):
        return self.handlers

def register_handler(handler_class):
    """
    Decorator function for registering a FizzBuzz handler.
    
    Parameters
    ----------
    handler_class : class
        The handler class to be registered.
    
    Returns
    -------
    class
        The registered handler class.
    """    
    registry = FizzBuzzHandlerRegistry()
    registry.register_handler(handler_class())
    return handler_class
