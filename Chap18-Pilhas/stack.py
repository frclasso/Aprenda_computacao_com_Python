#!/usr/bin/env python3


class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])


s = Stack()
s.push(45)
s.push(54)
s.push("+")


def evalPostfix (expr) :
  import re
  tokenList = re.split ("([^0-9])", expr)
  stack = Stack()
  for token in tokenList:
    if token == '' or token == ' ' :
      continue
    if token == '+' :
      sum = stack.pop() + stack.pop()
      stack.push(sum)
    if token == '*' :
      product = stack.pop() * stack.pop()
      stack.push(product)
    else:
      stack.push(int(token))
  return stack.pop()

#print(evalPostfix("56 47 + 2 * ")) # Erro: ValueError: invalid literal
                                            # for int() with base 10: '+'
                                            #valor correto: 206
print(evalPostfix("56 47  2 * "))