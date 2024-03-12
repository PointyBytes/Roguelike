# My first Roguelike
I recently completed a [tutorial](https://rogueliketutorials.com/tutorials/tcod/v2/) found at https://rogueliketutorials.com/ by @HexDecimal and @TStand90. Now and now I'm eager to expand my knowledge and skills. As an avid fan of the board game Dungeonquest (Sv. Drakborgen) from my childhood, I am drawn to exploring how to take my newfound expertise even further. In the game, players race against time to explore a stronghold and reach the chamber where a dragon guards its massive treasure. The player who collects the most treasure and escapes before the sun sets is declared the winner. I'm excited to explore how I can apply what I've learned to create my adventures and challenges.

After the player levels up the second time the player can become unbeatable and delve deeper without any chance of taking another point of damage. 


## Ideas I want to add:
- Traps
  - Spiks
  - Trapdoors
  - Arrows
- Different types of levels
  - Larger rooms
  - Specialised rooms
  - Caves further down
  - Flowing water (transparent non walkable tiles)
  - Traps (a new stat that makes it possible to notice traps before stepping on them)
  - Lairs with boss monsters
- More enemies
  - Goblins
  - Skeletons
  - Lich
  - Twisted Dwarfs
- More gear
  - Ranged weapons
  - Shields
  - Off-hand weapons/shields
- More slots for gear
  - Head
  - Body
  - Arms
  - Legs
- Soft and hard armor that affects Dexterity
- Different weapon characteristics for soft and hard armor.
  - Piercing
  - Slashing
  - Crushing
- States that can affect both the player and the monsters.
  - Poisoned
  - Disease
  - Wasting away
  - Healing over time
  - Regeneration (spell effect)
- Stairs back up where you spawn on the new level.
- A surface level with a little village.
  - Economics for the surface village.
  - This could be a menu.
- Light graphics or at least sprites
- A central file that holds all setting variables
- Better key bindings
  - A file where all keys are listed and can be changed. Same as the central variable file?
  - Key bindings can be found in game/input_handlers.py
- Random damage range
- Degrading armor
- Particle effects

## Controls
Not the controls at the moment but the controls I want to implement.

* `W` - move up
* `A` - move left
* `S` - move down
* `D` - move right
* `i` - show inventory
    * `W` - move up
    * `S` - move down
    * `Enter` - use, equip, or unequip item
    * `ESC` - exit inventory
    * `space` - drop item
* `space` - wait one turn
* `ESC` - save menu
* `Left Click` - select monster as target

##

` `   A floor space
`^`   A trap (known)
`´`   A glyph of warding
`'`   An open door      
`<`   A staircase up    
`>`   A staircase down  
`#`   A wall
`+`   A closed door
`%`   A mineral vein
`*`   A mineral vein with treasure
`:`   A pile of rubble     
`!`   A potion (or flask)            
`?`   A scroll (or book)             
`,`   A mushroom (or food)           
`-`   A wand or rod                  
`_`   A staff                        
`=`   A ring                         
`"`   An amulet                      
`$`   Gold or gems                   
`~`   Lights, Tools, Chests, etc     
`&`   Multiple items
`/`   A pole-arm
`|`   An edged weapon
`\`   A hafted weapon
`}`   A sling, bow, or crossbow
`{`   A shot, arrow, or bolt
`(`   Soft armor
`[`   Hard armor
`]`   Misc. armour
`)`   A shield
