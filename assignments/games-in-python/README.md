# 📘 Assignment: Games in Python

## 🎯 Objective

Create a simple text-based game in Python while practicing loops, conditionals, user input, and random selection. This assignment helps you apply core programming concepts in a fun, interactive project.

## 📝 Tasks

### 🛠️ Build a Hangman Game

#### Description
Write a Python program that lets a player guess letters to reveal a hidden word before running out of chances.

#### Requirements
Completed program should:

- Choose a random word from a predefined list of words.
- Show the current guessed word using underscores for unrevealed letters, such as `_ _ _ _ _`.
- Ask the user to enter one letter at a time.
- Reveal matching letters in the correct positions.
- Track the number of incorrect guesses remaining.
- End the game when the player wins or runs out of attempts.
- Display a clear message for either a win or a loss.

### 🛠️ Improve the Game Experience

#### Description
Add a few finishing touches that make the game feel complete and easier to play.

#### Requirements
Completed program should:

- Prevent duplicate guesses from being counted multiple times.
- Display the letters already guessed so the user can track their progress.
- Keep the game loop running until the player decides to quit or the game ends.
- Use clear prompts and friendly messages for the player.
- Example output:
  ```python
  Word: _ a _ _ e
  Guesses left: 5
  Enter a letter: a
  Correct! You guessed a.
  ```

### 🛠️ Add Game Logic and Validation

#### Description
Make the game robust by handling repeated inputs and invalid guesses in a clean way.

#### Requirements
Completed program should:

- Check whether the input is a single letter.
- Ignore or warn about invalid inputs such as numbers or multiple characters.
- Make sure the game continues smoothly after each guess.
- Use functions to organize the logic and keep the code readable.
- Example validation:
  ```python
  Enter a letter: 7
  Please enter a single valid letter.
  ```
