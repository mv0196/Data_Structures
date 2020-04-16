from stack_implementation import Stack
def rev(m):
    s=Stack()
    for i in m:
        s.push(i)
    rev=""
    while not s.is_empty():
        rev+=s.pop()
    return rev
print(rev("Mukul"))
