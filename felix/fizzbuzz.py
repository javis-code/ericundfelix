for i in range(1, 101):
    output = ""

    output += "fizz" if i % 3 == 0 else ""
    output += "buzz" if i % 5 == 0 else ""

    output += str(i) if output == "" else ""

    print(output)
