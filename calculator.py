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
#promt a value

while True:
    inp = input('Add(1) Subtract (2) Divide (3) Multiply(4)?')
    
#if a the input is not a num then return invalid input and break
    try:
        a = float(input ('what is the first value?'))
        b = float(input('what is your next value?'))
    except:
        print ('Choose A Valid Number')
        break

#if the inp is not 1 , 2 , 3 , 4 invalid is returned

    if inp == '1':
        print (a, '+', b, '=', add(a,b))
    elif inp == '2':
        print (a, '-', b, '=', sub(a,b))
    elif inp == '3':
        print (a, '/', b, '=', div(a,b))
    elif inp == '4':
        print (a, '*', b, '=', mult(a,b))
    else:
        print ('not a valid option')
        break

#ask for new calc, if yes (y) new calc, if no (n) or invalid input end loop
    
    next_calc = input ('New Calculation? Y/N')
    next_calc = next_calc.lower()
    if next_calc == 'y':
        continue
    if next_calc == 'n':
        break
    else:
        print ('invalid input')
        break