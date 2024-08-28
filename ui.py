from tkinter import *
from  tkinter import ttk

class Temp:

    def temp():
        print("HELLO!")

    def temp_progress():
        progress['value'] = 0
        root.update_idletasks()

        def update_progress(i):
            if i <= 101:
                progress['value'] = i
                root.after(50, update_progress, i + 1)
            else:
                print("Progress Complete")
        update_progress(0)

class CusButton:

    def submit():
        get_paragraph = paragraph.get('1.0', END).strip()
        all_words = [word.get() for word in words]
        paragraph.delete('1.0', END)
        paragraph.insert('1.0', "")
        print(get_paragraph)
        print(all_words)

    def add_word():
        new_word = Entry(root)
        new_word.pack()
        words.append(new_word)

        add_button.pack_forget()
        submit_button.pack_forget()
        progress.pack_forget()
        temp_button.pack_forget()

        add_button.pack()
        submit_button.pack()
        progress.pack()
        temp_button.pack()

def main():
    global root, menu_bar, words, paragraph, submit_button, add_button, progress, temp_button
    
    root = Tk()
    root.geometry('800x600')
    root.title('SimplifyTest')

    menu_bar = Menu(root)
    root.configure(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Temp', command=Temp.temp)
    menu_bar.add_cascade(label='Menu', menu=file_menu)

    label = Label(root, text="Type in the paragraph.")
    label.config(font=('Arial', 20, 'bold'))
    label.pack()

    words = []
 
    paragraph = Text(root, height=20, width=100)
    paragraph.pack()

    add_button = Button(root, text='Add word', command=CusButton.add_word)
    submit_button = Button(root, text='Submit', command=CusButton.submit)
    add_button.pack()
    submit_button.pack()
    
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    temp_button = Button(root, text="Start Progress", command=Temp.temp_progress)
    progress.pack()
    temp_button.pack()

    root.mainloop()

if __name__=='__main__':
    main()