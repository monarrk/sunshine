from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINTLN', r'println')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULTIPLY', r'\*')
        self.lexer.add('DIVIDE', r'\/')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Brackets
        self.lexer.add("OPEN_BRAC", r'\{')
        self.lexer.add("CLOSE_BRAC", r'\}')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()