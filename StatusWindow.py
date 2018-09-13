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
    
    form.ReadNonBlocking()
    form.FindElement('magic').Update(disabled=True)
   
    class_list = []
    element = []

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

        if all((strength, intel, dex)) < 10: class_list.append('')
        
        if intel < 10 and len(element) > 0: 
            del element[-1]
            form.FindElement('magic').Update(disabled=True)

        # What the 'Magic Type' button does 
        if button == 'Magic Type':
            emagic = magic_types()
            if emagic[0] is True: element.append('Fire')
            if emagic[1] is True: element.append('Ice')
            if emagic[2] is True: element.append('Water')
            if emagic[3] is True: element.append('Space')
            if emagic[4] is True: element.append('Earth')
            if emagic[5] is True: element.append('Time')
            if emagic[6] is True: element.append('Wind')
            if emagic[7] is True: element.append('Holy')
            if emagic[8] is True: element.append('Electricity')
            if emagic[9] is True: element.append('Shadow')
        
        # Classes based on one stat:
        if strength >= 10:
            class_list.append('Warrior')
        elif intel >= 10 and len(element) == 0:
            class_list.append('Wizard')
            form.FindElement('magic').Update(disabled=False)
        elif intel >= 10 and len(element) != 0:
            if element[-1] == 'Fire': class_list.append('Pyromancer')
            elif element[-1] == 'Ice': class_list.append('Cryomancer')
            elif element[-1] == 'Water': class_list.append('Hydromancer')
            elif element[-1] == 'Space': class_list.append('Spacial Wizard')
            elif element[-1] == 'Earth': class_list.append('Terra Mage')
            elif element[-1] == 'Time': class_list.append('Chronomancer')
            elif element[-1] == 'Wind': class_list.append('Sky Mage')
            elif element[-1] == 'Holy': class_list.append('Divine Mage')
            elif element[-1] == 'Electricity': class_list.append('Lightning Mage')
            elif element[-1] == 'Shadow': class_list.append('Umbral Mage')
        elif dex >= 10:
            class_list.append('Rogue')

        if intel < 10:
            form.FindElement('magic').Update(disabled=True)     
            
        # Classes based on two stats:
        if strength >= 10 and intel >= 10:
            class_list.append('Sword Mage')
        elif strength >= 10 and dex >= 10:
            class_list.append('Mercenary')
        elif intel >= 10 and dex >= 10:
            class_list.append('Sorcerer')

        # Classes based on three stats:
        if strength >= 10 and intel >= 10 and dex >= 10:
            class_list.append('All-Rounder')

        # Button that resets stats back initial values as well as class name
        if button == 'Reset Stats':
            form.Fill({'STR': 5, 'INT': 5, 'DEX': 5})
            form.FindElement('magic').Update(disabled=True)
            class_list.clear(); class_list.append('')  # Clears the list then appends an empty string to it as the first item
            element.clear()  # Clears the element list to an empty list
            
        # The class displayed in the window will be the last item that was appended to the class_list
        form.FindElement('class').Update(class_list[-1])
        
        # Makes the class list and element list only one item long
        if len(class_list) >= 2:
            del class_list[:-1]
        if len(element) >= 2:
            del element[:-1]

        # Class info button
        if button == 'Class Info' and class_list[-1] == '':
            sg.Popup('Not a Class:', 'If you see this, go back and obtain a class!')
        if button == 'Class Info' and class_list[-1] == 'Warrior':                         # Example of a popup display explaining the class when the button is pressed
            sg.Popup('Warrior Class:', 'A class that specializes in melee combat')         # Placeholder descriptions
