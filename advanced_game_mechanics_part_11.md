in the later game introduce mission-specific mechanics (we already mentioned and
discussed a few of these effects in Chapter 2). For example, in the level “The Devil’s
Playground,” minerals can be harvested only from low areas that are periodically
flooded with hot lava (Figure 2.6). This requires players to move their units to safety
from time to time. In effect, it adds a powerful slow cycle pattern to the internal
economy of StarCraft II. A different slow cycle appears in the “Outbreak” level, when
mutants attack the players base en masse during the night and the player goes out
to destroy infested structures during the day (Figure 10.2). Other levels force players
to keep moving their bases across the map to protect or attack periodic convoys or
to quickly capture specific targets.

228

Game mechanics: advanced Game desiGn

FIGURe 10.2
during the night cycle
in the “Outbreak”
level of StarCraft II ,
you must defend your
base against hordes of
mutants.

StarCraft II is a great example of how to build varying levels from the same core of
game mechanics. By changing goals, disabling certain mechanisms, or adding a
novel mechanism that works in a level only, you can get a lot of gameplay out of
the same core. These changes to the circumstances of individual levels will require
players to explore a wider variety of strategies—they can’t use the same approach to
every level.

Storytelling
As we discussed in Chapter 2, games of progression often tell stories as part of their
entertainment. Storytelling helps to structure levels and guide players. Stories give
players a motive for achieving goals that otherwise would remain abstract or meaningless. Killing orcs in a fantasy game obtains emotional significance when the
game’s story frames it as an act of vengeance or self-defense.
Stories in games work best when the mechanics, the level structure, and the dramatic
arc interconnect seamlessly. The typical dungeon structure in The Legend of Zelda
works because it creates synergy between story, level layout, and game mechanics.
Link nearly always fights a mini-boss halfway through the level to obtain a special
weapon that he’ll need to defeat the dungeon’s end boss. This structure gives the
player ample opportunity to explore the new mechanics associated with the special
weapon. It creates variety by introducing the new mechanics partway through the

inTeGraT inG LeveL desiGn and mechanics

229

dungeon and enables progression by unlocking previously unreachable areas.
In addition, it uses the familiar dramatic arc associated with adventure stories where
the hero fights his way through a series of tough challenges to gain that vital edge
and come out victorious.

Because this book concentrates on game economies, we don’t have room to discuss
the various efforts that people have made toward emergent storytelling. For the
moment, it remains a research topic for academics and is seldom attempted in
commercial video games.

Missions and Game Spaces
When we design levels, we usually do so working from one of two perspectives on
the task. One perspective focuses on the challenges that players must overcome (or
tasks they must perform) to complete the level. The other perspective focuses on
the layout of the game world—the simulated space in which it takes place.
In Chapter 9 of Fundamentals of Game Design, Ernest Adams explains that challenges
in video games form a hierarchy, with groups of short-duration challenges combining
to form larger challenges. The lowest level challenges are called atomic challenges
because they cannot be further subdivided. For example, successfully landing a
punch on an opponent in a boxing game is an atomic challenge, while winning the
fight is a mission made up of many such challenges, and it may be necessary to win
many fights to finish the game. From the challenges perspective on level design, we
concentrate on defining this hierarchy.
Viewing level design from the second perspective, that of layout, we define the
architecture of the level itself. In Chapter 12 of Fundamentals of Game Design, Adams
describes several common spatial layouts found across different games. Some games,
such as side-scrolling games or Half-Life, provide nearly linear levels. Track-based car
racing games use ring-shaped layouts. Spaces in first-person shooter games designed
for multiplayer combat are often quite sophisticated, with open and protected areas,
doors to guard, high vantage points, and so on.
Each of these two different perspectives has its own strengths when considering
different design issues. For example, it’s easier to think about pacing and difficulty
curves when you view the level as a series of tasks or challenges. But storytelling and

ChAptEr 10

Most storytelling in video games is either linear (the story is the same every time
the player plays the game) or branching (the player makes decisions that influence
the direction of the plot line in a large-scale way). Emergent storytelling, in which
a story emerges entirely from the game’s mechanics and the player’s actions, has
long been a holy grail of game designers. It has proven to be a particularly intractable problem because it requires designers to characterize dramatic situations and
human behavior in numeric and algorithmic terms. This is far more difficult than
creating the economy of even a very complex game world like that of Civilization.

230

Game mechanics: advanced Game desiGn

atmosphere are better understood in terms of the spatial layout of the level, at least
if the story concerns a journey.
In our analyses of game levels in this book, we find it important to keep the two
perspectives separate when trying to discuss them (although of course in the final
product they must work together to form a harmonious whole). We refer to the
mission of a level when we focus on the sequence of tasks or challenges in a level,
and we use the term game space when we focus on the spatial layout of a level.
Separating these two aspects of level design helps us see how they relate to emergent
gameplay. In some games, the mission of the level maps directly to its space (see
the “The Dungeon Is the Mission?” sidebar). However, this is not always the case.
Games can reuse the same space for different missions, as in the Grand Theft Auto
games. They demonstrate that the same space can accommodate many missions if
the designer makes imaginative use of it. This saves the developers time and money,
because they don’t have to create a new space for every level in the game. It has
gameplay benefits as well. For example, players can use previous knowledge of the
space to their advantage, adding to their player’s sense of control with each mission
that reuses the space.

