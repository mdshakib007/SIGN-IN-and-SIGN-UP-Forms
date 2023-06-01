from tkinter import Tk, messagebox, Label
from PIL import Image, ImageTk
import customtkinter as ctk

root = Tk()
root.title("Registration")
root.geometry("1200x800+150+50")
root.resizable(False, False)


### Get data 
def get_data():
    firstname_data = firstname.get()
    lastname_data = lastname.get()
    email_data = email.get()
    password_data = phone.get()
    
    if firstname_data and lastname_data and email_data and password_data != '':
        messagebox.showinfo('SIGN UP', 'Sign up successful!')
    else:
        messagebox.showerror('Error', "Data cannot be empty!")


### Background Image
regi_img = Image.open("login_assets/loginbg.png")
regi_resize = regi_img.resize((800, 800))
regi_image = ImageTk.PhotoImage(image=regi_resize)

Label(root, image=regi_image).place(x=0, y=0)


### label for title
ctk.CTkLabel(root, text='Registration', 
             font=('Serif', 36), 
             text_color='#000'
             ).place(x=820, y=140)


# first name
firstname = ctk.CTkEntry(root, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='First Name', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
firstname.place(x=800, y=250)

# last name
lastname = ctk.CTkEntry(root, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Last Name', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
lastname.place(x=800, y=300)

# email
email = ctk.CTkEntry(root, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Email', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
email.place(x=800, y=350)

# Phone
phone = ctk.CTkEntry(root, width=300, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=1, 
                         placeholder_text='Phone', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
phone.place(x=800, y=400)


# registartion button
ctk.CTkButton(root, text='Register', 
              font=('Arial', 18),
              width=180, height=40,
              command=get_data 
              ).place(x=920, y=470)

# cancel button
ctk.CTkButton(root, text='Cancel', 
              font=('Arial', 18),
              width=100, height=40,
              fg_color='orange',
              hover_color='red',
              text_color='black', 
              command=quit
              ).place(x=800, y=470)



root.mainloop()