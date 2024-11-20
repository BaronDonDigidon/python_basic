palindrome: str = input("Введите слово: ")
palindrome_symbal_list: list[str] = [sym for sym in palindrome]
revers_palindrome_list: list [str] = []
for index in range(-1, -len(palindrome_symbal_list) - 1, -1):
    revers_palindrome_list.append(palindrome_symbal_list[index])
if revers_palindrome_list == palindrome_symbal_list:
    print(f"Слово является палиндромом.")
else:
    print(f"Слово не является палиндромом.")
