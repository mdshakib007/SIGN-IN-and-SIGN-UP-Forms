from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Registration")
root.geometry("900x900+150+50")
root.resizable(False, False)


def get_data():
    username_data = user_name.get()
    password_data = password.get()
    
    if username_data and password_data != '':
        messagebox.showinfo("Successful", "Login Successful!")
        
    else:
        messagebox.showerror("Error", "Data cannot be empty!")

### Background Image
login_ = Image.open("login_assets/blur_login.jpg")
login_resize = login_.resize((900, 900))
login = ImageTk.PhotoImage(image=login_resize)

Label(root, image=login).place(x=0, y=0)

## Entries
user_name = ctk.CTkEntry(root, width=321, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='E-mail', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
user_name.place(x=310, y=397)

password = ctk.CTkEntry(root, width=321, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='Password', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
password.place(x=310, y=479)


### Checkbox
ctk.CTkCheckBox(root, text='Remember me', 
                text_color='black', 
                bg_color='#235ca3', 
                checkmark_color='white',
                width=140,
                corner_radius=10 
                ).place(x=270, y=582)


ctk.CTkButton(root, text='forgot password?',
              border_width=0,
              corner_radius=0,
              border_spacing=5,
              font=('Arial', 14, 'italic', 'underline'),
              hover=False,
              text_color='black'
              ).place(x=496, y=578)


### login button
ctk.CTkButton(root, text='LOGIN',
              font=("Arial", 18), 
              corner_radius=0,
              height=60, width=380,
              command=get_data
              ).place(x=262, y=643)



root.mainloop()