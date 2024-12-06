import re

TOKEN_SPECIFICATION = [
    ('COMMENT', r'#.*'),         # Comments
    ('KEYWORD', r'\b(true|false|none|print|if|else|elif|for|while|break|continue|return|def|class|try|except|import|from|as|with|yield|lambda|global|nonlocal|assert|del|pass|raise|and|or)\b'), # Keywords
    ('STRING',  r'"[^"]*"'),     # String literal
    ('NUMBER',   r'\d+'),        # Integer
    ('FLOAT',   r'\d*\.\d+'),    # Float
    ('ID',       r'[A-Za-z_]\w*'),  # Identifier
    ('OP',       r'[=+\-*/%&|]'),    # Operators
    ('LPAREN',   r'\('),         # Left parenthesis
    ('RPAREN',   r'\)'),         # Right parenthesis
    ('SKIP',     r'[ \t]+'),     # Skip whitespace
    ('MISMATCH', r'.'),          # Any other character
]

def tokenize(code):
    tokens = []
    for match in re.finditer('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION), code):
        kind = match.lastgroup
        value = match.group()
        if kind in ['SKIP', 'COMMENT']:
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens
