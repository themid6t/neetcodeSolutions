def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c in [')', '}', ']']:
            if not stack:
                return False
            top = stack.pop()
            if ((c == ')' and top != '(') or 
                (c == '}' and top != '{') or 
                (c == ']' and top != '[')):
                return False
    
    return not stack