###########################################################

   #  Computer Project #10

   # initialize() function
   # display() function
   # valid_tableau_to_tableau() function
   # move_tableau_to_tableau() function
   # valid_foundation_to_tableau() function
   # move_foundation_to_tableau() function
   # valid_tableau_to_foundation() function
   # move_tableau_to_foundation() function
   # check_for_win() function
   # get_option() function
   # main() function:
   #    while loop
   #        if statements for options
   #        checks and ends if q is entered
   # 
   # 
   # 
   # 
   # 
   # 
   
   ###########################################################
#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
                
def initialize():
    '''
    

    Returns
    -------
    tableau: list of eight lists
    
    foundation: empty list of four lists
    
    Shuffles and initializes the deck

    '''
    #initializes and shuffles
    foundation = [[],[],[],[]]
    deck = cards.Deck()
    deck.shuffle()
   #sets tableau equal to list of lists
    tableau = [[],[],[],[], [], [], [], [] ]
    # Goes through the range 
    for card in range(8):
        #If not equal to 0
        if card % 2 != 0:
            val = 6
        #If equal to 0
        elif card % 2 == 0:
            val = 7
        #appends tableau
        for j in range(val):
            tableau[card].append(deck.deal())


    return(tableau, foundation)

       
 

def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d):
    '''
    

    Parameters
    ----------
    tableau : list of eight lists
        .
    s : int
        
    d : int
    

    Returns
    -------
    valid or invalid : Boolean
    
    checks  if player can move a card from tableau to tableau

    '''
    #Sets valid and invalid equal to true or false
    valid = True
    invalid = False
    #If length of the tableau's source equal to 0
    if len(tableau[s]) == 0:
       return invalid
   # If length of tableau's destination is 0
    if len(tableau[d]) == 0:
        return valid
    #If rank equals rank -1
    if tableau[s][-1].rank() == tableau[d][-1].rank() - 1:
        return valid
    else:
        return invalid
        
   
    
def move_tableau_to_tableau(tableau,s,d):
    
    """

       

        Parameters: 
        ----------
        tableau : list
        
        s: int
        
        d: int

        Returns:
        -------
        True or False : boolean
        
        moves a card from tableau to tableau
 
     """
    # Appends if valid move
    if valid_tableau_to_tableau(tableau,s,d):
        tableau[d].append(tableau[s].pop())
        return True
    else:
        return False
   
    pass

def valid_foundation_to_tableau(tableau,foundation,s,d):
    '''
    

    Parameters
    ----------
    tableau : list of lists
        
    foundation : list of lists
        
    s : int
        
    d : int
       

    Returns
    -------
    valid or invalid : Boolean
        checks if player can move from foundation to tableau

    '''
    #Sets valid and invalid to true and false respectively
    valid = True
    invalid = False
    #if length of tableau source is 0
    if len(tableau[s]) == 0:
       return invalid
   #if length of tableau destination is 0
    if len(tableau[d]) == 0:
        return valid
    #Checks If rank equals rank -1
    if foundation[s][-1].rank() == tableau[d][-1].rank() - 1:
        return valid
    else:
        return invalid
        
    
    pass

def move_foundation_to_tableau(tableau,foundation,s,d):
    '''
    

    Parameters
    ----------
    tableau : list of lists
       
    foundation : list of lists
    
    s : int
        
    d : int
       

    Returns
    -------
     True or False:  boolean
        Moves card from foundation to tableau

    '''
    # Appends if valid move
    if valid_foundation_to_tableau(tableau, foundation, s, d) == True:
       
        tableau[d].append(foundation[s].pop())
        return True
    else:
        return False
    

def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''
    

    Parameters
    ----------
    tableau : list of lists
        .
    foundation : list of lists
        
    s : int
        
    d : int
        

    Returns
    -------
    True/False: boolean
       Checks if user can move card from tableau to foundation

    '''
    tab_len = len(tableau[s]) 
    foun_len = len(foundation[d])
    if tab_len == 0:
       return False
    if foun_len == 0 :
       if tableau[s][-1].rank() == 1:

           return True
       elif tableau[s][-1].rank() != 1:
           
           print(len(foundation[d]), tableau[s][-1].rank())
           return False
      
  
    if  tableau[s][-1].rank() - 1 == foundation[d][-1].rank() and tableau[s][-1].suit() == foundation[d][-1].suit():
        return True
    else:
        return False
   
    
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''
    

    Parameters
    ----------
    tableau : list of lists
        
    foundation : list of lists
        
    s : int
        
    d : int
        

    Returns
    -------
    True/False: boolean
     
    Moves cards from tableau to foundation

    '''
    # Appends if valid move
    if valid_tableau_to_foundation( tableau, foundation, s, d) == True:
        foundation[d].append(tableau[s].pop())
        return True
    else:
        return False
    
    pass

def check_for_win(foundation):
    '''
    

    Parameters
    ----------
    foundation : list of lists
       

    Returns
    -------
    True or False: boolean
        
    This function checks for a win

    '''
    #Win if true, lose if false
    win = True
    lose = False
    count = 0
    #Counter
    for s in (foundation):
        for card in s:
            count = count +1
    # Checks count 
    if count == 52:
        return win
    elif count != 52:
        return lose
    
    pass

