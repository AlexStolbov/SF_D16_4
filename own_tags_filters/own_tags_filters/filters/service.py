import logging


class RequireLoggingLevel(logging.Filter):
    """
    Фильтрует логи по именам уровней, заданным в конструкторе.
    """

    def __init__(self, name: str = '', level_name: set = {"DEBUG"}) -> None:
        self.level_name = level_name
        super().__init__(name)

    def filter(self, record: logging.LogRecord):
        return super().filter(record) and record.levelname in self.level_name
