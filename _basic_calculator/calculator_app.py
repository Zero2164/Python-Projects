# import loading animation
from loading_animation import loading_animation
# import required components
import operator
import time

#Define Operators for Main App Function
allowed_operators={
"+": operator.add,
"-": operator.sub,
"*": operator.mul,
"/": operator.truediv,
"%": operator.mod}

# Clear the terminal window to present script code
print("\033c", end="")

# Basic Calculator Code
def app ():
    print('Welcome to Calculator App!','\n Here you can calculate basic equations with 2 numbers and an operator.\n')
    num1 = float(input('First Number: '))
    operator = input('Choose an operator ( + , - , * , % , / ): ')
    num2 = float(input('Second Number: '))
    # Start Loading Animation
    loading_animation('load', 'Calculating..', '**** Calculating Complete. Below are the results: ****')
    time.sleep(1)
    # Display Results
    result = allowed_operators[operator](num1, num2)
    print('Here is the result:',result,'\n')
    print('Here is the result rounded:',round(result),'\n')
    # loading_animation('exit')
    loading_animation('exit')

# Run Calculator Main App code
app()




