from tkinter import *
from tkinter import ttk
import time

def add_word():
    new_word = Entry(root)
    new_word.pack()
    words.append(new_word)

    add_button.pack_forget()
    submit_button.pack_forget()

    add_button.pack()
    submit_button.pack()

def text():
    get_paragraph = paragraph.get("1.0", END).strip()
    all_words = [word.get() for word in words]
    print(get_paragraph)
    print(all_words)

def new_file():
    print("HELLO!")

def start_progress():
    progress['value'] = 0
    root.update_idletasks()

    def update_progress(i):
        if i <= 101:
            progress['value'] = i
            root.after(50, update_progress, i + 1)
        else:
            print("Progress Complete")

    update_progress(0)


def main():
    global root
    root = Tk()
    global menu_bar
    menu_bar = Menu(root)
    root.configure(menu=menu_bar)
    root.geometry("800x600")
    root.title('SimplifyTest')

    global words
    words = []

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=new_file)
    menu_bar.add_cascade(label="My Menu", menu=file_menu)
    
    # label
    l = Label(root, text="Type in the paragraph.")
    l.config(font =("Arial", 20, 'bold'))
    l.pack()

    # textbox
    global paragraph
    paragraph = Text(root, height=20, width=100)
    paragraph.pack()

    global submit_button, add_button
    submit_button = Button(root, text='Submit', command=text)
    add_button = Button(root, text="Add Word", command=add_word)

    add_button.pack()
    submit_button.pack()

    global progress
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)

    start_button = Button(root, text="Start Progress", command=start_progress)
    start_button.pack(pady=10)

    root.mainloop()

if __name__=='__main__':
    main()