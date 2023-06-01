from tkinter import Tk, Label, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

root = Tk()
root.title("Registration")
root.geometry("900x900+150+50")
root.resizable(False, False)

def login_page():
    pass

def get_data():
    first_name = firstname.get()
    last_name = lastname.get()
    user_name = username.get()
    email_data = email.get()
    phone_data = phone.get()
    
    if first_name and last_name and user_name and email_data and phone_data != '':
        messagebox.showinfo('SIGN UP', 'Sign up successful!')
    else:
        messagebox.showerror('Error', "Data cannot be empty!")

### Background Image
regi_img = Image.open("login_assets/registation.jpg")
regi_resize = regi_img.resize((900, 900))
regi_image = ImageTk.PhotoImage(image=regi_resize)

Label(root, image=regi_image).place(x=0, y=0)


# first name
firstname = ctk.CTkEntry(root, width=150, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='First Name', 
                         corner_radius=10,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
firstname.place(x=120, y=360)

# last name
lastname = ctk.CTkEntry(root, width=150, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Last Name', 
                         corner_radius=10,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
lastname.place(x=296, y=360)

# username
username = ctk.CTkEntry(root, width=330, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Username', 
                         corner_radius=10,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
username.place(x=120, y=424)

# email
email = ctk.CTkEntry(root, width=330, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Email', 
                         corner_radius=10,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
email.place(x=120, y=485)

# Phone
phone = ctk.CTkEntry(root, width=330, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Phone', 
                         corner_radius=10,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
phone.place(x=120, y=550)


## already have an account
ctk.CTkButton(root, text="Already have an Account?",
                     font=('Arial', 12),
                     bg_color='#fff',
                     text_color='blue',
                     fg_color='#ffffff',
                     hover=False,
                     command=login_page
                     ).place(x=200, y=605)


### Register button
regi_button = ctk.CTkButton(root, text='Register', 
                            width=250, height=55, 
                            corner_radius=10, 
                            border_color='black', 
                            border_width=1, 
                            hover_color='#4d527a',
                            font=('Arial', 18),
                            command=get_data
                            )
regi_button.place(x=160, y=628)



root.mainloop()