def generateParenthesis(n: int) -> list[str]:
    result = []
    generate("", 0, 0, n, result)
    return result

def generate(curr, open_count, close_count, n, result):
    if len(curr) == 2 * n:
        result.append(curr)
        return
    
    if open_count < n:
        generate(curr + '(', open_count + 1, close_count, n, result)

    if close_count < open_count:
        generate(curr + ')', open_count, close_count + 1, n, result)


n = 3
print(generateParenthesis(n))