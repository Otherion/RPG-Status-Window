import PySimpleGUI as sg


def status_window():

    sg.ChangeLookAndFeel('TealMono')  #Changes color scheme of window created
    form = sg.FlexForm('Status Window', auto_size_text=True, auto_size_buttons=False, grab_anywhere=False)
    
    cname = sg.Text('', size=(20, 1))   # The name of your character
    start_class = sg.Text('', size=(12, 1), font=('Helvetica', 20), background_color='black', text_color='white', justification='center')
    
    #Classes are placeholder names and will change
    class_list = ['Warrior', 'Wizard', 'Rogue', 'Sword Mage', 'Mercenary', 'Sorcerer', 'All-Rounder']

    layout = [[sg.Text('Name:'), cname, sg.RealtimeButton('Choose Name')],    #Layout for the status window
              [sg.Text('_' * 55)],
              [sg.Text('Stats:')],
              [sg.Text('STR:', size=(5, 1)), sg.Spin([i for i in range(0, 101)], initial_value=0, key='STR', size=(5, 1))],
              [sg.Text('INT:', size=(5, 1)), sg.Spin([i for i in range(0, 101)], initial_value=0, key='INT', size=(5, 1))],
              [sg.Text('DEX:', size=(5, 1)), sg.Spin([i for i in range(0, 101)], initial_value=0, key='DEX', size=(5, 1))],
              [sg.Text('Class:', size=(5, 1), font=('Helvetica', 20)), start_class, sg.RealtimeButton('Class Info')],
              [sg.Text(' ' * 34), sg.Exit()]]

    form.LayoutAndRead(layout, non_blocking=True)

    while True:
        button, values = form.ReadNonBlocking()
        
        if button == 'Choose Name':
            name = sg.PopupGetText('What is your name?')
            cname.Update(name)
        
        if values is None or button == 'Exit': break                        #Program ends successfully if 'Quit' is clicked or window is closed

        #When no stat requirements are met:
        if all([int(values['STR']), int(values['INT']), int(values['DEX'])]) < 10: start_class.Update('')

        #Classes based on one stat:
        if int(values['STR']) == 10: start_class.Update(class_list[0])
        elif int(values['INT']) == 10: start_class.Update(class_list[1])      #Class is displayed in window when the stat requirements are met  (stat requirements are placeholder)
        elif int(values['DEX']) == 10: start_class.Update(class_list[2])

        #Classes based on two stats:
        if int(values['STR']) >= 10 and int(values['INT']) >= 10: start_class.Update(class_list[3])
        elif int(values['STR']) >= 10 and int(values['DEX']) >= 10: start_class.Update(class_list[4])
        elif int(values['INT']) >= 10 and int(values['DEX']) >= 10: start_class.Update(class_list[5])

        #Classes based on three stats:
        if int(values['STR']) >= 10 and int(values['INT']) >= 10 and int(values['DEX']) >= 10: start_class.Update(class_list[6])

        #Class info button
        if button == 'Class Info' and start_class.DisplayText == '':
            sg.Popup('Not a Class:', 'If you see this, go back and obtain a class!')
        if button == 'Class Info' and start_class.DisplayText == 'Warrior':         #Example of a popup display explaining the class when the button is pressed
            sg.Popup('Warrior Class:', 'A class that specializes in melee combat')  #Placeholder descriptions
