# task1
"""
seed(19) використовуємо для рандому щоб у всіх було однаково.
Підкидається монетка орел\рішка
Гравець мав депозит очок.
Гравець може зробити ставку на випадок 100 1 - 100 на решку
Додати якусь кількість конкурентів ботів які також можть рботити ставки.
Вигриаєте то сумма банку розподіляжться до цілих між гравцями що вгадали.
100 кидкив монетки.
Записали в файл історію гри

"""

import random

random.seed(19)

# Функція для збереження історії гри у файл
def save_game_history(history):
    with open("game_history.txt", "w") as file:
        for entry in history:
            file.write(entry + "\n")

# Функція, яка запускає гру
def play_game(num_players):
    # Початковий депозит гравців
    deposits = [1000 for _ in range(num_players)]

    # Початок гри
    game_history = ["Game started with {} players.\n".format(num_players)]

    # Головний цикл гри (100 кидків монетки)
    for i in range(100):
        # Перемішуємо список гравців, щоб визначити порядок їх ходів
        random.shuffle(deposits)

        # Визначаємо результат кидка монетки (1 - орел, 2 - решка)
        coin_toss = random.randint(1, 2)

        # Записуємо результат кидка монетки до історії гри
        if coin_toss == 1:
            game_history.append("Toss {}: Heads.\n".format(i+1))
        else:
            game_history.append("Toss {}: Tails.\n".format(i+1))

        # Перевіряємо, чи зробив гравець правильну ставку, і збільшуємо його депозит, якщо він вгадав
        for j in range(num_players):
            player_bet = random.randint(1, 100)
            if ((coin_toss == 1 and player_bet <= 50) or (coin_toss == 2 and player_bet > 50)):
                deposits[j] += 100
                game_history.append("Player {} won 100 points.\n".format(j+1))

        # Якщо всі гравці програли, банк збільшується на 100 очок
        if all(deposit < 100 for deposit in deposits):
            game_history.append("All players lost. Bank increased by 100 points.\n")
            bank = 100
        else:
            # Розподіляємо банк між гравцями, які виграли
            bank = sum(deposit // 100 for deposit in deposits)
            for j in range(num_players):
                if deposits[j] >= 100:
                    winnings = deposits[j] // 100
                    deposits[j] -= winnings * 100
                    game_history.append("Player {} won {} points.\n".format(j+1, winnings * 100))

        # Додаємо банк до історії гри
        game_history.append("Bank increased by {} points.\n".format(bank))

    # Зберігає

play_game(3)
