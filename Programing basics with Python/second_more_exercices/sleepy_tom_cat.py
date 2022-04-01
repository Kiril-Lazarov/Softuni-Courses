off_days = int(input())

working_days_play_per_day = 63
off_days_play_per_day = 127
total_playing_hours = off_days_play_per_day * off_days + (365 - off_days) * working_days_play_per_day

if total_playing_hours < 30000:
    print('Tom sleeps well')
    print(f'{(30000 - total_playing_hours) // 60} hours and {(30000 - total_playing_hours) % 60} minutes less for play')
else:
    print('Tom will run away')
    print(f'{abs(30000 - total_playing_hours) // 60} hours and {abs(30000 - total_playing_hours) % 60}'
          f' minutes more for play')


# print(off_days_play_per_day * off_days, (365 - off_days) * working_days_play_per_day, total_playing_hours)
