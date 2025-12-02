import streamlit as st
import random

st.title("Simple Number Guessing Game 🎯")

# Initialize session state for the random number
target = st.session_state.get("target", random.randint(1, 20))
st.session_state.target = target

st.write("I'm thinking of a number between 1 and 20. Can you guess it?")

# Input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=20, step=1)

if st.button("Check"):
    if guess == target:
        st.success("🎉 Correct! You guessed the number!")
        # Reset with new number
        st.session_state.target = random.randint(1, 20)
        st.info("A new number has been generated. Try again!")
    elif guess < target:
        st.warning("Too low! Try a higher number.")
    else:
        st.warning("Too high! Try a lower number.")
