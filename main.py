import tkinter as tk
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''
food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, tk.END)
    calculator_display.insert(tk.END, operator)


def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0, tk.END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0, tk.END)
    calculator_display.insert(0, result)
    operator = ''


def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=tk.NORMAL)
            if food_box[x].get() == '0':
                food_box[x].delete(0, tk.END)
            food_box[x].focus()
        else:
            food_box[x].config(state=tk.DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=tk.NORMAL)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, tk.END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=tk.DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for b in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=tk.NORMAL)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, tk.END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=tk.DISABLED)
            dessert_text[x].set('0')
        x += 1


def total_calculations():
    food_subtotal = 0
    p = 0
    for unit in food_text:
        food_subtotal = food_subtotal + (float(unit.get()) * food_price[p])
        p += 1

    drink_subtotal = 0
    p = 0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (float(unit.get()) * drink_price[p])
        p += 1

    dessert_subtotal = 0
    p = 0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(unit.get()) * dessert_price[p])
        p += 1

    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_taxes = my_subtotal * 0.11
    my_total = my_subtotal + my_taxes

    food_cost_var.set(f'$ {round(food_subtotal, 2)}')
    drink_cost_var.set(f'$ {round(drink_subtotal, 2)}')
    dessert_cost_var.set(f'$ {round(dessert_subtotal, 2)}')
    subtotal_cost_var.set(f'$ {round(my_subtotal, 2)}')
    taxes_cost_var.set(f'$ {round(my_taxes, 2)}')
    total_cost_var.set(f'$ {round(my_total, 2)}')


