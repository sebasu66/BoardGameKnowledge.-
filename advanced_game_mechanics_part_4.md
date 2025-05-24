survive and produce offspring causing their population to rise again.
This particular balance between predators and prey in an ecosystem is attributed
to what is called a feedback loop. A feedback loop is created when the effects of a
change in one part of the system (such as the number of predators) come back and
affect the same part at a later moment in time. In this case, an increase of the number of predators will cause a decrease of prey, which in turn will cause a subsequent
decrease of predators. The effects of the changes to the predator population size are
quite literally fed back to the same population size.

ChAptEr 3

Tower Defense:
Lost Earth HD

52

Game mechanics: advanced Game desiGn

Feedback loops that work to maintain a balance within a system are called negative
feedback loops. Negative feedback loops are commonly used in the design of electrical
appliances. A thermostat is a typical example: A thermometer detects the temperature of the air, and when it becomes too low, it will activate a heater. The heater
will then cause the temperature to rise, which in turn will cause the thermostat to
turn the heater off again. A speed governor on a machine is another: When the
machine speeds up (perhaps because the load on it has been reduced), the governor
reduces the machine’s power source to make it slow down. When the machine slows
down, the governor increases the power source to make it speed up. This keeps the
machine’s speed constant. Speed governors are used to ensure that a machine works
at its most efficient rate of speed and cannot run dangerously fast if the load on it is
suddenly removed.
Negative feedback is frequently found in games. For example, in Civilization
(Figure 3.4), the population of a city is affected by negative feedback that is not
unlike the predator/prey example. As your cities grow, the growing population
demands more and more food. This causes the city to grow to a stable size that is
supported by the terrain and the player’s current level of technology.

FIGURe 3.4
Civilization V showing
population and food
supply of the city
of Thebes

cOmPLex sYsTems and The sTrUcTUre OF emerGence

53

The opposite of a negative feedback loop is, unsurprisingly, called a positive feedback
loop. Instead of creating balance by acting against the changes that activated the
feedback loop, a positive feedback loop will strengthen the effects that caused it.
Audio feedback is a good example: A microphone picks up a sound, an amplifier
amplifies it, and speakers reproduce the original sound louder. The microphone
then picks up the new sound from the speakers, which gets amplified again, and
so on. The result is a high-pitched shriek that can be stopped only by moving the
microphone away from the speakers.
Positive feedback is also frequently found in games. For example, if you take one
of your opponent’s pieces in a game of chess, it becomes easier to take another one
because now you have more pieces than your opponent. Positive feedback creates
volatile systems that can change quickly.
We will be discussing feedback extensively throughout this book. In most games of
emergence, several different feedback loops operate at the same time. For now, it is
important to remember that in complex systems feedback loops can exist. Negative
feedback loops work toward maintaining a balance in the system, while positive feedback loops can destabilize the system.

Different behavioral Patterns emerge at Different Scales

n

A live cell that has fewer than two live neighbors dies from loneliness.

n

A live cell that has more than three live neighbors dies from overcrowding.

n

A live cell that has two or three live neighbors stays alive.

n

A dead cell that has exactly three live neighbors becomes alive.

To start the Game of Life, you need to set up a grid and choose a number of cells
that are initially alive. An example of the effects that emerge from applying these
rules is depicted in Figure 3.5. However, to really appreciate the emergent behavior
of the Game of Life, we advise you to take a look at one of the many interactive
versions available online.

ChAptEr 3

Stephen Wolfram was not the only mathematician to study cellular automata.
Probably the most famous cellular automaton was invented by John Conway and
is called the Game of Life. Conway’s automaton consists of cells that are laid out on
a two-dimensional grid. In theory, this grid goes on indefinitely in all directions.
Each cell on the grid has eight neighbors: the cells that surround it orthogonally
and diagonally. Each cell can be in two different states: It is either dead or alive. In
most examples, dead cells are rendered white, while live cells are colored black. Each
iteration the following rules are applied to each cell:

T I P You can download an open-source,
cross-platform version
of the Game of Life at
http://golly.sourceforge.
net. Wikipedia’s entry,
“conway’s Game of
Life,” includes links to
a number of other versions available online.

54

Game mechanics: advanced Game desiGn

FIGURe 3.5
a few iterations of the
Game of Life
Step 0

Step 1

Step 2

Step 3

Step 4

Step 5

Step 6

When set into motion, the Game of Life usually has quite chaotic results, with a lot
of activity exploding from its original live cells. Frequently after a number of iterations the Game of Life settles in a more or less stable configuration, sometimes with
a few groups of cells that oscillate between two states.
One of the earliest questions that the researchers studying the Game of Life asked
themselves was this: “Is there an initial configuration of live cells that expands forever?” They quickly started finding configurations that showed some surprising
behavior. One of those configurations is called a glider. It is a group of five live cells
that replicates itself one tile away after four iterations. The effect of a glider is that
of a little creature that moves across the grid (Figure 3.6). More interesting patterns
were found, such as a glider gun, a pattern that stays in one place but produces new
gliders that move off every 30 iterations.

