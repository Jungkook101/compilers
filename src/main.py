from lexer import tokenize
from parser import parse
from interpreter import evaluate

def run_code(code):
    tokens = tokenize(code)
    print("TOKENS: " + str(tokens))
    ast = parse(tokens)
    print("AST: " + str(ast))
    result = evaluate(ast)
    print("Result:", result)

if __name__ == '__main__':
    with open('examples/hello_world.jpyl', 'r') as f:
        code = f.read()
    run_code(code)
