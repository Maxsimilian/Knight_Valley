'''
Maxsimilian - Game Screens(Menu, GameOver, Winning), Sounds(game background sounds), game lives system, sound effects (jump, attack), game frame label(title, description, instructions and credits), background images, README file for the game.

Westleigh - [main character sprite + enemy sprite], [enemy player iteraction - jump on head], boss sprite and movement/collision, [enemy gets to end wall changes direction], enemy on platform (if time add character customisation).

Jakub - Platforms, Walls, Boss stage, Gem Stage and its collision, entrance for final stage.
'''


import simplegui, random
from user305_o32FtUyCKk_0 import Vector
WIDTH = 800
HEIGHT = 500        


class Spritesheet:
    # Constructor for the SpriteSheet class
    def __init__(self):
        # Initialize instance variables
        self.mainCharacterIMG = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac186/cs1822/MCsmall.png")
        self.WIDTH = 394
        self.HEIGHT = 1062
        self.COLUMNS = 9
        self.ROWS = 24
        self.frame_width = self.WIDTH / self.COLUMNS
        self.frame_height = self.HEIGHT / self.ROWS
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [0, 0]
        self.transition_time = 10
        self.facing_right = True

    def draw(self, canvas):
        source_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x,
                     self.frame_height * self.frame_index[1] + self.frame_centre_y)
        source_size = (self.frame_width, self.frame_height)
        dest_centre = (300, 150)
        
        dest_size = (80, 80)
        canvas.draw_image(self.mainCharacterIMG,
                      source_centre,
                      source_size,
                      player.pos.get_p(),
                      dest_size)
       
        #standing still pose
        if self.facing_right and keyboard.no_key_press():
            self.frame_index = [0, 0]
        if not self.facing_right and keyboard.no_key_press():
            self.frame_index = [8, 12]
            
        #using the electrical move
        if keyboard.left and keyboard.c:
            self.facing_right = False
            if(the_clock.transition(self.transition_time)):
                self.run_left_E()
                
        if keyboard.right and keyboard.c:
            self.facing_right = True
            if(the_clock.transition(self.transition_time)):
                self.run_right_E()
                
        if keyboard.c and self.facing_right and not keyboard.right:
            self.frame_index = [0, 11]
        if keyboard.c and not self.facing_right and not keyboard.left:
            self.frame_index = [8, 23]
            

    
        #moving right or left animation
        if keyboard.left and not keyboard.c:
            self.facing_right = False
            if(the_clock.transition(self.transition_time)):
                self.run_left()
        elif keyboard.right and not keyboard.c:
            self.facing_right = True
            if(the_clock.transition(self.transition_time)):
                self.run_right()
        
        #Jumping and falling right animation
        if keyboard.space and self.facing_right:
            self.frame_index = [1, 0]
        elif not keyboard.space and player.vel.get_p()[1] > 1 and self.facing_right:
            self.frame_index = [2, 0]
        
        #Jumping and falling left animation
        if keyboard.space and not self.facing_right:
            self.frame_index = [7, 12]
            self.facing_right = False
        elif not keyboard.space and player.vel.get_p()[1] > 1 and not self.facing_right:
            self.frame_index = [6, 12]


        the_clock.tick()
        
    def run_right(self):
        self.frame_index[1] = 0
        self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS
        if (self.frame_index[0] == 0 or self.frame_index[0] == 1 or self.frame_index[0] == 2):
            self.frame_index[0] = 3
            
    def run_left(self):
        self.frame_index[1] = 12
        self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS
        if (self.frame_index[0] == 6 or self.frame_index[0] == 7 or self.frame_index[0] == 8):
            self.frame_index[0] = 0
            
    def run_right_E(self):
        self.frame_index[1] = 11
        self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS
        if (self.frame_index[0] == 0 or self.frame_index[0] == 1 or self.frame_index[0] == 2):
            self.frame_index[0] = 3
            
    def run_left_E(self):
        self.frame_index[1] = 23
        self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS
        if (self.frame_index[0] == 6 or self.frame_index[0] == 7 or self.frame_index[0] == 8):
            self.frame_index[0] = 0


