# Configuration #
modules_list = ['madecom']
# End Configuration #

# Import user-created modules.
for module in modules_list:
    exec('import mod_{0}'.format(module))

# Prompt for user input.
while True:
    print('Here are the options available to you. Enter an option number and press enter.')
    for index, module in enumerate(modules_list):
        print('[{0}] - Run {1}'.format(index,module))
    option = int(input("Option: "))    
    if option > len(modules_list) - 1:
        print('\nThe option you chose is invalid. Please try again.\n')
    else:
        result = eval('mod_{0}.{0}()'.format(modules_list[option]))
        print(result)
        break