What iF the dunGeon is the mission?
sometimes it can be useful to design a mission and a game space as one. in hack-andslash table-top role-playing games, the dungeon is a good way to quickly create a level
(or story) that is easy to manage for the dungeon master. all she has to do is draw a maze
on a piece of graph paper, litter it with monsters, and put some rewarding treasure at the
end. she can even rely on random encounters to spice up things as needed. in this case,
the dungeon map almost resembles a flow chart for the level’s mission; the structure of
the game space dominates the level, and the mission (if it has any independent structure
at all) has little impact. although this works well for a particular style of play (the Diablo
games demonstrate that there is a viable niche for that type of gameplay), it is an approach
to level design that does not work for all types of games. as a designer, you have little
control over the pacing of the game, and the action tends to get repetitive fast. if you
seek to offer a more complex gameplay arc, you would do well to consider the mission
separately from the game space and create quality structures for each.

A level’s mission and game space do depend on each other, even though we discuss
them separately. A space must accommodate the mission, while the mission should
ideally guide the player in her exploration of the space. In the next chapter, we’ll
explore in more detail how progression mechanisms, and lock and key mechanisms
in particular, serve to connect missions and spaces.
When designing a level, it often makes sense to start by designing its mission rather
than its space. A mission is easier to write down and organize; its structure is usually quite simple. However, this isn’t an absolute rule. There is a risk to beginning
with the mission: Designers sometimes create a very linear space to fit the mission,

inTeGraT inG LeveL desiGn and mechanics

231

leaving out any opportunities for the player to explore or enjoy the space for its
own sake. For some levels, it might be more interesting to start with designing an
engaging space (such as a castle, space station, or famous nonfictional location) and
design a mission to fit that space.

Mapping Mechanics to Missions

ChAptEr 10

Game mechanics interact with missions and game spaces differently. We’ll deal with
missions first and address game spaces in “Mapping Mechanics to Game Spaces” later
in this chapter. The interaction with missions is often straightforward. The game
mechanics dictate what actions are available in the game, and these actions suggest
tasks that can be used to build missions. For example, if the game allows the player to
collect flowers, a simple mission could be to collect ten flowers. In this section, we’ll
explore some variations on the flower-collecting mission to make it more enjoyable.

addinG chaLLenGes TO imPrOve The exPerience
When mapping mechanics to missions, it is important to be sure that the tasks are
not too trivial or repetitive. If collecting a flower only requires the player to navigate
to a location and press a button, it offers no challenge. You can use Machinations
diagrams to document the challenges that a mission offers and to help you think
of design strategies that avoid trivial and repetitive tasks. The mission to collect ten
flowers might look like Figure 10.3. From the diagram, you can see that the mission
is both trivial and repetitive. The way to complete this game is simply to click the
source ten times to win. There is no choice, and the game involves no player skill.
(Remember, at this point we’re discussing missions independently of the space they
take place in.)

FIGURe 10.3



 

repetitive and trivial
mechanics create poor
missions.



The mission can be improved by adding enemies that the player must avoid. The
new mechanics are represented by Figure 10.4. In this case, the player needs to
choose whether to focus on avoiding enemies or collecting flowers (if you built the
diagram yourself, make sure you put the diagram in synchronous time mode so that
the player can activate each element only once every second). The effect of avoiding
is randomized a little: The player removes one to three threat tokens when avoiding.
This randomness models variation in player skill.




 








FIGURe 10.4



 


adding enemies to
create choice

232

Game mechanics: advanced Game desiGn

Playing this diagram is already tricky, mostly because of its high pace (see the sidebar “Speed vs. Cognitive Effort”). However, once you find the right balance, it is not
too difficult. We can further change this by adding an interaction between the two
mechanisms. In Figure 10.5, we added a mechanism that increases the rate at which
threat is produced for every flower the player collects. This means that the player
must spend more and more time avoiding the enemies while progressing toward the
goal. This creates a nice difficulty curve for the mission. It starts out relatively easy
but gets more difficult quickly.

FIGURe 10.5



interaction between
progress and difficulty
!


 






!"





 


speed Vs. coGnitiVe eFFort
Figures 10.4 and 10.5 are good illustrations of the balance between speed and cognitive
effort described by chris crawford in his book the Art of Computer Game Design (1984).
The tasks of collecting and avoiding are not very difficult in themselves, and even finding
the right balance between the two does not involve too much strategic thinking. however,
because the diagram moves at a high speed, finding the right balance fast enough is
actually quite challenging. crawford suggests that speed and cognitive effort should be
balanced. Games that require a lot of cognitive effort should run at a low pace (or even
be turn based), while games that require little cognitive effort should run at a fast pace
to make them interesting. You can get an appreciation for this balance by changing the
speed of these diagrams or setting them to a turn-based time mode.

