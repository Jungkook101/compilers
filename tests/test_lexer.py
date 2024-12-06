import lexer

def test_tokenize():
    tokens = lexer.tokenize("3 + 5")
    assert tokens == [('NUMBER', '3'), ('OP', '+'), ('NUMBER', '5')]
