









while True:


    def factorial(n):
        if n == 1:
            return 1

        else:
            return n * factorial(n-1)


    user_input = int(input("Deine Zahl: "))

            
    print(factorial(user_input))

