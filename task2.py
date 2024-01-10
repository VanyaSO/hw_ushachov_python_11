# Завдання 2
# Користувач вводить із клавіатури рядок. Порахуйте кількість букв, цифр у рядку.
# Виведіть обидва результати на екран.

def main():
    user_string = input("Ender string: ")
    
    amount_num = 0
    amount_letter = 0
    
    for i in user_string:
        # checking an element for a letter 
        if i.isdigit():
            amount_num += 1
        else: 
            amount_letter += 1
            


    print(f"Amount numbers: {amount_num}, amount letters: {amount_letter}")
    
main()