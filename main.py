import random
from hangman_words import word_list
import hangman_art

# Imprimir el logo al inicio del juego
print(hangman_art.logo)

lives = 6
# Selecciona una palabra al azar de la lista
chosen_word = random.choice(word_list)

# Mostrar la longitud de la palabra y los placeholders
word_length = len(chosen_word)
placeholder = "_" * word_length
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    # Mostrar cuántas vidas quedan
    print(
        f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    # Verificar si el jugador ya adivinó esa letra
    if guess in correct_letters or guess in incorrect_letters:
        print(f"You've already guessed {guess}")
        continue

    # Si la letra está en la palabra, actualizar el placeholder
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        else:
            display += "_"

    # Si la letra no está en la palabra, restar vidas
    if guess not in chosen_word:
        incorrect_letters.append(guess)
        print(f'La letra "{guess}" no está en la palabra. Pierdes una vida.')
        lives -= 1

        if lives == 0:
            game_over = True
            print(f'La palabra era "{chosen_word}".')
            print(f"***********************YOU LOSE**********************")

    # Si adivinó la palabra completamente, ganar
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Mostrar el progreso actual
    print("Word to guess: " + display)

    # Mostrar la etapa del ahorcado según el número de vidas
    print(hangman_art.stages[lives])
