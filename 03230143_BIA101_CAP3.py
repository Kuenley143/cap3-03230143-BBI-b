# https://github.com/Kuenley143
# Kuenley Lhendrup Dorji
# BBI B
# 03230143
# References
#https://www.w3schools.com/python/
#https://www.geeksforgeeks.org/python-tkinter-tutorial/
#https://realpython.com/python-import/
#https://www.geeksforgeeks.org/python-gui-tkinter/

#solution:<488837>

import tkinter as tk
import re

class IndexCalculator:
    def __init__(self):
        pass

    def read_input(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            return lines
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return []

    def extract_numbers(self, line):
        first_char = ''
        last_char = ''
        
        for char in line:
            if char.isdigit():
                first_char = char
                break
        
        for char in reversed(line):
            if char.isdigit():
                last_char = char
                break
        
        if first_char and last_char:
            number = int(first_char + last_char)
            return number
        else:
            return 0

    def calculate_sum(self, file_name):
        total_sum = 0
        lines = self.read_input(file_name)
        for line in lines:
            line = line.strip()
            if line:
                total_sum += self.extract_numbers(line)
        return total_sum

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Index Calculator")
        self.geometry("400x200")  # Reduced window size

        self.index_label = tk.Label(self, text="Enter your index:")
        self.index_label.pack()

        self.index_entry = tk.Entry(self, width=20)
        self.index_entry.pack()

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_sum)
        self.calculate_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.thank_you_label = tk.Label(self, text="")
        self.thank_you_label.pack()

    def calculate_sum(self):
        index = self.index_entry.get()
        if not re.match(r'^\d+$', index):
            self.result_label.config(text="Invalid index. Please enter a numeric index.")
            return
        file_name = f"{index[-3:]}.txt"
        calculator = IndexCalculator()
        try:
            sum_result = calculator.calculate_sum(file_name)
        except Exception as e:
            print(f"An error occurred: {e}")
            sum_result = 0

        self.result_label.config(text=f"The sum of the two-digit numbers in the file {file_name} is: {sum_result}")
        self.thank_you_label.config(text="Thank you for using the program!")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()