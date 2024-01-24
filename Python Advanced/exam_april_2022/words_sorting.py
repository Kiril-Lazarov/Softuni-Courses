def words_sorting(*args):
    words_dict = {}
    total_sum = 0
    for word in args:
        sum_values = 0
        for letter in word:
            sum_values += ord(letter)
        words_dict[word] = sum_values
        total_sum += sum_values
    if total_sum % 2==0:
        sorted_dict = {k:v for k, v in sorted(words_dict.items(), key= lambda x:x[0])}
    else:
        sorted_dict = {k:v for k, v in sorted(words_dict.items(), key= lambda x: -x[1])}
    final_list = []
    for key, value in sorted_dict.items():
        final_list.append(f'{key} - {value}')
    return '\n'.join(final_list)



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

