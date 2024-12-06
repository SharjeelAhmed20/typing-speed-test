import tkinter as tk
import time
import random

words = [
    "the quick brown fox jumps over the lazy dog",
    "a journey of a thousand miles begins with a single step",
    "to be or not to be that is the question",
    "all that glitters is not gold",
    "the early bird catches the worm"
]

start_time = None
typed_sentence = ""
time_taken = 0


root = tk.Tk()
root.title("Typing Speed Test")
root.config(bg="#f7f7f7")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 24, "bold"), bg="#f7f7f7", fg="#333")
title_label.pack(pady=20)

sentence_var = tk.StringVar()
sentence_label = tk.Label(root, textvariable=sentence_var, font=("Helvetica", 16), bg="#f7f7f7", wraplength=400, justify="center")
sentence_label.pack(pady=20)

typing_var = tk.StringVar()
typing_entry = tk.Entry(root, textvariable=typing_var, font=("Helvetica", 14), width=40, bd=2, relief="solid", highlightthickness=1)
typing_entry.pack(pady=10)
typing_entry.config(state="disabled")

result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f7f7f7", fg="#333")
result_label.pack(pady=20)

def start_test():
    global start_time, typed_sentence, time_taken
    typed_sentence = random.choice(words)
    sentence_var.set(typed_sentence)
    typing_var.set("")
    typing_entry.config(state="normal")
    typing_entry.focus()
    start_time = time.time()
    start_button.config(state="disabled", bg="#aaa")
    typing_entry.bind("<KeyRelease>", check_input)

def check_input(event):
    typed_text = typing_var.get()

    if typed_text == typed_sentence:
        end_test()

def end_test():
    global start_time, typed_sentence, time_taken
    time_taken = round(time.time() - start_time, 2)

    word_count = len(typed_sentence.split())
    wpm = round((word_count / time_taken) * 60)

    result_label.config(
        text=f"Time: {time_taken} seconds\nWords Per Minute: {wpm} WPM",
        fg="#4CAF50"
    )

    start_button.config(state="normal", bg="#4CAF50")
    typing_entry.config(state="disabled")

start_button = tk.Button(root, text="Start Test", font=("Helvetica", 14), bg="#4CAF50", fg="white", relief="raised", command=start_test)
start_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()