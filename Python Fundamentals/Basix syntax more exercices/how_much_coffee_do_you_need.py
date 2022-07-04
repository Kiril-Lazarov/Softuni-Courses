command = input()
coffee_counter = 0
test_words_list = ["coding", "dog", "cat", "movie"]
while command != "END":
    if command.lower() in test_words_list:
        if 65 <= ord(command[0]) <= 90:
            coffee_counter += 2
        elif 97 <= ord(command[0]):
            coffee_counter += 1
    command = input()
if coffee_counter < 6:
    print(coffee_counter)
else:
    print('You need extra sleep')
