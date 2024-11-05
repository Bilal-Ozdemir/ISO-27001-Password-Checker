#Created By Bilal Ozdemir on November 11, 2024

import customtkinter
import re
import webbrowser

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1000x850")

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."
    if not re.search(r"[\W_]", password):
        return "Password must contain at least one special character (e.g., @, #, $, etc.)."
    if re.search(r"(1234|abcd|password|qwerty|letmein)", password.lower()):
        return "Password contains a predictable pattern or common sequence."
    return True

def password():
    entered_password = entry1.get()
    validation_result = validate_password(entered_password)
    if validation_result == True:
        result_label.configure(text="Password is strong!", text_color="#28a745")
    else:
        result_label.configure(text=validation_result, text_color="#dc3545")

def open_url(event):
    webbrowser.open("https://www.iso.org/standard/27001")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="ISO 27001 Password Checker", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Password")
entry1.pack(pady=12, padx=30)

button = customtkinter.CTkButton(master=frame, text="Check Password", command=password)
button.pack(pady=12, padx=10)

result_label = customtkinter.CTkLabel(master=frame, text="", font=("Roboto", 16))
result_label.pack(pady=12)

iso_explanation = """What is ISO 27001?\n\nISO 27001 is an international standard for managing information security. 
It provides a framework for establishing, implementing, operating, monitoring, reviewing, 
maintaining, and improving an Information Security Management System (ISMS). The goal of 
ISO 27001 is to ensure that sensitive information remains secure by addressing people, processes, 
and technology. Adhering to ISO 27001 helps organizations protect data and meet regulatory requirements."""

iso_label = customtkinter.CTkLabel(master=frame, text=iso_explanation, font=("Roboto", 14), wraplength=700, justify="left")
iso_label.pack(pady=20, padx=30)


more_info_label = customtkinter.CTkLabel(master=frame, text="For more info, visit: https://www.iso.org/standard/27001", font=("Roboto", 14), text_color="yellow", cursor="hand2")
more_info_label.pack(pady=10)


more_info_label.bind("<Button-1>", open_url)

footer_label = customtkinter.CTkLabel(master=frame, text="© 2024 Created by Bilal Ozdemir", font=("Roboto", 22), text_color="yellow")
footer_label.pack(side="bottom", pady=80)

root.mainloop()



