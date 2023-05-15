
def validate_brackets(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False  # There is no matching opening bracket
            last_opening = stack.pop()
            if bracket_pairs[last_opening] != char:
                return False  # Opening and closing brackets don't match
    
    return len(stack) == 0  # If stack is empty, all brackets are balanced


# print(validate_brackets("{}"))  # True
# print(validate_brackets("{}(){}"))  # True
# print(validate_brackets("()[[Extra Characters]]"))  # True
# print(validate_brackets("(){}[[]]"))  # True
# print(validate_brackets("{}{Code}[Fellows](())"))  # True
# print(validate_brackets("[({}]"))  # False
# print(validate_brackets("(]("))  # False
# print(validate_brackets("{(})"))  # False