desiGn challenGe
Figure 10.5 implements the escalating challenge pattern and comes very close to implementing the escalating complexity pattern (see appendix B for detailed descriptions of
these patterns). can you find a way to change the diagram so that it implements escalating complexity? how would you incorporate the new mechanics into the game’s fiction—
its imaginary world of flowers and enemies?

inTeGraT inG LeveL desiGn and mechanics

233

addinG sUBTasKs
Another way you can make the mechanics for the flower-collecting mission more
interesting is by adding subtasks that must be completed to achieve the goal. In
Figure 10.6, the goal is still the same: collect ten flowers. However, in this example, the player must perform three subtasks to unlock all the flowers to be able to
achieve the goal. In this case, every subtask is represented as a simple gate but can
be replaced by a more complex mechanism. For example, you can use the enemyavoiding mechanism to create a subtask. To create variation in the game, it is best to
create subtasks that offer the player different gameplay experiences, perhaps because
they have unique mechanics or because they emphasize different structures in the
general mechanics of the game.





Performing subtasks
necessary to collect all
the flowers





 



  










aVoid creatinG too many indiVidual mechanisms
When creating missions that rely on a number of subtasks that the player must complete, you have to be careful not to create too many individual mechanisms for all those
subtasks. This creates a lot of work, because all those mechanisms have to be designed
and tested. it also introduces a risk: all those different subtasks must be fun. Generally
speaking, players perceive your level as just as fun as the weakest mechanism in the
mission (people remember negative experiences more vividly than they do positive
ones). To avoid having to design too many individual mechanisms, create a solid core
of mechanics for your game first, and then zoom in on certain parts of that structure
for individual tasks. This is very similar to our advice about using a different focus for
each level, as we discussed in the section “Focusing on different structures in Your
mechanics” earlier in this chapter.

ChAptEr 10

FIGURe 10.6


234

Game mechanics: advanced Game desiGn

Many games that use subtasks do not make all the tasks available at once. They
create dependencies among the tasks. We can easily add dependencies to the flower
collection example (Figure 10.7). The advantage of these dependencies is that they
allow the designer to control the pacing of the tasks and create a nice difficulty
curve by making the more difficult tasks dependent on the easier ones. Sometimes,
this leads to completely linear missions, in which the order of all the subtasks is
fixed. You shouldn’t always choose this approach, however, because players appreciate some freedom of action. If your game has a fixed sequence of subtasks, you
should at least make sure that the actions required to complete a subtask allow some
options—otherwise, the gameplay amounts to checking off boxes. When evaluating the quality of your mission design, you should always ask yourself how many
options are available to the player at a time. More is generally better than fewer, as
long as you don’t overwhelm the player with options and no data about how to
choose one.

FIGURe 10.7



dependencies among
subtasks










 



  













linear missions in open Game spaces
if a mission is linear, that doesn’t mean the game space must also be linear. many
adventure games, especially those that rely heavily on a long sequence of locks and
keys, have one sequence of tasks that must be completed to beat the game; they have a
linear mission. But this mission can be set in a level in which the player must run back
and forth a lot—through a castle, for example. This is called backtracking and can be
frustrating if used too often. if you have a mission that is very linear, simply creating an
open game space to give it more variety is a poor strategy. Usually it is better to redesign
the mission to create a less linear experience. Give the player good reasons to explore
the castle through your mission, rather than forcing them to run through the same space
again and again.

inTeGraT inG LeveL desiGn and mechanics

235

exPLOrinG advanced TechniqUes: OPTiOnaL and mUTUaLLY
excLUsive TasKs
In this book we cannot go into too much detail about the fine art of creating missions and game spaces. However, we do encourage you to experiment with the way
you order the tasks and subtasks in a mission. Here we offer two advanced techniques to make missions less linear (but be warned that it also makes designing
them harder): optional tasks and mutually exclusive tasks.

ChAptEr 10

If you give the player an entirely optional task, be sure to think about the rewards
that performing the task brings. Does the reward have an effect on the game
mechanics? (For example, it might give the player a more powerful weapon.) Or
is the reward just some extra eye-candy or badge of honor? Optional tasks that do
affect the gameplay make the game richer, but you have to be careful that the impact
is not so great that the task actually becomes a requirement to finish the game.
Many games create alternative sequences of tasks to achieve a mission goal. (For
example, players might sneak past a guard and steal a key, or they might fight or bribe
the guard to the same effect.) When you create alternatives like this, you can make
certain tasks mutually exclusive. If the player tries to bribe the guard, it becomes
impossible to sneak past him (he is aware the player is there), and if the player tries
to sneak past him, bribing him no longer is an option (the guard’s suspicions are
now aroused). If you set up mutually exclusive tasks, you have to be careful not
to create a situation in which the game is no longer solvable. In this example, the
option to fight the guard serves as a backup strategy that is always available.

