name = input()
password = input()
entry_password = input()
while password != entry_password:
    entry_password = input()
print(f"Welcome {name}!")