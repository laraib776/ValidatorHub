import tkinter as tk
import re

"ISBN_10"
def isbn10():
    isbn10_var=inpt.get()
    # Strip spaces and dashes
    code_string = isbn10_var.replace("-", "").replace(" ", "")
    # Make sure string argument is valid
    if len(code_string) != 10:
        output_lbl2.config(text="InValid ISBN10 : ")
    if not code_string[0:8].isdigit() or not (code_string[9].isdigit() or code_string[9].lower() == "x"):
        output_lbl2.config(text="InValid ISBN10 : ")

    # Initialise result to 0
    result = 0

    # Iterate through code_string
    for i in range(9):
        # for each character, multiply by a different decreasing number: 10 - x
        result = result + int(code_string[i]) * (10 - i)

    # Handle last character
    if code_string[9].lower() == "x":
        result += 10
    else:
        result += int(code_string[9])

    #print(result," is the result ")  # For debugging if required

    # Return whether the isbn is valid
    if result % 11 == 0:
        output_lbl2.config(text="Valid ISBN10 --- "+str(result)+" is the result of X10 ")
    else:
        output_lbl2.config(text="InValid ISBN10 --- "+str(result) + " is the result of X10 ")

    # If you prefer and understand why it is equivalent
    # return result % 11 == 0
#validate_isbn10("77696985X")
#validate_isbn10("013-609-181-4")   # 013-609-181-4 is a valid ISBN-10
#isbn10("6757-8989-901")      # 3-598-21507-X is a valid ISBN-10

"Credit Card"
def credit_card():
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number=inpt.get()
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    if checkSum % 10 == 0:
        output_lbl2.config(text="Valid Credit Card Number")
    else:
        output_lbl2.config(text="InValid Credit Card Number")


# Python3 program to validate Visa
# Card number using regular expression

"Visa Card"
# Function to validate Visa Card
# number using regular expression.
def isValidVisaCardNo():
    string=inpt.get()
    # Regex to check valid Visa
    # Card number
    regex = "^4[0-9]{12}(?:[0-9]{3})?$"
 
    # Compile the ReGex
    p = re.compile(regex)
     
    # If the string is empty
    # return false
    if (string == ''):
        output_lbl2.config(text="InValid Visa Card Number")
         
    # Pattern class contains matcher()
    # method to find matching between
    # given string and regular expression.
    m = re.match(p, string)
     
    # Return True if the string
    # matched the ReGex else False
    if m is None:
        output_lbl2.config(text="InValid Visa Card Number")
    else:
        output_lbl2.config(text="Valid Visa Card Number")
        

"UPC : Universal Card Currency"

class ISBNValidator:
    class FormatException(Exception):
        pass

    @staticmethod
    def prepare_code_string(code_string):
        #code_string=inpt.get()
        retval = code_string.replace("-", "")
        retval = retval.replace(" ", "")
        return retval

    @staticmethod
    def calculate_upc_checkdigit(first_11_numbers:str)->str:
        if len(first_11_numbers) != 11 or not first_11_numbers.isnumeric():
            #raise ISBNValidator.FormatException("Improper format in first 11 numbers of UPC")
            output_lbl2.config(text="Invalid : Improper format")
        checksum = 0
        for (count, digit) in enumerate(first_11_numbers):
            weight = 1 + (((count + 1) % 2) * 2)
            checksum += (int(digit) * weight)
        checkdigit = (10 - (checksum % 10)) % 10
        return str(checkdigit)
        #output_lbl2.config(text=str(checkdigit)+" : is our check digit")

    @staticmethod
    def validate_upc():
        code_string=inpt.get()
        upc_string = ISBNValidator.prepare_code_string(code_string)
        if len(upc_string) != 12:
            output_lbl2.config(text="InValid : upc" )
        else:
            retval = ISBNValidator.calculate_upc_checkdigit(upc_string[:-1]) == upc_string[-1:]
            output_lbl2.config(text="Our UPC is :"+str(retval))


obj = ISBNValidator()
#obj.validate_upc("3-598-21507-X")

win = tk.Tk()
win.title('__DS-PROJECT__           210201001')

win.geometry("500x500")  # set the root1 dimensions
win.pack_propagate(False)  # tells the root1 to not let the widgets inside it determine its size
win.resizable(0, 0)  # makes the root1 window fixed in size.
win.config(background='PeachPuff2')

reg_var = tk.StringVar()
pas_var = tk.StringVar()

lbl1 = tk.Label(win, text='Universal Product Code :')
lbl1.config(background='PeachPuff3')

a = tk.Button(win, text="UPC", command=obj.validate_upc)
a.config(background='PeachPuff3')

lbl2 = tk.Label(win, text='Credit Card:')
lbl2.config(background='PeachPuff3')

b = tk.Button(win, text="Credit Card", command=credit_card)
b.config(background='PeachPuff3')

lbl3 = tk.Label(win, text='International Standard Book Number_10 :')
lbl3.config(background='PeachPuff3')

c = tk.Button(win, text="ISBN_10", command=isbn10)
c.config(background='PeachPuff3')

lbl4 = tk.Label(win, text='Visa Cards :')
lbl4.config(background='PeachPuff3')

d = tk.Button(win, text="VS_Card", command=isValidVisaCardNo)
d.config(background='PeachPuff3')

inpt_lbl = tk.Label(win, text="Input")
inpt_lbl.config(background='PeachPuff3')

output_lbl1 = tk.Label(win, text="0utput")
output_lbl1.config(background='PeachPuff3')

inpt = tk.Entry(win, textvariable=reg_var, font=('calibre', 10, 'bold'))
inpt.config(background='PeachPuff3')

output_lbl2 = tk.Label(win,  font=('arial', 10, 'bold'))
output_lbl2.config(background='PeachPuff3')

lbl1.place(x=50, y=50)
lbl2.place(x=50, y=100)
lbl3.place(x=50, y=150)
lbl4.place(x=50, y=200)

a.place(x=300, y=50)
b.place(x=300, y=100)
c.place(x=300, y=150)
d.place(x=300, y=200)

inpt_lbl.place(x=50, y=270)
output_lbl1.place(x=50, y=360)

inpt.place(x=50, y=310)
output_lbl2.place(x=50, y=410)

btn = tk.Button(win, text="  Exit  ", command=win.destroy)
btn.place(x=350, y=400)
btn.config(background='PeachPuff3')
win.mainloop()