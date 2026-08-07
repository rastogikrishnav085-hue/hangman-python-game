# 🎮 Hangman Game - Python Mini Project

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![SAII Project](https://img.shields.io/badge/SAII-Mini%20Project-orange.svg)](https://github.com/rastogikrishnav085-hue/hangman-python-game)

A classic console-based word guessing game built in Python with ASCII art graphics and comprehensive input validation.

<p align="center">
  <img src="https://img.icons8.com/color/200/000000/python.png" alt="Python Logo" width="100"/>
</p>

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [Code Overview](#code-overview)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## 📖 About

This project is a Python implementation of the classic **Hangman** word-guessing game, developed as part of our **Python Project-Based Learning** course at **Symbiosis Artificial Intelligence Institute (SAII)**. 

### What is Hangman?
Hangman is a word-guessing game where:
- A secret word is chosen from a themed vocabulary
- Player guesses letters one at a time
- Each wrong guess draws part of a hangman figure (7 stages)
- Player wins by guessing the word before the hangman is complete
- 6 wrong guesses = Game Over

### Project Highlights
- ✅ **217 lines** of clean, well-documented code
- ✅ **5 modular functions** for easy maintenance
- ✅ **10 computer-themed words** in the vocabulary bank
- ✅ **7 ASCII art stages** for visual feedback
- ✅ **20 test cases** with 100% pass rate
- ✅ **Zero external dependencies** - only Python standard library
- ✅ **Cross-platform** - Windows, macOS, and Linux compatible

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **ASCII Art Graphics** | 7-stage hangman progression with detailed drawings |
| 📝 **Themed Word Bank** | 10 computer science words (PYTHON, CODING, DEVELOPER, etc.) |
| 🛡️ **Input Validation** | Handles letters, numbers, duplicates, and empty inputs |
| 🔄 **Replay Functionality** | Play unlimited games without restarting |
| 🌐 **Cross-Platform** | Works seamlessly on Windows, macOS, and Linux |
| 😊 **Emoji UI** | Modern interface with emojis for better UX |
| ⚡ **Zero Dependencies** | No pip install needed - runs immediately |
| 🎯 **Beginner Friendly** | Clear code structure with extensive comments |

---

## 🎥 Demo

### 🎬 Video Demonstration
> **Watch our 5-minute project presentation:**  
> **[📹 View Demo Video](https://drive.google.com/file/d/1RHOXdujpIRFbXsqv_bYfY1f-f8D1ldxR/view?usp=sharing)**

### 📊 Presentation Slides
> **[📽️ View Presentation PDF](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/Presentation%20-%20Hangman%20Game-2.pdf)**

### 📄 Complete Project Report
> **[📖 Read Full Report](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/PROJECT_REPORT.pdf)**

### 🖼️ Quick Look

```
        ==================================================
             🎮 WELCOME TO HANGMAN GAME 🎮
        ==================================================

        📝 Instructions:
           - Guess one letter at a time
           - You have 6 wrong guesses before game over
           - Good luck!

        Press Enter to start...
```

---

## 🚀 Installation

### Prerequisites
- **Python 3.6 or higher** ([Download here](https://www.python.org/downloads/))
- No additional packages required! 🎉

### Quick Start

#### Option 1: Clone Repository
```bash
# Clone the repository
git clone https://github.com/rastogikrishnav085-hue/hangman-python-game.git

# Navigate to directory
cd hangman-python-game

# Run the game
python HangMan.py
```

#### Option 2: Direct Download
1. Download `HangMan.py` from this repository
2. Open terminal/command prompt
3. Navigate to download location
4. Run: `python HangMan.py`

---

## 🎮 Usage

### Running on Different Platforms

**Windows:**
```cmd
python HangMan.py
```

**macOS/Linux:**
```bash
python3 HangMan.py
```

**VS Code:**
- Open `HangMan.py`
- Press `F5` or click Run button

### Expected Output
```
==================================================
           🎮 HANGMAN GAME 🎮
==================================================

        --------
        |      |
        |      
        |     
        |     
        |     
     --------

📊 Wrong Guesses: 0/6
🔤 Letters Used: None

✨ Word: _ _ _ _ _ _ _

--------------------------------------------------
🎯 Enter a letter: 
```

---

## 📜 Game Rules

### How to Play

1. **Start the Game**
   - Run the program
   - Press Enter at welcome screen

2. **Make Guesses**
   - Enter one letter at a time
   - Letters are automatically converted to uppercase
   - Cannot guess the same letter twice

3. **Win Condition**
   - Guess all letters before 6 wrong attempts
   - Complete word revealed with celebration message

4. **Lose Condition**
   - 6 wrong guesses made
   - Hangman drawing complete
   - Word is revealed

5. **Replay**
   - Type `yes` or `y` to play again
   - Type `no` or `n` to exit

### Pro Tips 💡
- Start with common vowels: **A, E, I, O, U**
- Look for common patterns in technical words
- Think about the word length shown
- Computer terms often use letters like **P, T, R, C, D**

### Word Bank
The game includes 10 programming-related words:
- PYTHON
- CODING
- COMPUTER
- KEYBOARD
- PROGRAM
- DEVELOPER
- WEBSITE
- INTERNET
- SOFTWARE
- GAMING

---

## 📂 Project Structure

```
hangman-python-game/
│
├── 📄 HangMan.py                   # Main game file (217 lines)
├── 📖 README.md                    # This documentation
├── 📊 PROJECT_REPORT.pdf           # Detailed 53-page project report
├── 📽️ Presentation - Hangman Game-2.pdf  # Project presentation
└── 🎥 Demo Video Link              # Google Drive video link
```

---

## 💻 Code Overview

### Architecture

The game is built with **5 main functions**:

```python
1. clear_screen()                    # Cross-platform screen clearing
2. display_hangman(wrong_guesses)    # Shows ASCII art (7 stages)
3. display_word(word, guessed)       # Displays word with blanks
4. play_hangman()                    # Main game loop (80 lines)
5. main()                            # Replay control
```

### Function Flow Diagram

```
         ┌──────────┐
         │  START   │
         └────┬─────┘
              │
         ┌────▼─────┐
         │ main()   │ ◄───┐
         │ Replay   │     │
         └────┬─────┘     │
              │           │
         ┌────▼──────────┐│
         │ play_hangman()││
         │  Game Logic   ││
         └────┬──────────┘│
              │           │
    ┌─────────┼───────────┤
    │         │           │
┌───▼───┐ ┌──▼──┐ ┌─────▼──┐
│clear_ │ │disp │ │display_│
│screen │ │hang │ │word()  │
└───────┘ └─────┘ └────────┘
```

### Key Code Snippets

**1. Cross-Platform Screen Clear**
```python
def clear_screen():
    """Clears the terminal screen"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux
        os.system('clear')
```

**2. Comprehensive Input Validation**
```python
# Three-layer validation
if len(guess) != 1 or not guess.isalpha():
    print("⚠️  Please enter a single letter!")
elif guess in guessed_letters:
    print("⚠️  You already guessed that letter!")
```

**3. Word Display Logic**
```python
def display_word(word, guessed_letters):
    """Shows word with blanks for unguessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
```

**4. ASCII Art Stages**
The game includes 7 detailed ASCII art stages (0-6 wrong guesses), stored in a list for easy access based on the current wrong guess count.

---

## 🧪 Testing

### Test Coverage Summary

We conducted comprehensive testing with **20 test cases**:

| Category | Tests | Pass Rate | Status |
|----------|-------|-----------|--------|
| **Input Validation** | 8 | 100% | ✅ Pass |
| **Game Logic** | 6 | 100% | ✅ Pass |
| **Platform Compatibility** | 3 | 100% | ✅ Pass |
| **UI/Display** | 3 | 100% | ✅ Pass |
| **TOTAL** | **20** | **100%** | ✅ **All Pass** |

### Tested Platforms

| Platform | Version | Python | Result |
|----------|---------|--------|--------|
| 🪟 Windows | 10/11 | 3.8-3.10 | ✅ Pass |
| 🍎 macOS | Big Sur+ | 3.8-3.10 | ✅ Pass |
| 🐧 Linux | Ubuntu 20.04+ | 3.8-3.10 | ✅ Pass |

### Performance Metrics

- **Response Time:** < 0.1 seconds
- **Memory Usage:** 15-17 MB
- **CPU Usage:** < 1%
- **Reliability:** Zero crashes in 50+ test games
- **User Satisfaction:** 9.1/10 rating

For detailed test documentation, see the Testing section in [`PROJECT_REPORT.pdf`](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/PROJECT_REPORT.pdf) (Pages 29-33)

---

## 🛠️ Technologies Used

### Programming Language
- **Python 3.6+** - Modern, versatile, beginner-friendly

### Built-in Libraries
| Library | Purpose |
|---------|---------|
| `random` | Random word selection from word bank |
| `os` | Cross-platform screen clearing functionality |

### Development Environment
- **VS Code** - Primary code editor
- **Git** - Version control system
- **GitHub** - Repository hosting

### No External Dependencies! 🎉
This project uses **only Python standard library** - no pip install required!

---

## 📸 Screenshots

### Welcome Screen
```
==================================================
     🎮 WELCOME TO HANGMAN GAME 🎮
==================================================

📝 Instructions:
   - Guess one letter at a time
   - You have 6 wrong guesses before game over
   - Good luck!

Press Enter to start...
```

### Gameplay in Progress
```
==================================================
           🎮 HANGMAN GAME 🎮
==================================================

        --------
        |      |
        |      O
        |     /|\
        |     / 
        |     
     --------

📊 Wrong Guesses: 5/6
🔤 Letters Used: A, E, I, O, U, Z

✨ Word: C O _ P U T E R

--------------------------------------------------
🎯 Enter a letter: 
```

### Victory Screen
```
==================================================
     🎉 CONGRATULATIONS! YOU WON! 🎉
==================================================
     The word was: COMPUTER
==================================================

🔄 Play again? (yes/no): 
```

### Game Over Screen
```
==================================================
           💀 GAME OVER 💀
==================================================

        --------
        |      |
        |      O
        |     /|\
        |     / \
        |     
     --------

     The word was: KEYBOARD
==================================================

🔄 Play again? (yes/no): 
```

---

## 👥 Contributors

### Development Team

<table>
  <tr>
    <td align="center">
      <img src="https://via.placeholder.com/100" width="100px;" alt="Krishnav Rastogi"/><br />
      <b>Krishnav Rastogi</b><br />
      <sub>PRN: 25030422060</sub><br />
      <sub>BBA AI - Section A</sub>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100" width="100px;" alt="Mahek Desai"/><br />
      <b>Mahek Desai</b><br />
      <sub>PRN: 25030422065</sub><br />
      <sub>BBA AI - Section A</sub>
    </td>
  </tr>
</table>

**Institution:** Symbiosis Artificial Intelligence Institute (SAII)  
**Course:** Python Project-Based Learning  
**Program:** BBA AI (Section A) - Semester 1  
**Academic Year:** 2024-2025  
**Submission Date:** November 4, 2025  
**Project Guide:** Dr. Dawa Chyophel Lepcha

---

## 🙏 Acknowledgments

We would like to express our sincere gratitude to:

- **Dr. Dawa Chyophel Lepcha** - Project Guide and Faculty, Python Project-Based Learning, for invaluable guidance and continuous support
- **Symbiosis Artificial Intelligence Institute (SAII)** - For providing resources and academic environment
- **BBA AI Department** - For infrastructure and support
- **Python Software Foundation** - For excellent documentation and Python language
- **Open Source Community** - For learning resources and inspiration
- **Our Peers and Classmates** - For testing and valuable feedback

### Special Thanks
- Stack Overflow community for problem-solving assistance
- GitHub for hosting this project
- Online educational resources that aided our learning

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Krishnav Rastogi & Mahek Desai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Contact & Support

### Need Help?
- 🐛 Report bugs: [Open an Issue](https://github.com/rastogikrishnav085-hue/hangman-python-game/issues)
- 💡 Feature requests: [Open an Issue](https://github.com/rastogikrishnav085-hue/hangman-python-game/issues)
- ⭐ Star this repo if you found it helpful!

### Project Links
- 📁 **Repository:** [GitHub](https://github.com/rastogikrishnav085-hue/hangman-python-game)
- 🎥 **Demo Video:** [Google Drive](https://drive.google.com/file/d/1RHOXdujpIRFbXsqv_bYfY1f-f8D1ldxR/view?usp=sharing)
- 📊 **Presentation:** [View PDF](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/Presentation%20-%20Hangman%20Game-2.pdf)
- 📄 **Project Report:** [View PDF](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/PROJECT_REPORT.pdf)

---

## 🚀 Future Enhancements

### Short-Term (1-2 months)
- [ ] **Difficulty Levels** - Easy (8 attempts), Medium (6), Hard (4)
- [ ] **Expanded Word Bank** - Load from external file, 100+ words
- [ ] **Hint System** - Reveal random letters, show definitions
- [ ] **Score Tracking** - Save high scores, display leaderboard

### Medium-Term (3-6 months)
- [ ] **GUI Version** - Tkinter-based graphical interface
- [ ] **Multiplayer Mode** - Two-player word entry/guessing
- [ ] **Statistics Tracking** - Games played, win/loss ratio
- [ ] **Multiple Categories** - Animals, movies, countries, etc.

### Long-Term (6+ months)
- [ ] **Web Application** - Flask/Django implementation
- [ ] **Mobile App** - Android and iOS versions
- [ ] **AI Opponent** - Computer guessing using letter frequency
- [ ] **Sound Effects** - Audio feedback for actions
- [ ] **Achievements System** - Unlock badges and rewards

See [PROJECT_REPORT.pdf](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/PROJECT_REPORT.pdf) pages 43-46 for detailed enhancement plans.

---

## 📚 Learning Resources

### Python Learning
- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

### Game Development in Python
- [Python Arcade Library](https://api.arcade.academy/)
- [Pygame Tutorials](https://www.pygame.org/wiki/tutorials)
- [GeeksforGeeks Python Games](https://www.geeksforgeeks.org/python-programming-examples/)

---

## 📖 Project Documentation

This repository includes comprehensive documentation:

1. **README.md** (This file) - Overview and quick start guide
2. **[PROJECT_REPORT.pdf](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/PROJECT_REPORT.pdf)** - Complete 53-page academic report including:
   - Introduction and background
   - Literature review
   - Methodology and system design
   - Implementation details
   - Testing and results
   - Applications and limitations
   - Future work
3. **[Presentation - Hangman Game-2.pdf](https://github.com/rastogikrishnav085-hue/hangman-python-game/blob/main/Presentation%20-%20Hangman%20Game-2.pdf)** - Project presentation slides
4. **HangMan.py** - Well-commented source code (217 lines)

---

## ⭐ Show Your Support

Give a ⭐ if this project helped you learn Python or game development!

### Why Star This Repository?
- ✅ Supports student developers
- ✅ Helps others discover the project
- ✅ Encourages open-source contribution
- ✅ Shows appreciation for educational content

---

## 📊 Project Statistics

- **Total Lines of Code:** 217
- **Number of Functions:** 5
- **Word Bank Size:** 10 words
- **ASCII Art Stages:** 7 stages
- **Test Cases:** 20 (100% pass rate)
- **Development Time:** 2 weeks
- **Documentation Pages:** 53 (report) + this README
- **Supported Platforms:** 3 (Windows, macOS, Linux)

---

<p align="center">
  <b>Krishnav Rastogi & Mahek Desai</b><br/>
  <sub>Symbiosis Artificial Intelligence Institute (SAII) | 2024-2025</sub><br/>
  <sub>BBA AI Section A | Semester 1</sub>
</p>

---

<div align="center">

**[⬆ Back to Top](#-hangman-game---python-mini-project)**

---

*"Learning is a treasure that will follow its owner everywhere."*

---

**Last Updated:** November 4, 2025

</div>

## Contributors
- krishnavrastogi2025
