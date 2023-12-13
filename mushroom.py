#The mushroom forest will be a text adventure game which runs in an external window.
# It has art assets and also music (original work). It will have a clear ending and a puzzle mechanic 
# which involves collecting and distributing items to the correct places.
# Themes; spookey, mystery, retro.
#
#
#                       .-'~~~-.
#                     .'o  oOOOo`.
#                    :~~~-.oOo   o`.
#                     `. \ ~-.  oOOo.
#                       `.; / ~.  OO:
#                       .'  ;-- `.o.'
#                      ,'  ; ~~--'~
#                      ;  ;
#_______\|/__________\\;_\\//___\|/________      



import pygame                              #pip install pygame
from win32api import GetSystemMetrics      #pip install pywin32
from text import a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6,a7,b7,a8,b8,a9,b9,a10,b10,a11,b11,a12,b12,a13,b13,a14,b14,a15,b15,a16,b16               #import text lines as module 


pygame.init()
pygame.font.init()                             #creates an object to draw on (Text)   
#screen = pygame.display.set_mode((1024,1300)) #assets are 1024, this needed + text space
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)    # Changed to fullscreen mode for immersion 


#Items
item_image_gmushroom = pygame.image.load('Art assets/Gmushitem.jpg')           #item asset
item_image_feather = pygame.image.load('Art assets/Feather.jpg')
item_image_tooth = pygame.image.load('Art assets/Tooth.jpg')
item_image_sausage = pygame.image.load('Art assets/Sausage.jpg')
item_image_pmushroom = pygame.image.load('Art assets/Pmushitem.jpg')
item_image_bmushroom = pygame.image.load('Art assets/Bmushitem.jpg')
item_image_rmushroom= pygame.image.load('Art assets/Rmushitem.jpg')

has_gmushroom = False
has_feather = False
has_tooth = False
has_sausage = False
has_pmushroom = False
has_bmushroom = False
has_rmushroom = False


image = pygame.image.load('Art assets/123.jpg')                #test background imgage 
test_sound = pygame.mixer.Sound('Audio assets/test.wav')           #test background sound
test_sound.set_volume(0.1)                                          #Volume control. float split of whole number 1 for full volume 
test_sound2 = pygame.mixer.Sound('Audio assets/test2.wav')
#key_sound = pygame.mixer.Sound('Audio assets/next.wav')             #Not working          

#Fonts and text animation
font_title = pygame.font.SysFont('freesansbold.ttf', 60)
font_body = pygame.font.SysFont('freesansbold.ttf', 40)
font_controls = pygame.font.SysFont('freesansbold.ttf', 15)

title_messages = a1
text_surface_body_message = b1

text_surface_title = font_title.render('', False, (255, 255, 100))                 
text_surface_body = font_body.render('', False, (255, 255, 100))                     #Main body
text_controls = font_controls.render("EXIT - Esc    NEXT  - Enter   ", False, (255, 255, 100))   


timer = pygame.time.Clock()             #Timer to determine how fast text animates 
speed = 2                               #Text speed, more is less
active_message = 0
text_surface_title_message = title_messages[active_message]
counter = 0
done = False


x = 4                            #Location variables
y = 0

width = GetSystemMetrics(0)       #Gets the height and width of the screen so images can be centre on all systems 
height = GetSystemMetrics(1)

pygame.display.set_caption("Mushroom")
colour = (0,0,0)                #Change colour value to edit background colour 
screen.fill(colour)

pygame.mixer.Sound.play(test_sound) 








#        __.....__
#     .'" _  o    "`.
#   .' O (_)     () o`.
#  .           O       .
# . ()   o__...__    O  .
#. _.--"""       """--._ .
#:"                     ";
# `-.__    :   :    __.-'
#      """-:   :-"""
#        J     L
#         :     :
#        J       L
#        :       :
#        `._____.'
#---------------------------------------------------------------GAME LOOP------------------------------------------------------------------------------

