from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()

# Set the title of the window
root.title("Login Form")

# Set the icon for the window (make sure the path to the icon is correct)
root.iconbitmap('282155.png')

# Set the size of the window
root.geometry("400x800")

# Set the background color of the window
root.configure(background="teal")

# Load and resize the image to be displayed on the form
img = Image.open("1550439.jpg")
resize = img.resize((100, 100))
img = ImageTk.PhotoImage(resize)

# Create and configure a label for the form title
infotxt = Label(root, text="This is the form page", fg="white", bg="teal")
infotxt.config(font=("", 20))
infotxt.pack(pady=(10, 5))

# Create and configure a label to display the image
imglabel = Label(root, image=img, bg="teal")
imglabel.pack(pady=(20, 105))

# Create and configure a label for the email entry
emailtxt = Label(root, text="Enter your email", fg="white", bg="teal")
emailtxt.config(font=('cascadia code', 15))
emailtxt.pack()

# Create and configure an entry widget for the user to input their email
emailinp = Entry(root)
emailinp.pack(ipady=3.5, ipadx=75, pady=(5, 20))

# Create and configure a label for the password entry
passwordtxt = Label(root, text="Enter your password", fg="white", bg="teal")
passwordtxt.config(font=("verdana", 15))
passwordtxt.pack(pady=(15, 5))

# Create and configure an entry widget for the user to input their password
passwordinp = Entry(root, show='*')  # show='*' hides the password input
passwordinp.pack(ipady=3.5, ipadx=75)

# Define the function to be called when the login button is clicked
def login_action():
    # Get the email and password entered by the user
    email = emailinp.get()
    password = passwordinp.get()
    
    # Check if both email and password are provided
    if email and password:
        try:
            # Try to open the file and save the email and password
            with open("login_gui1_db.txt", "a+") as f:
                f.write(f"email = {email} \npassword = {password}\n")
            # Show a success message
            messagebox.showinfo("Success", "User registered")
        except Exception as e:
            # Show an error message if there is an issue with file operations
            messagebox.showerror("Error", f"Error saving login details: {e}")
    else:
        # Show a warning message if email or password is not provided
        messagebox.showwarning("Input Error", "Please enter both email and password")

# Create and configure the login button, set it to call login_action when clicked
loginbtn = Button(root, text="Login", command=login_action)
loginbtn.pack(pady=(20, 15))

# Define the function to clear the input fields
def clear_input():
    emailinp.delete(0, END)  # Clear the email entry
    passwordinp.delete(0, END)  # Clear the password entry

# Create and configure the clear button, set it to call clear_input when clicked
clearbtn = Button(root, text="Clear", command=clear_input)
clearbtn.pack(pady=(5, 15))

# Start the Tkinter main loop to display the window and wait for user interaction
root.mainloop()
