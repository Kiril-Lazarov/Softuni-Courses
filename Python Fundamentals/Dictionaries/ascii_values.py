character = input().split(', ')

character_dict = {char:ord(char) for char in character}
print(character_dict)