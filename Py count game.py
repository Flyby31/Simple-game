import random

# range 1 ... 100
b = random.randint(1, 20)
print("Добро пожаловать в цифровую угадайку")
print("Пополните счет угадайки")


# function which protects us from invalid inputs
def is_valid(protect):
    return protect.isdigit() and 1 <= int(protect) <= 100


# If our input is not correct
def valid_num():
    while True:
        n = input("Введите число от 1 до 100: ")
        if is_valid(n):
            return int(n)
        else:
            print("А может быть, всё-таки введем целое число от 1 до 100?")


# Check if the user has enough money to play
def bet_raid_fool(count):
    return 30 <= count <= 100


# Function to handle the player's money input
def money():
    while True:
        count = input("Введите количество средств(min 30, max 100): ")
        if count.isdigit() and bet_raid_fool(
            int(count)
        ):  # convert count to int for comparison
            return int(count)
        else:
            print("Недостаточно средств или неверный ввод. Минимум 50 монет.")


# Main game function
def game_num():
    count = money()  # Get initial money amount

    while True:
        n = valid_num()

        if count < 2:
            print("Недостаточно средств для игры.")
            break

        if int(n) < b:
            count -= 2
            print(f"Баланс: {count}")
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif int(n) > b:
            count -= 2
            print(f"Баланс: {count}")
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            count += 20
            print(f"Победа! +20 монет, баланс: {count}")
            print("Вы угадали, поздравляем! Хотите сыграть еще раз?")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break


game_num()
