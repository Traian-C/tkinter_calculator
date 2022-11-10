'''GUI Calculator using tkinter'''

import tkinter as tk

window = tk.Tk()

str_display_number = '0'
num1 = 0.0
str_oper = '0'


def cmd_clear():
    '''clear display'''
    global str_display_number
    str_display_number = '0'
    lbl_value["text"] = str_display_number


def cmd_del():
    '''delete last digit'''
    global str_display_number
    if float(str_display_number) < 10:
        str_display_number = 0
    else:
        str_display_number = str_display_number[:-1]
    lbl_value["text"] = str_display_number
        

def cmd_div():
    '''division'''
    global num1, str_oper, str_display_number
    num1 = float(lbl_value["text"])
    str_oper = '/'
    str_display_number = '0'


def cmd_mul():
    '''multiply'''
    global num1, str_oper, str_display_number
    num1 = float(lbl_value["text"])
    str_oper = 'X'
    str_display_number = '0'


def cmd_sub():
    '''substract'''
    global num1, str_oper, str_display_number
    num1 = float(str_display_number)
    str_oper = '-'
    str_display_number = '0'


def cmd_add():
    '''add'''
    global num1, str_oper, str_display_number
    num1 = float(str_display_number)
    str_oper = '+'
    str_display_number = '0'


def cmd_equal():
    '''equal calculation'''
    global num1, str_oper, str_display_number
    num2 = float(lbl_value["text"])
    if str_oper == '+':
        str_display_number = str(round(num1 + num2, 4))
    elif str_oper == '-':
        str_display_number = str(round(num1 - num2, 4))
    elif str_oper == 'X':
        str_display_number = str(round(num1 * num2, 4))
    elif str_oper == '/':
        str_display_number = str(round(num1 / num2, 4))
    str_oper = '0'
    lbl_value["text"] = str_display_number


def cmd_btn(btn):
    '''button numbers'''
    global str_display_number
    if btn == '.':
        if str_display_number.endswith('.0'):
            str_display_number = str_display_number.removesuffix('0')
            print('.1')
        else:
            str_display_number = str_display_number + btn
    else:
        if str_display_number == '0':
            str_display_number = btn
        else:
            num = int(btn)
            if str_display_number.endswith('.0'):
                str_display_number = str_display_number.removesuffix('.0')
                str_display_number = str_display_number + str(num)
            else:
                str_display_number = str_display_number + str(num)
    lbl_value["text"] = str_display_number


# define window grid 6 rows and 4 columns
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=70, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=80, weight=1)


# calculator's display is a label control
lbl_value = tk.Label(master=window, text="0", font=("Arial", 30))
lbl_value.grid(row=0, column=0, columnspan=4)


# buttons layout - in order of appearance :)
btn_clear = tk.Button(master=window, text="C", command=cmd_clear, font=("Arial", 14))
btn_clear.grid(row=1, column=0, columnspan=2, sticky="nsew")

btn_del = tk.Button(master=window, text="DEL", command=cmd_del, font=("Arial", 14))
btn_del.grid(row=1, column=2, sticky="nsew")

btn_div = tk.Button(master=window, text="/", command=cmd_div, font=("Arial", 14))
btn_div.grid(row=1, column=3, sticky="nsew")


btn_7 = tk.Button(master=window, text="7", command=lambda:cmd_btn('7'), font=("Arial", 14))
btn_7.grid(row=2, column=0, sticky="nsew")

btn_8 = tk.Button(master=window, text="8", command=lambda:cmd_btn('8'), font=("Arial", 14))
btn_8.grid(row=2, column=1, sticky="nsew")

btn_9 = tk.Button(master=window, text="9", command=lambda:cmd_btn('9'), font=("Arial", 14))
btn_9.grid(row=2, column=2, sticky="nsew")

btn_mul = tk.Button(master=window, text="X", command=cmd_mul, font=("Arial", 14))
btn_mul.grid(row=2, column=3, sticky="nsew")


btn_4 = tk.Button(master=window, text="4", command=lambda:cmd_btn('4'), font=("Arial", 14))
btn_4.grid(row=3, column=0, sticky="nsew")

btn_5 = tk.Button(master=window, text="5", command=lambda:cmd_btn('5'), font=("Arial", 14))
btn_5.grid(row=3, column=1, sticky="nsew")

btn_6 = tk.Button(master=window, text="6", command=lambda:cmd_btn('6'), font=("Arial", 14))
btn_6.grid(row=3, column=2, sticky="nsew")

btn_sub = tk.Button(master=window, text="-", command=cmd_sub, font=("Arial", 14))
btn_sub.grid(row=3, column=3, sticky="nsew")


btn_1 = tk.Button(master=window, text="1", command=lambda:cmd_btn('1'), font=("Arial", 14))
btn_1.grid(row=4, column=0, sticky="nsew")

btn_2 = tk.Button(master=window, text="2", command=lambda:cmd_btn('2'), font=("Arial", 14))
btn_2.grid(row=4, column=1, sticky="nsew")

btn_3 = tk.Button(master=window, text="3", command=lambda:cmd_btn('3'), font=("Arial", 14))
btn_3.grid(row=4, column=2, sticky="nsew")

btn_add = tk.Button(master=window, text="+", command=cmd_add, font=("Arial", 14))
btn_add.grid(row=4, column=3, sticky="nsew")


btn_0 = tk.Button(master=window, text="0", command=lambda:cmd_btn('0'), font=("Arial", 14))
btn_0.grid(row=5, column=0, columnspan=2, sticky="nsew")

btn_dec = tk.Button(master=window, text=".", command=lambda:cmd_btn('.'), font=("Arial", 14))
btn_dec.grid(row=5, column=2, sticky="nsew")

btn_equal = tk.Button(master=window, text="=", command=cmd_equal, font=("Arial", 14))
btn_equal.grid(row=5, column=3, sticky="nsew")


window.mainloop()
