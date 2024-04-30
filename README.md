[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14650905&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Lola Chan

***

## Project Description

<< Give an overview of your project >>

***    

## GUI Design

### Initial Design

![initial gui](assets/temp_gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Game over screen
3. Moveable character
4. Obstacle collision
5. Scrolling background

### Classes

class Player:
    def __init__(self, screen, x, y, height, width, player_img):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.player_img = player_img.png
    

- Enemy
- World
- Tiles
- Soul: pick up three from around map to end game

## ATP

Test Case 1: Menu --- test navigation through the game's main menu
| Step  |Procedure                           |Expected Results                           |
|-------|:----------------------------------:|------------------------------------------:|
|  1    | Start the game                     |                                           |
|  2    | Navigate through menu options      |                                           |
|       |   (start and quit game)            |                                           |
|  3    | Verify each option is selectable   |The main menu should allow the player to   |
|       |   and leads to expected actions    |navigate through options and select them.  |


Test Case 2: Spawn Test --- test player spawns on center of screen without falling through the ground
| Step  |Procedure                           |Expected Results                           |
|-------|:----------------------------------:|------------------------------------------:|
|  1    | Start the game                     |                                           |
|  2    | Check if player spawns without     |                                           |
|       |   falling through the ground       |                                           |
|       |                                    | Player spawns on the ground               |


Test Case 3: Player Movement --- test if player can move left, right, and jump
| Step  |Procedure                           |Expected Results                           |
|-------|:----------------------------------:|------------------------------------------:|
|  1    | Start the game                     |                                           |
|  2    | Press 'a'                          |                                           |
|  3    | Verify the player moves left       |                                           |
|  4    | Press 'b'                          | The player should move left and right     |
|  5    | Verify the player moves right      | in response to 'a' and 'd' keys           |


Test Case 4: Collision Detection --- player should collide with walls and flooring
| Step  |Procedure                           |Expected Results                           |
|-------|:----------------------------------:|------------------------------------------:|
|  1    | Start the game                     |                                           |
|  2    | Walk towards the left wall         |                                           |
|  3    | Verify that the player cannot phase| The player should be able to jump on      |
|       | through the walls                  | blocks and hit walls                      |


Test Case 5: Animation --- player should have walking and jumping animations
| Step  |Procedure                           |Expected Results                           |
|-------|:----------------------------------:|------------------------------------------:|
|  1    | Start the game                     |                                           |
|  2    | Press 'a'                          |                                           |
|  3    | Verify player is facing left and   |                                           |
|       | has a walking animation            |                                           |
|  4    | Press spacebar                     |                                           |
|  5    | Verify the player has a jumping    | The player should move and animate in     |
|       | animation                          | response to 'a', 'd', and spacebar        |