def create_invoice():
    invoice_text.delete(1.0, tk.END)
    invoice_number = f'N# - {random.randint(1000, 99999)}'
    my_date = datetime.datetime.now()
    invoice_date = f'{my_date.day}/{my_date.month}/{my_date.year} - {my_date.hour}:{my_date.minute}:{my_date.second}'
    invoice_text.insert(tk.END, f'INFORMATION: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(tk.END, f'*' * 47 + '\n')
    invoice_text.insert(tk.END, f'Items\t\tQuantity\tItems Cost\n')
    invoice_text.insert(tk.END, f'-' * 54 + '\n')

    x = 0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(tk.END, f'{food_list[x]}\t\t{f.get()}\t'
                                        f'$ {int(f.get()) * food_price[x]}\n')
        x += 1

    x = 0
    for d in drink_text:
        if d.get() != '0':
            invoice_text.insert(tk.END, f'{drink_list[x]}\t\t{d.get()}\t'
                                        f'$ {int(d.get()) * drink_price[x]}\n')
        x += 1

    x = 0
    for e in dessert_text:
        if e.get() != '0':
            invoice_text.insert(tk.END, f'{dessert_list[x]}\t\t{e.get()}\t'
                                        f'$ {int(e.get()) * dessert_price[x]}\n')
        x += 1

    invoice_text.insert(tk.END, f'*' * 47 + '\n')
    invoice_text.insert(tk.END, f'Food Subtotal: \t\t\t{food_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'Drink Subtotal: \t\t\t{drink_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'Dessert Subtotal: \t\t\t{dessert_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'-' * 54 + '\n')
    invoice_text.insert(tk.END, f'Subtotal: \t\t\t{subtotal_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'Taxes: \t\t\t{taxes_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'Total: \t\t\t{total_cost_var.get()}\n')
    invoice_text.insert(tk.END, f'*' * 47 + '\n')
    invoice_text.insert(tk.END, f'See you soon!')


def save_invoice():
    invoice_info = invoice_text.get(1.0, tk.END)
    my_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    my_file.write(invoice_info)
    my_file.close()
    messagebox.showinfo('Notification', 'Your invoice has been saved!')


def reset_all():
    invoice_text.delete(0.1, tk.END)

    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_box:
        box.config(state=tk.DISABLED)
    for box in drink_box:
        box.config(state=tk.DISABLED)
    for box in dessert_box:
        box.config(state=tk.DISABLED)

    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_cost_var.set('')
    taxes_cost_var.set('')
    total_cost_var.set('')


# Initialize TKinter
application = tk.Tk()

# Window size
application.geometry('1500x680+0+0')

# Prevent from maximizing
application.resizable(False, False)

# Set title
application.title('My Restaurant - Invoicing System')

# Window background color
application.config(bg='burlywood')

# Top panel
top_panel = tk.Frame(application, bd=1, relief=tk.FLAT)
top_panel.pack(side=tk.TOP)

# Title tag
title_tag = tk.Label(top_panel, text='Invoicing System', fg='azure4',
                     font=('Dosis', 58), bg='burlywood', width=27)
title_tag.grid(row=0, column=0)

# Left panel
left_panel = tk.Frame(application, bd=1, relief=tk.FLAT)
left_panel.pack(side=tk.LEFT)

# Cost panel
cost_panel = tk.Frame(left_panel, bd=1, relief=tk.FLAT, bg='azure4', padx=50)
cost_panel.pack(side=tk.BOTTOM)

# Food panel
food_panel = tk.LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                           bd=1, relief=tk.FLAT, fg='azure4')
food_panel.pack(side=tk.LEFT)

# Drink panel
drink_panel = tk.LabelFrame(left_panel, text='Drink', font=('Dosis', 19, 'bold'),
                           bd=1, relief=tk.FLAT, fg='azure4')
drink_panel.pack(side=tk.LEFT)

# Dessert panel
dessert_panel = tk.LabelFrame(left_panel, text='Dessert', font=('Dosis', 19, 'bold'),
                           bd=1, relief=tk.FLAT, fg='azure4')
dessert_panel.pack(side=tk.LEFT)

# Right panel
right_panel = tk.Frame(application, bd=1, relief=tk.FLAT)
right_panel.pack(side=tk.RIGHT)

# Calculator panel
calc_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
calc_panel.pack()

# Invoice panel
invoice_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
invoice_panel.pack()

# Buttons panel
buttons_panel = tk.Frame(right_panel, bd=1, relief=tk.FLAT, bg='burlywood')
buttons_panel.pack()

# Product list
food_list = ['Chicken', 'Lamb', 'Salmon', 'Hake', 'Kebabs', 'Pizza1', 'Pizza2', 'Pizza3']
drink_list = ['Lemonade', 'Soda', 'Juice', 'Cola', 'Wine1', 'Wine2', 'Beer1', 'Beer2']
dessert_list = ['Ice Cream', 'Fruit', 'Brownies', 'Pudding', 'Cheescake', 'Cake1', 'Cake2', 'Cake3']

# Create food items
food_variables = []
food_box = []
food_text = []
counter = 0
for food in food_list:
    # Create checkboxes
    food_variables.append('')
    food_variables[counter] = tk.IntVar()
    food = tk.Checkbutton(food_panel,
                          text=food.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=food_variables[counter],
                          command=review_check)
    food.grid(row=counter,
              column=0,
              sticky=tk.W)

    # Create input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = tk.StringVar()
    food_text[counter].set('0')
    food_box[counter] = tk.Entry(food_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=tk.DISABLED,
                                 textvariable=food_text[counter])
    food_box[counter].grid(row=counter,
                           column=1)

    counter += 1


# Create drink items
drink_variables = []
drink_box = []
drink_text = []
counter = 0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = tk.IntVar()
    drink = tk.Checkbutton(drink_panel,
                           text=drink.title(),
                           font=('Dosis', 19, 'bold'),
                           onvalue=1,
                           offvalue=0,
                           variable=drink_variables[counter],
                           command=review_check)
    drink.grid(row=counter, column=0, sticky=tk.W)

    # Create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = tk.StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = tk.Entry(drink_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=tk.DISABLED,
                                 textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column=1)
    counter += 1

# Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = tk.IntVar()
    dessert = tk.Checkbutton(dessert_panel,
                             text=dessert.title(),
                             font=('Dosis', 19, 'bold'),
                             onvalue=1,
                             offvalue=0,
                             variable=dessert_variables[counter],
                             command=review_check)
    dessert.grid(row=counter, column=0, sticky=tk.W)

    # Create input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = tk.StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = tk.Entry(dessert_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=6,
                                 state=tk.DISABLED,
                                 textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                           column=1)
    counter += 1

# Variables
food_cost_var = tk.StringVar()
drink_cost_var = tk.StringVar()
dessert_cost_var = tk.StringVar()
subtotal_cost_var = tk.StringVar()
taxes_cost_var = tk.StringVar()
total_cost_var = tk.StringVar()

# Cost labels and input fields
food_cost_label = tk.Label(cost_panel,
                           text='Food Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
food_cost_label.grid(row=0, column=0)
food_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=food_cost_var)
food_cost_text.grid(row=0, column=1, padx=41)

drink_cost_label = tk.Label(cost_panel,
                           text='Drink Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
drink_cost_label.grid(row=1, column=0)
drink_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=drink_cost_var)
drink_cost_text.grid(row=1, column=1, padx=41)

dessert_cost_label = tk.Label(cost_panel,
                           text='Dessert Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
dessert_cost_label.grid(row=2, column=0)
dessert_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2, column=1, padx=41)

subtotal_cost_label = tk.Label(cost_panel,
                           text='Subtotal Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
subtotal_cost_label.grid(row=0, column=2)
subtotal_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=0, column=3, padx=41)


taxes_cost_label = tk.Label(cost_panel,
                           text='Taxes Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
taxes_cost_label.grid(row=1, column=2)
taxes_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=taxes_cost_var)
taxes_cost_text.grid(row=1, column=3, padx=41)


total_cost_label = tk.Label(cost_panel,
                           text='Total Cost',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')
total_cost_label.grid(row=2, column=2)
total_cost_text = tk.Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=total_cost_var)
total_cost_text.grid(row=2, column=3, padx=41)

# Buttons
buttons = ['total', 'invoice', 'save', 'reset']
created_buttons = []
column = 0
for button in buttons:
    button = tk.Button(buttons_panel,
                       text=button.title(),
                       font=('Dosis', 14, 'bold'),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=9)

    created_buttons.append(button)

    button.grid(row=0,
                column=column)
    column += 1

created_buttons[0].config(command=total_calculations)
created_buttons[1].config(command=create_invoice)
created_buttons[2].config(command=save_invoice)
created_buttons[3].config(command=reset_all)

# Invoice area
invoice_text = tk.Text(invoice_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=42,
                       height=17)
invoice_text.grid(row=0, column=0)

# Calculator
calculator_display = tk.Entry(calc_panel,
                              font=('Dosis', 16, 'bold'),
                              width=32,
                              bd=1)
calculator_display.grid(row=0, column=0, columnspan=4)

calculator_buttons = ['7', '8', '9', '+',
                      '4', '5', '6', '-',
                      '1', '2', '3', 'x',
                      'CE', 'DELETE', '0', '/']

stored_buttons = []

my_row = 1
my_column = 0

for button in calculator_buttons:
    button = tk.Button(calc_panel,
                       text=button.title(),
                       font=('Dosis', 16, 'bold'),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=8)

    stored_buttons.append(button)

    button.grid(row=my_row, column=my_column)
    if my_column == 3:
        my_row += 1

    my_column += 1
    if my_column == 4:
        my_column = 0

stored_buttons[0].config(command=lambda: click_button('7'))
stored_buttons[1].config(command=lambda: click_button('8'))
stored_buttons[2].config(command=lambda: click_button('9'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('1'))
stored_buttons[9].config(command=lambda: click_button('2'))
stored_buttons[10].config(command=lambda: click_button('3'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=lambda: get_result())
stored_buttons[13].config(command=lambda: delete_all())
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))

# Prevent window from closing
application.mainloop()
