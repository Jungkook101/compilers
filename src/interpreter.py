def evaluate(node):
    if node.type == 'NUMBER':
        return int(node.value)
    elif node.type == 'BIN_OP':
        left = evaluate(node.children[0])
        right = evaluate(node.children[1])
        if node.value == '+':
            return left + right
        elif node.value == '-':
            return left - right
        # Add other operations
    else:
        raise RuntimeError(f'Unknown node type: {node.type}')