class Spritesheet_enemy:
    def __init__(self):
        self.IMG = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac186/cs1822/Slime.png")
        self.WIDTH = 128
        self.HEIGHT = 32
        self.COLUMNS = 8
        self.ROWS = 2
        self.frame_width = self.WIDTH / self.COLUMNS
        self.frame_height = self.HEIGHT / self.ROWS
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [7,1]
        self.facingforward = True

    def draw(self, canvas):
        source_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x,
                     self.frame_height * self.frame_index[1] + self.frame_centre_y)
        source_size = (self.frame_width, self.frame_height)
        # doesn't have to be same aspect ration as frame!
        dest_size = (35, 35)
        canvas.draw_image(self.IMG,
                      source_centre,
                      source_size,
                      enemy.pos.get_p(),
                      dest_size)
        if the_clock.transition(15):
            if self.facingforward:
                self.moveForward()
            else:
                self.moveBackwards()
        if enemy.dead:
            self.die()
        
    def moveForward(self):
        if self.frame_index[1] == 0:
            self.frame_index =  [6,1]
        self.frame_index[0] -= 1
        if(self.frame_index[0] == 1):
            self.frame_index[0] = 7
            
    def moveBackwards(self):
        if self.frame_index[1] == 1:
            self.frame_index = [0,0]
        self.frame_index[0] += 1
        if(self.frame_index[0] == 6):
            self.frame_index[0] = 0
            
    def die(self):
        self.frame_index[0] = self.frame_index[0] - 1


class Spritesheet_boss:
    def __init__(self):
        self.IMG = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac186/cs1822/boss.png")
        self.WIDTH = 1000
        self.HEIGHT = 2000
        self.COLUMNS = 10
        self.ROWS = 20
        self.frame_width = self.WIDTH / self.COLUMNS
        self.frame_height = self.HEIGHT / self.ROWS
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [9,0]
        self.facingLeft = True

    def draw(self, canvas):
        source_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x,
                     self.frame_height * self.frame_index[1] + self.frame_centre_y)
        source_size = (self.frame_width, self.frame_height)
        # doesn't have to be same aspect ration as frame!
        dest_size = (200, 200)
        canvas.draw_image(self.IMG,
                      source_centre,
                      source_size,
                      boss.pos.get_p(),
                      dest_size)
        
        if boss.dead and the_clock.transition(15) and self.frame_index != [3,19]:
            self.die()
        
    def die(self):
        if self.frame_index[1] < 16:
            self.frame_index = [0,16]
        if self.frame_index[0] == 9:
            self.frame_index[1] += 1
            self.frame_index[0] = 0
        if self.frame_index != [3,19]:
            self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS


