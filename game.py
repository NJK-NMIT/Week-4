#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3


""" 
A comment describing the game module
"""
from ast import Delete
import PySimpleGUI as sg

# Brief comment about how the following lines work
game_state = 'Forest'
game_places = {'Forest':{'Story':'You are in the forest.',
                        'North':'Castle', 'South':'Cave', 'East':'Village'},
              'Village':{'Story':'You are at the village.\nIt looks abandoned.',
                        'South':'Garden', 'West':'Forest', 'East':'Farm'},
              'Farm':{'Story':'You arrive at a farm.\nCrops once grew here but now ... nothing.\nIt is a dead end.',
                        'West':'Village'},
              'Garden':{'Story':'You are at the Garden of Sorrow.\nIt is not a happy place.',
                        'North':'Village', 'West':'Cave', 'South':'Wizzard Tower'},
              'Wizzard Tower':{'Story':'You enter the Wizzard Tower.\nThe Wizzard is not happy!\nHe lifts his wand..',
                        'Panic!':'Game Over'},
              'Cave':{'Story':'You are at the cave.\nIt is a bit chilly.',
                        'North':'Forest', 'South':'Cavern', 'East':'Garden'},
              'Castle':{'Story':'You have found a castle.\nNobody comes out to greet you.',
                        'North':'Troll Bridge', 'South':'Forest', 'West':'Fort'},
              'Troll Bridge':{'Story':'You make your way across the bridge.\nIt is very scary.\nThere is no way forward.',
                        'South':'Castle'},
              'Fort':{'Story':'You enter an abandoned Fort.\nIt is very quiet.',
                        'East':'Castle', 'South':'Giant Bungalo'},
              'Giant Bungalo':{'Story':'You enter a bungalo that was clearly made for giants.\nYou feel out of place.',
                        'North':'Fort', 'South':'Gremlin Hole'},
              'Gremlin Hole':{'Story':'It is obvious that gremlins once lived here.\nPizza boxes litter the floor.',
                        'North':'Fort', 'South':'Ogre Hotel', 'Eat pizza':'Pizza'},
              'Ogre Hotel':{'Story':'You enter a hotel.\nThere is an Ogre at the reception desk.',
                        'North':'Gremlin Hole', 'East':'Cavern', 'Check in':'Check in Death'},
              'Cavern':{'Story':'You stumble into a cavern.\nThe floor is quite slippery.',
                        'West':'Ogre Hotel', 'South':'Grotto'},
              'Grotto':{'Story':'This grotto exudes the class and sophistication\nof a Kardashian bowel movement.\nThere is no turning back!',
                        'East':'Lair'},
              'Lair':{'Story':'You have encountered a monster!',
                        'Panic!':'Game Over','Say Hello':'Gain XP'},
              'Game Over':{'Story':'It is never a good idea to panic.\nYou are now dead.',
                         },
              'Gain XP':{'Story':'Congratulations.\nYou gain 100 XP',
                        'Continue':'Forest'},
              'Pizza':{'Story':'You start to eat stale pizza.\nYou begin to choak.',
                        'Panic!':'Game Over'},

                }

directions = ('North', 'South', 'East', 'West')

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return game_places[game_state]['Story']

def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: North, South, etc

    Returns:
        string: the sory at the current place
    """
    global game_state
    game_place = game_places[game_state]
    proposed_state = game_place[direction]
    if proposed_state == '' :
         return 'You can not go that way.\n'+game_places[game_state]['Story']
    else :
        game_state = proposed_state
        return game_places[game_state]['Story']
        
        
def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """
    sg.theme('Dark Blue 3')
    buttons = [sg.Button('Button1', key='-B1-'), sg.Button('Button2', key='-B2-'), sg.Button('Button3', key='-B3-')]
    exit_button = [sg.Button('Exit')]
    clue = [ sg.Text('Placeholder',size=(100,4), font='Any 14', key='-CLUES-') ]
    command_col = sg.Column([buttons],element_justification='r')
    clue_col = sg.Column([clue],element_justification='r')
    exit_col = sg.Column([exit_button],element_justification='r')
    
    layout = [[sg.Text('Story:', size=(7,1), font='Any 14'),
                sg.Text(show_current_place(),size=(100,4), font='Any 14', key='-OUTPUT-'),
                ],
                [command_col],
                [clue_col],
                [exit_col]]

    return  sg.Window('Adventure Game', layout, size=(480,300), finalize=True)
    

if __name__ == "__main__":
    #testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())
    
    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()
    while True:
        choices = list( game_places[game_state].keys() )
        # Text that appears on each button: bt = Button Text
        bt1, bt2, bt3 = '', '', ''
        # Flags to indicate if the button is visible: bv = Button Visable
        bv1, bv2, bv3 = False, False, False
        # What will be the result of each button: br = Button Result
        br1, br2, br3 = '', '', ''
        # How many choices (buttons) do we have.  Note that "Story" is an uncounted item
        c = len(choices)
        if c > 1:
            bt1 = choices[1]
            bv1 = True
            br1 = game_places[game_state][bt1]
        if c > 2:
            bt2 = choices[2]
            bv2 = True
            br2 = game_places[game_state][bt2]
        if c > 3:
            bt3 = choices[3]
            bv3 = True
            br3 = game_places[game_state][bt3]
        
        #print(f'==={game_state}', choices, b1, b2, b3, c, br1, br2, br3)
        # Update the text on each button
        window['-B1-'].update(bt1)
        window['-B2-'].update(bt2)
        window['-B3-'].update(bt3)
        # Hide/Show each button
        window['-B1-'].update(visible=bv1)
        window['-B2-'].update(visible=bv2)
        window['-B3-'].update(visible=bv3)
        
        clue = ''
        if bt1 in directions :
            clue += f"The path {bt1} leads to a {br1}\n"
        if bt2 in directions :
            clue += f"The path {bt2} leads to a {br2}\n"
        if bt3 in directions :
            clue += f"The path {bt3} leads to a {br3}"
        window['-CLUES-'].update(clue)

        event, values = window.read()

        print("Event", event)
        if event == '-B1-': 
            current_story = game_play(bt1)
        elif event == '-B2-':
            current_story = game_play(bt2)
        elif event == '-B3-':
            current_story = game_play(bt3)
        elif event == 'Exit' or event is None:
            break
        else :
            print(f"Unknown event: {event}")
            pass
        window['-OUTPUT-'].update(current_story)            
    
    window.close()
    
    
    
    