FIGURe 3.6
a glider in the Game
of Life

Step 0

Step 1

Step 2

Step 3

Step 4

Gliders and glider guns show that in complex systems the most interesting behavior
takes place not at the scale of the individual parts but at the scale of groups of parts.
This is something that can be observed in many other complex systems as well. The
flocking of birds is a good example. A flock of birds moves as one; the group as a
whole seems to have a distinctive shape, direction, and purpose (Figure 3.7). In this
case, the “rules” that steer the birds operate on both scales. Flocking can be simulated by having individual birds balancing their movement between moving toward
the center of the group, matching speed and direction with their neighbors, and
avoiding getting too close to their neighbors.

cOmPLex sYsTems and The sTrUcTUre OF emerGence

55

FIGURe 3.7

In games, we see similar effects. Over the years players have wondered if the ghosts
in Pac-Man are deliberately teaming up against the player and laying traps to catch
the player. In fact, the ghosts do not collaborate, and their collective behavior appears
to be much smarter than it actually is. The ghosts in Pac-Man are simple machines
that follow simple rules. The game alternates between two states: scatter and chase.
In the scatter state, the ghosts do not hunt the player, but each seeks out a different
corner of the maze. Most of the time, however, the game is in the chase state, when
the ghosts hunt the player. To hunt the player, the ghosts have to make a decision
at each intersection in the maze. The algorithm that is used chooses the direction
that brings the ghost closer to the player. It simply ignores any walls between the
ghost and the player. Their behavior is implemented just a little differently for every
ghost: Blinky (the red ghost) tries to go the player’s current position; Pinky (the
pink ghost) tries to go to a position four tiles ahead of the player; Inky (the blue
ghost) combines the player’s position and the position of Blinky to determine where
to go; and finally Clyde (the orange ghost) chases the player when he is far away
but tries to get to lower-left corner of the maze when he gets close. Together, the
effects of the movements seem surprisingly smart: Blinky will follow the player
while Pinky and Inky try to get ahead of the player, and Clyde adds in some noise.
As a group, the ghosts are fairly effective hunters even with no knowledge of where
the others are actually located. This combination of simple behaviors gives players
the impression they are being hunted collaboratively, when they simply have complementary strategies.

ChAptEr 3

Flocking birds

T I P For an extended
discussion of the
ghost’s behavior in
Pac-Man, see http://
gameinternals.com/
post/2072558330/
understanding-pacmanghost-behavior.

56

Game mechanics: advanced Game desiGn

Categorizing emergence
Scientists distinguish among various levels of emergence in a complex system. Some
effects are more emergent than others. Feedback loops and the different scales that
exist within a complex system together go a long way to describe and explain different levels of emergence. In his paper “Types and Forms of Emergence,” scientist
Jochen Fromm uses feedback and scales to build the following taxonomy of emergence (2005).
In the simplest form, nominal or intentional emergence, there is either no feedback or
feedback only between agents on the same level of organization. Examples of such
systems include most man-made machinery where the function of the machine is
an intentional (and designed) emergent property of its components. The behavior
of machines that exhibit intentional emergence is deterministic and predictable but
lacks flexibility or adaptability. A speed governor and a thermostat are examples of
this type of predictable feedback.
Fromm’s second type of emergence, weak emergence, introduces top-down feedback
between different levels within the system. He uses flocking to illustrate this type of
behavior. A bird reacts to the vicinity of other birds (agent-to-agent feedback) and at
the same time perceives the flock as a group (group-to-agent feedback). The entire
flock constitutes a different scale from the individual birds. A bird perceives and
reacts to both. This behavior is not confined to birds; schools of fish behave similarly. Flocking can be generalized to any kind of unit capable of perceiving both its
immediate surroundings and the state of its group as a whole.
One step up the complexity ladder from weakly emergent systems are systems that
exhibit multiple emergence. In these systems, multiple feedback traverses the different
levels of organization. Fromm illustrates this category by explaining how interesting emergence can be found in systems that have short-range positive feedback
and long-range negative feedback. The stock market exhibits such behavior. When
stocks are going up, people begin to notice and to buy more, driving the price up
further (short-term positive feedback). People also know from experience that the
stock will eventually reach a peak, and they make plans to sell the stock when they
believe it has reached its peak, thus driving the price down (long-term negative feedback). The phenomenon works in reverse, too: People will sell a stock when they see
it dropping but buy later when they think it has reached bottom and is a bargain.
John Conway’s Game of Life also exhibits this type of emergence. The Game of Life
includes both positive feedback (the rule that governs the birth of cells) and negative feedback (the rules that govern the death of cells). The Game of Life also shows
different scales of organization: At the lowest end there is the scale of the individual
cells; on a higher level of organization, you can recognize persistent patterns and
behaviors such as gliders and glider guns.

cOmPLex sYsTems and The sTrUcTUre OF emerGence

57

