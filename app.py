# Archivo: streamlit_hangman.py

import streamlit as st
import random
from hangman_words import word_list
import hangman_art

# Inicializar estados de sesión
if 'lives' not in st.session_state:
    st.session_state.lives = 6
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.correct_letters = []
    st.session_state.incorrect_letters = []
    st.session_state.display = "_" * st.session_state.word_length
    st.session_state.game_over = False
    st.session_state.message = ""

# Mostrar el título y el logo
st.title("🎯 Hangman Game")
st.text(hangman_art.logo)

# Mostrar el estado actual
st.subheader(f"Lives left: {st.session_state.lives}/6")
st.write("Word to guess: " + st.session_state.display)
st.write("✅ Correct letters: " + ", ".join(st.session_state.correct_letters))
st.write("❌ Incorrect letters: " +
         ", ".join(st.session_state.incorrect_letters))

# Entrada del jugador
guess = st.text_input("Enter a letter:", max_chars=1).lower()

if st.button("Submit Guess") and not st.session_state.game_over:
    if not guess.isalpha():
        st.warning("Please enter a valid letter!")
    elif guess in st.session_state.correct_letters or guess in st.session_state.incorrect_letters:
        st.info(f"You've already guessed '{guess}'. Try a different letter.")
    else:
        # Actualizar el juego
        new_display = ""
        correct_guess = False
        for index, letter in enumerate(st.session_state.chosen_word):
            if letter == guess:
                new_display += letter
                correct_guess = True
            else:
                new_display += st.session_state.display[index]

        if correct_guess:
            st.session_state.correct_letters.append(guess)
            st.session_state.display = new_display
        else:
            st.session_state.incorrect_letters.append(guess)
            st.session_state.lives -= 1
            st.warning(
                f'La letra "{guess}" no está en la palabra. Pierdes una vida.')

        # Verificar condiciones de victoria o derrota
        if "_" not in st.session_state.display:
            st.session_state.game_over = True
            st.success("🎉 YOU WIN! Congratulations!")
        elif st.session_state.lives == 0:
            st.session_state.game_over = True
            st.error(
                f"💀 YOU LOSE! The word was '{st.session_state.chosen_word}'.")

# Mostrar arte del ahorcado según las vidas
st.text(hangman_art.stages[st.session_state.lives])

# Botón para reiniciar el juego
if st.button("Restart Game"):
    st.session_state.lives = 6
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.correct_letters = []
    st.session_state.incorrect_letters = []
    st.session_state.display = "_" * st.session_state.word_length
    st.session_state.game_over = False
    st.experimental_rerun()  # Refrescar la app
