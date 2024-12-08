class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

def parse(tokens):
    def expr():
        node = term()
        while current_token[0] == 'OP':
            op = current_token
            advance()
            node = ASTNode('BIN_OP', [node, term()], op[1])
        return node
    
    # Statements like print()
    def statement():
        if current_token[1].lower() == 'print':
            return parse_print_statement() # Jump to the parse print statement method
        elif current_token[1].lower() == 'if':
            return parse_if_statement()
        elif current_token[1].lower() == 'while':
            return parse_while_statement()
        else:
            raise SyntaxError('Unknown statement')
        
    def parse_print_statement():
        advance()  # Move past 'print'
        if current_token[0] == 'STRING':
            value = current_token[1][1:-1] # Strip quotes
            advance() # Move past string
            return ASTNode('PRINT', value=value)
        else:
            raise SyntaxError('Expected string after print')

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

    program = []
    while current_token:
        if current_token[0] == 'KEYWORD':
            program.append(statement())
        elif current_token[0] == 'ID' and peek_next_token() == ('ASSIGN', '='):
            program.append(statement())
        else:
            program.append(expr())
    return program
