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
    
    main_menu_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    menu_label = tk.Label(main_menu_frame, text="Main Menu", font=("Helvetica", 18), bg="#f0f0f0")
    menu_label.grid(row=0, columnspan=2, pady=10)

    login_button = tk.Button(main_menu_frame, text="Login", command=adminLogin, width=15, font=("Helvetica", 12))
    login_button.grid(row=1, column=0, pady=10)

    register_button = tk.Button(main_menu_frame, text="Register", command=adminRegister, width=15, font=("Helvetica", 12))
    register_button.grid(row=1, column=1, pady=10)

# ADMIN LOGIN
def adminLogin():
    for widget in root.winfo_children():
        widget.destroy()

    login_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    login_label = tk.Label(login_frame, text="Admin Login", font=("Helvetica", 18), bg="#f0f0f0")
    login_label.grid(row=0, columnspan=2, pady=10)

    username_label = tk.Label(login_frame, text="Username:", font=("Helvetica", 12), bg="#f0f0f0")
    username_label.grid(row=1, column=0, sticky=tk.E, pady=5)
    username_entry = tk.Entry(login_frame, font=("Helvetica", 12))
    username_entry.grid(row=1, column=1, pady=5)

    password_label = tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg="#f0f0f0")
    password_label.grid(row=2, column=0, sticky=tk.E, pady=5)
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
    password_entry.grid(row=2, column=1, pady=5)

    register_button = tk.Button(login_frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get()), width=10, font=("Helvetica", 12))
    register_button.grid(row=3, columnspan=2, pady=10)

    back_button = tk.Button(login_frame, text="Back", command=mainMenu, width=10, font=("Helvetica", 12))
    back_button.grid(row=4, columnspan=2, pady=10)

def login(username, password):
    with open('AdminDatabase.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo("Success", "Logged in as " + username)
                AdminWindow()
                return
    messagebox.showerror("Error", "Invalid username or password")

# CHECK INVENTORY, MODIFY AND EXIT
def AdminWindow():
    for widget in root.winfo_children():
        widget.destroy()

    def check_inventory():
        messagebox.showinfo("Check Inventory", "Inventory checked.")

    def modify_inventory():
        messagebox.showinfo("Modify Inventory", "Inventory modified.")

    def exit_application():
        root.destroy()

    welcome_label = tk.Label(root, text="Welcome Admin!", font=("Helvetica", 18))
    welcome_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    check_inventory_btn = tk.Button(root, text="Check Inventory", command=check_inventory, width=15, height=2, font=("Helvetica", 12))
    check_inventory_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    modify_inventory_btn = tk.Button(root, text="Modify Inventory", command=modify_inventory, width=15, height=2, font=("Helvetica", 12))
    modify_inventory_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    exit_btn = tk.Button(root, text="Exit", command=exit_application, width=15, height=2, font=("Helvetica", 12))
    exit_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# REGISTER
def adminRegister():
    for widget in root.winfo_children():
        widget.destroy()

    register_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
    register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    registration_label = tk.Label(register_frame, text="Admin Registration", font=("Helvetica", 18), bg="#f0f0f0")
    registration_label.grid(row=0, columnspan=2, pady=10)

    username_label = tk.Label(register_frame, text="Username:", font=("Helvetica", 12), bg="#f0f0f0")
    username_label.grid(row=1, column=0, sticky=tk.E, pady=5)
    username_entry = tk.Entry(register_frame, font=("Helvetica", 12))
    username_entry.grid(row=1, column=1, pady=5)

    password_label = tk.Label(register_frame, text="Password:", font=("Helvetica", 12), bg="#f0f0f0")
    password_label.grid(row=2, column=0, sticky=tk.E, pady=5)
    password_entry = tk.Entry(register_frame, show="*", font=("Helvetica", 12))
    password_entry.grid(row=2, column=1, pady=5)

    register_button = tk.Button(register_frame, text="Register", command=lambda: register(username_entry.get(), password_entry.get()), width=10, font=("Helvetica", 12))
    register_button.grid(row=3, columnspan=2, pady=10)

    back_button = tk.Button(register_frame, text="Back", command=mainMenu, width=10, font=("Helvetica", 12))
    back_button.grid(row=4, columnspan=2, pady=10)

# ADMIN REGISTER
def register(username, password):
    file_exists = False
    try:
        with open('AdminDatabase.csv', mode='r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open('AdminDatabase.csv', mode='a' if file_exists else 'w', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Password"])

        with open('AdminDatabase.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username:
                    messagebox.showerror("Error", "Username already exists")
                    return

        writer.writerow([username, password])
    messagebox.showinfo("Success", "Registered successfully")
root = tk.Tk()
root.title("Login Panel")

window_width = 700
window_height = 500
center_window(root, window_width, window_height)

mainMenu()

root.mainloop()
