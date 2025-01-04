class Solution: 
    def isValid(self, s: str) -> bool: # Function to check if the given string has valid parenthesis
        stack = [] # Stack to store the opening parenthesis
        for i in s:
            if i == '(' or i == '{' or i == '[': # If the character is an opening parenthesis, push it to the stack
                stack.append(i)
            else:
                if len(stack) == 0: # If the stack is empty and the character is a closing parenthesis, return False
                    return False
                if i == ')' and stack[-1] == '(': # If the character is a closing parenthesis and the top of the stack is the corresponding opening parenthesis, pop the opening parenthesis
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else: # If the character is a closing parenthesis and the top of the stack is not the corresponding opening parenthesis,
                    return False
        if len(stack) == 0: # If the stack is empty that means all the opening parenthesis have been closed, and the answer is True
            return True
        return False