Fromm’s last category is strong emergence. His two main examples are life as an emergent property of the genetic system and culture as an emergent property of language
and writing. Strong emergence is attributed to the large difference between the
scales on which the emergence operates and the existence of intermediate scales
within the system. Strong emergence is multilevel emergence in which the outcome
of the emergent behavior on the highest level can be separated from the agents on
the lowest level in the system. For example, it is possible to set up a grid of the cells
used for the Game of Life in such a way that on a higher level it acts as a computer
able to perform simple computations and from which new complex systems (such
as games) can be built. In this case, causal dependency between the behavior displayed by the computer and the Game of Life itself is minimal.
These categories suggest that in games different levels of emergent behavior also
exist, often at the same time. More importantly, it also shows that structural characteristics of the game’s mechanics (such as feedback loops and the existence of
different scales) play a vital role in the emergence of complex and interesting
behavior.

Games are complex systems that can produce unpredictable results but must deliver a
well-designed, natural user experience. To achieve this, game designers must understand the nature of emergent behavior in general and of their game in particular.
We regard the many active and interconnected parts, feedback loops, and different
scales as structural qualities of the game as a system. In games, these structural qualities
play a vital role in the creation of emergent gameplay. Studying game mechanics
will reveal these (and other) structures in much more detail. The rest of this book is
dedicated to this study.
The three structural qualities that were the main subject of this chapter are also the
first stepping-stones toward the construction of an applied theoretical framework
called Machinations that deals with emergence in games head-on. The Machinations
framework allows you, as a game designer, to get a better grip on the elusive process
of building quality games displaying emergent behavior. In the following chapters, we
will zoom in on the game mechanics of the internal economy. We’ll explain how
the Machinations framework can be used to visualize game mechanics and how structural qualities of the mechanics can be read from these visualizations. In Chapter 10,
“Integrating Level Design and Mechanics,” and Chapter 11, “Progression Mechanisms,”
we will zoom out and show how on a larger scale mechanics can be grouped and
used to design interesting levels that use both progression and emergence.

ChAptEr 3

Harnessing Emergence in Games

58

Game mechanics: advanced Game desiGn

Summary
In this chapter, we discussed the definition of complex systems and showed how
gameplay emerges from them. We described the continuum between strictly ordered
systems and entirely chaotic ones and showed that emergence takes place somewhere between the two. Three structural qualities of complex systems contribute
to emergence: active and interconnected parts; feedback loops; and interaction at
different scales.
We used cellular automata as an example of simple systems that can produce emergence, and we described how tower defense games work like cellular automata.
Finally, we introduced Fromm’s categories of emergence, which are produced by
different combinations of feedback loops and interactions among the parts of a
system at different scales.

Exercises
1. Revise some of Wolfram’s rules as shown in Figure 3.2 so that some of the eight
possible combinations shown produce a different outcome from Wolfram’s original.
Using graph paper and a pencil, start with a single occupied cell and apply your new
rules repeatedly down the page. How do the results differ from the ones in the
figure?

2. Conway’s Game of Life is set on a rectangular grid and uses rules that modify a
cell based on the state of the eight cells around it. On a hexagonal grid, each cell has
six neighbors rather than eight, and on a triangular grid, each cell has only three
neighbors. Try devising Game of Life–like rules for a hexagonal or triangular grid
and see what results you get.

ChAptEr 4
Internal Economy
In real life, an economy is a system in which resources are produced, consumed, and
exchanged in quantifiable amounts. Many games also include an economy, consisting of the resources the game manipulates and the rules about how they are
produced and consumed. However, in games, the internal economy can include all
sorts of resources that are not part of a real-life economy. In games, things like health,
experience, and skill can be part of the economy just as easily as money, goods, and
services. You might not have money in Doom, but you do have weapons, ammunition,
health, and armor points. In the board game Risk, your armies are a vital resource that
you must use and risk in a gambit to conquer countries. In Mario Galaxy, you collect
stars and power-ups to gain extra lives and to get ahead in the game. Almost all genres
of games have an internal economy (see Table 1.1 in Chapter 1 for some more examples), even if it does not resemble a real-world economy.
To understand a game’s gameplay, it is essential to understand its economy. The
economies of some games are small and simple, but no matter how big or small
the economy is, creating it is an important design task. It is also one of the few
tasks that belongs exclusively to the designer and no one else. To get game physics right, you need to work closely with the programmers; to get a level right, you
need to work closely with the story writers and level designers; but you must design
the economy on your own. This is the core of the game designer’s trade: You craft
mechanics to create a game system that is fun and challenging to interact with.
In Fundamentals of Game Design, Ernest Adams discussed the internal economy of
games. The discussion in this book repeats some of those points and expands the
notion of internal economy.

NOT E We use a
very broad definition
of the word economy.
it’s not just about
money! in an information economy, there are
data producers, data
processors, and data
consumers. Political
economy studies the
way that political forces
influence government
policies. economies
about money are called
market economies.
But we use the term
in a more abstract way
to refer to any kind
of system in which
resources—of any
type—can be produced, exchanged,
and consumed.

Elements of Internal Economies
In this section, we briefly introduce the basic elements of game economies: resources,
entities, and the four mechanics that allow the resources to be produced, exchanged,
and consumed. This is only a summary; if you need a more in-depth introduction,
please see Chapter 10, “Core Mechanics,” in Fundamentals of Game Design.