Mapping Mechanics to Game Spaces
Machinations diagrams can be used to represent game spaces. To explore that idea
further, we start with a diagram representing a trivial game where the objective is to
make your way from a starting point to finish (Figure 10.8). A series of pools represent different locations in the game, and a single resource representing the player
can be moved between these locations simply by clicking them. In this case, the
player can move in only one direction. (Remember that pools pull by default. To
move the player you must click an empty pool to pull him in.)

FIGURe 10.8





You can use this type of diagram to represent more open or maze like structures. For
example, Figure 10.9 represents a space for a simple version of the flower-collecting
game discussed in the previous section. The player is represented as a blue resource
element, while the flowers are red ones. The presence of the player at a certain location makes it possible to transfer the flower to the player’s inventory by clicking an
adjacent gate. Acquiring five flowers unlocks the place the player needs to reach to win.

Using machinations
to represent a simple,
linear game space

236

Game mechanics: advanced Game desiGn

FIGURe 10.9
a simple space for the
flower-collecting game

In this case, the presence of the player in a certain location unlocks particular
actions. This is a common use of space in a game and works equally well with one
resource to represent a single-player character or multiple resources to represent a
number of units under the player’s control. In fact, we can take into account the
location of resources in a real-time strategy game space by allowing production units
to be moved across the map. Figure 10.10 represents the mechanics of mineral harvesting in the level “The Devil’s Playground” in StarCraft II, including the periodic
destruction of all SCV units in low-lying areas. Note that the distances between
the pools in the diagram do not indicate the physical distance to the resources on
the map. Rather, the lowered effect of SCV units on the production rate for the
resources on the right represents the real distance to the base.
You can use the player’s location in the game to activate certain mechanisms, and
you can also use it the other way around to use the state of the mechanics to make
certain locations accessible. Figure 10.9 illustrates this idea. The goal location is
activated only when the player has collected five or more flowers. Mechanisms that
control the accessibility of certain locations in the game space are typically lockand-key mechanisms. In its simplest form, a lock-and-key mechanism depends on one
binary state: whether or not the player has acquired the correct key. Figure 10.11
adds such a lock-and-key mechanism to the flower-collecting game.

inTeGraT inG LeveL desiGn and mechanics

237

FIGURe 10.10
resource harvesting
on several locations in

FIGURe 10.11
a key mechanism
(green) unlocks access
to extra flowers.

ChAptEr 10

StarCraft II

238

Game mechanics: advanced Game desiGn

can you use machinations as a leVel desiGn tool?
The machinations framework was not set up to explore level design in much detail.
as you can see from the examples, it works better with simple representations of game
spaces, consisting of a handful of pools to represent locations. This is particularly suitable
for point-and-click adventure games, but you will end up duplicating many mechanics
if you are making a more detailed level design. moving units around the map is poorly
supported. still, it can be done, and using machinations can be a good way to explore
and experiment with different structures for game levels. The fact that machinations
forces you to focus on the abstract level structure allows you to try out and implement
ideas much faster than most prototyping techniques would allow, and it makes the interactions among the game space, its mission, and its game mechanics visible.

learning to Play
Part of the level designer’s job is to train the player in the required gameplay skills
necessary to complete the game. Nowadays, players don’t want to read manuals
to play a game; they expect to learn the mechanics as a natural part of playing the
game. This is especially true of casual gamers playing games online or on mobile
devices. This means that you must structure your levels in such a way that they
introduce the mechanics to the players in an incremental, comprehensible progression. In this section, we will discuss two slightly different but compatible
approaches to teaching the mechanics while the player plays the game.

Skill Atoms
In an article entitled “The Chemistry of Game Design” published on the Gamasutra
website, designer Daniel Cook analyzed the way that players learn skills to play
games (2007). He broke his hypothetical game into multiple skill atoms. Each atom
constitutes a step in the learning process and consists of four events:

1. Action. This is the action the player performs, such as pressing a button or
moving a mouse cursor.

2. Simulation. The game responds by applying mechanics and changing its state.
3. Feedback. This is the way the game communicates its state change via output
devices. (Note that this is not positive or negative feedback within the mechanics
but information “fed back” to the player.)

4. Modeling. The player then updates her mental model of the game.

inTeGraT inG LeveL desiGn and mechanics

239

Cook gives an example of these steps in the skill atom that governs jumping in
Super Mario Bros.:

1. Action. The player presses the A button.
2. Simulation. The game moves the player character within its internal model of
the world by applying a jumping force and gravity.

3. Feedback. The player character moves, its animation changes, and the game
plays a jumping sound.

