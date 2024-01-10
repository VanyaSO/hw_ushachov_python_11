# Завдання 4
# Користувач вводить із клавіатури рядок і слово для пошуку. Порахуйте скільки разів
# у рядку зустрічається шукане слово. Отримане число виведіть на екран.

def main():
    # Users input values
    user_string = input("Ender string: ")
    search_word = input("Ender word for search: ")
    
    amount_search_word = 0
    
    for word in user_string.split(" "):
        
        # checking search value and word
        if word == search_word.strip(): 
            amount_search_word += 1

    print(amount_search_word)
    
main()