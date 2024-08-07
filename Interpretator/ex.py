import enum


class Token:
    class Type(enum.Enum):
        INTEGER = enum.auto()
        PLUS = enum.auto()
        MINUS = enum.auto()
        LPAREN = enum.auto()
        RPAREN = enum.auto()

    def __init__(self, type_, text):
        self.type = type_
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input_):
    result = []

    i = 0
    while i < len(input_):
        if input_[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input_[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input_[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input_[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [input_[i]]
            for j in range(i + 1, len(input_)):
                if input_[j].isdigit():
                    digits.append(input_[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1

    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(enum.Enum):
        ADDITION = enum.auto()
        SUBTRACTION = enum.auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer

        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION

        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION

        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j

        i += 1

    return result


def calc(input_):
    tokens = lex(input_)
    print(' '.join(map(str, tokens)))
    parsed = parse(tokens)
    print(f'{input_} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
