class Scanner:
    def __init__(self, source: str):
        self._source = source
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 1

    def scanTokens(self):
        while (!self.isAtEnd()):
            self._start = self._current
            scanToken()
        self._tokens.add(Token(EOF, "", None, self._line))
        return self._tokens

    def isAtEnd(self):
        return self._current >= len(self._source)