Skill atoms can depend on previously learned skills. Continuing the Super Mario
Bros. example, the player needs to learn how to jump before she can learn that she
can jump onto platforms or that jumping into a certain block will reveal hidden
objects. Linked skill atoms form chains and trees of related skills that can be represented as graphs. For example, a small part of the skill tree for Super Mario Bros. is
depicted in Figure 10.12.
Two important characteristics of a skill tree are its relative width and depth. If a skill
tree is wide, the player must learn many new skills independently of one another.
If a skill tree is deep, it has long chains of skills that depend on each other. In general, it is better to have skill trees that are relatively deep instead of relatively wide,
at least to teach the skills required early in the game. The reason is that the player
can pick up secondary skills (skills that build on other skills in the game) comparatively easily as an addition to something she already knows, whereas primary skills
(skills at the beginning of the chain) must be learned explicitly without the benefit
of any prior experience. For example, when encountering a new and unfamiliar type
of game, the player has two ways of finding out what the primary skills are: She can
look for in-game instructions, or she can simply try random buttons or other available input devices. When she has learned a few primary skills, she will use them to
play the game and will very likely either deduce combinations that work as secondary skills or stumble on those combinations by accident. However, if she missed a
primary skill (for example, she never pressed the button to shoot), she might never
realize that shooting was an option and miss out on an entire branch of the skill tree.
The skill atoms work very well with dexterity-based action games in which each skill
atom maps to mastering the controls to play the game. However, it can be applied
just as easily to more strategic games whose challenges don’t depend on mastery of
the controls. For example, in a turn-based strategy game, skill atoms might include
the player understanding that a cavalry unit is very effective at fighting units of
archers. The steps to learn this skill are similar to any action-based skill atom. The
player needs to perform an action (order cavalry to attack archers), and the game
runs a simulation (decides how effective the attack is) and provides feedback (animations and visual effects to indicate the effectiveness of the attack) that allows the
player to update her mental model (attacking archers with cavalry is effective).

ChAptEr 10

4. Modeling. The player learns that pressing A allows her to jump.

240

Game mechanics: advanced Game desiGn

FIGURe 10.12
a partial skill tree for
Super Mario Bros.

“easy to learn but a liFetime to master”
When we’re teaching a player to play a game, we use tutorials and other methods to
teach some skills explicitly. Other skills, however, the player must learn on her own
through experience. For example, the number of explicit skills in chess is very small—a
few rules about the moves, plus castling, en passant capture, and pawn promotion. But
the number of skills the player must learn implicitly in chess is enormous. designers
characterize this quality of a game with the phrase “easy to learn but a lifetime to
master.” Games that have this quality also tend to have skill trees that are deep instead
of wide. Games that depend on only a few primary skills don’t have to teach players a lot
to get them going. at the same time, the long chains of skills learned through experience
might take a lifetime to master.

inTeGraT inG LeveL desiGn and mechanics

241

hidden inFormation in Games
certain games depend on hiding information from the players. This seems to contradict
the idea that it is important to provide the player with information about changes to the
state of the mechanics. however, there is a subtle difference between being clear about
the game’s state as a whole and being clear about when the state changes. To learn how
a game’s mechanics work, the players need to know when changes occur. a game can
hide its exact state from the player.

Martial Arts learning Principles
Our first approach to learning in games was to define skill atoms and organize them
into skill trees. Our second approach draws on the methods used in karate (and various other Japanese martial arts) training. Students must train in four different stages
to complete every “level” (properly called belts or, in Japanese, dan). These stages,
which build upon one another, are as follows:
Kihon (fundamentals). The student learns to perform an individual technique.
The focus is on getting the technique right.

n

Kihon-kata. The student repeats the new technique endlessly to master it and
perform it without thinking. If you never received martial arts training, you might
recognize this stage from the endless chores the main character in the movie Karate
Kid had to go through (“wax on, wax off”).

n

Kata (form). The student learns how to combine different techniques in a fixed,
choreographed sequence of moves called a kata.

n

Kumite (sparring). To prove his mastery, the student fights his master in a free
fight. For the first few levels, the master will use only a subset of simple and predictable moves, but as the student advances, the master will draw from a wider range of
attacks and use them less predictably.

n

You might recognize these stages in many games. For example, you can apply these
learning stages to Super Mario Bros. and Crash Bandicoot as well:
Kihon. The player gets to practice a new move (such as jump) in a fairly safe
environment. Once she has learned to jump, she is able to move on.

n

Kihon-kata. The move is then repeated several times: The player needs to perform
a series of jumps, often with increasing difficulty. Before long, the player doesn’t
need to think about how to perform a jump or what button to push; she simply
jumps when she needs to jump.

n

ChAptEr 10

many card games hide the exact state of the game while making it quite clear that things
are changing: You can see how many cards other players pick up or discard. By observing
those changes, you may be able to deduce something about the game’s state: the actual
distribution of the cards and whether your hand is better than your opponent’s.

242

Game mechanics: advanced Game desiGn

Kata. During the level the player encounters a series of challenges that require
combinations of moves to overcome. For example, the player needs to jump and
shoot at the same time. At this stage, the movement patterns of enemies tend to
be deterministic and predictable. Once the player finds the right combination of
moves, that combination will work every time (during this stage).

n

Kumite. The learning process is completed with a boss encounter. Boss encounters require the player to use combinations of moves in a free fight. Especially
toward the end of the game, boss behavior gets more and more difficult to predict,
requiring a greater and greater mastery of the moves by the player.

n

