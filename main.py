import streamlit as st
import random

if "user_guess" not in st.session_state:
    st.session_state.user_guess = 0

if "chances" not in st.session_state:
    st.session_state.chances = 0

st.set_page_config(page_title="Guess The Number", layout="centered")
st.title("Guess The Number 🎮") 

start_number = st.number_input("Enter the start number", 1, 100, 1)
end_number = st.number_input("Enter the end number", 1, 100, 100)
set_level = st.selectbox("Select the level", ["Easy", "Medium", "Hard"])

guess_number = random.randint(start_number, end_number)
guessed_number = st.number_input("Enter your guess number", start_number, end_number)

if set_level == "Easy":
    st.write("Easy level selected")
    st.write("You have 10 chances to guess the number")
    chance = 10
elif set_level == "Medium":
    st.write("Medium level selected")
    st.write("You have 5 chances to guess the number")
    chance = 5
else:
    st.write("Hard level selected")
    st.write("You have 3 chances to guess the number")
    chance = 3

col1, col2 = st.columns([5,1])
with col1:
    check_button = st.button("Check")
with col2:
    play_again_button = st.button("Play Again")
if check_button:
    st.session_state.chances += 1
    if guessed_number == guess_number:
        st.write(f"🎊🎉Congratulations! You guessed the right number 😍")
    elif guessed_number > guess_number:
        st.write("Try a Lower number")
        st.write(f"Chances left: {st.session_state.chances}/{chance}")
        if chance == st.session_state.chances:
            st.write(f"😯 Sorry! You lost the game. The number is {guess_number}")
    else:
        st.write("Try a Higher number")
        st.write(f"Chances left: {st.session_state.chances}/{chance}")
        if chance == st.session_state.chances:
            st.write(f"😯 Sorry! You lost the game. The number is {guess_number}")
if play_again_button:
    st.session_state.chances = 0
    guessed_number = st.number_input("Enter your guess number", start_number, end_number)