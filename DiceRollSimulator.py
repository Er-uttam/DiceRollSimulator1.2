

# import random
# print("----DICE ROLL SIMULATOR----")
# while True:
#   print("---PLEASE TYPE---")
#   print("1. FOR ROLL THE DICE.")
#   print("2. FOR QUIT \n")
#   user_input = int(input("Enter here : "))
#   if user_input==1:
#     number = random.randint(1,6)
#     print("The Number is :",number)
#   else:
#     print("Successfully Quit The Simulator.")
#     break


import tkinter as tk
import random

# Function to roll the dice
def roll_dice():
    number = random.randint(1, 6)
    result_label.config(text=f"The Number is: {number}")

# Function to quit the application
def quit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Dice Roll Simulator")

# Create and place widgets
roll_button = tk.Button(root, text="Roll the Dice", command=roll_dice)
roll_button.pack(pady=20)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the application
root.mainloop()
