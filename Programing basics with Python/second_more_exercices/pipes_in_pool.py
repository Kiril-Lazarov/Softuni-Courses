volume = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
hours_missing = float(input())

total_debit = debit_first_pipe * hours_missing + debit_second_pipe * hours_missing
final_quantity = volume - total_debit
if final_quantity >= 0:
    print(f"The pool is {(total_debit / volume) * 100:.2f}% full. Pipe 1: {((debit_first_pipe * hours_missing) / total_debit) * 100:.2f}%."
          f" Pipe 2: {((debit_second_pipe * hours_missing) / total_debit) * 100:.2f}%.")
else:
    print(f"For {hours_missing:.2f} hours the pool overflows with {abs(final_quantity):.2f} liters.")
