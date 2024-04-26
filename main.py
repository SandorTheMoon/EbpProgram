import tkinter as tk
from tkinter import messagebox
import csv
import os

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def mainMenu():
    for widget in root.winfo_children():
        widget.destroy()

    login_button = tk.Button(root, text="Login", command=adminLogin)
    login_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    register_button = tk.Button(root, text="Register", command=adminRegister)
    register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

def adminLogin():
    for widget in root.winfo_children():
        widget.destroy()

    username_label = tk.Label(root, text="Admin Login")
    username_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    username_label = tk.Label(root, text="Username:")
    username_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    username_entry = tk.Entry(root)
    username_entry.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    password_label = tk.Label(root, text="Password:")
    password_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    password_entry = tk.Entry(root, show="*")
    password_entry.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    login_button = tk.Button(root, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    back_button = tk.Button(root, text="Back", command=mainMenu)
    back_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def login(username, password):
    # Check if the username and password exist in the CSV file
    with open('AdminDatabase.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo("Success", "Logged in as " + username)
                return
    messagebox.showerror("Error", "Invalid username or password")

def adminRegister():
    for widget in root.winfo_children():
        widget.destroy()

    username_label = tk.Label(root, text="Admin Registration")
    username_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    username_label = tk.Label(root, text="Username:")
    username_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    username_entry = tk.Entry(root)
    username_entry.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

    password_label = tk.Label(root, text="Password:")
    password_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    password_entry = tk.Entry(root, show="*")
    password_entry.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    register_button = tk.Button(root, text="Register", command=lambda: register(username_entry.get(), password_entry.get()))
    register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    back_button = tk.Button(root, text="Back", command=mainMenu)
    back_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def register(username, password):
    # Check if the username already exists
    with open('AdminDatabase.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == username:
                messagebox.showerror("Error", "Username already exists")
                return

    # If username is unique, write it to the CSV file
    with open('AdminDatabase.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    messagebox.showinfo("Success", "Registered successfully")

root = tk.Tk()
root.title("Login Panel")

window_width = 700
window_height = 500
center_window(root, window_width, window_height)

mainMenu()

root.mainloop()
