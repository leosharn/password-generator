import tkinter as tk
import random
from tkinter import ttk



def increase_length():
    """Increase the length of the generated password, no more than 12 characters"""
    global length
    if length < 12:
        length += 1
    length_entry.config(state=tk.NORMAL)
    length_entry.delete(0, tk.END)
    length_entry.insert(1, ' '+str(length))
    length_entry.config(state=tk.DISABLED) 

def decrease_length():
    """Reducing the length of the generated password, at least 6 characters"""
    global length
    if length > 6:
        length -= 1
    length_entry.config(state=tk.NORMAL) 
    length_entry.delete(0, tk.END)
    length_entry.insert(1, ' '+str(length))
    length_entry.config(state=tk.DISABLED) 

length = 9 #password default length


def is_digits(is_digits_check, temp):
    """"The function of checking whether to use numbers in the final result"""
    if not is_digits_check:
        temp_without_digits = ''.join(i for i in temp if i not in '0123456789')
        temp = temp_without_digits
        return temp
    else:
        return temp
    
def is_lower(is_lower_check, temp):
    """The function checks whether to use lowercase letters in the final result"""
    if not is_lower_check:
        temp_without_lower = ''.join(i for i in temp if i not in 'abcdefghijklmnopqrstuvwxyz')
        temp = temp_without_lower
        return temp
    else:
        return temp
    
def is_upper(is_upper_check, temp):
    """"The function checks whether to use capital letters in the final result"""
    if not is_upper_check:
        temp_without_upper = ''.join(i for i in temp if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        temp = temp_without_upper
        return temp
    else:
        return temp

def is_punctual(is_punctual_check, temp):
    """The function of checking whether to use signs !#$%&*+-=?@^ in the final result"""
    if not is_punctual_check:
        temp_without_punctual = ''.join(i for i in temp if i not in '!#$%&*+-=?@^_')
        temp = temp_without_punctual
        return temp
    else:
        return temp
    
def is_problematic(is_problematic_check, for_gen):
    """The function checks whether the characters 0oO1iIlL should be used in the final result.
The function takes as input the result of the functions is_digits, is_lower, is_upper_, is_punctual"""
    if not is_problematic_check:
        for_gen_without_problematic = ''.join(i for i in for_gen if i not in '0oO1iIlL')
        for_gen = for_gen_without_problematic
        return for_gen
    else:
        return for_gen

def update_digits(*args):
    global is_digits_check
    is_digits_check = chk2_var.get()

def update_lower(*args):
    global is_lower_check
    is_lower_check = chk3_var.get()

def update_upper(*args):
    global is_upper_check
    is_upper_check = chk4_var.get()

def update_punctual(*args):
    global is_punctual_check
    is_punctual_check = chk5_var.get()

def update_problematic(*args):
    global is_problematic_check
    is_problematic_check = chk6_var.get()

is_digits_check = True
is_lower_check = True
is_upper_check = True
is_punctual_check = True
is_problematic_check = True




window = tk.Tk(screenName='Password Generator')
window.title("Password Generator")



temp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'

font_for_output = ('San Francisco', 16)
font_for_length = ('San Francisco', 16)
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', '#45dfb1'), ('active', '#80ed99')],
            )

# fill frames on the left, right and in the middle, without functionality
frame_left = tk.Frame(master=window, width=20, height=600,)
frame_center = tk.Frame(master=window, width=610, height=500)
frame_right = tk.Frame(master=window, width=20, height=600)

main_frame = tk.Frame(width=1000, height=800)

# main frame for password OUTPUT
frame_output = tk.Frame(master=main_frame, height=200, width=1000)
frame_output.pack_propagate(True)

# mainframe for both checkboxes and buttons
frame_input = tk.Frame(master=main_frame, height=200, width=600)


# label frame
label_frame = tk.Frame(master=frame_input, height=200, width=450)
# checkboxes frame
checkboxes_frame = tk.Frame(master=frame_input, height=200, width=50)
# generate button frame
button_frame = tk.Frame(master=frame_input, height=200, width=200)


# This is where the framing starts
frame_left.pack(side='left', fill='both', expand=True) #empty left frame-placeholder
frame_center.pack(side='left', fill="both", expand=True, padx=.5, pady=.5) #central frame-placeholder
frame_right.pack(side='left', fill='both', expand=True) #empty right frame-placeholder
main_frame.place(in_=frame_center, anchor="c", relx=.5, rely=.5) #here goes all interactive 

frame_output.pack()
frame_input.pack() 
label_frame.pack(side='left', expand=True, fill='both') 
checkboxes_frame.pack(side='left', expand=True, fill='both') 
button_frame.pack(side='left', expand=True, fill='both') 

