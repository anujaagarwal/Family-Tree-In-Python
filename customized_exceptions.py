class Error(Exception):
    pass

# Customized Exceptions 
class PersonNotFoundError(Error):  
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class ChildAdditionFailedError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class InsufficientInformationError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class CommandNotFoundError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class NullPointerError(Error):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
