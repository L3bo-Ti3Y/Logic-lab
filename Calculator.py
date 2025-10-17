#Created by Lebohang
import tkinter as tk
field_text = ""
def add_to_field(sth):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)
def calculate():
    global field_text
    try:
       result = str(eval(field_text))
       field.delete("1.0", "end")
       field.insert("1.0", result)
    except ZeroDivisionError:
       field.delete("1.0", "end")
       field.insert("1.0", "Error")
    except Exception:
       field.delete("1.0", "end")
       field.insert("1.0", "Error")
def clear():
    global field_text
    field_text= ""
    field.delete("1.0", "end")

window = tk.Tk()
window.title("Lebohang's Logic Lab")
window.geometry("300x500")
field = tk.Text(window, height =4, width = 21, font = ("Times New Roman", 20))
field.grid(row = 1, column = 1, columnspan = 4)

#Buttons

btn_1= tk.Button(window, text = "1", command = lambda: add_to_field(1), width = 6, height = 2, font = ("Times New Roman" , 18,))
btn_1.grid(row = 4, column = 1, padx = 5, pady = 5)

btn_2= tk.Button(window, text = "2", command = lambda: add_to_field(2), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_2.grid(row = 4, column = 2, padx = 5, pady = 5)

btn_3= tk.Button(window, text = "3", command = lambda: add_to_field(3), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_3.grid(row = 4, column = 3, padx = 5, pady = 5)

btn_4= tk.Button(window, text = "4", command = lambda: add_to_field(4), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_4.grid(row = 3, column = 1, padx = 5, pady = 5)

btn_5= tk.Button(window, text = "5", command = lambda: add_to_field(5), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_5.grid(row = 3, column = 2, padx = 5, pady = 5)

btn_6= tk.Button(window, text = "6", command = lambda: add_to_field(6), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_6.grid(row = 3, column = 3, padx = 5, pady = 5)

btn_7= tk.Button(window, text = "7", command = lambda: add_to_field(7), width = 6, height = 2,  font = ("Times New Roman" , 18))
btn_7.grid(row = 2, column = 1, padx = 5, pady = 5)

btn_8= tk.Button(window, text = "8", command = lambda: add_to_field(8), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_8.grid(row = 2, column = 2, padx = 5, pady = 5)

btn_9= tk.Button(window, text = "9", command = lambda: add_to_field(9), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_9.grid(row = 2, column = 3, padx = 5, pady = 5)

btn_0= tk.Button(window, text = "0", command = lambda: add_to_field(0), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_0.grid(row = 5, column = 1, padx = 5, pady = 5)


#Operation Buttons With Colour

btn_plus=tk.Button(window, text = "+", command = lambda: add_to_field("+"), width = 6, height = 2, font = ("Times New Roman" , 18), bg = "#E66479")
btn_plus.grid(row = 4, column = 4, padx = 5, pady = 5)

btn_minus=tk.Button(window, text = "-", command = lambda: add_to_field("-"), width = 6, height = 2, font = ("Times New Roman" , 18), bg = "#5896AA")
btn_minus.grid(row = 5, column = 4, padx = 5, pady = 5)

btn_times=tk.Button(window, text = "*", command = lambda: add_to_field("*"), width = 6,height = 2, font = ("Times New Roman" , 18), bg = "#FFA07A")
btn_times.grid(row = 3, column = 4, padx = 5, pady = 5)

btn_division=tk.Button(window, text = "/", command = lambda: add_to_field("/"), width = 6,height = 2, font = ("Times New Roman" , 18),bg = "#922092")
btn_division.grid(row = 2, column = 4, padx = 5, pady = 5)

btn_clear=tk.Button(window, text = "clear", command = lambda: clear(), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_clear.grid(row = 5, column = 3, padx = 5, pady = 5)

btn_decimal=tk.Button(window, text = ".", command = lambda: add_to_field("."), width = 6, height = 2, font = ("Times New Roman" , 18), bg = "#DEE846")
btn_decimal.grid(row = 5, column = 2, padx = 5, pady = 5)

btn_open_parenthesis=tk.Button(window, text = "(", command = lambda: add_to_field("("), width = 6, height = 2, font = ("Times New Roman" , 18))
btn_open_parenthesis.grid(row = 6, column = 1, padx = 5, pady = 5)

btn_close_parenthesis=tk.Button(window, text = ")", command = lambda: add_to_field(")"), width = 6, height = 2,  font = ("Times New Roman" , 18))
btn_close_parenthesis.grid(row = 6, column = 2, padx = 5, pady = 5)

btn_equal=tk.Button(window, text = "=", command = lambda: calculate(), width = 13, height = 2, font = ("Times New Roman" , 18), bg = "#B56B77")
btn_equal.grid(row = 6, column = 4, columnspan = 2)



window.mainloop()