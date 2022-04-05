goal = 10000
walked_steps = 0
end_walk = False
while walked_steps <= goal:
    steps_count = input()
    if steps_count != "Going home":
        walked_steps += int(steps_count)
    elif steps_count == "Going home":
        steps_count = input()
        walked_steps += int(steps_count)
        if walked_steps > goal:
            print("Goal reached! Good job!")
            print(f"{walked_steps - goal} steps over the goal!")
            end_walk = True
            break
        else:
            print(f"{goal - walked_steps} more steps to reach goal.")
            end_walk = True
            break
if end_walk == False:
    print("Goal reached! Good job!")
    print(f"{walked_steps - goal} steps over the goal!")

