film_name = input()

final_count = 0
students_count = 0
standard_count = 0
kid_count = 0

while film_name != 'Finish':
    vacant_chairs = int(input())
    capacity = vacant_chairs
    total_count = 0
    while vacant_chairs > 0:
        ticket_type = input()

        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            students_count += 1
        elif ticket_type == 'standard':
            standard_count += 1
        elif ticket_type == 'kid':
            kid_count += 1
        vacant_chairs -= 1
        total_count += 1
        final_count += 1
    print(f"{film_name} - {total_count / capacity * 100:.2f}% full.")
    film_name = input()

print(f"Total tickets: {final_count}")
print(f"{students_count / final_count * 100:.2f}% student tickets.")
print(f"{standard_count / final_count * 100:.2f}% standard tickets.")
print(f"{kid_count / final_count * 100:.2f}% kids tickets.")