# frames for every label
label_1_frame = tk.Frame(master=label_frame, height=100, width=400)
label_1_frame.pack_propagate(True)
label_2_frame = tk.Frame(master=label_frame, height=50, width=400)
label_2_frame.pack_propagate(True)
label_3_frame = tk.Frame(master=label_frame, height=50, width=400)
label_3_frame.pack_propagate(True)
label_4_frame = tk.Frame(master=label_frame, height=50, width=400)
label_4_frame.pack_propagate(True)
label_5_frame = tk.Frame(master=label_frame, height=50, width=400)
label_5_frame.pack_propagate(True)
label_6_frame = tk.Frame(master=label_frame, height=50, width=400)
label_6_frame.pack_propagate(True)

# frames for every checkbox
checkboxes_frame_1 = tk.Frame(master=checkboxes_frame, height=100, width=50) #here will be +- button and length entry
checkboxes_frame_2 = tk.Frame(master=checkboxes_frame, height=50, width=50)
checkboxes_frame_3 = tk.Frame(master=checkboxes_frame, height=50, width=50)
checkboxes_frame_4 = tk.Frame(master=checkboxes_frame, height=50, width=50)
checkboxes_frame_5 = tk.Frame(master=checkboxes_frame, height=50, width=50)
checkboxes_frame_6 = tk.Frame(master=checkboxes_frame, height=50, width=50)

# button frame
generate_frame = tk.Frame(master=button_frame)


# THIS IS WHERE THE CONTENT SETUP STARTS, ALL FRAMES ARE CONFIGURED CORRECTLY

# placing label frames
label_1_frame.pack(fill='both')
label_2_frame.pack(fill='both')
label_3_frame.pack(fill='both')
label_4_frame.pack(fill='both')
label_5_frame.pack(fill='both')
label_6_frame.pack(fill='both')

# setup labels
length_label = tk.Label(master=label_1_frame, text='Password length\n(from 6 to 12 characters, default is 9)', font=font_for_length, bg='#45dfb1', fg='#213a57')
digits_label = tk.Label(master=label_2_frame, text='Whether to use numeric\n  characters in the password  ', font=font_for_length, bg='#45dfb1', fg='#213a57')
lower_label = tk.Label(master=label_3_frame, text='Whether to use lowercase\n  characters in the password  ', font=font_for_length, bg='#45dfb1', fg='#213a57')
upper_label = tk.Label(master=label_4_frame, text='Whether to use uppercase\n  characters in the password  ', font=font_for_length, bg='#45dfb1', fg='#213a57')
punct_label = tk.Label(master=label_5_frame, text='Whether to use punctuation\n  characters in the password  ', font=font_for_length, bg='#45dfb1', fg='#213a57')
problematic_label = tk.Label(master=label_6_frame, text='Include characters\n    (0oO1iIlL) in the password  ', font=font_for_length, bg='#45dfb1', fg='#213a57')

length_label.place(in_=label_1_frame, anchor="c", relx=.5, rely=.5)
digits_label.place(in_=label_2_frame, anchor="c", relx=.5, rely=.5)
lower_label.place(in_=label_3_frame, anchor="c", relx=.5, rely=.5)
upper_label.place(in_=label_4_frame, anchor="c", relx=.5, rely=.5)
punct_label.place(in_=label_5_frame, anchor="c", relx=.5, rely=.5)
problematic_label.place(in_=label_6_frame, anchor="c", relx=.5, rely=.5)

# place checkboxes
checkboxes_frame_1.pack(fill='both')
checkboxes_frame_1.propagate(False)
checkboxes_frame_2.pack(fill='both')
checkboxes_frame_3.pack(fill='both')
checkboxes_frame_4.pack(fill='both')
checkboxes_frame_5.pack(fill='both')
checkboxes_frame_6.pack(fill='both')

# setup window with buttons +- and entry for password length
button_plus = ttk.Button(master=checkboxes_frame_1, text='+', command=increase_length, style='C.TButton')
length_entry = tk.Entry(master=checkboxes_frame_1, bg='#45dfb1', fg='red',
                         width=3, font=font_for_length, relief='raised', disabledforeground='#213a57',
                          disabledbackground='#45dfb1' )
length_entry.insert(0, ' '+str(length))
length_entry.configure(state='disabled')
button_minus = ttk.Button(master=checkboxes_frame_1, text='-', command=decrease_length, style='C.TButton')
button_plus.pack(side='top')
length_entry.place(anchor="c", relx=.5, rely=.5)
button_minus.pack(side='bottom')



