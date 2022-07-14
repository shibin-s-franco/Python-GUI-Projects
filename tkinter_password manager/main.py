from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list1=[random.choice(letters) for char in range(nr_letters)]
    password_list2=[random.choice(symbols) for char in range(nr_symbols)]
    password_list3=[random.choice(numbers) for char in range(nr_numbers)]

    password_list=password_list1+password_list2+password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_x=website_entry.get().title()
    email_x=email_username_entry.get()
    password_x=password_entry.get()
    new_data={
        website_x:{
            "email":email_x,
            "password":password_x,
        }
    }
    # print(new_data)
    if website_x=="" or password_x=="":
        messagebox.showinfo(title="oops",message="Please don't leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website_x,message=f"These are the details entered:"
        f"\nEmail:{email_x}\nPassword:{password_x}\nIs it ok to save")
        
        if is_ok:
            try:
                with open(r"P:\PYTHON\my prog\intermediate level programs\tkinter_password manager\data.json",mode="r") as data:
                    # Reading old data
                    data_file=json.load(data)
                    # Updating old data with new data
                    data_file.update(new_data)
            except FileNotFoundError:
                with open(r"P:\PYTHON\my prog\intermediate level programs\tkinter_password manager\data.json",mode="w") as data:
                   json.dump(new_data,data,indent=4)
            else:
                with open(r"P:\PYTHON\my prog\intermediate level programs\tkinter_password manager\data.json",mode="w") as data:
                    json.dump(data_file,data,indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0,END)

# -----------------------------SEARCH THROUGH JSON FILE----------------#
def search():
    search_item=website_entry.get().title()
    
    try:
        with open(r"P:\PYTHON\my prog\intermediate level programs\tkinter_password manager\data.json",mode="r") as data:
            data_file=json.load(data)
        search_dict=data_file[search_item]
    except FileNotFoundError :
        messagebox.showinfo(title="error",message="No data file found")
    except KeyError:
        messagebox.showinfo(title="error",message=f"No details for {search_item} exist")
    else:
        messagebox.showinfo(title=search_item,message=f"Email: {search_dict['email']}\nPassword: {search_dict['password']}")

# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file=r"P:\PYTHON\my prog\intermediate level programs\tkinter_password manager\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

# label
website=Label(text="Website:")
website.grid(row=1,column=0)

email_username=Label(text="Email/Username:")
email_username.grid(row=2,column=0)

password=Label(text="Password:")
password.grid(row=3,column=0)

# entry
website_entry=Entry(width=27)
website_entry.focus()
website_entry.grid(row=1,column=1,sticky=E)

email_username_entry=Entry(width=46)
email_username_entry.insert(0,"shibin@gmail.com")
email_username_entry.grid(row=2,column=1,columnspan=2,sticky=E)

password_entry=Entry(width=27)
password_entry.grid(row=3,column=1,sticky=E)
# button
password_button=Button(text="Generate Password",width=15,highlightthickness=0,command=generate_password)
password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=38,highlightthickness=0,command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky=E)

search_button=Button(text="Search",width=15,highlightthickness=0,command=search)
search_button.grid(row=1,column=2)




window.mainloop()