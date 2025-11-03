# ===================================================
# HANGMAN WORD GUESSING GAME
# Python Mini Project
# ===================================================

import random  # For picking random words
import os      # For clearing the screen

# ===================================================
# FUNCTION 1: CLEAR SCREEN
# ===================================================
def clear_screen():
    """Clears the terminal screen"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')

# ===================================================
# FUNCTION 2: SHOW HANGMAN DRAWING
# ===================================================
def display_hangman(wrong_guesses):
    """Shows hangman based on wrong guesses (0-6)"""
    stages = [
        # Stage 0 - Empty
        """
           --------
           |      |
           |      
           |     
           |     
           |     
        --------
        """,
        # Stage 1 - Head
        """
           --------
           |      |
           |      O
           |     
           |     
           |     
        --------
        """,
        # Stage 2 - Body
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        # Stage 3 - Left arm
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        # Stage 4 - Both arms
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        # Stage 5 - Left leg
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        # Stage 6 - Both legs (Game Over)
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    return stages[wrong_guesses]

# ===================================================
# FUNCTION 3: SHOW WORD WITH BLANKS
# ===================================================
def display_word(word, guessed_letters):
    """Shows word with blanks for unguessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# ===================================================
# FUNCTION 4: MAIN GAME
# ===================================================
def play_hangman():
    """Runs one complete game"""
    
    # Word list
    words = ['PYTHON', 'CODING', 'COMPUTER', 'KEYBOARD', 'PROGRAM', 
             'DEVELOPER', 'WEBSITE', 'INTERNET', 'SOFTWARE', 'GAMING']
    
    # Setup
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    # Welcome screen
    print("\n" + "="*50)
    print("     🎮 WELCOME TO HANGMAN GAME 🎮")
    print("="*50)
    print("\n📝 Instructions:")
    print("   - Guess one letter at a time")
    print("   - You have 6 wrong guesses before game over")
    print("   - Good luck!\n")
    input("Press Enter to start...")
    
    # Game loop
    while wrong_guesses < max_wrong:
        clear_screen()
        
        # Display
        print("\n" + "="*50)
        print("           🎮 HANGMAN GAME 🎮")
        print("="*50)
        print(display_hangman(wrong_guesses))
        print(f"\n📊 Wrong Guesses: {wrong_guesses}/{max_wrong}")
        
        if guessed_letters:
            print(f"🔤 Letters Used: {', '.join(sorted(guessed_letters))}")
        else:
            print(f"🔤 Letters Used: None")
        
        current_display = display_word(word, guessed_letters)
        print(f"\n✨ Word: {current_display}")
        
        # Check win
        if "_" not in current_display:
            print("\n" + "="*50)
            print("     🎉 CONGRATULATIONS! YOU WON! 🎉")
            print("="*50)
            print(f"     The word was: {word}")
            print("="*50)
            return True
        
        # Get input
        print("\n" + "-"*50)
        guess = input("🎯 Enter a letter: ").upper()
        
        # Validate
        if len(guess) != 1 or not guess.isalpha():
            input("\n⚠️  Please enter a single letter! Press Enter to continue...")
            continue
        
        if guess in guessed_letters:
            input("\n⚠️  You already guessed that letter! Press Enter to continue...")
            continue
        
        # Process guess
        guessed_letters.append(guess)
        
        if guess not in word:
            wrong_guesses += 1
            if wrong_guesses < max_wrong:
                input(f"\n❌ Wrong! '{guess}' is not in the word. Press Enter to continue...")
    
    # Game over
    clear_screen()
    print("\n" + "="*50)
    print("           💀 GAME OVER 💀")
    print("="*50)
    print(display_hangman(wrong_guesses))
    print(f"\n     The word was: {word}")
    print("="*50)
    return False

# ===================================================
# FUNCTION 5: REPLAY LOOP
# ===================================================
def main():
    """Controls replay"""
    while True:
        play_hangman()
        print("\n")
        play_again = input("🔄 Play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            clear_screen()
            print("\n" + "="*50)
            print("     👋 Thanks for playing! Goodbye! 👋")
            print("="*50)
            print()
            break

# ===================================================
# START PROGRAM
# ===================================================
if __name__ == "__main__":
    main()