59

ChAptEr 4

In Chapter 1, we listed five types of mechanics that you might find in a game:
physics, internal economy, progression mechanisms, tactical maneuvering, and
social interaction. In this chapter, we’ll focus on the internal economy.

60

Game mechanics: advanced Game desiGn

Resources
All economies revolve around the flow of resources. Resources refer to any concept
that can be measured numerically. Almost anything in a game can function as a
resource: money, energy, time, or units under the player’s control all are examples
of resources, as are items, power-ups, and enemies that oppose the player. Anything
the player can produce, gather, collect, or destroy is probably a resource of some
sort, but not all resources are under the player’s control. Time is a resource that normally disappears by itself, and the player usually cannot change that. Speed is also
a resource, although it is generally used as part of a physics engine rather than part
of an internal economy. However, not everything in a game is a resource: platforms,
walls, and any other type of inactive or fixed-level features are not resources.
Resources can be tangible or intangible. Tangible resources have physical properties
in the game world. They exist in a particular location and often have to be moved
somewhere else. Examples include items the avatar carries around in an inventory
or trees that can be harvested in Warcraft. In a strategy game, the player’s units are
also tangible resources that must be directed through the world.
Intangible resources have no physical properties in the game world—they do not
occupy space or exist in a particular location. For example, once the trees in
Warcraft have been harvested, they are changed into lumber, which is intangible.
Lumber is just a number—it doesn’t exist in a location. The player doesn’t need to
physically direct lumber to a site to build a new building. Simply having the right
amount of lumber is enough to start building, even if the building is constructed far
away from the location where the lumber was harvested. Warcraft’s handling of trees
and lumber is a good example of how games can switch between tangible and intangible treatments of resources. Medical kits (tangible) and health points (intangible)
in shooter games are another example.
Sometimes it is useful to identify resources as either abstract or concrete. Abstract
resources do not really exist in the game but are computed from the current state
of the game. For example, in chess you might sacrifice a piece to gain a strategic
advantage over your opponent. In this case, “strategic advantage” can be treated
as an abstract resource. (Abstract resources are intangible too—obviously, “strategic
advantage” is not a thing stored in a location.) Similarly, the altitude of your avatar
or units can be advantageous in a platform or strategy game; in this case, it might
make sense to treat altitude as a resource, if only as a way of factoring it into the
equation for the strategic value of capturing particular positions. The game normally does not explicitly tell the player about abstract resources; they are used only
for internal computation.

inTernaL ecOnOmY

61

Note that in video games some resources that might appear to be abstract are in
fact quite concrete. For example, experience points are not an abstract resource in a
role-playing game. Instead, they are an intangible, but real, commodity that must
be earned and (sometimes) spent like money. Happiness and reputation are two more
resources used by many games that, although they are intangible, are nevertheless
concrete parts of the game.
To design a game’s internal economy or to study the internal economy of an existing game, it is most useful to start identifying the main resources and only then
describe the mechanisms that govern the relationships between them and how they
are produced or consumed.

entities
Specific quantities of a resource are stored in entities. (If you are a programmer, an
entity is essentially a variable.) A resource is a general concept, but an entity stores
a specific amount of a resource. An entity named “Timer,” for example, stores the
resource time—probably the number of seconds remaining before the end of the
game. In Monopoly, each player has an entity that stores available cash resources.
As the player buys and sells, pays rent and fines, and so on, the amount of cash in
the entity changes. When a player pays rent to another player, cash flows from the
first player’s entity to the second player’s entity.
Entities that store one value are called simple entities. Compound entities are groups
of related simple entities, so a compound entity can contain more than one value.
For example, a unit in a strategy game normally includes many simple entities that
describe its health, damage capability, maximum speed, and so on. Collectively,
these make up a compound entity, and the simple entities that make it up are known
as its attributes. Thus, a unit’s health is an attribute of the unit.

Economies commonly include four functions that affect resources and move them
around. These are mechanics called sources, drains, converters, and traders. We describe
them here. Again, this is a summary; for further details, see Chapter 10 of Fundamentals
of Game Design.
Sources are mechanics that create new resources out of nothing. At a certain
time, or upon certain conditions, a source will generate a new resource and store it
in an entity somewhere. Sources may be triggered by events in the game, or they
may operate continuously, producing resources at a certain production rate. They
may also be switched on and off. In simulation games, money is often generated
by a source at intervals, with the amount of money created proportional to the
population. As another example, some games that involve combat automatically
regenerate health over time.

n

ChAptEr 4

Four economic Functions

62

Game mechanics: advanced Game desiGn

Drains are the opposite of sources: They take resources out of the game, reducing the amount stored in an entity and removing them permanently. In simulation
games in which it is necessary to feed a population, the food is drained at a rate proportional to the population. It does not go anywhere or turn into anything else; it
simply disappears. In shooter games, ammunition is drained by firing weapons.

n