Games that use these learning principles often integrate them closely with their
mission structure. Every stage of learning becomes a subtask, or a series of subtasks,
that the player must complete to proceed. This also means that these games put more
emphasis on testing the abilities of the player. To advance past the kihon stage, the
player must prove that she is able to jump. These tests are easy to set up: Simply create
a challenge that the player cannot avoid and that requires her to use the right skill.
During the initial stages, it’s best to keep the levels simple and safe to build player
confidence. During later stages you can increase the risk. These learning principles
work best with fairly linear missions, or at least missions in which you have made
sure that the player can face only tasks from later stages after she has completed the
tasks of the early stages.

FIGURe 10.13 structure of the “Forest Temple” mission

You can find this type of learning structure in the Forest Temple level in The Legend
of Zelda: Twilight Princess. (We also discussed this level in Chapter 2.) In the Forest
Temple level, Link has to overcome many challenges. In the early stages of the
level, he encounters bomblings, small creatures that explode a few seconds after
Link picks them up. His first task (kihon) with the bombling is to use it to destroy a
large carnivorous plant that prevents him from reaching the next dungeon room.
After that, he needs to repeat similar moves a couple of times (kihon-kata) to blast
walls. When Link gains the Gale Boomerang, he learns to use the boomerang to flip
special switches and pick up distant items over a series of simple tests (kihon and
kihon-kata). These tests require that the player demonstrate that he is able to direct
the boomerang toward a particular sequence of targets. Near the end of the level,
Link must use the boomerang to pick up distant bomblings and deliver them to
another carnivorous plant (kata). This prepares Link to use the same technique to
fight and defeat the level boss (kumite). Figure 10.13 illustrates the structure of the
mission and the locations of the learning stages within it. In this figure, the boxes
represent tasks, and arrows indicate dependencies between tasks: A task is available
only when the player has completed all the tasks that lead into it. Note that it omits
many details to concentrate on the mission’s structure. (You can see a map of the
spatial layout of the level in Figure 2.3.)

243

ChAptEr 10

inTeGraT inG LeveL desiGn and mechanics

244

Game mechanics: advanced Game desiGn

You can find a similar structure in the second dungeon of the game, the Goron
Mines. To gain access to this dungeon, Link must acquire the Iron Boots, an item
that he can equip to make himself very heavy, and must demonstrate how to use
it (kihon). The dungeon trains the player in the various applications of this item: to
sink to the bottom of bodies of water, to walk on vertical or upside-down stretches
of magnetic rock, and to fight heavy and strong creatures (kihon-kata). Halfway
through the dungeon, Link acquires the hero’s bow and has to use it to open several
pathways by shooting at targets (kihon, kihon-kata). During this stage, he engages in
several fights in which the player must switch in and out of his boots quickly and
combine it with archery and sword fighting (kata). Finally, the player must combine
all three skills to defeat the level boss (kumite). In fact, this structure is repeated for
all dungeons in Twilight Princess. Figure 10.14 shows an overview of the mechanisms that are introduced during each dungeon and each intermission between
dungeons. It shows that the game slowly introduces new mechanisms over its entire
course and focuses on a different combination of mechanisms for each level. It is
a very fine example of using levels to structure a smooth learning curve and create
prolonged and varied gameplay. You can use such a chart to plan the learning stages
of your own games as well as to analyze published games.

Summary
In this chapter, we examined the ways that game mechanics interact with level
design. We noted four different ways of measuring progress through a game:
through completed tasks, through advancement toward a numerical goal, through
character growth, and through growth in the player’s own abilities. We showed
how it is possible to use a subset of all your core mechanics to create a specific level,
using our Lunar Colony game as an example. In the section “Missions and Game
Spaces,” we introduced an important distinction between the structure of a level’s
mission, or sequence of tasks to be performed, and its physical layout. You can use
Machinations diagrams to help you design both. The chapter ended with a discussion of the ways in which players learn to play games and how cleverly designed
games always prepare a player well for what is to come. The Legend of Zelda: Twilight
Princess serves as an ideal example.
In the next chapter, we will study progression mechanisms in games, especially the
lock-and-key mechanism, in more detail.

inTeGraT inG LeveL desiGn and mechanics

FIGURe 10.14 The introduction and focus of mechanisms in The Legend of Zelda: The Twilight Princess

245

ChAptEr 10

246

Game mechanics: advanced Game desiGn

Exercises
1. Review the Machination diagrams you made for earlier designs. Look for a diagram
that allows you to focus on different structures that can serve as a starting point for
different levels. Create a sequence of at least three different levels of ascending difficulty, simply by leaving out certain parts and changing the end conditions.

2. Examine either of the following games: Knytt Stories (http://nifflas.ni2.se/?page=
Knytt+Stories) or Robot Wants Kitty (www.maxgames.com/play/robot-wants-kitty.html).
Analyze how these games have structured their levels and how they train the players
in playing the game. What are the differences between the structure of these games’
mission and game space? What are the skills the player learns while playing, and
how are these skills linked and combined?

ChAptEr 11
progression
Mechanisms
In Chapter 10, “Integrating Level Design and Mechanics,” we focused on the structural features of levels on a large scale. In this chapter, we examine the mechanisms
that drive progression and that can be used to structure levels. We don’t restrict ourselves to the traditional mechanisms found in games of progression, but we look for
ways to apply what we’ve learned from studying emergent gameplay to the mechanisms of progression.

