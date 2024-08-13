class Stack:
    '''абстрактный тип данных, представляющий список элементов, организованных по принципу LIFO'''

    def __init__(self, stack=None):
        if stack is None:
            self.value = []
        else:
            self.value = stack

    def is_empty(self):
        '''is_empty — проверка стека на пустоту. Метод возвращает True или False'''
        return not(bool(self.value))

    def push(self, element):
        '''push — добавляет новый элемент на вершину стека. Метод ничего не возвращает'''
        self.value.append(element)

    def pop(self):
        '''pop — удаляет верхний элемент стека. Стек изменяется.
        Метод возвращает верхний элемент стека'''
        return self.value.pop(-1)

    def peek(self):
        '''peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется'''
        return self.value[-1]

    def size(self):
        '''size — возвращает количество элементов в стеке'''
        len(self.value)

    def __str__(self):
        return str(self.value)
