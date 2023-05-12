#Calulator for two numbers

#defying functions for add,sub,etc.
def add(a,b) :
    added = a + b
    return added
def mult(a,b):
    multiplied = a * b
    return multiplied
def div(a,b):
    divided = a / b
    return divided
def sub(a,b):
    subtracted = a - b
    return subtracted
#ask for add,sub,etc.

print ('Would You Like To')
print ('1. Add')
print ('2. Subtract')
print ('3. Divide')
print ('4. Multiply')
#loop to ask for new calc after one is made
while True:
    inp = input('Would you like to add, subtract, divide, or multiply two numbers?')
    inp = inp.lower()

#promt a value
#if a number is not entered, invalid input is returned
#same for the second value

    a = input ('what is the first value?')
    b = input('what is your next value?')
    try:
        a=float(a)
        b=float(b)
    except:
        print ('Invalid Input')
        break

#if the input can be converted to an interger, invalid input is returned
#if it can't, except is ran and the input checks if add, sub, etc. is entered, if not , 'not a valid option' is returne
#defied functions are used to calculate a and b. End loop if an invalid input is entered

    try:
        int(inp)
        print ('Invalid Input')
        break
    except:
        if inp == 'add':
            print (a, '+', b, '=', add(a,b))
        elif inp == 'subtract':
            print (a, '-', b, '=', sub(a,b))
        elif inp == 'divide':
            print (a, '/', b, '=', div(a,b))
        elif inp == 'multiply':
            print (a, '*', b, '=', mult(a,b))
        else:
            print ('not a valid option')
            break
#ask for new calc, if yes new calc, if n or invalid input end loop
    next_calc = input ('New Calculation? Y/N')
    next_calc = next_calc.lower()
    if next_calc == 'y':
        continue
    if next_calc == 'n':
        break
    else:
        print ('invalid input, you did not input Y,y or N,n')
        break