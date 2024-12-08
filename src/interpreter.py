def evaluate(program):
    for node in program:
        if node.type == 'NUMBER':
            return int(node.value)
        elif node.type == 'BIN_OP':
            left = evaluate(node.children[0])
            right = evaluate(node.children[1])
            if node.value == '+':
                return left + right
            elif node.value == '-':
                return left - right
        elif node.type == 'PRINT':
            value = node.value
            print(value)  # Print the value associated with the PRINT node
        else:
            raise RuntimeError(f'Unknown node type: {node.type}')
