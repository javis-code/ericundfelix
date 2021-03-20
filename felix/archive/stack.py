# Stack

stack1 = ["Hund", "Katze", "Maus", "Oktopus",
          "Papageintaucher", "Jesus", "Lorenz", "Gurkenwasser"]


def stackfind(stack, index):
    temp = []

    while len(stack) - 1 > index:
        i = len(stack) - 1
        temp.append(stack[i])
        stack.pop()
        print("Stack: {}".format(stack))

    print(stack[len(stack) - 1])

    temp.reverse()

    for i in temp:
        stack.append(i)


stackfind(stack1, 0)
