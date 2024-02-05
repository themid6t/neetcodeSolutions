def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens:
        print(stack)
        if  i == "+": 
            stack.append(stack.pop() + stack.pop())
        elif  i == "-": 
            stack.append(stack.pop() - stack.pop())
        elif  i == "*": 
            stack.append(stack.pop() * stack.pop())
        elif  i == "/": 
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2 / n1))
        else: 
            stack.append(int(i))
    return stack.pop()

# tkn = ["4","13","5","/","+"]
tkn = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tkn))