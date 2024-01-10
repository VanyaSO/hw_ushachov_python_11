# Завдання 5
# Користувач вводить із клавіатури рядок, слово для пошуку, слово для заміни. Зробіть
# у рядку заміну одного слова на інше. Отриманий рядок відобразіть на екрані.

def main():
    # Users input values
    user_string = input("Ender string: ")
    search_word = input("Ender word for search: ")
    change_word = input("Ender word for change: ")
    
    new_string = ''
    
    
    for word in user_string.split(" "):
        # checking search value and word
        if word == search_word.strip(): 
            # change the search value
            word = change_word
        
        # add word in new string
        new_string += word

    # joining array elements via " "
    new_string = " ".join(new_string)
    
    print(new_string)
    
main()