# Завдання 3
# Користувач вводить із клавіатури рядок і символ для пошуку. Порахуйте скільки разів
# у рядку зустрічається шуканий символ. Отримане число виведіть на екран.

def main():
    user_string = input("Ender string: ")
    search_char = input("Ender char for search: ")
    
    amount_search_char = 0
    
    
    for i in user_string:
        if i == search_char: amount_search_char += 1

    print(amount_search_char)
    
main()