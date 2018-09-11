import PySimpleGUI as sg

def magic_types():
    with sg.FlexForm('Popup') as form: # begin with a blank form

        layout = [[sg.Text('Choose a magic to specialize in:')],
                  [sg.Radio('Fire', 'magic', size=(8, 1)), sg.Radio('Ice', 'magic', size=(8, 1))],
                  [sg.Radio('Water', 'magic', size=(8, 1)), sg.Radio('Space', 'magic', size=(8, 1))],
                  [sg.Radio('Earth', 'magic', size=(8, 1)), sg.Radio('Time', 'magic', size=(8, 1))],
                  [sg.Radio('Wind', 'magic', size=(8, 1)), sg.Radio('Holy', 'magic', size=(8, 1))],
                  [sg.Radio('Electricity', 'magic', size=(8, 1)), sg.Radio('Shadow', 'magic', size=(8, 1))],
                  [sg.OK()]]

        button, values = form.LayoutAndRead(layout)
        return values
    
def status_window():

    sg.ChangeLookAndFeel('TealMono')  #Changes color scheme of window created
    form = sg.FlexForm('Status Window', auto_size_text=True, auto_size_buttons=False, grab_anywhere=False, return_keyboard_events=True)
    
    #Classes are placeholder names and will change
    class_list = ['Warrior', 'Wizard', 'Rogue', 'Sword Mage', 'Mercenary', 'Sorcerer', 'All-Rounder']


    # Layout for the status window
    layout = [[sg.Text('Name:'), sg.Text('', size=(20, 1), background_color='black', text_color='white', key='cname'),
               sg.ReadFormButton('Choose Name')],
              [sg.Text('_' * 55)],
              [sg.Text('Stats:')],
              [sg.Text('STR:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=5, key='STR', size=(5, 1), change_submits=True)],
              [sg.Text('INT:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=5, key='INT', size=(5, 1), change_submits=True),
               sg.ReadFormButton('Magic Type')],
              [sg.Text('DEX:', size=(5, 1)),
               sg.Spin([i for i in range(5, 101)], initial_value=5, key='DEX', size=(5, 1), change_submits=True)],
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
        except:
            continue

        if all((strength, intel, dex)) < 10: form.FindElement('class').Update('')

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
            
        # What the 'Magic Type' button does and an example of it changing the class
        if button == 'Magic Type':
            values = magic_types()
            if values[0] is True and form.FindElement('class').DisplayText == 'Wizard':
                form.FindElement('class').Update('Fire' + ' Wizard')

        # Button that resets stats back initial values as well as class name
        if button == 'Reset Stats':
            form.Fill({'STR': 5, 'INT': 5, 'DEX': 5})
            if all((strength, intel, dex)) < 10: form.FindElement('class').Update('')

        # Class info button
        if button == 'Class Info' and form.FindElement('class').DisplayText == '':
            sg.Popup('Not a Class:', 'If you see this, go back and obtain a class!')
        if button == 'Class Info' and form.FindElement('class').DisplayText == 'Warrior':  # Example of a popup display explaining the class when the button is pressed
            sg.Popup('Warrior Class:', 'A class that specializes in melee combat')         # Placeholder descriptions
