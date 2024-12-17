from tkinter import messagebox as msgbox
import pyperclip
from customtkinter import CTk, CTkButton, CTkLabel, set_appearance_mode, set_default_color_theme
from urllib.request import Request, urlopen
import random

def passwordMaker():
    signs = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', ',', '.', '/', '?', '\\', '|', ':', ';']
    random_number = random.randint(0, 1000)

    url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req).read()

    webpage = web_byte.decode('utf-8')
    everything = webpage[::].split("\n")
    random.shuffle(everything)

    replace_word = random.choice(everything).capitalize()

    random_sign = random.choice(signs)

    all_of_them = [replace_word, str(random_number), random_sign]
    random.shuffle(all_of_them)

    return ''.join(all_of_them)

class pwd:
        
    @classmethod
    def generate_password(cls):
        
        global password
        cls.password = passwordMaker()
        password_label.configure(text=cls.password)
    
    @classmethod
    def copy_password(cls):
        pyperclip.copy(cls.password)
        msgbox.showinfo(title="Password Copied", message=f"Password '{cls.password}' copied to clipboard!")



# Create the main window
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = CTk()
root.title("Password Generator")

root.geometry("300x240")

# Create a button
generate_button = CTkButton(root, text="Generate Password", command=pwd.generate_password)
generate_button.pack(pady=20)

# Create a button TO copy The Text
generate_button = CTkButton(root, text="Copy Password", command=pwd.copy_password)
generate_button.pack(pady=10)

exit_button = CTkButton(root, text="Exit", command=root.quit, width=60)
exit_button.pack(pady=20)

# Create a label to display the password
password_label = CTkLabel(root, text="", font=("Helvetica", 16))
password_label.pack(pady=10)

# Start the GUI main loop
root.mainloop()
