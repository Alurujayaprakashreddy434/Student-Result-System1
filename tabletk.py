from tkinter import *

def calculate_total():
    
    total = int(subject1_entry.get()) + int(subject2_entry.get()) + int(subject3_entry.get())
    total_label.config(text="Total: " + str(total))

def calculate_average():
 
    total = int(subject1_entry.get()) + int(subject2_entry.get()) + int(subject3_entry.get())
    average = total / 3
    average_label.config(text="Average: " + str(average))

def calculate_result():
    
    total = int(subject1_entry.get()) + int(subject2_entry.get()) + int(subject3_entry.get())
    average = total / 3

    
    if average >= 75:
        result = "Distinction"
    elif average >= 60:
        result = "First Class"
    elif average >= 50:
        result = "Second Class"
    elif average >= 35:
        result = "Third Class"
    else:
        result = "Fail"
    
    result_label.config(text="Result: " + result)

window = Tk()
window.geometry("600x400")
window.title("Student Result System")

heading_label = Label(window, text="Student Result System", font=("Arial", 20))
heading_label.grid(row=0, column=0, columnspan=4)

student_name_label = Label(window, text="Student Name:")
student_name_label.grid(row=1, column=0)

student_number_label = Label(window, text="Student Number:")
student_number_label.grid(row=2, column=0)

subject1_label = Label(window, text="Subject 1:")
subject1_label.grid(row=3, column=0)

subject2_label = Label(window, text="Subject 2:")
subject2_label.grid(row=4, column=0)

subject3_label = Label(window, text="Subject 3:")
subject3_label.grid(row=5, column=0)

total_label = Label(window, text="Total:")
total_label.grid(row=6, column=0)

average_label = Label(window, text="Average:")
average_label.grid(row=7, column=0)

result_label = Label(window, text="Result:")
result_label.grid(row=8, column=0)

# Entries
student_name_entry = Entry(window)
student_name_entry.grid(row=1, column=1)

student_number_entry = Entry(window)
student_number_entry.grid(row=2, column=1)

subject1_entry = Entry(window)
subject1_entry.grid(row=3, column=1)

subject2_entry = Entry(window)
subject2_entry.grid(row=4, column=1)

subject3_entry = Entry(window)
subject3_entry.grid(row=5, column=1)


total_button = Button(window, text="Total", command=calculate_total)
total_button.grid(row=6, column=2)

average_button = Button(window, text="Average", command=calculate_average)
average_button.grid(row=7, column=2)

result_button = Button(window, text="Result", command=calculate_result)
result_button.grid(row=8, column=2)

window.mainloop()