# checkboxes 2-6
style = ttk.Style()
style.configure("Custom.TCheckbutton", background="green", foreground="green", font=("Helvetica", 12))



chk2_var = tk.BooleanVar(value=True)
chk2_var.trace_add('write', update_digits)
chk_2 = ttk.Checkbutton(master=checkboxes_frame_2, variable=chk2_var, style="Custom.TCheckbutton")
chk2_var.set(True)


chk3_var = tk.BooleanVar(value=True)
chk3_var.trace_add('write', update_lower)
chk_3 = ttk.Checkbutton(master=checkboxes_frame_3, variable=chk3_var, style="Custom.TCheckbutton")
chk3_var.set(True)

chk4_var = tk.BooleanVar(value=True)
chk4_var.trace_add('write', update_upper)
chk_4 = ttk.Checkbutton(master=checkboxes_frame_4, variable=chk4_var, style="Custom.TCheckbutton")
chk4_var.set(True)

chk5_var = tk.BooleanVar(value=True)
chk5_var.trace_add('write', update_punctual)
chk_5 = ttk.Checkbutton(master=checkboxes_frame_5, variable=chk5_var, style="Custom.TCheckbutton")
chk5_var.set(True)

chk6_var = tk.BooleanVar(value=True)
chk6_var.trace_add('write', update_problematic)
chk_6 = ttk.Checkbutton(master=checkboxes_frame_6, variable=chk6_var, style="Custom.TCheckbutton")
chk6_var.set(True)

chk_2.place(anchor='c', relx=.5, rely=.5)
chk_3.place(anchor='c', relx=.5, rely=.5)
chk_4.place(anchor='c', relx=.5, rely=.5)
chk_5.place(anchor='c', relx=.5, rely=.5)
chk_6.place(anchor='c', relx=.5, rely=.5)

# OUTPUT WINDOW
greeting = (['Welcome to the password generation program.\n',
            ' Please select the desired password generation options:\n',
            ' - Password length (from 6 to 12 characters, default is 9);\n',
            ' - Whether to use numeric characters in the password;\n',
            ' - Whether to use lowercase characters in the password;\n',
            ' - Whether to use uppercase characters in the password;\n',
            ' - Whether to use punctuation characters in the password;\n',
            ' - Whether to use problematic characters in the password.\n',
            ' After the final selection, click the Generate button\n'])

output_text = tk.Text(master=frame_output, bg='#45dfb1', fg='#213a57', height=10, relief='flat', border=3, font=font_for_output, width=70)
output_text.place(anchor='center', relx=.5, rely=.5)


for i in range(len(greeting)):
    output_text.insert(f'{i+1}.0', greeting[i])
output_text.configure(state='disabled')


# MAIN BUTTON SETTINGS
def put_temp(temp):
    """The function for generating the total value"""
    temp = is_digits(is_digits_check, temp)
    temp = is_lower(is_lower_check, temp)
    temp = is_upper(is_upper_check, temp)
    for_gen = is_punctual(is_punctual_check, temp)
    for_gen = is_problematic(is_problematic_check, for_gen)
    output_text.configure(state='normal')
    output_text.delete('1.0', 'end')
    list_gen = []
    while True:
        shuffled = list(for_gen)  
        random.shuffle(shuffled)
        generated_string = (''.join(shuffled))[:length]
        if (is_digits_check and not any(c.isdigit() for c in generated_string)) \
            or (is_lower_check and not any(c.islower() for c in generated_string)) \
            or (is_upper_check and not any(c.isupper() for c in generated_string)) \
            or (is_punctual_check and not any(c in '!#$%&*+-=?@^_' for c in generated_string)) \
            or (sum(c in '!#$%&*+-=?@^_' for c in generated_string) > 1
            or (sum(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in generated_string) > 2)):
            # If at least one of the conditions is not met, i.e. the generated string does not meet the requirements
                continue

        if generated_string in list_gen: #if the generated value is already in the list of results, then skip it and do not use it.
            continue
        list_gen.append(generated_string)
        if len(list_gen) == 10: #if the list is filled with 10 passwords, we interrupt the cycle
            break
    for lst in list_gen:
        output_text.insert(tk.END, f'{lst}\n') #inserting the generation results into the output_txt column
    output_text.configure(state='disabled')

def on_click_generate():
    """a function for a button that displays the result of the put_temp() function on the screen"""
    put_temp(temp)

generate_frame.place(anchor='c', relx=.5, rely=.5)

generate_button = ttk.Button(master=generate_frame, text='Generate', command=on_click_generate, style='C.TButton')
generate_button.pack(anchor='center', ipadx=.5, ipady=.5)




# END OF PROGRAM
window.minsize(width=740, height=600)
window.mainloop()
