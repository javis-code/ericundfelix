user_input = input()

input_list = user_input.split()
output_list = []

print(user_input)
print(input_list)


for arg in input_list:
    arg += "187"
    print(arg)

    output_list.append(arg)

    
print(output_list)