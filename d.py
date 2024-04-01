from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def perform_action(self):
        self.logger.log("Action performed")

class FileLogger(Logger):
    def log(self, message):
        # Implementation for file logging
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        # Implementation for console logging
        pass

# Usage
file_logger = FileLogger()
console_logger = ConsoleLogger()

app_with_file_logger = Application(file_logger)
app_with_console_logger = Application(console_logger)

app_with_file_logger.perform_action()
app_with_console_logger.perform_action()
