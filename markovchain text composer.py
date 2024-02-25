import tkinter as tk
from tkinter import filedialog
import random

class MarkovTextComposer:
    def __init__(self, master):
        self.master = master
        master.title("Markov Chain Text Composer")

        self.text = tk.Text(master)
        self.text.pack()

        self.load_button = tk.Button(master, text="Load Text File", command=self.load_text_file)
        self.load_button.pack()

        self.generate_button = tk.Button(master, text="Generate Text", command=self.generate_text)
        self.generate_button.pack()

    def load_text_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete('1.0', 'end')
                self.text.insert('1.0', file.read())
        else:
            print("No file selected!")

    def generate_text(self):
        text = self.text.get('1.0', 'end-1c')
        if text:
            markov_chain = self.generate_markov_chain(text)
            generated_text = self.generate_text_from_chain(markov_chain)
            print("Generated Text:\n", generated_text)
        else:
            print("No text provided!")

    def generate_markov_chain(self, text, order=2):
        words = text.split()
        markov_chain = {}

        for i in range(len(words) - order):
            prefix = tuple(words[i:i+order])
            suffix = words[i+order]

            if prefix in markov_chain:
                markov_chain[prefix].append(suffix)
            else:
                markov_chain[prefix] = [suffix]

        return markov_chain

    def generate_text_from_chain(self, markov_chain, length=100):
        prefix = random.choice(list(markov_chain.keys()))
        text = list(prefix)

        while len(text) < length:
            if prefix in markov_chain:
                next_word = random.choice(markov_chain[prefix])
                text.append(next_word)
                prefix = tuple(text[-len(prefix):])
            else:
                break

        return ' '.join(text)

root = tk.Tk()
app = MarkovTextComposer(root)
root.mainloop()
