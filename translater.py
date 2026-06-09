import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    source = source_lang.get()
    target = target_lang.get()

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def copy_text():
    translated = output_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(translated)
    messagebox.showinfo("Copied", "Translated text copied!")


root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "bengali": "bn",
    "marathi": "mr",
    "telugu": "te",
    "bhojpuri": "bho",
    "oriaya": "or" 
}

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)

input_text = tk.Text(root, height=7, width=70)
input_text.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Source Language").grid(row=0, column=0, padx=10)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
source_lang.grid(row=1, column=0)
source_lang.set("English")

tk.Label(frame, text="Target Language").grid(row=0, column=1, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
target_lang.grid(row=1, column=1)
target_lang.set("Hindi")

translate_btn = tk.Button(
    root,
    text="Translate",
    command=lambda: translate_action(),
    bg="lightblue"
)
translate_btn.pack(pady=10)

tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack()

output_text = tk.Text(root, height=7, width=70)
output_text.pack(pady=5)

copy_btn = tk.Button(
    root,
    text="Copy Translation",
    command=copy_text
)
copy_btn.pack(pady=10)


def translate_action():
    source_code = languages[source_lang.get()]
    target_code = languages[target_lang.get()]

    text = input_text.get("1.0", tk.END).strip()

    if text:
        translated = GoogleTranslator(
            source=source_code,
            target=target_code
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)


root.mainloop()