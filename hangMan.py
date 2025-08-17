import tkinter as tk
import random

COLORS = {
    'bg': '#1e1e2f',           # Deep space blue-purple
    'fg': '#e0e0e0',           # Soft white text
    'button': '#00bcd4',       # Cyan button
    'button_fg': '#0a0a0a',    # Dark text on light button
    'highlight': '#00e676',    # Neon green for restart
    'game_over': '#ff5252',    # Bright red for game over
    'win': '#69f0ae'           # Bright mint green for win
}

# Fonts
FONT_LARGE = ("Consolas", 26, "bold")
FONT_MEDIUM = ("Consolas", 18)
FONT_SMALL = ("Consolas", 14)

# Word -> Hint Dictionary
WORDS_HINTS = {
    "python": "A popular programming language.",
    "hangman": "A classic word guessing game.",
    "computer": "An electronic device that processes data.",
    "programming": "The act of writing code.",
    "developer": "A person who builds software.",
    "interface": "A shared boundary for interaction.",
    "algorithm": "A step-by-step problem-solving method.",
    "software": "Programs and operating systems.",
    "keyboard": "Hardware used to type.",
    "designer": "Creates visuals and layouts.",
    "engineer": "Builds technical systems.",
    "project": "A structured software task.",
    "debugging": "Fixing code errors.",
    "terminal": "Text interface for command input.",
    "function": "A reusable block of code.",
    "variable": "Stores a value in programming.",
    "condition": "Used in decision-making logic.",
    "iteration": "Repeating a process.",
    "compiler": "Converts code to machine language.",
    "gaming": "Playing interactive video games.",
    "graphics": "Visual elements of a program.",
    "hardware": "Physical parts of a computer.",
    "frontend": "The part of software users see.",
    "backend": "Server-side of software.",
    "database": "Stores organized information.",
    "framework": "A software development skeleton.",
    "repository": "A code storage location (e.g., GitHub).",
    "cloud": "Remote servers accessed online.",
    "network": "Connected computers and devices.",
    "stack": "Combination of tech used together."
}

# Global game state
word = ""
guessed_letters = set()
attempts_left = 6

def choose_word():
    word = random.choice(list(WORDS_HINTS.keys()))
    return word.lower(), WORDS_HINTS[word]

def update_word_display(word_label):
    display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    word_label.config(text=f"Word: {display}")

def disable_buttons(buttons_frame):
    for widget in buttons_frame.winfo_children():
        widget.config(state=tk.DISABLED)

def handle_guess(letter, word_label, attempts_label, message_label, buttons_frame):
    global attempts_left
    if letter in guessed_letters:
        return
    guessed_letters.add(letter)

    if letter in word:
        update_word_display(word_label)
        if all(l in guessed_letters for l in word):
            message_label.config(text="🎉 You Won! 🎉", fg=COLORS['win'])
            disable_buttons(buttons_frame)
    else:
        attempts_left -= 1
        attempts_label.config(text=f"Attempts Left: {attempts_left}")
        if attempts_left == 0:
            update_word_display(word_label)
            message_label.config(text=f"💀 Game Over! Word was: {word}", fg=COLORS['game_over'])
            disable_buttons(buttons_frame)

def create_alphabet_buttons(buttons_frame, word_label, attempts_label, message_label):
    for widget in buttons_frame.winfo_children():
        widget.destroy()
    for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        button = tk.Button(buttons_frame, text=letter.upper(), width=4, height=2,
                           bg=COLORS['button'], fg=COLORS['button_fg'], font=FONT_SMALL,
                           activebackground=COLORS['highlight'],
                           command=lambda l=letter: handle_guess(l, word_label, attempts_label, message_label, buttons_frame))
        button.grid(row=i // 13, column=i % 13, padx=3, pady=3)

def start_game(window, word_label, attempts_label, message_label, hint_label, buttons_frame):
    global word, guessed_letters, attempts_left
    word, hint = choose_word()
    guessed_letters = set()
    attempts_left = 6
    message_label.config(text="", fg=COLORS['fg'])
    update_word_display(word_label)
    hint_label.config(text=f"💡 Hint: {hint}")
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    create_alphabet_buttons(buttons_frame, word_label, attempts_label, message_label)

def setup_ui(window):
    window.title("🎮 Hangman ")
    window.geometry("850x680")
    window.configure(bg=COLORS['bg'])

    title_label = tk.Label(window, text="🧠 Hangman Game", fg=COLORS['highlight'], bg=COLORS['bg'], font=FONT_LARGE)
    title_label.pack(pady=20)

    word_label = tk.Label(window, text="", fg=COLORS['fg'], bg=COLORS['bg'], font=FONT_MEDIUM)
    word_label.pack(pady=10)

    hint_label = tk.Label(window, text="", fg=COLORS['highlight'], bg=COLORS['bg'], font=FONT_SMALL)
    hint_label.pack(pady=5)

    attempts_label = tk.Label(window, text="", fg=COLORS['fg'], bg=COLORS['bg'], font=FONT_MEDIUM)
    attempts_label.pack(pady=5)

    message_label = tk.Label(window, text="", fg=COLORS['fg'], bg=COLORS['bg'], font=FONT_MEDIUM)
    message_label.pack(pady=10)

    buttons_frame = tk.Frame(window, bg=COLORS['bg'])
    buttons_frame.pack(pady=10)

    restart_button = tk.Button(window, text="🔁 Restart Game", font=FONT_SMALL,
                               bg=COLORS['highlight'], fg=COLORS['button_fg'],
                               activebackground=COLORS['button'], width=18,
                               command=lambda: start_game(window, word_label, attempts_label, message_label, hint_label, buttons_frame))
    restart_button.pack(pady=20)

    start_game(window, word_label, attempts_label, message_label, hint_label, buttons_frame)

def main():
    window = tk.Tk()
    setup_ui(window)
    window.mainloop()

if __name__ == "__main__":
    main()
