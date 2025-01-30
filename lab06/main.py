integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")

print(f"Type of integer_input: {type(integer_input)}")
print(f"Type of float_input: {type(float_input)}")
print(f"Type of string_input: {type(string_input)}")

string_number = "123"
converted_int = int(string_number)
converted_float = float(converted_int)

print(f"String to integer: {converted_int}")
print(f"Integer to float: {converted_float}")

personal_details = {
    "name": "John Doe",
    "age": 25
}

print(f"Name: {personal_details['name']}")
print(f"Age: {personal_details['age']}")

my_set = {1, 2, 3, 4, 5}

my_set.add(6)
print(f"Set after adding 6: {my_set}")

my_set.remove(2)
print(f"Set after removing 2: {my_set}")

if 3 in my_set:
    print("3 is in the set.")
else:
    print("3 is not in the set.")
