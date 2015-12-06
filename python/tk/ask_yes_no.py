# ask_yes_no.py
from tkinter import messagebox

dialog_title = 'Please answer'
dialog_text = 'Do you like bacon?'
answer = messagebox.askquestion(dialog_title, dialog_text)

if answer == 'yes':
    print('I like bacon too!')
else:  # 'no'
    print('You must have clicked the wrong button by accident.')