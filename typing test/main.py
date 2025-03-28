from customtkinter import *
import random

# x----------------RESOURCES----------------x

DARK_MAROON = '#7C444F'
MAROON = '#9F5255'
DARK_ORANGE = '#E16A54'
OCHRE = '#F39E60'
FONT_NAME = 'Cascadia Code'
TIMER = 60
wpm = 0

# x----------------MECHANISM----------------x

with open('1-1000.txt') as f:
    wordlist = [line.strip() for line in f]

def start_test():
    global TIMER, wordlist, wpm

    root.configure(padx=150)
    start_button.destroy()

    if TIMER > 0:
        TIMER -= 1
        if TIMER < 10:
            count = f'0{TIMER}'
            welcome.configure(text=f'00:{count}')
        else:
            welcome.configure(text=f'00:{TIMER}')
        root.after(1000, start_test)

    else:
        words.destroy()
        input_label.destroy()
        done = CTkLabel(root,
                        text=f'\nTime is up!\n\nYour speed is {wpm} wpm',
                        font=(FONT_NAME, 20, 'bold'),
                        text_color='white',
                        padx=15,
                        pady=20)
        done.grid(row=1, column=1)

def check_input(event=None):
    global wpm
    if input_label.get().strip() == current_word.get():
        wpm += 1
        input_label.delete(0, END)
        current_word.set(random.choice(wordlist))

# x----------------UI SETUP----------------x

root = CTk()
root.geometry('500x300')
root.configure(pady=30, padx=55, fg_color=DARK_MAROON)
root.title('Typing Test')

welcome = CTkLabel(root,
                   text='Want to test how fast are your fingers?',
                   font=(FONT_NAME, 18, 'bold'))
welcome.grid(row=0, column=1, pady=10)

current_word = StringVar()

if isinstance(current_word, StringVar):
    current_word.set(random.choice(wordlist))

words = CTkLabel(root,
                 textvariable=current_word,
                 text_color='white',
                 padx=15,
                 pady=15,
                 font=(FONT_NAME, 20, 'bold'))
words.grid(row=1, column=1)

input_label = CTkEntry(root,
                       fg_color=DARK_ORANGE,
                       width=250,
                       corner_radius=15,
                       border_color=OCHRE,
                       justify='center',
                       height=50,
                       font=(FONT_NAME, 15))
input_label.grid(row=2, column=1, pady=20)
input_label.bind("<Return>", check_input)

start_button = CTkButton(root,
                         text='Start',
                         corner_radius=15,
                         fg_color=OCHRE,
                         hover_color=MAROON,
                         font=(FONT_NAME, 15, 'bold'),
                         command=start_test)
start_button.grid(row=3, column=1, pady=20)


root.mainloop()