def get_option():
    '''
    

    Returns
    -------
    option : list
        
    this function returns the option entered by the user 

    '''
    options = ["MTT","MTF","MFT","U","R","H","Q"]
    option = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): " )
    #Makes option uppercase and splits
    option = option.upper()
    option= option.split()
    
    #Goes through the options list and checks if input is in it
    if option[0] not in options:
        print("Error in option:" ,  option[0])
        return None
    #If input has MTT, MTF or MFT  
    if option[0] in ("MTT", "MTF", "MFT"):
        #If the entered option isn't 3 in length
        if (len(option)!= 3):
            print("Error in option:" , option[0])
            return None
        else:
            
            if option[0] == "MTT":
                #Checks range 
                if (int(option[1])) in range(0,8)  and (int(option[2])) in range(0,8):
                    option1 = int(option[1])
                    option2 = (int(option[2]))
                    return [option[0], option1, option2]
                #If destination isn't in range
                elif  (int(option[2]))  not in range(0,8):
                    print("Error in Destination")
                    return None
                #If source isn't in range
                elif (int(option[1])) not in range(0,8):
                    print("Error in Source.")
                    return None
            
            if option[0] == "MTF":
                #Checks range
                if (int(option[1])) in range(0,8) and (int(option[2])) in range(0,4):
                    option1 = int(option[1])
                    option2 = (int(option[2]))
                    return [option[0], option1, option2]
                #If destination isn't in range
                elif  (int(option[2]))  not in range(0,4):
                    print("Error in Destination")
                    return None
                #If source isn't in range
                elif (int(option[1])) not in range(0,8):
                    print("Error in Source.")
                    return None
            #if option is MFT
            if option[0] == "MFT":
               if (int(option[1])) in range(0,4) and (int(option[2])) in range(0,8):
                   option1 = int(option[1])
                   option2 = (int(option[2]))
                   return [option[0], option1, option2]
               #If destination isn't in range
               elif  (int(option[2]))  not in range(0,8):
                   print("Error in Destination")
                   return None
               #If source isn't in range
               elif (int(option[1])) not in range(0,4):
                   print("Error in Source.")
                   return None
           
    else: 
        return option


def main():  
    #Beginning print statement
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    #initializes
    tableau, foundation = initialize()
    #displays 
    display(tableau, foundation)
    #prints the menu
    print(MENU)
    #get option 
    option = get_option()
    while option == None:
        option = get_option()
    movelist = []
   
   
       
    while True:
       
        #If entered option is MTT
        if option[0] == "MTT":
            #Sets s and d to the correct index
            s = int(option[1])
            d = int(option[2])
            #if move works
            if move_tableau_to_tableau(tableau, s, d):
                #appends empty list
                movelist.append(option)
                #Checks win
                if check_for_win(foundation):
                    print('You won!')
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)
                     
                else:
                     display(tableau, foundation)
                           
            else:
                print("Error in move: {} , {} , {}".format(option[0].upper(), option[1], option[2]))
        #If entered option is MTF       
        if option[0] == "MTF":
            #Sets s and d to the correct index
            s = int(option[1])
            d = int(option[2])
            #if move works
            if move_tableau_to_foundation(tableau,foundation, s, d):
                #appends empty list
                movelist.append(option)
                #Checks for win
                if check_for_win(foundation):
                    print('You won!')
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    display(tableau, foundation)
                    print(MENU)
                else:
                    display(tableau, foundation)
                    
            #prints error message
            else:
                print("Error in move: {} , {} , {}".format(option[0].upper(), option[1], option[2]))
         #If user enters MFT     
        if option[0] == "MFT":
            #sets s and d to the correct indexes
            s = int(option[1])
            d = int(option[2])
            #if move works
            if move_foundation_to_tableau(tableau, foundation, s, d):
                #appends empty list
                movelist.append(option)
                #checks for the win
                if check_for_win(foundation):
                    print('You won!')
                    #displays 
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    tableau, foundation = initialize()
                    
                    display(tableau, foundation)
                    print(MENU)
                    
                else:
                    display(tableau, foundation)
             #prints error message      
            else:
                print("Error in move: {} , {} , {}".format(option[0].upper(), option[1], option[2]))
       #If option entered is R
        if option[0] == "R":
            tableau, foundation = initialize()
            display(tableau, foundation)
        #If option entered is H
        if option[0] == "H":
            print(MENU)
        #If user wants to undo
        if option[0] == "U":
            if movelist:
                #pops to get the last move
                lastmove = movelist.pop()
                #prints the undo command
                print("Undo: {} {} {}".format(lastmove[0].upper(), lastmove[1], lastmove[2]) )
                #If the last move was MTT
                if lastmove[0] == "MTT":
                    d = lastmove[1]
                    s = lastmove[2]
                    #appends tableau
                    tableau[d].append(tableau[s].pop())
                    display(tableau, foundation)
                #If the last move was MTF
                if lastmove[0] == "MTF":
                    d = lastmove[1]
                    s = lastmove[2]
                    #appends tableau
                    tableau[d].append(foundation[s].pop())
                    display(tableau, foundation)
                #If the last move was MFT
                if lastmove[0] == "MFT":
                    d = lastmove[1]
                    s = lastmove[2]
                    #appends the foundation
                    foundation[d].append(tableau[s].pop())
                    display(tableau, foundation)
            else:
                
                    print("No moves to undo.")
                    
                    
               
        option = get_option()
        #If option returns none
        while option == None:
            option = get_option()
        #quits if entered option is Q
        if option[0] == "Q":      
            print("Thank you for playing.")
            break
 
 

if __name__ == '__main__':
     main()

