import Stack

def checking_the_balance(string: str):
    data = {'{': '}', '}': '{', '[': ']', ']': '[', '(': ')', ')': '('}
    len_ = len(string)
    if len_%2 != 0:
        return 'Несбалансированно'
    stack = Stack.Stack()
    for i in string:
        if not stack.is_empty():
            if stack.peek() == data[i]:
                stack.pop()
            else:
                stack.push(i)
        else:
            stack.push(i)
    if stack.is_empty():
        return 'Сбалансированно'
    return 'Несбалансированно'


if __name__ == '__main__':
    data = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for i in data:
        print(checking_the_balance(i))
