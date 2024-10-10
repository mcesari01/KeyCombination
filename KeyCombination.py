import tkinter as tk
from character_map import character_map

def find_combination(character):
    return character_map.get(character, 'Combination not found')

def get_response():
    entered_character = character_entry.get().strip()  # Remove any whitespace
    key_combination = find_combination(entered_character)
    response_label.config(text=f'Key Comb.: {key_combination}')

app = tk.Tk()
app.title('Key Combination App')

instruction_label = tk.Label(app, text='Enter a character:', font=('Arial', 14))
instruction_label.pack(pady=10)

character_entry = tk.Entry(app, font=('Arial', 14))
character_entry.pack(pady=10)

calculate_button = tk.Button(app, text='Calculate Combination', command=get_response, font=('Arial', 14))
calculate_button.pack(pady=20)

response_label = tk.Label(app, text='', font=('Arial', 16, 'bold'))
response_label.pack(pady=10)

app.mainloop()
