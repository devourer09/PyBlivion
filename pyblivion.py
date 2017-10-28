'''A program to help manage the levels of player characters in Elder Scolls: Oblivion'''

from tkinter import *
from tkinter import ttk, filedialog

import json


attributes = ('Strength', 'Intelligence', 'Willpower', 'Agility', 'Speed', 'Endurance', 'Luck')
skills = ('Alteration', 'Destruction', 'Illusion', 'Mysticism', 'Restoration',
        'Security', 'Sneak', 'Armorer', 'Athletics', 'Blade', 'Block', 'Blunt',
        'Hand to Hand', 'Heavy Armor', 'Alchemy', 'Conjuration', 'Acrobatics',
        'Light Armor', 'Marksman', 'Mercantile', 'Speechcraft')


def level_ups_remaining():
    pass

def max_major_selected():
'''Enable or disable the major skill check boxes depending on if seven are 
already ticked or not'''
    count = 0
    for key in check_value:
        if check_value[key].get() == '1':
            count += 1
            for check in check_value:
                if check_value[check].get() == '0':
                    check_buttons[check]['state'] = NORMAL
        if count == 7:
            for check in check_value:
                if check_value[check].get() == '0':
                    check_buttons[check]['state'] = DISABLED
            break

def load_character():
    file_path = filedialog.askopenfilename()

    if file_path is not '':
        with open(file_path, 'r') as f:
            json_data = json.loads(f.read())
        character_name.set(json_data['character name'])
        for attribute in attributes:
            attributeVal[attribute].set(json_data['attributes'][attribute])
        for skill in skills:
            skillVal[skill].set(json_data['skills'][skill][0])
            if json_data['skills'][skill][1] is '':
                check_value[skill].set('0')
            else:
                check_value[skill].set(json_data['skills'][skill][1])

def save_character():
    attribute_json = {}
    json_data = {}
    json_data['character name'] = character_name.get()

    json_data['attributes'] = {}
    for value in attributeVal:
            json_data['attributes'][value] = attributeVal[value].get()

    json_data['skills'] = {}
    for value in skillVal:
            json_data['skills'][value] = [skillVal[value].get(), check_value[value].get()]

    file_path = filedialog.asksaveasfilename()

    if file_path is not '':
        with open(file_path, 'w') as f:
            f.write(json.dumps(json_data))


# Create root and set the title
root = Tk()
root.title('PyBlivion Level Manager')

# Frames
top_frame = ttk.Frame(root)
bottom_frame = ttk.Frame(root)
save_button_frame = ttk.Frame(root)

top_frame.grid(row=0, sticky=(N, W, E, S))
bottom_frame.grid(row=1, sticky=(N, W, E, S))
save_button_frame.grid(row=2, sticky=(N, W, E, S))

# Character name
character_name = StringVar()
ttk.Label(top_frame, text='Character name:').grid(column=0, row=0)
ttk.Entry(top_frame, textvariable=character_name).grid(column=1, row=0, sticky=E)

# Attributes
ttk.Label(bottom_frame, text='Attributes').grid(column=0, row=0, sticky=W)
attributeVal = {}
for pos, attr in enumerate(attributes):
    ttk.Label(bottom_frame, text=attr).grid(column=0, row=pos+1, sticky=W)
    attributeVal[attr] = StringVar()
    Spinbox(bottom_frame, width=3, textvariable=attributeVal[attr]).grid(column=1, row=pos+1, stick=W)

# Skills
ttk.Label(bottom_frame, text='Skills').grid(column=0, row=8, sticky=W)
ttk.Label(bottom_frame, text='Major skill').grid(column=2, row=8)
skillVal = {}
check_value = {}
check_buttons = {}
for pos, name in enumerate(skills):
    ttk.Label(bottom_frame, text=name).grid(column=0, row=pos+9, sticky=W)
    skillVal[name] = StringVar()
    check_value[name] = StringVar()
    Spinbox(bottom_frame, width=3, textvariable=skillVal[name]).grid(column=1, row=pos+9, sticky=W)
    check_buttons[name] = ttk.Checkbutton(bottom_frame, command=max_major_selected, variable=check_value[name])
    check_buttons[name].grid(column=2, row=pos+9)
    check_value[name].set('0')

# Save and load buttons
ttk.Button(save_button_frame, text='Load', command=load_character).grid(row=0, column=0)
ttk.Button(save_button_frame, text='Save', command=save_character).grid(row=0, column=1)

root.mainloop()
