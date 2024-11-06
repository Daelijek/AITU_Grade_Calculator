import customtkinter as ctk
from tkinter import messagebox

# A function to check that a number has been entered and that it is in the range from 0 to 100
def validate_input(value):
    try:
        value = int(value)
        if 0 <= value <= 100:
            return value
        else:
            return None
    except ValueError:
        return None

# Function for calculating the total score
def calculate_total():
    mid_term = validate_input(mid_term_entry.get())
    end_term = validate_input(end_term_entry.get())
    final_exam = validate_input(final_exam_entry.get())

    if mid_term is None or end_term is None or final_exam is None:
        messagebox.showerror("Error", "Please enter numeric values for all fields from 0 to 100.")
        return

    if mid_term < 25:
        result_text.set("F because of Mid-Term.")
        return
    if end_term < 25:
        result_text.set("F because of End-Term.")
        return
    if final_exam < 25:
        result_text.set("F because of Final Exam.")
        return

    total = (0.3 * mid_term) + (0.3 * end_term) + (0.4 * final_exam)
    result = f"Your total Grade is: {total}\n"

    if final_exam < 50:
        result += "Result: FX - пересдача"
    else:
        result += "Result: Passed"

    result_text.set(result)

# The function for calculating the scholarship
def calculate_scholarship():
    mid_term = validate_input(mid_term_entry.get())
    end_term = validate_input(end_term_entry.get())

    if mid_term is None or end_term is None:
        messagebox.showerror("Ошибка", "Please enter numeric values for all fields from 0 to 100.")
        return

    if mid_term < 25:
        result_text.set("F because of Mid-Term.")
        return
    if end_term < 25:
        result_text.set("F because of End-Term.")
        return

    term = (0.3 * mid_term + 0.3 * end_term)
    scholarship = abs((term - 70)) / 0.4
    inc_scholarship = abs((term - 90)) / 0.4

    if scholarship < 50:
        scholarship = 50
    elif scholarship > 100:
        scholarship = "You're not going to get a scholarship. You're cooked :("

    if inc_scholarship < 50:
        inc_scholarship = 50
    elif inc_scholarship > 100:
        inc_scholarship = "You won't be able to get an increased scholarship :("

    # Only if you can get a scholarship, we display the necessary message
    if isinstance(scholarship, str):
        result_text.set(scholarship)
    else:
        result_text.set(f"To get scholarship you need to get: {scholarship}\n"
                        f"To get increased scholarship you need to get: {inc_scholarship}")

# Functions for displaying the required fields
def show_total_fields():
    # We show the fields for calculating the total
    mid_term_label.pack(pady=10)
    mid_term_entry.pack(pady=5)
    end_term_label.pack(pady=10)
    end_term_entry.pack(pady=5)
    final_exam_label.pack(pady=10)
    final_exam_entry.pack(pady=5)
    calculate_total_button.pack(pady=10)
    
    # Hiding the fields for calculating the scholarship
    calculate_scholarship_button.pack_forget()

def show_scholarship_fields():
    # We show the fields for calculating the scholarship
    mid_term_label.pack(pady=10)
    mid_term_entry.pack(pady=5)
    end_term_label.pack(pady=10)
    end_term_entry.pack(pady=5)
    calculate_scholarship_button.pack(pady=10)

    # Hiding the fields for calculating the total
    final_exam_label.pack_forget()
    final_exam_entry.pack_forget()
    calculate_total_button.pack_forget()

# Configuring the interface using CustomTkinter
root = ctk.CTk()
root.title("Grade Calculator")
root.geometry("400x600")

# We apply the style and font
root.configure(bg="#f5f5f5")

# Text labels and input fields with updated style
font = ("Montserrat", 12)

mid_term_label = ctk.CTkLabel(root, text="Mid-Term Grade:", font=font, text_color="#333")
mid_term_entry = ctk.CTkEntry(root, font=font)

end_term_label = ctk.CTkLabel(root, text="End-Term Grade:", font=font, text_color="#333")
end_term_entry = ctk.CTkEntry(root, font=font)

final_exam_label = ctk.CTkLabel(root, text="Final Exam Grade:", font=font, text_color="#333")
final_exam_entry = ctk.CTkEntry(root, font=font)

# Buttons for selecting a function with an updated style
button_style = {
    "font": font, 
    "fg_color": "#333",  # The black color of the text on the buttons
    "width": 200, 
    "height": 40,
    "corner_radius": 10
}

ctk.CTkButton(root, text="Calculate Total Grade", command=show_total_fields, **button_style).pack(pady=10)
ctk.CTkButton(root, text="Calculate Scholarship", command=show_scholarship_fields, **button_style).pack(pady=10)

# Buttons for performing calculations
calculate_total_button = ctk.CTkButton(root, text="Calculate Total", command=calculate_total, **button_style)
calculate_scholarship_button = ctk.CTkButton(root, text="Calculate Scholarship", command=calculate_scholarship, **button_style)

# A field for displaying results with an improved style
result_text = ctk.StringVar()
result_label = ctk.CTkLabel(root, textvariable=result_text, font=("Arial", 14), text_color="#333", wraplength=350, justify="left")
result_label.pack(pady=20)

# The field for displaying the author's name
author_label = ctk.CTkLabel(root, text="Created by Daelijek", font=("Arial", 10), text_color="#888")
author_label.pack(side="bottom", pady=10)

# Starting the main cycle
root.mainloop()
