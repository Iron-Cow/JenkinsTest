class Calculator:
    def __init__(self):
        self._last_result = 0

    def add(self, first: int, second: int):
        result = first + second
        self._last_result = result
        return result

    @property
    def last_result(self):
        return self._last_result