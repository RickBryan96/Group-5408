#This program reverses the user input
def inputreverse(ui):
    words = ui.split(' ')
    reversed_input = ' '.join(reversed(words))
    return reversed_input

s = input("What would you like to reverse?" "\n") 
print(inputreverse(s))

