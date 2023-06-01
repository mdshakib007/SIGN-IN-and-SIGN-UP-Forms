from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
from oop_responsive_login_form import Login

root = Tk()
root.title("Sign up")
root.geometry("900x900+150+50")
root.resizable(False, False)


### Get data 
def get_data():
    firstname_data = firstname.get()
    lastname_data = lastname.get()
    email_data = email.get()
    password_data = password.get()
    
    if firstname_data and lastname_data and email_data and password_data != '':
        messagebox.showinfo('SIGN UP', 'Sign up successful!')
    else:
        messagebox.showerror('Error', "Data cannot be empty!")
    


def login_page():
    root.destroy()
    Login()


### Background Image
signup_img = Image.open("login_assets/white_signup.jpg")
signup_resize = signup_img.resize((900, 900))
signup_image = ImageTk.PhotoImage(image=signup_resize)

Label(root, image=signup_image).place(x=0, y=0)


# first name
firstname = ctk.CTkEntry(root, width=230, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='First Name', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
firstname.place(x=300, y=352)

# lastname
lastname = ctk.CTkEntry(root, width=235, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='Last Name', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
lastname.place(x=300, y=407)

# email
email = ctk.CTkEntry(root, width=235, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='E-mail', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
email.place(x=300, y=462)

# Password
password = ctk.CTkEntry(root, width=235, 
                         font=('Arial', 18), 
                         height=40, 
                         border_width=0, 
                         placeholder_text='Password', 
                         corner_radius=0,
                         bg_color='white',
                         fg_color='white',
                         text_color='black'
                         )
password.place(x=300, y=517)



### sign up button
ctk.CTkButton(root, text='SIGNUP', 
              font=('Arial', 18),
              width=237, height=45,
              border_width=0, 
              fg_color='blue',
              command=get_data
              ).place(x=300, y=595)



### login anchor
ctk.CTkLabel(root, text='Already have an account?',
             font=('Arial', 12, 'italic'),
             fg_color='#aacbff', 
             text_color='black'
             ).place(x=300, y=650)

ctk.CTkButton(root, text='Login',
             font=('Arial', 12, 'bold'),
             height=10, width=20,
             fg_color='#aacbff', 
             text_color='black',
             hover=False,
             corner_radius=0,
             border_width=0,
             bg_color='#aacbff',
             command=login_page
             ).place(x=450, y=654)

root.mainloop()