while True:                     #Main loop. == False to end.
    pygame.display.update()
    timer.tick(60)               #Frame rate

    pygame.draw.rect(screen, 'black', [0, height - 416, width, height - 1024])              #Draw space for text

    text_surface_title = font_title.render(text_surface_title_message[0:counter//speed], True, (255, 255, 200))    #determines the speed of text cycle
    text_surface_body = font_body.render(text_surface_body_message, True, (255, 255, 200)) 

    screen.blit(image, (width / 2 - (1024 /2), 0)) 
    screen.blit(text_surface_title, (width / 2 - (width / 2 / 2) ,1024))
    screen.blit(text_surface_body, (width / 3 - (1024 /2), 1300))
    screen.blit(text_controls, (width - 300, height - 1400))

    if counter < speed * len(text_surface_title_message):                                    #ensures all of the message has been written to sceen
         counter += 1
    elif counter >= speed * len(text_surface_title_message):
         done = True

    #if counter < speed * len(text_surface_body_message):                                    #digit adding text for body text. Disabled for now due to design decision.
    #     counter += 1
    #elif counter >= speed * len(text_surface_body_message):
    #     done = True



 #------------------------------------------------------------LOCATIONS--------------------------------------------------------------------  
 
    if x == 4 and y == 1:
        image = pygame.image.load('Art assets/road.jpg')
        title_messages = a2
        text_surface_body_message = b2
        text_surface_title_message = title_messages[active_message]
       
    if x == 4 and y == 0:
        image = pygame.image.load('Art assets/123.jpg')
        title_messages = a1
        text_surface_body_message = b1
        text_surface_title_message = title_messages[active_message]
    
    if x == 4 and y == 2:
        image = pygame.image.load('Art assets/crossroads 2.jpg')
        title_messages = a3
        text_surface_body_message = b3
        text_surface_title_message = title_messages[active_message]

    if x == 4 and y == 3:
        image = pygame.image.load('Art assets/large tree.jpg')
        title_messages = a4
        text_surface_body_message = b4
        text_surface_title_message = title_messages[active_message]

    if x == 4 and y == 4:
        image = pygame.image.load('Art assets/owl.jpg')
        title_messages = a5
        text_surface_body_message = b5
        text_surface_title_message = title_messages[active_message]

    if x == 4 and y == 5:
        image = pygame.image.load('Art assets/pooped.jpg')
        title_messages = a6
        text_surface_body_message = b6
        text_surface_title_message = title_messages[active_message]
    
    if x == 5 and y == 4:
        image = pygame.image.load('Art assets/phoenix.jpg')
        title_messages = a7
        text_surface_body_message = b7
        text_surface_title_message = title_messages[active_message]
        screen.blit(item_image_feather, (width /8  - (1024 /6), 0)) 
        has_feather = True
    
    if x == 5 and y == 2:
        image = pygame.image.load('Art assets/river.jpg')
        title_messages = a8
        text_surface_body_message = b8
        text_surface_title_message = title_messages[active_message]

    if x == 5 and y == 3:
        image = pygame.image.load('Art assets/deadend1.jpg')
        title_messages = a9
        text_surface_body_message = b9
        text_surface_title_message = title_messages[active_message] 

    if x == 5 and y == 1:
        image = pygame.image.load('Art assets/deadend2.jpg')
        title_messages = a10
        text_surface_body_message = b10
        text_surface_title_message = title_messages[active_message] 

    if x == 6 and y == 2:
        image = pygame.image.load('Art assets/green1.jpg')
        title_messages = a11
        text_surface_body_message = b11
        text_surface_title_message = title_messages[active_message] 
    
    if x == 6 and y == 1:
        image = pygame.image.load('Art assets/green2.jpg')
        title_messages = a12
        text_surface_body_message = b12
        text_surface_title_message = title_messages[active_message]
        screen.blit(item_image_gmushroom, (width /10  - (1024 /6), 0))
        has_gmushroom = True 

    if x == 6 and y == 3:
        image = pygame.image.load('Art assets/green3.jpg')
        title_messages = a13
        text_surface_body_message = b13
        text_surface_title_message = title_messages[active_message]

    if x == 3 and y == 2:
        image = pygame.image.load('Art assets/westroad.jpg')
        title_messages = a14
        text_surface_body_message = b14
        text_surface_title_message = title_messages[active_message]

    if x == 2 and y == 2:
        image = pygame.image.load('Art assets/split.jpg')
        title_messages = a15
        text_surface_body_message = b15
        text_surface_title_message = title_messages[active_message]

    if x == 2 and y == 1:
        image = pygame.image.load('Art assets/red1.jpg')
        title_messages = a16
        text_surface_body_message = b16
        text_surface_title_message = title_messages[active_message]



        
        


    for event in pygame.event.get():             #Makes the X work.                                                       
        if event.type == pygame.QUIT:
                pygame.quit()           
                quit()








#        __.....__ 
#     .'"         "`. 
#   .'               `.  
#  .                   . 
# .       __...__       .
#. _.--"""       """--._ .
#:"                     ";
# `-.__    :   :    __.-'
#      """-:   :-"""   
#         J     L    
#         :     :  
#        J       L
#        :       : 
#        `._____.'                 
#----------------------------------------------------------------------------------------------------------Controls---------------------        
    
        if event.type == pygame.KEYDOWN:    # Events for cycling through text lines 
            if event.key == pygame.K_RETURN and done and active_message < len(title_messages) -1: 
                active_message += 1
                done = False
                text_surface_title_message = title_messages[active_message]
                counter = 0
                
            

        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()               

        if event.type == pygame.KEYDOWN:                     #Go North
            if event.key == pygame.K_1:
                y += 1
                active_message = 0             
                   
        if event.type == pygame.KEYDOWN:                     #Go East
            if event.key == pygame.K_2:
                x += 1
                active_message = 0

        if event.type == pygame.KEYDOWN:                     #Go West
            if event.key == pygame.K_3:
                x -= 1
                active_message = 0

        if event.type == pygame.KEYDOWN:                     #Go South
            if event.key == pygame.K_4:
                y -= 1
                active_message = 0                             

       
             
              


    

        
           