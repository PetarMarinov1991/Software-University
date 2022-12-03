def check(expression):
    open_bracket, close_bracket = '(', ')'
    # filtering only brackets in expression
    brackets = [x for x in expression if x == open_bracket or x == close_bracket]
    # dividing brackets to even and odd indexes in expression
    even_brackets = [brackets[x] for x in range(len(brackets)) if x % 2 == 0]
    odd_brackets = [brackets[x] for x in range(len(brackets)) if x % 2 != 0]

    if len(even_brackets) == len(odd_brackets):
        # close brackets must be odd index and open brackets even index
        if close_bracket not in even_brackets and open_bracket not in odd_brackets:
            return 'BALANCED'
    return 'UNBALANCED'


lines = int(input())
expression = ''.join([input() for _ in range(lines)])

print(check(expression))
