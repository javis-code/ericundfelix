user_input = input()

# >> Hallo ich heiße Felix

input_list = user_input.split()
output_list = []

# >> ["Hallo", "ich", "heiße", "Felix"]

print(user_input)
print(input_list)

for arg in input_list:
    arg += "187"

    # >> Hallo >> Hallo187

    print(arg)

    # >> Hallo187

    output_list.append(arg)

    # ["Hallo", "ich", "heiße", "Felix"] + ["Hallo187"] >> ["Hallo", "ich", "heiße", "Felix", "Hallo187"]

print(output_list)
