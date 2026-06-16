# Snake Water Gun Game - GUI Version using Tkinter

import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x400")
root.config(bg="lightblue")


# Choices dictionary
choices = {
    "s": "Snake 🐍",
    "w": "Water 💧",
    "g": "Gun 🔫"
}


# Result function
def play(user):

    computer = random.choice(["s", "w", "g"])

    user_choice_label.config(
        text=f"You Chose: {choices[user]}"
    )

    computer_choice_label.config(
        text=f"Computer Chose: {choices[computer]}"
    )

    # Game Logic
    if user == computer:
        result = "🤝 Match Draw!"

    elif (
        (user == "s" and computer == "w") or
        (user == "w" and computer == "g") or
        (user == "g" and computer == "s")
    ):
        result = "🎉 You Win!"

    else:
        result = "😢 You Lose!"

    result_label.config(text=result)


# Heading
heading = tk.Label(
    root,
    text="Snake Water Gun Game",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)

heading.pack(pady=20)


# Buttons
snake_btn = tk.Button(
    root,
    text="Snake 🐍",
    font=("Arial", 14),
    width=15,
    command=lambda: play("s")
)

snake_btn.pack(pady=10)


water_btn = tk.Button(
    root,
    text="Water 💧",
    font=("Arial", 14),
    width=15,
    command=lambda: play("w")
)

water_btn.pack(pady=10)


gun_btn = tk.Button(
    root,
    text="Gun 🔫",
    font=("Arial", 14),
    width=15,
    command=lambda: play("g")
)

gun_btn.pack(pady=10)


# User choice label
user_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="lightblue"
)

user_choice_label.pack(pady=10)


# Computer choice label
computer_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="lightblue"
)

computer_choice_label.pack(pady=10)


# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="red"
)

result_label.pack(pady=20)


# Run window
root.mainloop()