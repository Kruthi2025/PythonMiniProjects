import tkinter as tk

# Define story and placeholders
story = """Yesterday, I went to the **place** to meet my **adjective** friend **name**. We decided to **verb** to the **place**. On the way, we saw a **adjective** **noun**.

After reaching the **place**, we **verb** for a while and then decided to **verb** a delicious **food**. It was a **adjective** day filled with **noun** and laughter.

I can't wait to do it again with **name**!"""

placeholders = {
    "place": ["park", "beach", "mall"],
    "adjective": ["funny", "exciting", "beautiful"],
    "name": "Emily",
    "verb": ["walk", "explore", "eat"],
    "noun": ["bird", "flower", "movie"],
    "food": ["pizza", "ice cream", "burger"]
}

def generate_story():
    user_inputs = {}
    for placeholder, options in placeholders.items():
        user_input = entry_widgets[placeholder].get()
        if placeholder == "verb":
            # Allow multiple verbs separated by commas
            user_inputs[placeholder] = [verb.strip() for verb in user_input.split(",")]
        else:
            user_inputs[placeholder] = user_input.strip()

    completed_story = story
    for placeholder, value in user_inputs.items():
        if isinstance(value, list):
            # If value is a list, replace each occurrence of the placeholder in the story
            for item in value:
                completed_story = completed_story.replace(placeholder, item, 1)
        else:
            # If value is a single string, replace the placeholder in the story
            completed_story = completed_story.replace(placeholder, value)
    story_label.config(text=completed_story)

# Create the main window
root = tk.Tk()
root.title("Mad Libs Generator")

# Add labels and entry fields for each placeholder
entry_widgets = {}
for placeholder, options in placeholders.items():
    label = tk.Label(root, text=f"{placeholder}:")
    label.pack()
    entry = tk.Entry(root, width=20)
    entry.pack()
    entry_widgets[placeholder] = entry

# Add a button to generate the story
generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack()

# Add a label to display the completed story
story_label = tk.Label(root, text="")
story_label.pack()

# Start the event loop
root.mainloop()
