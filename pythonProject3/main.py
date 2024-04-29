import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=False):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters.strip():
        messagebox.showerror("Eroare", "Vă rog selectați măcar un set de caractere.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)
    if password:
        generated_password_label.config(text="Parola generată: " + password)


window = tk.Tk()
window.title("Password Generator")
window.attributes("-fullscreen", True)

#definirea variabilelor
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar()


background_image = tk.PhotoImage(file="C:\\Users\\elena\\pythonProject3\\.venv\\Scripts\\parola.png")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

background_image = background_image.subsample(int(background_image.width() / screen_width), int(background_image.height() / screen_height))

canvas = tk.Canvas(window, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")


length_label = tk.Label(window, text="Lungimea parolei:", bg="white", fg="#2980B9", font=("Arial", 16))
length_label.place(relx=0.5, rely=0.2, anchor="center")
length_entry = tk.Entry(window, font=("Arial", 14))
length_entry.place(relx=0.5, rely=0.25, anchor="center")


checkbox_font = ("Arial", 14)
uppercase_check = tk.Checkbutton(window, text="Include majuscule", variable=uppercase_var, bg="white", fg="#2980B9", selectcolor="white", font=checkbox_font)
uppercase_check.place(relx=0.5, rely=0.35, anchor="center")
lowercase_check = tk.Checkbutton(window, text="Include minuscule", variable=lowercase_var, bg="white", fg="#2980B9", selectcolor="white", font=checkbox_font)
lowercase_check.place(relx=0.5, rely=0.4, anchor="center")
digits_check = tk.Checkbutton(window, text="Include cifre", variable=digits_var, bg="white", fg="#2980B9", selectcolor="white", font=checkbox_font)
digits_check.place(relx=0.5, rely=0.45, anchor="center")
special_chars_check = tk.Checkbutton(window, text="Include caractere speciale", variable=special_chars_var, bg="white", fg="#2980B9", selectcolor="white", font=checkbox_font)
special_chars_check.place(relx=0.5, rely=0.5, anchor="center")

button_font = ("Arial", 16)
generate_button = tk.Button(window, text="Generează parola", command=generate_password_gui, bg="#3498DB", fg="white", relief="flat", font=button_font)
generate_button.place(relx=0.5, rely=0.6, anchor="center")


password_font = ("Arial", 18)
generated_password_label = tk.Label(window, text="", bg="white", fg="#2980B9", font=password_font)
generated_password_label.place(relx=0.5, rely=0.7, anchor="center")

# Run Tkinter event loop
window.mainloop()
