# •	На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# •	На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден. Цяло число в интервала [0…10 000]

period = int(input())

medics_count = 7
total = 0

treated_patients_in_day = 0
untreated_patients_in_day = 0
total_treated_patients = 0
total_untreated_patients = 0

for days in range(1, period + 1):
    patients_count = int(input())
    if days % 3 == 0:
        if total_untreated_patients > total_treated_patients:
            medics_count += 1
    if patients_count <= medics_count:
        treated_patients_in_day = patients_count
        untreated_patients_in_day = 0
    else:
        treated_patients_in_day = medics_count
        untreated_patients_in_day = patients_count - medics_count

    total_treated_patients += treated_patients_in_day
    total_untreated_patients += untreated_patients_in_day


    # if untreated_patients > treated_patients:
    #     medics_count += 1
print(f'Treated patients: {total_treated_patients}.')
print(f"Untreated patients: {total_untreated_patients}.")