Converters turn resources of one kind into another. As we mentioned, in
Warcraft, trees (a tangible resource) turn into lumber (an intangible one) when the
trees are harvested. The act of harvesting is a converter mechanic that converts trees
into lumber at a specific rate: A given number of trees will produce a given amount
of lumber. Many simulation games include technology upgrades that enable players
to improve the efficiency of the converter mechanics in the game, causing them to
produce more of the new resource from the old one.

n

Traders are mechanics that move a resource from one entity to another, and
another resource back in the opposite direction, according to an exchange rule. If
a player buys a shield from a blacksmith for three gold pieces, the trader mechanic
transfers the gold from the player’s cash entity to the blacksmith’s and transfers the
shield from the blacksmith’s inventory to the player’s. Traders are not the same as
converters. Nothing is created or destroyed; things are just exchanged.

n

Economic Structure
It is not particularly difficult to identify the entities and the resources that comprise
an economy, but it is harder to get a good perspective on the system as a whole. If
you were to make graphs of the elements in your economy, what shapes would the
graphs reveal? Is the amount of a given resource increasing over time? How does the
distribution of resources change? Do resources tend to accumulate in the hands of
a particular player, or does the system tend to spread them out? Understanding the
structure of your economy will help you find the answers.

economic Shapes
In the real world, people represent features of an economy with charts and figures
(Figure 4.1). These graphs have a few interesting properties. At the small scale, their
lines move chaotically, but at larger scales, patterns become visible. It is easy to see
whether a line is going up or down in the long run and to identify good and bad
periods. In other words, we can recognize and identify distinctive shapes and patterns from these types of charts.

inTernaL ecOnOmY

Wall Street Crash on the Dow Jones Industrial Average, 1929

63

FIGURe 4.1

400

Graph of the stock
market crash leading to
the Great depression.
most movement is
chaotic, but the crash
is clearly visible.

300

200

100

Oct

Jan

Apr

Jul

1929

Oct

Jan

Apr

Jul

Oct

1930

We can draw similar charts displaying the fortunes of players in a game. As you will
see, distinctive shapes and patterns emerge from the internal economy of a game.
However, there is no one shape that identifies quality gameplay. What constitutes
good gameplay depends on the goals you set for your game and the context that
surrounds it. For example, in one game you might want the player to struggle for a
long time before managing to come out on top (Figure 4.2). In another, you might
aim for quick reversals in fortune and a much shorter play-through (Figure 4.3).

FIGURe 4.2

ChAptEr 4

a long game in which
the player triumphs
after an extended
struggle against a
powerful opponent

64

Game mechanics: advanced Game desiGn

FIGURe 4.3
a short game with
quick reversals of
fortune

The Shape of a Game of Chess
We can take the development of players’ fortunes in a game of chess as a basis for
studying shapes in game economies. In chess, the important resources are the players’
pieces. Chess players (and computer chess programs) assign a point value to each
piece depending on what kind it is. For example, in one system, pawns are worth
one point, rooks five, and the queen nine. Adding up the value of all the pieces one
player has on the board produces a number called material. Players use their pieces
to maneuver on the board to gain strategic positions. Strategic advantage can be
measured as an abstract resource in the game. Figure 4.4 depicts what might be the
course of play between two players in a game of chess.

FIGURe 4.4
The course of a particular game of chess.
The color of a line indicates the color of the
player it refers to.

inTernaL ecOnOmY

65

You can discover a few important patterns in this chart. To start with, the long-term
trend of both players’ main resource (material) is downward. As play progresses,
players will lose and sacrifice pieces. Gaining material is very difficult. In chess, the
only way to gain a piece is to bring a pawn to the other side of the board to be promoted to another, stronger piece, which would lead to an increase of material. This
is a rare event that usually initiates a dramatic change of fortune for the players. If
we consider only the material, chess appears to be a battle of attrition: Players who
can make their material last longest will probably come out on top.

A game of chess generally progresses through three different stages: the opening, the
middle game, and the endgame. Each stage plays a particular role in the game and is
analyzed differently. The opening usually consists of a sequence of prepared and
well-studied moves. During the opening, players try to maneuver themselves into a
position of advantage. The endgame starts when there are relatively few pieces left,
and it becomes safer to involve the king in the game. The middle game falls somewhere between the opening and the endgame, but the boundaries between the stages
are not clear. These three stages can also be identified from the economic analysis in
Figure 4.4. During the opening, the number of pieces decreases only slowly, while
both players build up strategic advantage. The middle game starts when players are
exploiting their strategic advantage to take their opponents’ pieces; it is characterized
by a sharper decline of material. During the endgame, the material stabilizes again
as the players focus on their final attempts to push the strategic advantage to a win.

From Mechanics to Shapes
To produce a particular economic shape, you need to know what type of mechanical structures create what shapes. Fortunately, there is a direct relationship between
shapes in a game’s economy and the structure of its mechanics. In the next sections,
we discuss and illustrate the most important building blocks of economic shapes.

neGaTive FeedBacK creaTes an eqUiLiBriUm
Negative feedback (as discussed in Chapter 3, “Complex Systems and the Structure of
Emergence”) is used to create stability in dynamic systems. Negative feedback makes
a system resistant to changes: The temperature of your refrigerator is kept constant

