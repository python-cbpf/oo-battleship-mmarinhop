table_size = 5
battle_points = 12

class Player():
    '''Class representing a player in a game of battleship.'''
    def __init__(self, name = 'dummy'):
        '''a player object is initialized with the name of the player.'''
        self.player_name = name
        self.player_score = 0
        self.player_ships = battle_points
        self.seamap = np.zeros((table_size, table_size), dtype = np.float)
        self.enemymap = np.zeros((table_size, table_size), dtype = np.float)
        self.ship_dict = {'Cruiser': 5, 'Battleship': 4, 'Destroyer': 3, 'Submarine': 3}
 
       
    def display_map(self):
        '''method to visualize player's map.'''
        return self.seamap

    
    def place_ships(self):
        '''before the game start this method places the ships.'''
        count = 0
        while count < self.player_ships:
            try:
                x_y_coord = input('Enter the coordinates (x,y), e.g. 0 1: ')
                x_coord = int(x_y_coord.split()[0])
                y_coord = int(x_y_coord.split()[1])
                ship_type = input('Enter the class of the ship: ').capitalize()
                count += self.ship_dict[ship_type]
                if self.seamap[x_coord][y_coord] != 0:
                    print('Repeated coordinates. Try again.\n-------------------------------------------------')
                    count -= self.ship_dict[ship_type]
                else:
                    if count > battle_points - 3 and count < battle_points:
                        print('*************No more ships available*************\n')
                        self.seamap[x_coord][y_coord] = self.ship_dict[ship_type]
                        break
                    elif count > battle_points:
                        print('You have exceed the maximum quantity!\nMaximum:', battle_points,'\nCurrent:',count,
                              '\nPrevious:',count - self.ship_dict[ship_type])
                        count -= self.ship_dict[ship_type]
                    else:
                        self.seamap[x_coord][y_coord] = self.ship_dict[ship_type]
            except:
                print('Wrong input. Try again.\n-------------------------------------------------')
#            else:        
#                if self.seamap[x_coord][y_coord] == 1:
#                    print('Repeated coordinates. Try again.\n-------------------------------------------------')
#                else:
#                    self.seamap[x_coord][y_coord] = 1
##                    count += ship_dict[ship_type]

         
    def shoot(self, x, y, seamap):
        '''don't forget a docstring...'''
        if seamap[x][y] != 0:
            self.record(seamap[x][y])
            seamap[x][y] = 2
            return True
        else:
            return False

   
    def evaluate(self, seamap):
        '''don't forget a docstring...'''
        index = True
        while index:
            try:
                print('We now shoot')
                print('Enemy field\n', self.enemymap)
                x_y_coord = (input('Choose the coordinates, e.g.: 0 1; ')).split()
                x_coord = int(x_y_coord[0])
                y_coord = int(x_y_coord[1])
            except:
                print('Wrong input. Try again.\n-------------------------------------------------')
            else:
                if self.shoot(x_coord, y_coord, seamap):
                    print('-------------------------------------------------\nHit!')
                    self.enemymap[x_coord][y_coord] = 2
                    print('Updated field\n', self.enemymap)
                    index = False
                else:
                    print('-------------------------------------------------\nMiss')
                    self.enemymap[x_coord][y_coord] = 9
                    print('Updated field\n', self.enemymap)
                    index = False
            
            
    def record(self, points):
        '''don't forget a docstring...'''
        self.player_score += points
        pass

ask_play = input('Do you want to play? ')

if ask_play.capitalize() == 'Yes':
    # create players
    player1 = Player('Alice')
    player2 = Player('Bob')
    print(player1.ship_dict)
    
    # place ships
    print('\nPlease place your ships,', player1.player_name)
    player1.place_ships()
    print('-------------------------------------------------\nPlease place your ships,', player2.player_name)
    player2.place_ships()
    
    print('Check map player 1')
    print('Check map player 2')
#    while (not winning_condition) and (not interupted):
#         game loop
#         player 1: shoot
#         player 1: evaluate
#        player1.evaluate(player2.seamap)
#         player 1: record
#         player 2: shoot
#         player 2: evaluate
#         player 2: record
else:
    print('Shutting down...')    
    
#def divide():
#    ins = input('Write down two numbers: ')
#    ins = ins.split()
#    a = int(ins[0])
#    b = int(ins[1])
#    index = True
#    while index:
#        try:
#            result = a / b
#        except:
#            print('Something went wrong, e.g.: division by zero, input an string...\n------------------------------------------------------')
#            ins = input('Write down two numbers: ')
#            ins.split()
#        else:
#            print(result)
#            index = False
    
f, axarr = plt.subplots(1, 2)    
axarr[0].imshow(player1.display_map())
axarr[1].imshow(player2.display_map())
axarr[0].set_title('Player 1 Map')
axarr[1].set_title('Player 2 Map')
