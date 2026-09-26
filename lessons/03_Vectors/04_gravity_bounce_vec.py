"""
Gravity bounce using Vectors. 

This version of the Gravity Bounce program uses Pygame's Vector2 class to handle
the player's position and velocity. This makes the code more readable and
understandable, and makes it easier to add more complex features to the game.


"""
import pygame
from dataclasses import dataclass
pygame.init

class Colors:
    """Constants for Colors"""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PLAYER_COLOR = (0, 0, 255)
    BACKGROUND_COLOR = (255, 255, 255)


@dataclass
class GameSettings:
    """Settings for the game"""
    width: int = 500
    height: int = 500
    gravity: float = 0.3
    player_start_x: int = 100
    player_start_y: int = 20
    player_v_y: float = 0  # Initial y velocity
    player_v_x: float = 4  # Initial x velocity
    player_width: int = 20
    player_height: int = 20
    player_jump_velocity: float = 100
    frame_rate: int = 150



class Game:
    """Main object for the top level of the game. Holds the main loop and other
    update, drawing and collision methods that operate on multiple other
    objects, like the player and obstacles."""

    def __init__(self, settings: GameSettings):
        pygame.init()

        self.settings = settings
        self.running = True



        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.clock = pygame.time.Clock()
    def vec_to_center(self, pos):
        pos=pos
        vector = (250-pos.x, 250-pos.y)
        return vector
        

        # Turn Gravity into a vector
        


    #def draw(self, show_line=True):
        """Draws the player and the direction vector on the screen."""
        #pygame.draw.rect(screen, Settings.PLAYER_COLOR, (self.position.x - Settings.PLAYER_SIZE // 2, self.position.y - Settings.PLAYER_SIZE // 2, Settings.PLAYER_SIZE, Settings.PLAYER_SIZE))
        
        # The end position of the direction vector is the player's position plus the direction vector
        #end_position = self.position + self.direction_vector
        
        #if show_line:
            #pygame.draw.line(screen, Settings.LINE_COLOR, self.position, end_position, 2)

    def run(self):
        """Main game loop"""
        player = Player(self)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False

            player.update()
            
            self.screen.fill(Colors.BACKGROUND_COLOR)
            player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.settings.frame_rate)


        pygame.quit()


class Player:
    """Player class, just a bouncing rectangle"""

    def __init__(self, game: Game):
        self.game = game
        settings = self.game.settings
        self.gravity = pygame.Vector2(0,0)
        self.width = settings.player_width
        self.height = settings.player_height

        # Vector for our jump velocity, which is just up
        self.v_jump = pygame.Vector2(0, -settings.player_jump_velocity)

        # Player position
        self.pos = pygame.Vector2(settings.player_start_x,
                                  settings.player_start_y if settings.player_start_y is not None else settings.height - self.height)

        self.gravity = pygame.Vector2(0, settings.gravity)

        # Player's velocity
        self.vel = pygame.Vector2(settings.player_v_x, settings.player_v_y)  # Velocity vector

  



    # Direction functions. IMPORTANT! Using these functions isn't really
    # necessary, but it makes the code more readable. You could just use
    # self.vel.x < 0, but writing "self.going_left()" is a lot easier to read and
    # understand, it makes the code self-documenting.

    def going_up(self):
        """Check if the player is going up"""
        return self.vel.y < 0

    def going_down(self):
        """Check if the player is going down"""
        return self.vel.y > 0

    def going_left(self):
        """Check if the player is going left"""
        return self.vel.x < 0

    def going_right(self):
        """Check if the player is going right"""
        return self.vel.x > 0

    v = pygame.math.Vector2(3, 4)


    # Location Fuctions

    def at_top(self):
        """Check if the player is at the top of the screen"""
        return self.pos.y <= 0

    def at_bottom(self):
        """Check if the player is at the bottom of the screen"""
        return self.pos.y >= self.game.settings.height - self.height

    def at_left(self):
        """Check if the player is at the left of the screen"""
        return self.pos.x <= 0

    def at_right(self):
        """Check if the player is at the right of the screen"""
        return self.pos.x >= self.game.settings.width - self.width

    # Updates

    def update(self):
        """Update player position, continuously jumping"""
        self.update_jump()
        self.update_gravity()
        self.update_v()
        self.update_pos()

    def update_gravity(self):
        v = pygame.math.Vector2(250, 250)-self.pos

        # Calculate the magnitude (r) of the vector
        r = v.length()

        # Avoid division by zero by checking if r is non-zero
        if r != 0:
        # Scale the vector by 1 / r^2
            v_scaled = v * (1 / r**2)
        else:
            v_scaled = pygame.math.Vector2(0, 0)  # Handle zero-length vector if necessary


    def update_v(self):
        """Update the player's velocity based on gravity and bounce on edges"""

        self.vel += self.gravity*0.2 # Add gravity to the velocity
        drag = self.vel * -0.001

        self.vel = self.vel + drag



        if self.at_bottom() and self.going_down():
            self.vel.y = self.vel.y * -1
            #if abs(self.vel.y) <= 5:
                #self.vel.y=0
                #self.pos.y = 490


        if self.at_top() and self.going_up():
            self.vel.y = -self.vel.y # Bounce off the top.

        # If the player hits one side of the screen or the other, bounce the
        # player. we are also checking if the player has a velocity going farther
        # off the screeen, because we don't want to bounce the player if it's
        # already going away from the edge

        if (self.at_left() and self.going_left() ) or ( self.at_right() and self.going_right()):
            self.vel.x = -self.vel.x

    def update_pos(self):
        """Update the player's position based on velocity"""
        self.pos += self.vel  # Update the player's position based on the current velocity

        # If the player is at the bottom, stop the player from falling and
        # stop the jump

        if self.at_bottom():
            self.pos.y = self.game.settings.height - self.height

        if self.at_top():
            self.pos.y = 0

        # Don't let the player go off the left side of the screen
        if self.at_left():
            self.pos.x = 0

        # Don't let the player go off the right side of the screen
        elif self.at_right():
            self.pos.x = self.game.settings.width - self.width

    def update_jump(self):
        keys = pygame.key.get_pressed()
        thrust = self.vel * 0.1
        #pygame.draw
        """Handle the player's jumping logic"""
        if keys[pygame.K_SPACE]:
            self.vel = self.vel + thrust
        if keys[pygame.K_UP]:
            self.vel = self.vel*1.05
        if keys[pygame.K_DOWN]:
            self.vel = self.vel*0.9
        if keys[pygame.K_LEFT]:
            self.vel = self.vel.rotate(-1)
        if keys[pygame.K_RIGHT]:
            self.vel = self.vel.rotate(1)





        # Notice that we've gotten rid of self.is_jumping, because we can just
        # check if the player is at the bottom.
        #if self.at_bottom():
            #self.vel += self.v_jump
         

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.PLAYER_COLOR, (self.pos.x, self.pos.y, self.width, self.height))
        end_pos = self.pos + self.vel*20
        pygame.draw.line(screen, Colors.PLAYER_COLOR, self.pos, end_pos, 2)


settings = GameSettings()
game = Game(settings)
game.run()