NOT E This analysis
of chess is a highlevel abstraction to
illustrate an economic
principle using a
familiar game. classic
texts on the theory
of chess do not treat
it in economic terms,
because chess is about
checkmating the king,
not taking the most
pieces. however, our
illustration shows that
gameplay and game
progress can be understood in economic
terms even if the game
itself is not about
economy.

ChAptEr 4

Strategic advantage is more dynamic in the game; it is gained and lost over the
course of play. Players use their material to gain strategic advantage or reduce the
strategic advantage of their opponents. There is an indirect relationship between
the different amounts of material the players have and their ability to gain strategic
advantage: If a player has more material, then gaining strategic advantage becomes
easier. In turn, strategic advantage might be leveraged to take more pieces of an
opponent and reduce that player’s material. Sometimes it is possible to sacrifice
one of your pieces to gain strategic advantage or to lure your opponent into losing
strategic advantage.

66

Game mechanics: advanced Game desiGn

even if the temperature outside the refrigerator changes. The point at which
the system stabilizes is called the equilibrium. Figure 4.5 displays the effects of
negative feedback.

FIGURe 4.5
The effect of negative
feedback

The simplest shape of the equilibrium is a straight horizontal line, but some systems
might have different equilibriums. An equilibrium might change steadily over time
or be periodical (Figure 4.6). Changing equilibriums requires a dynamic factor that
changes more or less independently of the negative feedback mechanism. The outside temperature throughout the year is an example of a periodical equilibrium that
is caused by the periodic waxing and waning of the available hours of daylight and
the relative strength of the sun.

FIGURe 4.6
negative feedback on
changing equilibriums.
On the left, a rising
equilibrium; on the
right, a periodically
changing equilibrium.

POsiTive FeedBacK creaTes an arms race
Positive feedback creates an exponential curve (Figure 4.7). Collecting interest on
your savings account is a classic example of such a curve. If the interest is the only
source of money going into your savings account, the money will spiral upward,
gaining speed as the accumulated sum creates more and more interest over time.
In games, this type of positive feedback is often used to create an arms race between
multiple players. A good example is the harvesting of raw materials in StarCraft (or
similar constructions in many other RTS games). In StarCraft, you can spend 50

inTernaL ecOnOmY

67

minerals to build a mining unit (called an SCV, for Space Construction Vehicle) that
can be used to collect new minerals. If StarCraft players set aside a certain portion
of their mineral income to build new SCVs, they get the same curve as money in a
savings account.

FIGURe 4.7
Positive feedback
creates exponential
curves.

Obviously, StarCraft players do not spend their resources only on SCV units. They
also need to spend resources to build military units, to expand their bases, and to
develop new technology. However, the economic growth potential of a base in
StarCraft is vital in the long run. Many players build up their defenses first and
harvest many resources before pushing to destroy their enemy with a superior
capacity to produce military units.

Positive feedback mechanisms can create deadlocks and mutual dependencies. in StarCraft,
to get minerals, you need scv units, and to get scv units, you need minerals. These
two resources are mutually dependent, and this dependency can lead to a deadlock
situation: if you are left without minerals and scv units, you can never get production
started. in fact, you need enough minerals and at least one scv unit to be able to build
a headquarters, a third resource that enables this feedback loop. This deadlock situation
is a potential threat. an enemy player might destroy all your scv units. if this happens
when you have spent all your minerals on military units, you are in trouble. it can also
be used as a basis for level design. Perhaps you start a mission with military units, some
minerals, but no scv units or headquarters. in this case, you must find and rescue scv
units. deadlocks and mutual dependencies are characteristics of particular structures
in mechanics.

ChAptEr 4

deadlocks and mutual dependencies

68

Game mechanics: advanced Game desiGn

One of the most useful applications of positive feedback in games is that it can be
used to make players win quickly once a critical difference is created. As should
become clear from Figure 4.7, positive feedback works to amplify small differences:
The difference between the balances of two bank accounts with equal interest rates
but different initial deposits will only grow over time. This effect of positive feedback can be used to drive a game toward a conclusion after the critical difference
has been made. After all, nobody likes to keep playing for long once it has become
clear who will win the game.

positiVe Feedback on destructiVe mechanisms
Positive feedback does not always work to make a player win; it can also make a player
lose. For example, losing pieces in a game of chess weakens your position and increases
the chance that you will lose more pieces; this is the result of a positive feedback loop.
Positive feedback can be applied to a destructive mechanism (as is the case with losing
material in chess). in this case, it is sometimes called a downward spiral. it is important
to understand that positive feedback on a destructive mechanism is not the same as negative feedback—negative feedback tends to damp out effects and produce equilibrium.
You can also have negative feedback attached to a destructive mechanism. The shooter
game Half-Life starts spawning more health packs when a player is low on hit points.

