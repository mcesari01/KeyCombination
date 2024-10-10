import tkinter as tk
from character_map import character_map
from word_to_symbol import word_to_symbol

def find_combination(input_text):
    symbol = word_to_symbol.get(input_text.lower(), input_text)
    return character_map.get(symbol, 'Combination not found / Combinazione non trovata')

def get_response():
    entered_text = character_entry.get().strip()
    key_combination = find_combination(entered_text)
    response_label.config(text=f'Key Comb.: {key_combination}')

app = tk.Tk()
app.title('Key Combination App')

instruction_label = tk.Label(app, text='Enter a character or word (e.g., tilde, at):', font=('Arial', 14))
instruction_label.pack(pady=10)

character_entry = tk.Entry(app, font=('Arial', 14))
character_entry.pack(pady=10)

calculate_button = tk.Button(app, text='Calculate Combination', command=get_response, font=('Arial', 14))
calculate_button.pack(pady=20)

response_label = tk.Label(app, text='', font=('Arial', 16, 'bold'))
response_label.pack(pady=10)

app.mainloop()
