# n! = n * n-1 * n-2 ... 1
# 5! = 5 * 4 * 3 * 2 * 1
# 1! = 1

while True:
    def factorial(n):
        print(n)

        if n == 1:
            return 1

        else:
            return n * factorial(n-1)

    user_input = int(input("Deine Zahl: "))

    print(factorial(user_input))

# string = "shdfjhsdfjsdf"
# int = 186234
# float = 19234.19234731438745