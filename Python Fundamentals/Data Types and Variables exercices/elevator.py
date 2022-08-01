persons = int(input())
capacity = int(input())
if persons % capacity == 0:
    courses = persons // capacity
else:
    courses = persons /capacity + 1
print(int(courses))