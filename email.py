from smtplib import SMTP
from tkinter import *
import unittest

root = Tk()
root.title("Email sender")
root.geometry("500x500")
root.config(bg="blue")

# Creating a header for the GUI

heading = Label(root, text="GUI for sending emails", bg="pink", fg="white", font=("Helvetica", 20), width=500, height=3)
heading.pack()

# Creating the To email
to_email = Label(root, text="Enter recipients email address: srenzaho@gmail.com")
to_email.place(x=15, y=70)

address = StringVar()
email_body = StringVar()
subject = StringVar()

address_entry = Entry(textvariable=address, width=40)
address_entry.place(x=15, y=100)

# Creating the part where a person can enter their subject
subject_heading = Label(root, text="Subject: hi")
subject_heading.place(x=15, y=150)

subject_entry = Entry(textvariable=subject, width=40)
subject_entry.place(x=15, y=180)

# Creating the part where user can enter their message

email_body_label = Label(root, text="Enter your message here: misscosmo43@gmail.com")
email_body_label.place(x=15, y=220)

email_body_entry = Entry(textvariable=email_body, width=40)
email_body_entry.place(x=15, y=250, height=100)

# Defining and creating button that will send the email

def send_button():

    address_info = address.get()
    email_body_content = email_body.get()
    print(address_info, email_body_content)



try:
    server = SMTP("smtp.gmail.com", 587)
    sender_email = "misscosmo43@gmail.com"
    receiver_email = "srenzaho@gmail.com"
    password = str(input("Please enter your password: "))
    server.starttls()

    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, 'This is a test email.')
    print("the message has been successfully sent")
except Exception as err:
    print("Something went wrong...", err)
finally:
    server.close()

    button_send = Button(root, text="Send Email", command=send_button, width=30, height=2, bg="grey")
    button_send.place(x=15, y=450)

# Creating the clear the button

def clear():
    address_entry.delete(0, END)
    subject_entry.delete(0, END)
    email_body_entry.delete(0, END)

    clear_button = Button(root, text="Clear", command=clear, width=30, height=2, bg="grey")
    clear_button.place(x=15, y=500)

root.mainloop()
