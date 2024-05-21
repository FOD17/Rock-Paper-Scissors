import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize counters for the tally
user_wins = 0
computer_wins = 0

# Function to determine the result of the game
def determine_winner(user_choice, computer_choice):
    global user_wins, computer_wins
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_wins += 1
        update_tally()
        return "You win!"
    else:
        computer_wins += 1
        update_tally()
        return "You lose!"

# Function to update the tally
def update_tally():
    user_tally_label.config(text=f"User Wins: {user_wins}")
    computer_tally_label.config(text=f"Computer Wins: {computer_wins}")

# Function to handle the user's choice
def user_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    user_image = images[choice].resize((256, 256), Image.LANCZOS)
    computer_image = images[computer_choice].resize((256, 256), Image.LANCZOS)
    
    user_image_tk = ImageTk.PhotoImage(user_image)
    computer_image_tk = ImageTk.PhotoImage(computer_image)
    
    user_choice_label.config(image=user_image_tk)
    user_choice_label.image = user_image_tk
    
    computer_choice_label.config(image=computer_image_tk)
    computer_choice_label.image = computer_image_tk
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Loading images
rock_img = Image.open("./assets/rock.jpg")
paper_img = Image.open("./assets/paper.jpg")
scissors_img = Image.open("./assets/scissors.jpg")

images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

# Adding a frame for the tally
tally_frame = tk.Frame(root)
tally_frame.pack(pady=10)

# Adding labels for the tally
user_tally_label = tk.Label(tally_frame, text=f"User Wins: {user_wins}", font=("Helvetica", 14))
user_tally_label.grid(row=0, column=0, padx=20)

computer_tally_label = tk.Label(tally_frame, text=f"Computer Wins: {computer_wins}", font=("Helvetica", 14))
computer_tally_label.grid(row=0, column=1, padx=20)

# Adding a frame for the choices
choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)

# Adding labels for user and computer choices
user_choice_text = tk.Label(choices_frame, text="Your Choice", font=("Helvetica", 16))
user_choice_text.grid(row=0, column=1, padx=20)

computer_choice_text = tk.Label(choices_frame, text="Computer's Choice", font=("Helvetica", 16))
computer_choice_text.grid(row=0, column=0, padx=20)

# Adding placeholders for images
placeholder_img = ImageTk.PhotoImage(Image.open("./assets/gray-square.jpg"))

computer_choice_label = tk.Label(choices_frame, image=placeholder_img)
computer_choice_label.grid(row=1, column=0)

user_choice_label = tk.Label(choices_frame, image=placeholder_img)
user_choice_label.grid(row=1, column=1)

# Adding a label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 16))
label.pack(pady=20)

# Adding buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"), height=2, width=15)
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"), height=2, width=15)
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"), height=2, width=15)
scissors_button.pack(pady=5)

# Adding labels to display the computer's choice and result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Running the main event loop
root.mainloop()
