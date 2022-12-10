import tkinter
from tkinter import*
import ctypes
import random

#to sharpen the tkinter window.
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Type Speed Test")
root.geometry("700x700")

# setting the font of all labels and buttons to consolas to avoid confusion and jumbling of words.
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# used to reset the test sentences for every refresh
def reset_test_writing():
    # list of possible text
    possible_text = [
        'Python is a widely-used general-purpose, high-level programming language. It was initially designed by '
        'Guido van Rossum in 1991 and developed by Python Software Foundation. It was mainly developed for emphasis '
        'on code readability, and its syntax allows programmers to express concepts in fewer lines of code.',
        'Tkinter is included with standard Linux, Microsoft Windows and macOS installs of Python. The name Tkinter '
        'comes from Tk interface. Tkinter was written by Steen Lumholt and Guido van Rossum, then later revised by '
        'Fredrik Lundh. Tkinter is free software released under a Python license. It is used to perform various '
        'operations in a Python Program.',
        'If we talk about the basic difference between module and package in Python. A Python package serves as a '
        'user-variable interface, whereas Python modules serve as a ready-made library.',
        'A Python package defines the code as a separate unit for each function when using a library. While the '
        'modules themselves are a distinct library with built-in functionality, the advantage of packages over '
        'modules is their reusability. So this is the difference between a module and a package in Python.',
        'Python Modules are essentially Python Programming Statements containing various types of Python Functions '
        'used to perform various operations in a Python Program. In the script, Python modules serve as a ready-made '
        'library available to programmers and users.'
    ]

    # stores the random possible text in lower case
    text = random.choice(possible_text).lower()

    # point at which the test starts
    split_point = 0

    # label of text on left side set to east
    global leftLabel
    leftLabel = Label(root, text=text[0:split_point], fg='grey')
    leftLabel.place(relx=0.5, rely=0.5, anchor=E)

    # label of text on right side set to west
    global rightLabel
    rightLabel = Label(root, text=text[split_point:])
    rightLabel.place(relx=0.5, rely=0.5, anchor=W)

    # label to display the letter to be entered
    global current_letter
    current_letter = Label(root, text=text[split_point], fg='grey')
    current_letter.place(relx=0.5, rely=0.6, anchor=N)

    # label to display the leftover time
    global timeLabel
    timeLabel = Label(root, text=text[split_point], fg='red')
    timeLabel.place(relx=0.5, rely=0.4, anchor=S)

    # binds every key which we enter
    global writable
    writable = True
    root.bind('<Key>', key_press)

    # finished time/seconds
    global passed_seconds
    passed_seconds = 0

    # after 60sec abort/finish the test
    # after 1sec add one more sec until <= 60sec
    root.after(60000, stop_test)
    root.after(1000, add_second)


# method to stop the test
def stop_test():
    # set to false after abort/finish of test
    global writable
    writable = False

    # stores the count of list
    word_count = len(leftLabel.cget('text').split(' '))

    # destroy the methods from further execution
    timeLabel.destroy()
    current_letter.destroy()
    rightLabel.destroy()
    leftLabel.destroy()

    # labels the result of test
    global result
    result = Label(root, text=f"Words per Minute: {word_count}", fg='green')
    result.place(relx=0.5, rely=0.4, anchor=CENTER)

    # button to restart/retry the test
    global result_btn
    result_btn = Button(root, text="Retry", command=restart)
    result_btn.place(relx=0.5, rely=0.6, anchor=CENTER)


# restarts the test
def restart():
    # reformat the test by removing result and result_btn
    result.destroy()
    result_btn.destroy()

    # restarts the test
    reset_test_writing()


# to add seconds until <= 60 seconds
def add_second():
    # labels finished seconds
    global passed_seconds
    passed_seconds += 1
    timeLabel.config(text=f"{passed_seconds} Seconds")

    # if <= 60 seconds add one second
    if writable:
        root.after(1000, add_second)


# input entered by user
def key_press(event=None):
    try:
        # if both entered letter equals letter to be entered
        if event.char.lower() == rightLabel.cget('text')[0].lower():
            # shift the entered letter by one index on right side
            rightLabel.configure(text=rightLabel.cget('text')[1:])
            # add the entered letter on to left side
            leftLabel.configure(text=leftLabel.cget('text') + event.char.lower())

            # place the next letter on right side as current letter to be entered
            current_letter.configure(text=rightLabel.cget('text')[0])
    except tkinter.TclError:
        pass


# starts the test
reset_test_writing()

# starts the mainloop
root.mainloop()
