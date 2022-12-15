words = input().split(' ')
palindrome = input()
palindrome_list = [i for i in words if i == i[::-1]]


print(palindrome_list)
print(f"Found palindrome {words.count(palindrome)} times")