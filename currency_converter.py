from tkinter import *
from api import eur_rate

# colors
color_1 = 'black'
color_2 = 'white'

# window
window = Tk()
window.minsize(330, 80)
window.resizable(False, False)
window.title('Currency converter')
window.config(bg=color_1)

# user value input
user_input = Entry(window, justify=CENTER)
user_input.focus()
user_input.grid(row=0, column=0, padx=10, pady=10)

# result label
output = Label(window, anchor='center', width=17, height=1)
output.grid(row=1, column=0, padx=10, pady=10)

# Currency selection
rol_1 = StringVar(window)
rol_1.set('CZK')
rol_1_opt = OptionMenu(window, rol_1, 'CZK', 'EUR')
rol_1_opt.grid(row=0, column=1, padx=10)

rol_2 = StringVar(window)
rol_2.set('EUR')
rol_2_opt = OptionMenu(window, rol_2, 'CZK', 'EUR')
rol_2_opt.grid(row=1, column=1, padx=10)

# function conversion
def count():
    from_value = rol_1.get() 
    to_value = rol_2.get()
        
    user_value = float(user_input.get().replace(',', '.'))
    
    if from_value == to_value:
        result = "{:.2f}".format(user_value)
        output.config(text=result)
    elif from_value == 'EUR':
        if to_value == 'CZK':
            result = "{:.2f}".format(user_value*eur_rate, 2)
            output.config(text=result)
    
    elif from_value == 'CZK':
        if to_value == 'EUR':
            result = "{:.2f}".format(user_value/eur_rate, 2)
            output.config(text=result)
    

# button conversion
button = Button(text='Conversion', width=17, command=count)
button.grid(row=0, column=2, padx=10)

# API source citation
source = Label(window, text='"API source: kurzy.cz"', font=('',8,'italic'), bg=color_1, fg=color_2)
source.grid(row=1, column=2, padx=10)


window.mainloop()