ChAptEr 11

Our goal is to find more emergent mechanisms of progression than commercial video
games typically use, and we consider two different approaches. In the first half of
this chapter, we investigate traditional lock-and-key mechanisms and identify
ways to make them more dynamic. In the second half of the chapter, we abandon
the conventional view of progression in terms of the player character’s movement
through a level and toward a goal location, and instead we frame the notion of
progression in more abstract terms: changing the state of the game toward a goal
state. This perspective allows us to go beyond the common design strategies found
in contemporary games and speculate about emergent progression, an approach
that might bridge the gap between Jesper Juul’s games of progression and games
of emergence.

lock-and-key Mechanisms
Games that feature many levels often rely on lock-and-key mechanisms to control
the player’s progress through each level. In some cases, these mechanisms are
described as actual locks and keys. For example, in Doom, the player can find a red,
yellow, and blue keycard in most levels to open red, yellow, and blue doors. In The
Legend of Zelda, Link typically uses small keys to open doors and needs to find the
master key to unlock the door that leads the final boss of that level. However, we
use the term lock-and-key mechanism to refer to any mechanism that controls access
to parts of a level. In the original Adventure, a snake blocked the player’s path at one
point (it was the lock), and it could be driven away only by releasing a bird from a
cage (the key). The Legend of Zelda frequently uses other things that the player needs
to collect as keys: the monkeys, bomblings, and the boomerang in the Forest Temple
are all good examples.

247

248

Game mechanics: advanced Game desiGn

General design wisdom dictates that it is usually preferable to have the player find
the lock before he finds the key. There are three reasons for this:
If the player generally encounters the keys before the locks, he develops the habit
of collecting everything that he encounters without discrimination, just in case it
might be a key that will be needed later. This makes for simplistic gameplay. When
the player encounters a lock, rather than going to look for a suitable key, he tries
everything in his inventory. Older adventure games tended to exhibit this weakness.

n

When a lock (obstacle) doesn’t look like a real lock and its key (solution) doesn’t
look like a real key, it is easier for the player to recognize the key if he has seen the
lock first. Upon finding the key, the player usually can often guess its function and
will actively formulate the intention to return to the lock. This makes the player’s
role more active than simply reacting to whatever task the game throws at him. It is
also more likely to make the player feel smart because he figured it out himself.

n

When players can negotiate obstacles they were unable to get past earlier, they
experience progress and accomplishment. There may have been obstacles he could
not overcome, but he now has the power to do so. (You have to be careful not to
frustrate your player too much, however; young children and casual players are less
tolerant of obstructions than more experienced ones.)

n

It is not always possible to guarantee that the player will find the lock before the
key; it depends on the topology of the space that he’s exploring. If the world is
largely open and the player has the freedom to roam at will, then he may well find
the key before the lock, although he may not recognize it as a key. We discuss lockand-key mechanisms in the context of game spaces in the next section.

T I P in our illustrations
of game spaces in this
chapter, the green
objects are enemies,
and the large one next
to a treasure chest
is a boss enemy. The
player’s character is
not visible but enters
the level through the
arched door from the
outside. The colors of
the keys match the
colors of the locks
they open.

Mapping Missions to Game Spaces
Lock-and-key mechanisms help the game designer to map missions onto spaces.
(Remember that mission in this context refers to the collection of tasks required to
complete a level.) As we saw in the previous chapter, game missions can be quite
linear, especially in levels in which the player still is learning the basic mechanics
of the game. At best, a mission allows a few alternative tasks for the player to work
on. Again, the structure of the mission of the Forest Temple level (Figure 10.13) is a
good example. In the most extreme case, a mission might be completely linear (Figure
11.1), but mapping such a mission to a physically linear game space is seldom the
best option. Lock-and-key mechanisms allow a different way to map a linear mission to a nonlinear game space (Figure 11.2): It allows the designer to move the
lock forward (closer to the level’s entry point). In theory, it also allows the designer
to move the lock backward, but because, as we already argued, it is better to have
the lock before the key, moving the lock forward makes the most sense.

PrOGressiOn mechanisms

249

FIGURe 11.1
mapping a linear
mission to a linear
game space. note that
acquiring the sword
will help defeat the big
boss at the end.

FIGURe 11.2

ChAptEr 11

Using locks and
keys to map a linear
mission to a nonlinear
game space

Despite the addition, the solution to the level in Figure 11.2 is still always the same.
Any player playing it must perform the same tasks in the same order. To create more
variation and provide the player with a choice to make, many games use multiple
keys to unlock a single door (Figure 11.3). The monkeys in the Forest Temple offer a
good example of that construction.

FIGURe 11.3
Using multiple keys to
unlock a single door

250

Game mechanics: advanced Game desiGn

