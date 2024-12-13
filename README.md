# Flash Card App

## Description

The Flash Card App is a simple Python program that helps users learn Spanish vocabulary through flashcards. The app uses the `Tkinter` library for its graphical interface and the `pandas` library to manage the words data.

## Features

- Displays Spanish words on one side of the card and their English translations on the other.
- Allows users to mark words as "known" to track progress.
- Saves progress to a file for future study sessions.

## Requirements

- Python 3.9+
- Libraries:
  - `tkinter`
  - `pandas`
  - `random`
  - `os`

## How to Run

1. Install Python and required libraries.
2. Place the `data/Spanish_Words.csv` file in the appropriate directory.
3. Place the images (`wrong.png`, `right.png`, `card_back.png`, `card_front.png`) in the `images` folder.
4. Run the script using:

   ```bash
   python flash_card_app.py
   ```

## File Structure

```
.
├── data
│   ├── Spanish_Words.csv
│   ├── words_to_learn.csv (Generated after running the program)
├── images
│   ├── wrong.png
│   ├── right.png
│   ├── card_back.png
│   ├── card_front.png
├── flash_card_app.py
└── README.md
```

## Controls

- **Flip Card**: Shows the English translation of the word.
- **Check Button**: Marks the word as "known."
- **Wrong Button**: Skips to the next card.

## License

This project is licensed under the MIT License.