LOnG-Term invesTmenTs vs. shOrT-Term Gains
If StarCraft were a race to collect as many minerals as possible without any other
considerations, would the best strategy be to build a new SCV unit every time
you’ve collected enough minerals? No, not exactly. If you keep spending all your
income on new SCVs, you would never save any minerals, which is what you need
to win the game. To collect minerals, at some point you need to stop producing
SCVs and start stockpiling. The best moment to do this depends on the goals and
the constraints of the game—and what the other players do. If the goal is to accumulate the biggest pile of minerals in a limited amount of time or to accumulate a
specific number of minerals as quickly as possible, there is an ideal number of SCV
units you should produce.
To understand this effect, look at Figure 4.8. It shows that as long as you’re investing in new SCVs, your minerals do not accumulate. However, as soon as you stop
investing, the minerals increase at a steady pace. This pace depends on the number
of SCV units you have. The more you have, the faster your minerals will increase.
The longer you keep investing, the later you will start accumulating minerals, but
you will eventually catch up and overtake anybody who started accumulating before
you did. Depending on the target goal, one of those lines is the most effective.

inTernaL ecOnOmY

69

FIGURe 4.8
a race of accumulation

It is a good thing StarCraft is about more than just collecting minerals. Spending
all your minerals on SCV units is a poor strategy because eventually you will be
attacked. You have to balance your long-term goals with short-term requirements
such as the protection of your base. In addition, some players favor a tactic in which
they build up an offensive force quickly in a gambit to overwhelm their opponent
before they can build up their defenses—the “tank rush,” which was first made
famous in Command & Conquer: Red Alert. On some maps, initial access to resources
is limited, and you must move around the map quickly to consolidate your access
to future resources. Investing in SCV units is a good strategy in the long run, but it
requires you take some risk in the beginning, possibly giving up on quick military
gains via the tank rush.

in StarCraft, it is not only the number of scv units that determines the pace at which
you harvest minerals. minerals come from deposits of crystals, which have a particular
location on the map. Finding the best location for your base, and micro-managing your
scv units to harvest minerals from crystals effectively, is a skill in itself. These are good
examples of how player skill and game world terrain can produce input variation that
affects the economic behavior of your game. Of course, the players’ inputs must influence the economy, but it is best if the player’s inputs occur frequently but no one input
has too large an effect.

ChAptEr 4

Variation From player perFormance
and resource distribution

70

Game mechanics: advanced Game desiGn

FeedBacK Based On reLaTive scOres
During Marc LeBlanc’s talk on feedback mechanisms in games at the Game Developers
Conference in 1999, he described two alternate versions of basketball. In “negative
feedback basketball,” for every five points that the leading team is ahead, the trailing team is allowed to field one extra player. In “positive feedback basketball,” this
effect is reversed: The leading team is allowed to field one extra player for every
five points they are ahead. The effects of using the difference between two players
to create a feedback mechanism are slightly different from using absolute values to
feed this mechanism: The effects of the feedback mechanisms affect the difference
between the players, not their absolute resources. This can produce some counterintuitive effects. The economic chart of negative feedback basketball, for example,
shows the lead of the better team settling on a stable distance at which the lack of
the skill of the trailing team is offset by the extra players they can field (Figure 4.9).

FIGURe 4.9
score graph of
negative feedback
basketball

dynamic equilibrium
The equilibrium that is created by a negative feedback mechanism that is fed by the difference in resources between two players is a dynamic equilibrium: it is not set to a fixed
value but is dependent on other, changing factors in the game. You will find that most
interesting applications of negative feedback in games are dynamic in this way. making
the equilibrium of a negative feedback loop dynamic by making it dependent on the relative fortune of multiple players, or other factors in the game, is a good way to move away
from a too predictable balance created by a nondynamic equilibrium. With experience,
knowledge, and skill, you will be able to combine several factors to compose dynamic
equilibriums that are periodic, are progressive, or follow another desired shape.

inTernaL ecOnOmY

71

When two teams are playing positive feedback basketball, the differences in skills are
aggravated. When one side is better than the other, this will result in a very one-sided
match. However, when both sides are closely matched, a different pattern emerges:
The game will probably remain close, until one side manages to take a decisive lead
after which the match becomes very one-sided again. In this latter case, a small difference in skill, an extra effort, or sheer luck can become the decisive factor.
In Chapter 6, we explore the gameplay effects of positive and negative feedback on
basketball in more detail.

rubberbandinG is neGatiVe Feedback
on relatiVe position
racing games frequently use negative feedback based on the players’ position in the
field to keep the race tight and exciting. This mechanism is often referred to as rubberbanding, because it seems to players as if the other cars are attached to theirs by a rubber band—they never get too far ahead or too far behind. some games implement rubberbanding by simply slowing leading cars down and speeding trailing cars up. Other games
use more subtle negative feedback mechanics to reach similar effects. in MarioKart,
players are awarded with a random power after picking up a power-up. however, trailing
players have a better chance of picking up a more powerful power-up than leading ones
do. in addition, because most weapon power-ups in MarioKart are used on opponents in
front of the player, the leader of the field is a target more often than the player in the last
position. This causes the lead to change hands frequently and increases the excitement
of the game, increasing the likelihood of a last-minute surge past the leader.