We can also do the converse and give the player a single key to unlock multiple
doors. The boomerang in the Forest Temple serves this purpose. Unfortunately, it
cannot be used to reorder the game space directly, because this potentially cuts the
level short and creates a problem for the player (Figure 11.4). The trick to create
multiple locks for a single key, and still place those locks before the key, is to add
extra lock-and-key mechanisms (Figure 11.5) or to mirror the multiple locks mechanism with a multiple keys mechanism (Figure 11.6).

FIGURe 11.4
Poor use of a single
key that opens multiple
locks: The player might
encounter the boss
before she finds the
sword.

FIGURe 11.5
combining multiple
locks for a single
key with an additional lock-and-key
mechanism

PrOGressiOn mechanisms

251

FIGURe 11.6
multiple locks for a
single key with multiple keys for a single
lock

Lock-and-key mechanisms are more common in games than actual locks and keys;
most lock-and-key mechanisms are characterized as something else, such as switches
or a permanent power-up that allows the player to smash down particular doors.
It is a common game design strategy to control a player’s progress by granting her
permanent abilities that act as keys. For example, in a platform game, gaining
the ability to double jump allows the player to cross wider gaps and reach higher
platforms than before. Devising clever lock-and-key mechanisms that are closely
integrated to the core gameplay is an important aspect of the level designer’s job.
Because gameplay is created by mechanics, you must invent locks and keys that are
based upon, or interact with, the game’s core mechanics. For example, if the game
is about jumping, special jumping abilities should function as keys. If it is a game
about sword fighting, you should look for ways to create keys for special sword
fighting abilities, and so on.
One difficulty with using permanent abilities as keys is that it creates a single key
used for multiple locks. As we explained in the previous section, that type of construction isn’t always easy to use. If you want the player to encounter a number
of locks before finding the key, you have to be careful that you don’t accidentally
create a lot of unintended shortcuts. At the same time, the player needs to be able
to clearly see that an area is locked (rather than just difficult to access). One way
to create many locks that the player passes on her way to the key is to have these
locks lead to bonus tasks and rewards that do not affect the game too much, but just
enough to feel rewarding to exploration-minded players.

ChAptEr 11

Using Abilities as Keys

252

Game mechanics: advanced Game desiGn

Creating key mechanisms from player abilities, rather than from game world objects,
also has advantages. You can combine these actions in interesting ways with each
other and with other elements in the game. For example, a double jump might be
the key to cross a wide gap, or to avoid creatures that are too tall to jump over with
a single jump. Being able to identify possible combinations of mechanisms in the
game that you can use to create locks and keys to structure your levels is a very useful skill. It allows you to get the most out of a game’s mechanics and lets you to
create varied gameplay efficiently.

desiGn challenGe
how many different ways can you think of to use a sword as a key in a lock-and-key
mechanism? (don’t design a level; just think of alternative uses for swords.)

lock-and-Key Machinations
In Chapter 6, “Common Mechanisms,” we showed you how you can use
Machinations diagrams to represent lock-and-key mechanisms: A key mechanism
often is a simple state change that unlocks new areas in the game space. Its essential
structure is represented by Figure 11.7.

FIGURe 11.7
a simple lock-and-key
mechanism (blue) to
control progression
through a space (black)

This structure has a weakness, however. The game can be in only one of two states:
Either the player has the key or he doesn’t have it. There is little room for dynamic
behavior. The Machinations diagram reveals that simplicity. The mechanism is built
from two pools and based on a resource (the key) that can move in only one direction (into the inventory). One consequence of this is that the player can never put
the key down. Many games implement this system deliberately so that the player
can never accidentally leave a critical key behind—The Longest Journey is a wellknown example.
Even if we look at typical variations found on locks and keys, the mechanics do not
get much more complex or dynamic. A few examples include nested locks, such as
when a nonplayer character requires the player to undertake several quests before
providing a key; multiple keys for a single lock (Figure 11.8); or keys that are consumed when they open a door (such as the mysteriously disappearing small keys in

PrOGressiOn mechanisms

253

The Legend of Zelda, as in Figure 11.9). Note that in the case of a consumable key,
the player might be forced to choose between two directions because she cannot
unlock both doors with a single key. In the case of Figure 11.9, the “level” will
always be solvable because behind lock B, there is another key, and once a door is
unlocked, the player cannot “spend” a key to unlock it again.

FIGURe 11.8
a lock requiring multiple keys to open

FIGURe 11.9

ChAptEr 11

Keys that are consumed upon use

If we want to involve player skill, rather than simply the presence or absence of
a player ability, we need a different mechanism. In games like Fallout 3 and The
Elder Scrolls: Skyrim, the player uses lockpicks to try to open locks. There is a chance
the lockpick will break, and the player will fail. In these games, the chance of failure
depends on the skills of the player and the attributes of his character. Lockpicks
are a consumable resource, and if it is vital that the player get past a certain lock in
this manner, the game must ensure that she has an unlimited source of lockpicks.
Figure 11.10 represents this type of lock-and-key mechanism.

FIGURe 11.10
skill-based lock-andkey mechanism

254

Game mechanics: advanced Game desiGn

In The Legend of Zelda, the bow and arrow can be used to open doors by shooting
distant switches. The mechanism (Figure 11.11) combines a skill-based lock with
