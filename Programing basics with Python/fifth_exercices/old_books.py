# •	Ако не открие търсената книгата да се отпечата на два реда:
# o	"The book you search is not here!"
# o	"You checked {брой} books."
# •	Ако открие книгата си се отпечатва един ред:
# o	"You checked {брой} books and found it."

book_name = input()
current_book = input()
current_book_count = 0
while current_book != book_name and current_book != 'No More Books':
    current_book = input()
    current_book_count += 1
if current_book == book_name:
    print(f"You checked {current_book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {current_book_count} books.")