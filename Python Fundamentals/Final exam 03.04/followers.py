followers = {}
while True:
    data = input()
    if data == "Log out":
        break
    commands = data.split(": ")
    if commands[0] == 'New follower':
        if commands[1] not in followers:
            followers[commands[1]] = {"Likes": 0, "Comments": 0}
    elif commands[0] == 'Like':
        if commands[1] not in followers:
            followers[commands[1]] = {"Likes": int(commands[2]), "Comments": 0}
        else:
            followers[commands[1]]["Likes"] += int(commands[2])
    elif commands[0] == 'Comment':
        if commands[1] not in followers:
            followers[commands[1]] = {"Likes": 0, "Comments": 1}
        else:
            followers[commands[1]]["Comments"] += 1
    elif commands[0] == 'Blocked':
        if commands[1] not in followers:
            print(f"{commands[1]} doesn't exist.")
        else:
            del followers[commands[1]]
print(f'{len(followers)} followers')
for name in followers:
    print(f"{name}: {followers[name]['Likes'] + followers[name]['Comments']}")