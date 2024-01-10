# Завдання 1
# Користувач вводить із клавіатури рядок. Зробіть поворот рядків і отриманий
# результат виведіть на екран.

def main():
    user_string = input("Ender string: ")
    reverse_string = ''.join(reversed(user_string))


    print(reverse_string)
    
main()