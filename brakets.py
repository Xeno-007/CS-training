def is_balanced(input_string):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


input_string = input("Enter a string with parentheses, curly braces, and square brackets: ")
if is_balanced(input_string):
    print("The string is balanced.")
else:
    print("The string is not balanced.")
