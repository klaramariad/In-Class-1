import random
import tkinter as tk

# ASCII Art for each move
moves_art = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    "paper": '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

# Determine winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "YOU WON!"
    else:
        return "YOU LOST!"

# Main function to play a round
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    user_label.config(text=f"Your choice:\n{user_choice}\n{moves_art[user_choice]}")
    comp_label.config(text=f"Computer's choice:\n{computer_choice}\n{moves_art[computer_choice]}")
    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("700x500")
root.config(padx=20, pady=20, bg="#f0f0f0")

# Labels
user_label = tk.Label(root, text="Your choice will appear here", justify="left", font=("Courier", 10), bg="#f0f0f0")
user_label.grid(row=0, column=0, padx=10, pady=10)

comp_label = tk.Label(root, text="Computer's choice will appear here", justify="left", font=("Courier", 10), bg="#f0f0f0")
comp_label.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.grid(row=1, column=0, columnspan=2, pady=20)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=2, column=0, columnspan=2)

rock_button = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("scissors"))

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

# Start the GUI event loop
root.mainloop()