# Importing Script Dependencies 
import itertools
import threading
import time
import sys


# Define Loading Animation Function
def loading_animation(opt, load_msg='Clearing History', exit_msg='History Cleared. Bye!'):
    loadmsg = load_msg
    exitmsg = exit_msg
    done = False
    def animate(load_msg, exit_msg):
    # def animate():
        print('')
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write(load_msg + c)
            sys.stdout.flush()
            time.sleep(0.1)
        print(exit_msg)
        time.sleep(1.6)


    def play_animate(load_msg, exit_msg):
        t = threading.Thread(target=animate, args=(load_msg, exit_msg))
        t.start()

    # loading option
    if opt == 'load':
        play_animate('\r'+loadmsg,'\n \n'+exitmsg+'\n')
        time.sleep(1)
        done = True

    # exit code option 
    if opt == 'exit':
        inpt_end_script = input('\nClear script output before closing? (y/n):')

        if inpt_end_script == 'y':
            play_animate('\033c\r'+loadmsg,'\033c'+exitmsg)
            time.sleep(1)
            done = True
            time.sleep(1.6)
            print("\033c", end="")
        if inpt_end_script == 'n' :
            print('\n**** Ok above this line is previous script output. Have a great day. ****\n')
    
