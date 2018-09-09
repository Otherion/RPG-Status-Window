import PySimpleGUI as sg


def status_window():

    sg.ChangeLookAndFeel('TealMono')  #Changes color scheme of window created
    form = sg.FlexForm('Status Window', auto_size_text=True, auto_size_buttons=False, grab_anywhere=False, return_keyboard_events=True)
    
    cname = sg.Text('', size=(20, 1))   # The name of your character
    start_class = sg.Text('', size=(12, 1), font=('Helvetica', 20), background_color='black', text_color='white', 
                          justification='center', key='class')
    
    #Classes are placeholder names and will change
    class_list = ['Warrior', 'Wizard', 'Rogue', 'Sword Mage', 'Mercenary', 'Sorcerer', 'All-Rounder']

    istat = 5   # Initial stat value
    layout = [[sg.Text('Name:'), cname, sg.ReadFormButton('Choose Name')],  # Layout for the status window
              [sg.Text('_' * 55)],
              [sg.Text('Stats:')],
              [sg.Text('STR:', size=(5, 1)),
               sg.Spin([i for i in range(0, 101)], initial_value=istat, key='STR', size=(5, 1), change_submits=True)],
              [sg.Text('INT:', size=(5, 1)),
               sg.Spin([i for i in range(0, 101)], initial_value=istat, key='INT', size=(5, 1), change_submits=True)],
              [sg.Text('DEX:', size=(5, 1)),
               sg.Spin([i for i in range(0, 101)], initial_value=istat, key='DEX', size=(5, 1), change_submits=True)],
              [sg.Text('Class:', size=(5, 1), font=('Helvetica', 20)), start_class, sg.ReadFormButton('Class Info')],
              [sg.ReadFormButton('Reset Stats'), sg.Text(' ' * 51), sg.Exit()]]

    form.Layout(layout)

    while True:
        button, values = form.Read()
        
        if button == 'Choose Name':                      # Button to type in your name for your character
            name = sg.PopupGetText('What is your name?')
            cname.Update(name)
        
        if button is None or button == 'Exit': break     # Program ends successfully if 'Quit' is clicked or window is closed

        #When no stat requirements are met:
        try:
            strength = int(values['STR'])
            intel = int(values['INT'])
            dex = int(values['DEX'])
        except:
            continue

        if all((strength, intel, dex)) < 10: start_class.Update('')

        # Classes based on one stat:
        if strength == 10:
            start_class.Update(class_list[0])
        elif intel == 10:
            start_class.Update(class_list[1])  
        elif dex == 10:
            start_class.Update(class_list[2])

        # Classes based on two stats:
        if strength >= 10 and intel >= 10:
            start_class.Update(class_list[3])
        elif strength >= 10 and dex >= 10:
            start_class.Update(class_list[4])
        elif intel >= 10 and dex >= 10:
            start_class.Update(class_list[5])

        # Classes based on three stats:
        if strength >= 10 and intel >= 10 and dex >= 10: start_class.Update(class_list[6])
        
        # Button that resets stats back initial values as well as class name
        if button == 'Reset Stats':
            form.FindElement('STR').Update(istat)
            form.FindElement('INT').Update(istat)
            form.FindElement('DEX').Update(istat)
            form.FindElement('class').Update('')
        
        #Class info button
        if button == 'Class Info' and start_class.DisplayText == '':
            sg.Popup('Not a Class:', 'If you see this, go back and obtain a class!')
        if button == 'Class Info' and start_class.DisplayText == 'Warrior':         #Example of a popup display explaining the class when the button is pressed
            sg.Popup('Warrior Class:', 'A class that specializes in melee combat')  #Placeholder descriptions