In the previous sections, we discussed the elements and common structures of
internal game economies. In this section, we will discuss how game economies are
typically used in games of different genres. Table 1.1 provided a quick overview of
some mechanics that are typically part of that economy. Now, we will discuss the
typical economic structures found across game genres in more detail.

Use an Internal economy to Complement Physics
Obviously, physics make up the largest part of action games’ core mechanics. Physics
are used to test the player’s dexterity, timing, and accuracy. Still, most action games
add an internal economy to create an integral reward system or to establish a system
of power-ups that requires resources. In a way, the simple use of a scoring system
adds economic mechanics to many action games. If you collect points for taking out
enemies, players will have to consider how much they will invest to take out that

ChAptEr 4

uses for Internal Economies in Games

72

Game mechanics: advanced Game desiGn

enemy. Will they put their avatars at risk, or will they waste ammunition or some
sort of energy that cannot easily be regained?
Super Mario Brothers and many other similar platform games use a simple economy
to create a reward system. In Super Mario Brothers, you can collect coins to gain extra
lives. Because you need to collect quite a few coins, the designer can place them
liberally throughout a level and add or remove them during play-testing without
affecting the economy significantly. In this way, coins can be used to guide a player
through a level. (Collectible objects that are used to guide players are often called
breadcrumbs.) It is safe to assume that you are able to reach all coins, so if you spot a
coin, there must be a way to reach it. This creates the opportunity to reward skillful
players for reaching difficult places in the game. Used in this way, the internal economy
of the game can be very simple. However, even a simple economy like this already
involves a feedback loop. If players go out of their way to collect many coins, they
will gain more lives, thus allowing them to take more risks to collect more coins.
When setting up a system like this, you must be careful to balance the risks and
rewards. If you lure players into deadly traps with just a single coin, you are inviting them to risk a life to gain a single coin. That simply isn’t fair, and the player will
probably feel cheated. As a designer, you have a responsibility to match the risks
and rewards, especially when they are placed close to the path novice players will
take. (Creating a reward that the player can see but never reach is even worse—it
causes players to take risks for rewards they can never obtain.)
Power-ups, including weapons and ammunition in first-person shooters, create a
similar economy. Power-ups and ammo can be rewards in themselves, challenging
the player to try to eliminate all enemies in a level. As a game designer, you have to
make sure that the balance is right. In some games, it is perfectly all right if killing
enemies will, on average, cost more bullets than the players can loot from their
remains. However, if this leads to a situation in which the player is eventually short
on the proper ammo for the big confrontation with a boss character, you risk penalizing players for making an effort in the game. In survival-oriented first-person
shooters, creating a scarce economy of weapons and ammo is generally a good thing
because it adds to the tension and the drama, but it is a difficult balance to create.
If your shooter is more action-oriented, then it is probably best to make sure there
is plenty of ammo for the player, and you should make sure that taking out extra
enemies is properly rewarded.

Use an Internal economy to Influence Progression
The internal economy of a game can also be used to influence progression through
a game that involves movement. For example, power-ups and unique weapons can
play a special role in an action game’s economy. They can be used to gain access
to new locations. A double-jump ability in a platform game will allow the player
to reach higher platforms that were initially unreachable. In economic terms, you
can think of these abilities as new resources to produce the abstract resource access.

inTernaL ecOnOmY

73

Access can be used to gain more rewards or can be required to progress through
the game.
In both cases, as a designer, you should be wary of a deadlock situation. For example,
you might have a special enemy guard the exit of a level. Somewhere in the same
level there is a unique weapon that is required to kill that enemy with a single shot.
The weapon is usable throughout the level. When the player finds the weapon, it is
loaded with ten bullets, and there are no more until the next level—but the player
doesn’t know this the first time playing. Now, a first-time player finds the weapon,
fires a couple of shots to experiment with it, uses it on a couple of other enemies,
and finds himself at the exit with one bullet left. The player fires and misses. You
have just created a deadlock situation. The player needs access to the next level to
gain bullets but needs bullets to gain access.

deadlock resolution in Zelda

ChAptEr 4

in many Zelda games, players frequently must use consumable items—arrows or
bombs—to gain access to new areas. This creates a risk of deadlocks, if the player runs
out of the items needed. The designers of Zelda games prevent these no-win situations
by making sure there are plenty of renewable sources for the required resources.
dungeons are littered with useful pots that yield these resources if the player destroys
them (Figure 4.10). Broken pots are mysteriously restored as the player moves from room
to room, creating a source that is replenished from time to time. Because the pots can
contain anything, as a designer you can use a mechanism like this to provide the player
with any resource required. You can even use it as a way of providing gameplay hints:
if players are finding a lot of arrows, they are probably going to need a bow soon.

FIGURe 4.10 Pottery is a useful source in Zelda games.

74

Game mechanics: advanced Game desiGn

Use an Internal economy to Add Strategic Gameplay
It is surprising how many of the strategic challenges in real-time strategy games are
economic in nature. In a typical game of StarCraft, you probably spend more time
