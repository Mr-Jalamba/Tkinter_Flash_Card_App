from tkinter import *
from tkinter import messagebox
import pandas
from random import *
import os

# Constants for UI design
BACKGROUND_COLOR = "#B1DDC6"  # Background color for the app
FONT_NAME = "Arial"  # Font used in the app
SPANISH_FILE_PATH = "data/Spanish_Words.csv"  # File containing original Spanish words
FILE_PATH = "data/words_to_learn.csv"  # File to save progress
ORIENT = "records"  # Orientation for pandas DataFrame conversion
current_card = {}  # Stores the current card data
to_learn = {}  # Dictionary of words to learn
words_to_learn = []  # List of words the user is currently studying


# Load cards data from CSV files
def get_cards():
    global to_learn
    try:
        data = pandas.read_csv(FILE_PATH)  # Try to load user's progress
    except FileNotFoundError:
        # If no progress file exists, load the original set of words
        original_data = pandas.read_csv(SPANISH_FILE_PATH)
        to_learn = original_data.to_dict(orient=ORIENT)
    except pandas.errors.EmptyDataError:
        # Handle empty progress file by resetting to original words
        original_data = pandas.read_csv(SPANISH_FILE_PATH)
        to_learn = original_data.to_dict(orient=ORIENT)
    else:
        # Load user's progress into the `to_learn` dictionary
        to_learn = data.to_dict(orient=ORIENT)


# Display the next flashcard
def next_card():
    global current_card
    global words_to_learn
    if words_to_learn:
        # Display a random word from words_to_learn
        canvas.itemconfig(card_face, image=card_front_img)
        current_card = choice(words_to_learn)
        canvas.itemconfig(language_text, text="Spanish", fill="black")
        canvas.itemconfig(word_text, text=current_card["Spanish"], fill="black")
    elif to_learn:
        # If no specific words_to_learn, choose from the `to_learn` list
        canvas.itemconfig(card_face, image=card_front_img)
        current_card = choice(to_learn)
        canvas.itemconfig(language_text, text="Spanish", fill="black")
        canvas.itemconfig(word_text, text=current_card["Spanish"], fill="black")
    else:
        # If all cards are learned, show a message and restart
        messagebox.showerror(title="Done", message="There are no more cards to study.\nRestarting Session...")
        get_cards()


# Flip the card to show the English translation
def flip_card():
    canvas.itemconfig(card_face, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# Mark the word as known and update the progress
def word_known():
    try:
        if len(words_to_learn) < 1:
            # If no words left, delete the progress file
            os.remove(FILE_PATH)
        # Remove the current card from `to_learn`
        to_learn.remove(current_card)
    except ValueError:
        pass  # Ignore if card is already removed
    except FileNotFoundError:
        pass  # Ignore if progress file is missing
    finally:
        print(len(to_learn))  # Debugging: Print remaining words
        save_to_file()  # Save updated progress to file
        next_card()  # Move to the next card


# Save the `to_learn` dictionary to a CSV file
def save_to_file():
    df = pandas.DataFrame(to_learn)
    df.to_csv(FILE_PATH, index=False)


# Initialize the Tkinter window
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Load images for UI
x_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

# Set up the canvas for flashcards
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_face = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(columnspan=3)

# Buttons for interactions
x_button = Button(command=next_card, image=x_image, highlightthickness=0)
x_button.grid(row=1, column=0)

check_button = Button(command=word_known, image=check_image, highlightthickness=0)
check_button.grid(row=1, column=2)

flip_button = Button(command=flip_card, text="Flip Card", font=(FONT_NAME, 21, "bold"))
flip_button.grid(row=1, column=1)

# Load initial cards and start the app
get_cards()
next_card()

window.mainloop()
