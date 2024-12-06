class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

def parse(tokens):
    # Statements like print()s
    def statement():
        if current_token[0] == 'KEYWORD':
            advance()  # Move past the 'print' keyword
            if current_token[0] == 'STRING':
                # Remove quotes and pass the raw string value
                value = current_token[1][1:-1]  # Strip quotes
                advance()
                return ASTNode('PRINT', value=value)
            else:
                raise SyntaxError('Expected a string after "print"')
        else:
            raise SyntaxError('Unknown statement')

    # Simple example: Parse expressions like "3 + 5"
    def expr():
        node = term()
        while current_token[0] == 'OP':
            op = current_token
            advance()
            node = ASTNode('BIN_OP', [node, term()], op[1])
        return node

    def term():
        if current_token[0] == 'NUMBER':
            value = current_token[1]
            advance()
            return ASTNode('NUMBER', value=value)
        elif current_token[0] == 'LPAREN':
            advance()
            node = expr()
            if current_token[0] != 'RPAREN':
                raise SyntaxError('Expected ")"')
            advance()
            return node
        raise SyntaxError('Unexpected token')

    def advance():
        nonlocal current_token
        current_token = next(tokens_iter, None)

    tokens_iter = iter(tokens)
    current_token = None
    advance()
    return expr()