class Spritesheet_gem:
    def __init__(self):        
        self.IMG = simplegui.load_image("https://www.cs.rhul.ac.uk/home/zlac223/crystal-qubodup-ccby3-32-yellow.png")
        self.WIDTH = 192
        self.HEIGHT = 32
        self.COLUMNS = 6
        self.ROWS = 1
        self.frame_width = self.WIDTH / self.COLUMNS
        self.frame_height = self.HEIGHT / self.ROWS
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.frame_index = [0, 0]
        
    def draw(self, canvas):
        source_centre = (self.frame_width * self.frame_index[0] + self.frame_centre_x,
                     self.frame_height * self.frame_index[1] + self.frame_centre_y)
        source_size = (self.frame_width, self.frame_height)
        # doesn't have to be same aspect ration as frame!
        dest_size = (50, 50)
        canvas.draw_image(self.IMG,
                      source_centre,
                      source_size,
                      (375, 250),
                      dest_size)
        self.next_frame()
        
    def next_frame(self):
        if the_clock.transition(10):
            self.frame_index[0] = (self.frame_index[0] + 1) % self.COLUMNS


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False
        self.c = False
        # Load Sounds
        self.sound_jump = simplegui.load_sound('https://opengameart.org/sites/default/files/audio_preview/qubodup-cfork-ccby3-jump.ogg.mp3')
        self.sound_attack = simplegui.load_sound('https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-35448/zapsplat_sound_design_electricity_arc_001_37854.mp3')

    def key_down(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['space']:
            self.sound_jump.set_volume(0.5)
            self.sound_jump.play()
            self.space = True
            
        if key == simplegui.KEY_MAP['c']:
            self.sound_attack.set_volume(1)
            self.sound_attack.play()
            self.c = True

    def key_up(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
        if key == simplegui.KEY_MAP['c']:
            self.c = False
            self.sound_attack.pause()

    def no_key_press(self):
        if not self.right:
            if not self.left:
                if not self.space:
                    if not self.c:
                        return True


class Player:
    def __init__(self, pos, spritesheet):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.radius = 40
        self.colour = "Red"
        self.spriteSheet = spritesheet
        self.normal = Vector(1.2, 0)
        
    def draw(self, canvas):
        self.spriteSheet.draw(canvas)

    def update(self):
        self.pos.add(self.vel)
    
    def top(self):
        return self.pos - Vector(0, self.radius)
    
    def bottom(self):
        return self.pos + Vector(0, self.radius)
    
    def left(self):
        return self.pos - Vector(self.radius, 0)
    
    def right(self):
        return self.pos + Vector(self.radius, 0)
    
    def bounce(self, normal):
        self.vel.reflect(normal)
        self.vel.x *= 0.85


class Enemy:
    def __init__(self, pos, spritesheet):
        self.pos = pos
        self.vel = Vector(0.25, 0)
        self.radius = 17
        self.colour = "Red"
        self.spriteSheet = spritesheet
        self.dead = False
        self.normal = Vector(1.2,0)
        
    def draw(self, canvas):
        self.spriteSheet.draw(canvas)

    def update(self):
        self.pos.add(self.vel)
    
    def top(self):
        return self.pos - Vector(0, self.radius)
    
    def bottom(self):
        return self.pos + Vector(0, self.radius)
    
    def left(self):
        return self.pos - Vector(self.radius, 0)
    
    def right(self):
        return self.pos + Vector(self.radius, 0)

class Boss:
    def __init__(self, pos, spritesheet):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.radius = 50
        self.colour = "Red"
        self.spriteSheet = spritesheet
        self.dead = True
        self.normal = Vector(1.2,0)
        
    def draw(self, canvas):
        self.spriteSheet.draw(canvas)

    def update(self):
        self.pos.add(self.vel)
    
    def top(self):
        return self.pos - Vector(0, self.radius)
    
    def bottom(self):
        return self.pos + Vector(0, self.radius)
    
    def left(self):
        return self.pos - Vector(self.radius, 0)
    
    def right(self):
        return self.pos + Vector(self.radius, 0)      
        
    def bounce(self, normal):
        self.vel.reflect(normal)
        self.vel.x *= 0.4


class Gem:
    def __init__(self, pos, spritesheet):
        self.pos = pos
        self.radius = 30
        self.spriteSheet = spritesheet
        self.activated = False
        
    def top(self):
        return self.pos - Vector(0, self.radius)
    
    def bottom(self):
        return self.pos + Vector(0, self.radius)
    
    def left(self):
        return self.pos - Vector(self.radius, 0)
    
    def right(self):
        return self.pos + Vector(self.radius, 0)
        
    def draw(self, canvas):
        self.spriteSheet.draw(canvas)
        
    def collision(self):
        bottom = self.player.bottom()
        top = self.player.top()
        left = self.player.left()
        right = self.player.right()
        return left.x <= self.gem.right().x and right.x >= self.gem.left().x
    
class Interaction:
    # Constructor for the Interaction class
    def __init__(self, player, enemy, boss, gem, level1, keyboard):
        # Initialize instance variables
        self.player = player
        self.enemy = enemy
        self.boss = boss
        self.gem = gem
        self.keyboard = keyboard
        self.platforms = level1[0]
        self.platforms_list = level1
        self.i = 0
        self.game = True
        self.defeat = False
        self.win = False
        self.lives = 3
        self.enemyVel = -0.25
        self.boss_lives = 10
        self.boss_firstSpawn = True
        self.timer = 0
        # Load images and sounds
        self.heart_image = simplegui.load_image('https://opengameart.org/sites/default/files/heart%20pixel%20art%2032x32.png')
        self.defeatbg =simplegui.load_image("https://img.freepik.com/free-vector/game-with-glitch-effect_225004-661.jpg?w=1380&t=st=1678302739~exp=1678303339~hmac=be6083cf7eb1d7b3a9b10e0423511a68b78081707f2987715c25cee6673b1040")
        self.winbg = simplegui.load_image("https://static.vecteezy.com/system/resources/previews/011/234/047/large_2x/you-win-video-game-vector.jpg")
        self.sound_game = simplegui.load_sound('https://opengameart.org/sites/default/files/menu_0.wav')
        self.sound_gameover = simplegui.load_sound('https://opengameart.org/sites/default/files/Devlin%20Bataric%20-%20Game%20Over%20Jingles%20Pack%20-%2001%20Game%20Over%20-%20Repeating%20Dream.wav')
        self.sound_boss = simplegui.load_sound('https://opengameart.org/sites/default/files/audio_preview/bermensch%20%5B%20Main%20Menu%20%5D_0.ogg.mp3')
        self.sound_win = simplegui.load_sound('https://opengameart.org/sites/default/files/Can%27t%20Stop%20Winning%20MP3.mp3')
        self.sound_cupstage = simplegui.load_sound('https://opengameart.org/sites/default/files/song21.mp3')

    # Function to format time
    def format_time(self, time):
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    # Function to draw on the canvas    
    def draw(self, canvas):
        self.update()
        theImage = simplegui.load_image("https://img.freepik.com/free-vector/space-background-with-landscape-alien-planet_107791-1125.jpg?w=1380&t=st=1678290264~exp=1678290864~hmac=7fa1d3593fe7fda1aed730aff01d7f880c38f928d612ad6b5bff93d994af6d1d")
        
        # Draw defeat screen
        if self.defeat:
            self.game = False
            if self.defeatbg is not None and self.defeatbg.get_width() > 0 and self.defeatbg.get_height() > 0:
            
                canvas.draw_image(self.defeatbg, (self.defeatbg.get_width()/2, self.defeatbg.get_height()/2), 
                                  (self.defeatbg.get_width(), self.defeatbg.get_height()),
                                  (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
            frame.set_draw_handler(self.draw)
            canvas.draw_text("Exit", (360, HEIGHT/2 + 190), 40, "GOLD", "sans-serif")
            frame.set_mouseclick_handler(interaction.click)
            self.sound_cupstage.pause()
            self.sound_game.pause()
            self.sound_boss.pause()			   # Pause Sound
            self.sound_gameover.set_volume(1)  # Set the volume
            self.sound_gameover.play()         # Play Sound
        
        # Draw Win screen
        if self.win:
            self.game = False
            if self.winbg is not None and self.winbg.get_width() > 0 and self.winbg.get_height() > 0:

                canvas.draw_image(self.winbg, (self.winbg.get_width()/2, self.winbg.get_height()/2), 
                                  (self.winbg.get_width(), self.winbg.get_height()),
                                  (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))

                
            text_width = frame.get_canvas_textwidth("Timer: "+self.format_time(self.timer), 25)
            canvas.draw_text("Timer: "+self.format_time(self.timer), ((800 - text_width) / 2, 20), 25, "White")
            frame.set_draw_handler(self.draw)
            canvas.draw_text("Exit", (360, HEIGHT/2 + 190), 40, "Magenta", "sans-serif")
            frame.set_mouseclick_handler(interaction.click)
            self.sound_cupstage.pause()
            self.sound_gameover.pause()
            self.sound_win.set_volume(1)
            self.sound_win.play()

        # Draw Game    
        else:
            if self.game == True and theImage is not None and theImage.get_width() > 0 and theImage.get_height() > 0:
                canvas.draw_image(theImage, (theImage.get_width()/2, theImage.get_height()/2), 
                                              (theImage.get_width(), theImage.get_height()),
                                              (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))

                # Increase Timer
                if not self.win or not self.defeat:  
                    self.timer += 1
   
                text_width = frame.get_canvas_textwidth(self.format_time(self.timer), 22)
                canvas.draw_text(self.format_time(self.timer), ((800 - text_width) / 2, 20), 22, "White")
                
                for platform in self.platforms:
                    platform.draw(canvas)
                self.player.draw(canvas)
                if self.i < 4:
                    self.enemy.draw(canvas)
                    self.sound_game.set_volume(1)
                    self.sound_game.play()
                    
                if self.i == 4:
                    if self.boss_firstSpawn:
                        self.boss.dead = False
                        self.boss_firstSpawn = False
                    self.enemy.dead = True
                    self.boss.draw(canvas)
                    for i in range(self.boss_lives):
                        canvas.draw_image(self.heart_image, (16, 16), (32, 32), (25*i + 20, 20), (25, 25))
                    self.sound_game.pause()
                    self.sound_boss.set_volume(1)
                    self.sound_boss.play()
                    
                if self.i == 5:
                    self.enemy.dead = True
                    self.boss.dead = True
                    self.gem.draw(canvas)
                    self.sound_boss.pause()
                    self.sound_cupstage.set_volume(1)
                    self.sound_cupstage.play()

                for i in range(self.lives):
                    canvas.draw_image(self.heart_image, (16, 16), (32, 32), (WIDTH-25*i-20, 20), (25, 25))
                    
    # Handle click events    
    def click(self, pos):
        if self.defeat and pos[0] >= 362 and pos[0] <= 425 and pos[1] >= 410 and pos[1] <= 439:
            self.sound_gameover.pause()
            frame.stop()
        elif self.win and pos[0] >= 362 and pos[0] <= 425 and pos[1] >= 410 and pos[1] <= 439:
            self.sound_win.pause()
            frame.stop()

    def update(self):
        
        self.player.update()
        if not self.enemy.dead:
            self.enemy.update()

        if not self.boss.dead:
            self.boss.update()
            
        if not self.boss.dead:
            
            on_platform_boss = False
            beside_platform_boss = False
            
            for platform in self.platforms:
                on_platform_boss |= platform.interact_Player_Vertical(self.boss)
                beside_platform_boss |= platform.interact_Player_Horizontal(self.boss)
                
            if not on_platform_boss:
                self.boss.vel.add(Vector(0,1))
            else:
                randomNo = random.randint(1, 2)
                if the_clock.transition(15):
                    if randomNo == 1:
                        self.boss.vel.add(Vector(-2, -20))
                    elif randomNo == 2:
                        self.boss.vel.add(Vector(2, -20))
                self.player.vel.x *= 0.85
                
            if self.boss_hits_player() and self.keyboard.c:
                self.boss_lives -= 1
                boss_knockback_direction = (self.boss.pos - self.player.pos).normalize()
                self.boss.vel += boss_knockback_direction * 2
            elif self.boss_hits_player():
                if self.jumpOnBoss():
                    self.player.vel.add(Vector(0, -5))
                    self.boss_lives -= 1
                else:
                    knockback_force = 25  # You can adjust this value to change the strength of the knock back
                    knockback_direction = (self.player.pos - self.boss.pos).normalize()
                    self.player.vel += knockback_direction * knockback_force
                    self.lives -= 1

            if self.lives == 0:
                self.game = False
                self.defeat = True

            if self.boss_lives <= 0:
                self.boss.dead = True
            
        if self.enemy.left().x > 0 and self.enemy.left().x < 25 and self.enemy.spriteSheet.facingforward:
            self.enemy.spriteSheet.facingforward = False
            self.enemyVel *= -1
        elif self.enemy.right().x > WIDTH - 25 and self.enemy.right().x < WIDTH and not self.enemy.spriteSheet.facingforward:
            self.enemy.spriteSheet.facingforward = True
            self.enemyVel *= -1
            
        self.enemy.vel.add(Vector(self.enemyVel, 0))
        self.enemy.vel.x *= 0.85
        if not self.enemy.dead:
            if self.enemy_hits_player() and self.keyboard.c:
                self.enemy.spriteSheet.die()
                self.enemy.dead = True
            elif self.enemy_hits_player():
                if self.jumpOnEnemy():
                    self.player.vel.add(Vector(1,0))
                    self.enemy.spriteSheet.die()
                    self.enemy.dead = True
                else:
                    self.player.vel.reflect(self.player.normal)
                    self.player.vel.x *= 1.5
                    self.enemy.vel.reflect(self.enemy.normal)
                    self.enemy.vel.x *= 1.5
                    self.lives -= 1
                    if self.lives == 0:
                        self.defeat= True
        
        on_platform_player = False
        beside_platform_player = False

        for platform in self.platforms:
            on_platform_player |= platform.interact_Player_Vertical(self.player)
            beside_platform_player |= platform.interact_Player_Horizontal(self.player)

        if(self.i == 4 and self.boss.dead == True and len(self.platforms) == 6):
            self.platforms.pop()
            
        if not on_platform_player:
            if not beside_platform_player:
                self.player.vel.add(Vector(0,1))
                if self.keyboard.left:
                    self.player.vel.add(Vector(-1, 0))
                    self.player.vel.x *= 0.85
                if self.keyboard.right:
                    self.player.vel.add(Vector(1, 0))
                    self.player.vel.x *= 0.85
                    
            if self.player.pos.get_p() <= (0, HEIGHT - 80):
                
                if not (self.i == 0):
                    self.player.pos = Vector(WIDTH - self.player.radius, self.player.pos.get_p()[1])
                    self.i -= 1
                    self.platforms = self.platforms_list[self.i]
                    self.player.vel.y = 0
                    self.enemy.dead = False
                    self.spawn_enemy()
            elif self.player.pos.get_p() >= (WIDTH, HEIGHT - 80):
                self.player.pos = Vector(self.player.radius, self.player.pos.get_p()[1])
                self.i += 1
                self.platforms = self.platforms_list[self.i]
                self.player.vel.y = 0
                self.spawn_enemy()
        else:
            if self.keyboard.left:
                self.player.vel.add(Vector(-1, 0))
                
            if self.keyboard.right:
                self.player.vel.add(Vector(1, 0))
                
            if self.keyboard.space:
                self.player.vel.add(Vector(0, -20))

            if self.player.pos.get_p()[0] <= 0:
                if not (self.i == 0):
                    self.player.pos = Vector(WIDTH - self.player.radius, self.player.pos.get_p()[1])
                    self.i -= 1
                    self.platforms = self.platforms_list[self.i]
                    self.player.vel.y = 0
                    self.enemy.dead = False
                    self.spawn_enemy()
            elif self.player.pos.get_p()[0] >= WIDTH:
                self.player.pos = Vector(self.player.radius, self.player.pos.get_p()[1])
                self.i += 1
                self.platforms = self.platforms_list[self.i]
                self.player.vel.y = 0
                self.enemy.dead = False
                self.spawn_enemy()
            # Apply friction
            self.player.vel.x *= 0.85
        
        if self.gem_collision() and not self.gem.activated and self.i == 5:
            self.gem.activated = True
            self.win = True

    def enemy_hits_player(self):
        return self.enemy.pos.copy().subtract(self.player.pos).length() <= self.enemy.radius + self.player.radius
    
    def boss_hits_player(self):
        return self.boss.pos.copy().subtract(self.player.pos).length() <= self.boss.radius + self.player.radius
    
    def spawn_enemy(self):
        self.enemy.pos = Vector(600, HEIGHT - 40)
        self.enemy.dead = False
        self.enemy.spriteSheet.frame_index = [7,1]
        
    def jumpOnEnemy(self):
        bottom = self.player.bottom()
        top = self.player.top()
        return (
            bottom.y > self.enemy.top().y
            and top.y < self.enemy.bottom().y
            and self.enemy.left().x - 10 < bottom.x
            and bottom.x < self.enemy.right().x + 10
        )
    
    def jumpOnBoss(self):
        bottom = self.player.bottom()
        top = self.player.top()
        return (
            bottom.y > self.boss.top().y
            and top.y < self.boss.bottom().y
            and self.boss.left().x - 10 < bottom.x
            and bottom.x < self.boss.right().x + 10
        )
        
    def gem_collision(self):
        bottom = self.player.bottom()
        top = self.player.top()
        left = self.player.left()
        right = self.player.right()
        return ( 
            bottom.y > self.gem.top().y
            and top.y < self.gem.bottom().y
            and self.gem.left().x < bottom.x
            and bottom.x < self.gem.right().x 
        )


class Clock:
    def __init__(self):
        self.time = 0
        
    def tick(self):
        self.time+=1
        
    def transition(self,frame_duration):
        return (self.time % frame_duration == 0)            


class Platform:
    def __init__(self, ytop, ybottom, xstart, xend, width):
        self.ytop = ytop
        self.ybottom = ybottom
        self.xstart = xstart
        self.xend = xend
        self.width = width
        self.color = "Black"
        self.top = ((self.ytop + self.ybottom) / 2) - self.width / 2
        self.bottom = ((self.ytop + self.ybottom) / 2) + self.width / 2
        self.left = ((self.xstart + self.xend) / 2) - self.width
        self.right = ((self.xstart + self.xend) / 2) + self.width
        self.in_collision1 = set()
        self.in_collision2 = set()
        self.normal = Vector(1.2,0)

    def draw(self, canvas):
        canvas.draw_line(
            (self.xstart, self.ybottom),
            (self.xend, self.ytop),
            self.width,
            self.color
        )
        
    def hitVertical(self, player):
        bottom = player.bottom()
        top = player.top()
        return (
            bottom.y > self.top
            and top.y < self.bottom
            and self.xstart < bottom.x
            and bottom.x < self.xend   
        )
        
    def hitHorizontal(self, player):
        bottom = player.bottom()
        top = player.top()
        left = player.left()
        right = player.right()
        if bottom.y > self.top and top.y + 50 < self.bottom and self.xstart < bottom.x and bottom.x < self.xend:
            return (left.x <= self.xend or right.x >= self.xstart)
        elif self.xstart == self.xend:
            return (left.x <= self.xend and right.x >= self.xstart)
        else:
            return False
        
    def interact_Player_Vertical(self, player):                
        if self.hitVertical(player):
            if player not in self.in_collision1:
                self.in_collision1.add(player)
                if player.vel.y >= 0:
                    # player has landed
                    player.vel.y = 0
                    player.pos.y = self.top - player.radius
                    return True
                else:
                    # player has hit the bottom
                    player.vel.y = 0
        else:
            self.in_collision1.discard(player)
        return False
    
    def interact_Player_Horizontal(self, player):
        if self.hitHorizontal(player):
            if player not in self.in_collision2:
                self.in_collision2.add(player)
                player.bounce(self.normal)
                return True
        else:
            self.in_collision2.discard(player)
        return False


class Menu:
    # Constructor for the Menu class
    def __init__(self):
        self.play_clicked = False
        self.instructions_shown = False
        # Load menu sound
        self.sound_menu = simplegui.load_sound('https://opengameart.org/sites/default/files/3XOSCMenu.wav')
        # Load menu image
        try:
            self.menu_image = simplegui.load_image("https://images4.alphacoders.com/100/1008904.png")
        except ValueError:
            print("Error: Image dimensions must be > 0. Run the program again to fix this.")
            self.menu_image = None
            
    # Draw the menu and instructions on the canvas
    def draw(self, canvas):
        if self.instructions_shown:
            if self.instructions_image is not None and self.instructions_image.get_width() > 0 and self.instructions_image.get_height() > 0:
                canvas.draw_image(self.instructions_image, (self.instructions_image.get_width()/2, self.instructions_image.get_height()/2), 
                                      (self.instructions_image.get_width(), self.instructions_image.get_height()),
                                      (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
                self.sound_menu.set_volume(1)
                self.sound_menu.play()
                frame.set_mouseclick_handler(menu.click)
            else:
                print("")
            canvas.draw_polygon([[150, 25], [650, 25], [650, 475], [150, 475]], 12, '#757bbe', '#757bbe73')
            canvas.draw_text("Instructions", (310, HEIGHT/2 - 180), 36, "Purple", "sans-serif")
            canvas.draw_text("Use the arrows to move the character", (170, HEIGHT/2 - 100), 28, "White", "sans-serif")
            canvas.draw_text("Use spacebar to jump", (280, HEIGHT/2 - 50), 26, "White", "sans-serif")
            canvas.draw_text("Press 'C' to attack", (295, HEIGHT/2 ), 26, "White", "sans-serif")
            canvas.draw_text("Close", (360, HEIGHT/2 +200 ), 30, "Purple", "sans-serif")

        else:
            if self.menu_image is not None and self.menu_image.get_width() > 0 and self.menu_image.get_height() > 0:
                canvas.draw_image(self.menu_image, (self.menu_image.get_width()/2, self.menu_image.get_height()/2), 
                                  (self.menu_image.get_width(), self.menu_image.get_height()),
                                  (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
                self.sound_menu.set_volume(1)
                self.sound_menu.play()
            else:
                print("")
            canvas.draw_text("Knight Valley", (275, HEIGHT/2 - 140), 46, "White", "sans-serif")
            canvas.draw_polygon([[290, 215], [500, 215], [500, 260], [290, 260]], 3, '#CAC2B3', '#CAC2B3D9')
            canvas.draw_text("Click to play", (300, HEIGHT/2 -2), 36, "Purple", "sans-serif")
            canvas.draw_polygon([[330, 270], [455, 270], [455, 300], [330, 300]], 3, '#CAC2B3', '#CAC2B3D9')
            canvas.draw_text("Instructions", (332, HEIGHT/2 + 40), 24, "Purple", "sans-serif")

    # Handle click events on the menu        
    def click(self, pos):
        
        if not self.instructions_shown and not self.play_clicked and pos[0] >= 288 and pos[0] <= 501 and pos[1] >= 213 and pos[1] <= 260:
            self.play_clicked = True
            self.sound_menu.pause()
            self.start_game()
        elif not self.instructions_shown and not self.play_clicked and pos[0] >= 329 and pos[0] <= 456 and pos[1] >= 268 and pos[1] <= 300:
            self.instructions_shown = True
            self.show_instructions()
        elif self.instructions_shown and pos[0] >= 360 and pos[0] <= 433 and pos[1] >= 428 and pos[1] <= 448:
            self.instructions_shown = False

    # Show instructions
    def show_instructions(self):
        
        # Load instructions image
        try:
            self.instructions_image = simplegui.load_image("https://i.pinimg.com/736x/2c/08/20/2c0820784d838c0394311d7bccb4e1c6.jpg")
        except ValueError:
            print("Error: Image dimensions must be > 0. Run the program again to fix this.")
            self.instructions_image = None
        frame.set_draw_handler(self.draw)
        
    # Start the game
    def start_game(self):
        frame.set_draw_handler(interaction.draw)


# Create instances of game objects
menu = Menu()
spritesheet = Spritesheet()
enemySpriteSheet = Spritesheet_enemy()
bossSprteSheet = Spritesheet_boss()
gemSprite = Spritesheet_gem()
the_clock = Clock()

# Create keyboard object to handle keyboard inputs
keyboard = Keyboard()

# Create the game frame
frame = simplegui.create_frame("Platforms", WIDTH, HEIGHT)
frame.set_keyup_handler(keyboard.key_up)
frame.set_keydown_handler(keyboard.key_down)
frame.set_draw_handler(menu.draw)
frame.set_mouseclick_handler(menu.click)

# Initialize player, enemy, boss, and gem objects
player = Player(Vector(100, HEIGHT - 200), spritesheet)
enemy = Enemy(Vector(600, HEIGHT - 40), enemySpriteSheet)
boss = Boss(Vector(WIDTH/2, HEIGHT/2), bossSprteSheet)
gem = Gem(Vector(WIDTH/2, HEIGHT/2), gemSprite)

# Define platform stages and levels
stage1 = [Platform(HEIGHT, -HEIGHT, 0, 0, 50), Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 200, HEIGHT - 200, 150, 300, 50), Platform(HEIGHT - 250, HEIGHT - 250, 500, 700, 50)]
stage2 = [Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 150, HEIGHT - 150, 125, 250, 50), Platform(HEIGHT - 250, HEIGHT - 250, 300, 450, 50), Platform(HEIGHT - 350, HEIGHT - 350, 550, 750, 50)]
stage3 = [Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 130, HEIGHT - 130, 175, 300, 50), Platform(HEIGHT - 350, HEIGHT - 350, 100, 350, 50), Platform(HEIGHT - 175, HEIGHT - 175, 450, 650, 50)]
stage4 = [Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 150, HEIGHT - 150, 150, 350, 50), Platform(HEIGHT - 250, HEIGHT - 250, 450, 700, 50)]
stage5 = [Platform(HEIGHT, -HEIGHT, 0, 0, 50), Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 200, HEIGHT - 200, 250, 500, 50), Platform(HEIGHT - 350, HEIGHT - 350, 100, 200, 50), Platform(HEIGHT - 350, HEIGHT - 350, 550, 650, 50), Platform(HEIGHT, -HEIGHT, WIDTH, WIDTH, 50)]
stage6 = [Platform(HEIGHT, -HEIGHT, 0, 0, 50), Platform(HEIGHT, HEIGHT, -5, WIDTH + 5, 50), Platform(HEIGHT - 200, HEIGHT - 200, 220, 525, 50), Platform(HEIGHT, -HEIGHT, WIDTH, WIDTH, 50)]
level1= [stage1, stage2, stage3, stage4, stage5, stage6]

# Create the Interaction object with game objects and levels
interaction = Interaction(
    player,
    enemy,
    boss,
    gem,
    level1,
    keyboard
)

### Copyright ###
frame.add_label("<<< Knight Valley >>>")
frame.add_label("by Maxsimilian, Jakub and Westleigh")
frame.add_label("======================")
frame.add_label("Game Description")
frame.add_label(
    "2D platform game. Clear stages to Win. Pay attention to the walking minions. In case of contact, you will lose a life. If you lose all your lives its 'GameOver'.")
frame.add_label("======================")
frame.add_label("<<<INSTRUCTIONS>>>")
frame.add_label("Left, Right Arrows => move character")
frame.add_label("Space => jump")
frame.add_label("C => attack")
frame.add_label("======================")
frame.add_label("<<<CREDITS>>>")
frame.add_label("Images from: veecteezy.com, opengameart.org and img.freepik.com.")
frame.add_label("Devlin Bataric - Game Over & Jonathan Shaw (www.jshaw.co.uk).")
frame.start()
