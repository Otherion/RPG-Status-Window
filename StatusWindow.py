import PySimpleGUI as sg


def status_window():

    sg.ChangeLookAndFeel('TealMono')  #Changes color scheme of window created
    form = sg.FlexForm('Status Window', auto_size_text=True, auto_size_buttons=False, grab_anywhere=False, return_keyboard_events=True)
    
    #Classes are placeholder names and will change
    class_list = ['Warrior', 'Wizard', 'Rogue', 'Sword Mage', 'Mercenary', 'Sorcerer', 'All-Rounder']

    istat = 5   # Initial stat value
    # Layout for the status window
    layout = [[sg.Text('Name:'), sg.Text('', size=(20, 1), background_color='black', text_color='white', key='cname'),
               sg.ReadFormButton('Choose Name')],
              [sg.Text('_' * 55)],
              [sg.Text('Stats:')],
              [sg.Text('Points Remaining'), sg.InputText('15', size=(3, 1), do_not_clear=True, key='points')],
              [sg.Text('STR:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=istat, key='STR', size=(5, 1), change_submits=True)],
              [sg.Text('INT:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=istat, key='INT', size=(5, 1), change_submits=True)],
              [sg.Text('DEX:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=istat, key='DEX', size=(5, 1), change_submits=True)],
              [sg.Text('Class:', size=(5, 1), font=('Helvetica', 20)),
               sg.Text('', size=(13, 1), font=('Helvetica', 20), background_color='black', text_color='white',
                       justification='center', key='class'),
               sg.ReadFormButton('Class Info')],
              [sg.ReadFormButton('Reset Stats'), sg.Text(' ' * 51), sg.Exit()]]

    form.Layout(layout)

    while True:
        button, values = form.Read()
        
        if button == 'Choose Name':                      # Button to type in your name for your character
            name = sg.PopupGetText('What is your name?')
            form.FindElement('cname').Update(name)
        
        if button is None or button == 'Exit': break     # Program ends successfully if 'Quit' is clicked or window is closed

        #When no stat requirements are met:
        try:
            strength = int(values['STR'])
            intel = int(values['INT'])
            dex = int(values['DEX'])
            spoints = int(values['points'])
        except:
            continue

        if all((strength, intel, dex)) < 10: form.FindElement('class').Update('')

        # How skill points remaining is determined (not sure how to stop stats from increasing when spoints = 0)
        if 0 < spoints < 16:
            stat = [strength, intel, dex]
            if 15 < sum(stat) <= 30:
                spoints = 15 - (sum(stat) - 15)
                form.FindElement('points').Update(spoints)

        # Classes based on one stat:
        if strength >= 10:
            form.FindElement('class').Update(class_list[0])
        elif intel >= 10:
            form.FindElement('class').Update(class_list[1])  # Class is displayed in window when the stat requirements are met  (stat requirements are placeholder)
        elif dex >= 10:
            form.FindElement('class').Update(class_list[2])

        # Classes based on two stats:
        if strength >= 10 and intel >= 10:
            form.FindElement('class').Update(class_list[3])
        elif strength >= 10 and dex >= 10:
            form.FindElement('class').Update(class_list[4])
        elif intel >= 10 and dex >= 10:
            form.FindElement('class').Update(class_list[5])

        # Classes based on three stats:
        if strength >= 10 and intel >= 10 and dex >= 10:
            form.FindElement('class').Update(class_list[6])

        # # Button that resets stats back initial values as well as class name
        elif button == 'Reset Stats':
            form.Fill({'STR': '5', 'INT': '5', 'DEX': '5', 'points': 15})
            if all((strength, intel, dex)) < 10: form.FindElement('class').Update('')

        # Class info button
        if button == 'Class Info' and form.FindElement('class').DisplayText == '':
            sg.Popup('Not a Class:', 'If you see this, go back and obtain a class!')
        if button == 'Class Info' and form.FindElement('class').DisplayText == 'Warrior':  # Example of a popup display explaining the class when the button is pressed
            sg.Popup('Warrior Class:', 'A class that specializes in melee combat')         # Placeholder descriptions
