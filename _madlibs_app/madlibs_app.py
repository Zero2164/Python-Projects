# import loading animation
from loading_animation import loading_animation
# import required components
import time

# Clear the terminal window to present script code
print("\033c", end="")

# Mad Libs App Code
def app():
    # Define Variables
    color = input('Enter a color: ')
    plural_noun = input('Enter a Plural Noun: ')
    celebrity = input('Enter a Celebrity: ')
    # Start Loading Animation
    loading_animation('load', 'Loading Script', '**** Loading Complete. Below are the results: ****')
    time.sleep(1)
    # Display Results
    print('Roses are',color)
    print(plural_noun,'are blue')
    print('I love',celebrity)
    # loading_animation('exit')
    loading_animation('exit')
    
# Run MadLibs Main App code
app()

