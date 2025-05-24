managing the economy than fighting the battle. Including an internal economy is
a good way to introduce a strategic dimension to a game that operates on a larger
time span than most physical and/or tactical action.
One of the reasons that most real-time strategy games have elaborate internal
economies is that these economies allow the games to reward planning and longterm investments. A game about military conflict with little forward planning and
no long-term investments would be a game of tactics rather than strategy, because
it would probably be more about maneuvering units on the battle field. To sustain
a level of strategic interaction, a game’s internal economy needs to be more complicated than the internal economies that simply complement the physics of an action
game. Economies in strategy games usually involve multiple resources and involve
many feedback loops and interrelationships. Setting up an economy like that for
the first time is challenging, and finding the right balance is even more difficult.
As a designer, you need to understand the elements of the economy and develop a
keen sense to judge its dynamic effects. Even if you have years of experience, it is
easy to make mistakes: There have been many tweaks to the economy of games like
StarCraft to retain the right balance after players developed new strategies, even after
the game had been long published!
Even without a focus on the economics of production (such as StarCraft’s minerals
and SCV units), internal economies can add strategic depth to almost any game. In
most cases, this involves planning to use the available resources wisely. As already
discussed, the economy of chess can be understood in terms of material (playing
pieces) and strategic advantage. Chess is not about production, and gaining a piece
in chess is unusual. Rather, the game is about using and sometimes sacrificing your
material in order to produce as much strategic advantage as possible. In other words,
chess is all about getting the most mileage out of your pieces.
You can find something similar in the game Prince of Persia: The Sands of Time. In
this action-adventure game, the player progresses through many levels filled with
dexterity and combat challenges. Early in the game, the player is awarded a magical
dagger that allows that player to control time. If anything goes wrong, the player
can use sand from the dagger to rewind time and to try again. This power can also
be used during combat, for example just after the player has taken a big hit. In addition, the player can use sand as a magical power to freeze time. This helps when
battling multiple enemies. The sand is not limitless, however. The player can rewind
time only so often, but fortunately, defeating enemies provides the player with new
sand. This means that, in additional to the usual action-oriented gameplay, the
player has to manage a vital resource. The player must decide when is the best time
to invest some sand. Different players will have different ideas about when they
should use their sand. Some will use it more often to help out with combat, while

inTernaL ecOnOmY

75

others will prefer to save it for challenging jumping puzzles. In this way, the sand is
a versatile resource: Players are able to use it to boost their performance where they
need it most.

Use an Internal economy to Create large Probability Spaces
As internal economies grow more complex, the probability space of your game
expands quickly. Games with a large probability space tend to offer more replay
value, because players will have more options to explore than is generally achievable with a single play-through. Another benefit is that these games can also create
a more personal experience, because the performance of players and their choices
directly affect what parts of the probability space open up for exploration.

When using an internal economy to customize the gameplay, there are three things
you need to watch out for. First, in an online role-playing game, if a particular
combination of items and skills is more efficient than others, players will quickly
identify and share this information, and the economy will be thrown off-balance.
Either players will choose only that option, effectively reducing the probability
space and creating a monotonous experience, or they will complain that they cannot keep up with players who did. In games like this, it is important to understand
that customization features are best balanced by some sort of negative feedback.
Role-playing games usually implement many negative feedback mechanisms for
this reason: Every time characters gain a level and improved skills, they need more
experience points to get to the next level. This effectively works to reduce the differences in levels and abilities and requires more investment from a player for each
level earned.
Second, you have to be sure that the probability space is large enough that players do
not end up exploring it entirely in one play session. For example, if in a role-playing
game players have a rating between 1 and 5 for the attributes of strength, dexterity,
and wisdom, and the player can choose which one to increase from time to time, it
is generally a poor design decision to require them to upgrade all these attributes to
the maximum in order to finish the game. Similarly, if the player has only limited
choice over what order to upgrade her attributes, the consequences of those choices
are reduced. A good way to include choices that have real consequences is to create
choices that exclude each other. For example, players can generally choose only one

ChAptEr 4

Games that use an internal economy to govern character development, technology,
growth, or vehicle upgrades often use an internal currency to provide options to
the player. This is a typical gameplay feature found in role-playing games, in which
players spend in-game money to outfit their characters and spend experience points
to develop skills and abilities. It is also found in certain racing games that allow
players to tune or upgrade their vehicles between (or sometimes even during) races.
As long as there are enough options and the options present really different solutions
to problems encountered in the game, or are otherwise important to the player, this
is a good strategy.

76

Game mechanics: advanced Game desiGn

class for their character in a role-playing game. Each class should have a unique set
of different skills and abilities. In Deus Ex, the player is also presented with choices
to improve the cyborg character that have gameplay consequences: The player
might be forced to choose between installing a module that will render the character invisible for short periods and a special type of subdermal armor that will make
the character much more resistant to damage.
Third, you should ideally design your levels in such a way that players can use different strategies to complete them. For example, in Deus Ex, the player can choose
to develop a character in different ways. The player can focus on combat, stealth,
or hacking as alternative ways of solving the many challenges in the game. This
means that almost every level has multiple solutions. This is not an easy balance to
strike. If you estimate that the player has managed to upgrade three options before
a certain level, you have to take into account that the player upgraded the combat
abilities three times, stealth three times, hacking three times, or perhaps all of them
once. In Deus Ex, this problem is even more pronounced because all the sources of
experience points that you require to upgrade are not renewable: You gain them for
progressing and performing certain side quests. Going back to a previous area to
harvest some more experience is not an option.
This example illustrates that the levels in games that permit customization must
be more flexible, and more general, than in conventional action games, because
you don’t know exactly what abilities the player’s avatar will have. Deus Ex Human
Revolution contained a flaw: It allowed the players different ways to play the game
but only one way to beat the boss characters, which defeated the point of allowing
the players to customize their avatars.

Tips for economy Construction Games
Games in which the player builds an economy, such as construction and management simulations, tend to have large and complex internal economies. SimCity is a
good example. As players zone areas and build infrastructure, they use these building blocks to craft an economic structure that produces the resources they need to
increase it even further. Building a game like this requires the designer to assemble a
toolbox of mechanics that the player can combine in many interesting ways. This is
even harder than designing a complete, functional, and balanced economy yourself. You have to be aware of all the different ways your economic building blocks
combine. When successful, playing the game can be very rewarding, because the
economy the players build up through play directly reflects their choices and strategies. This is why no two cities in SimCity are alike.

inTernaL ecOnOmY

77

If you are designing an economy construction game, there are three strategies that
can help you keep the complexity of your task under control:
Don’t introduce all the player’s building blocks at once. Construction and
management simulations typically allow the player to build something—a farm,
factory, or city, for example—out of elementary units, building blocks, that play a
role in the economy. (In SimCity, these are zoned land and specialized buildings.) It
is a good idea to gently introduce players to the different elements in your game, a
few at a time. This makes it easier to control the probability space, at least initially.
By allowing certain building blocks and disallowing others, you can craft scenarios
and create special challenges. If your game has no distinct levels or special scenarios,
make sure that not all building options are available from the start. Have players
accumulate resources before they can use the more advanced building blocks that
unlock new options. Civilization is an excellent example of an economy construction game in which most of the building blocks are locked at the beginning of the
game and must be unlocked one by one before the players can use them.

n

Be aware of the meta-economic structure. In an ideal economy construction
game, the number of ways of putting the economic building blocks together is endless. However, in most such games, certain approaches are better than others (and
in games with a victory condition, some approaches are unwinnable). As a designer,
you should be aware of typical constructions that might be called meta-economic
structures. For example, in SimCity, a particular mix of industrial, residential, and
commercial zones will prove to be very effective. Players will probably discover
these structures quickly and follow them closely. One difficult, but effective, way of
dealing with patterns that could become too dominant is to make sure that patterns
that are effective early in the game cease to be effective later. For example, a particular layout of zones might be an effective way to grow your population initially but
causes a lot of pollution in the long run. Slow-working, destructive positive feedback
is a good mechanism to create this sort of effect.

n

Use maps to produce variety and constrain the possibility space. SimCity and
Civilization wouldn’t be nearly as much fun if you could build your city or empire
on an ideal piece of land. Part of the challenge of these games is to deal with the
limitations of the virtual environment’s initial state. As a designer, you can use the
design of the map to constrain players or to present opportunities. So, although
there might be a best way of building the economy (something that we might call
a dominant meta-economic structure), it is simply not possible to do so in particular
terrain. This forces players to improvise, and rewards players who are more flexible
and versatile. In SimCity, the disaster scenarios in which players can unleash several
natural disasters on their cities challenges their improvisation and flexibility in a
similar vein; and of course, SimCity also generates disasters at random, setting back
the player’s progress.

ChAptEr 4

n

78

Game mechanics: advanced Game desiGn

Summary
In this chapter, we introduced the essential elements of an internal economy:
resources, entities, and some of the mechanics that manipulate them, including
sources, drains, converters, and traders. We examined the concept of economic
shapes as seen through graphs and showed how different mechanical structures can
produce different shapes. Negative feedback creates equilibrium, while positive feedback creates an arms race among opponents. Implemented another way, positive
feedback can produce a downward spiral, because a player finds it harder and harder
to grow his economy. Feedback systems based on relationships between two players
can produce effects that keep games close or tend to cause the player in the lead to
stay in the lead.
Game designers can use internal economics in many ways to make games interesting,
enriching both the progression of a game and the strategic choices a player has to
make. The internal economy also affects the competitive landscape between diverse
or closely matched players in multiplayer games. The chapter ended with specific
suggestions about how to build games in which players construct an economy, as
in SimCity.

Exercises
1. Identify the resources and economic functions in a published game. (Your
instructor may specify particular games to study.)

2. Find an example of a game (not referred to in this chapter) that exhibits one of
these properties: negative feedback with periodic equilibrium, a downward spiral,
a short-term versus long-term investment trade-off, feedback based on players’
relative scores, or rubberbanding. Explain which resources are involved, and show
how the game’s mechanics produce the effect you discovered.

3. Find an example of a game (other than a Zelda game) in which a deadlock may
occur. Does the game provide a means of breaking the deadlock? Explain.

ChAptEr 5
ChAptEr 5

Machinations
In the previous chapter, we showed how a game’s internal economy is one important aspect of its mechanics. We used diagrams to visualize economic structures
and their effects. In this chapter, we introduce the Machinations framework, or
visual language, to formalize this perspective on game mechanics. Machinations
was devised by Joris Dormans to help designers and students of game design create,
document, simulate, and test the internal economy of a game. At the core of this
framework are Machinations diagrams, a way of representing the internal economy
of a game visually. The advantage of Machinations diagrams is that they have a
clearly defined syntax. This lets you use Machinations diagrams to record and communicate designs in a clear and consistent way.
We will be using Machinations diagrams throughout this book, so it is important
that you learn how to read them. This chapter will take you through most of the
elements that make up a Machinations diagram. However, a word of caution: The
Machinations framework is a lot to take in at once. The framework comprises many
interrelated concepts that are best understood together. This means there is no real
natural starting point to explain all these concepts. We have tried to introduce the
elements of a Machinations diagram in a logical order, but don’t be surprised if you
find yourself referring to earlier concepts on occasion.
Machinations is more than just a visual language for creating diagrams, however.
Dormans has built an online tool for drawing the diagrams and simulating them
in real time. With it, you can construct and save Machinations diagrams easily, and
you can also study the behavior of your internal economy. You can find the tool at
www.jorisdormans.nl/machinations.
Appendix C (which you can find online at www.peachpit.com/gamemechanics) includes
a tutorial on how to use the Machinations Tool. You can find a quick reference
guide to the most important elements of Machinations diagrams in Appendix A.

The Machinations Framework
Game mechanics and their structural features are not immediately visible in most
games. Some mechanics might be apparent to the player, but many are hidden
within the game code. We need a way to describe and discuss them.
Unfortunately, the models that are sometimes used to represent game mechanics,
such as program code, finite state diagrams, or Petri nets, are complex and not
really accessible for designers. Moreover, they are ill-suited to represent games at a

79

80

Game mechanics: advanced Game desiGn

sufficient level of abstraction, in which structural features such as feedback loops
are immediately apparent. Machinations diagrams are designed to represent game
mechanics in a way that is accessible yet retains the structural features and dynamic
behavior of the games they represent.
The theoretical vision that drives the Machinations framework is that gameplay is
ultimately determined by the flow of tangible, intangible, and abstract resources
through the game system. Machinations diagrams represent these flows, and they
let you see and study the feedback structures that might exist within the game
system. These feedback structures determine much of the dynamic behavior of
game economies. By using Machinations diagrams, a designer can observe game
systems that would normally be invisible. Figure 5.1 provides an overview of the
Machinations framework and its most important components.

FIGURe 5.1
The machinations
framework

The Machinations Tool
You can draw Machinations diagrams on paper or with a computerized drawing tool.
At the same time, the syntax of the language is exact. It describes unambiguously how
different elements of an internal economy interact. The syntax of the Machinations
language is formal enough to be interpreted and executed on a computer; it is close
to a visual programming language designed to represent game mechanics.

Digital Machinations diagrams are dynamic and interactive representations of game
mechanics. Unfortunately, we can’t show their dynamic and interactive nature in the
static illustrations printed in this book. However, Dormans has created a free, online
application named the Machinations Tool. The tool lets you draw Machinations
diagrams, simulate their operation in real time, and interact with them. On the
Machinations website, you can find interactive versions of many of the examples
that we discuss in this and later chapters. To a certain extent, the digital versions
of Machinations diagrams are playable. Some diagrams are so much like playing an
actual game that experimenting with them is fun and challenging in itself.

81

NOT E You can find
the machinations Tool,
and many resources
for using it, at www.
jorisdormans.nl/
machinations.

How the Machinations Tool Works
A static Machinations diagram, such as the ones printed in this book, can display
only one distribution of resources. However, the Machinations Tool allows you to
load digital versions of the diagrams and see how they change over time.
The Machinations Tool looks similar to an object-oriented 2D drawing application
such as Microsoft Visio. It has a workspace in the middle and a variety of selectable
tools in a side panel. You can create diagrams in the workspace or load them from
a file.
When you tell the tool to run, it performs the events that are specified by the diagram in a series of time steps or iterations (we use the terms interchangeably). The
tool changes the state of the diagram. When it has completed one iteration, the tool
then executes another with the diagram in its new state, and so on, repeatedly until
you tell it to stop. (You can also build a feature into the diagram that will cause iteration to stop automatically when certain conditions are met—like when the clock
runs out in basketball.) You can control the length of each time step by setting an
interval value; if you want the tool to run slowly, you can set the interval to several
seconds per time step.

Scope and level of Detail
In earlier chapters, we discussed the notion of abstraction: the process of simplifying
or eliminating details of a system to make it less complex and easier to study and
tune. For example, the computers that ran the early versions of SimCity did not have
enough CPU power to represent each automobile individually. Instead, the game
simply computed traffic density in a general way along each stretch of road and displayed an animation that showed how dense it was.
Machinations diagrams permit you to abstract as much or as little as you like. You can
use them to focus on all, or only part, of a game’s mechanics. Using Machinations
diagrams, you can design and test your game’s mechanics at different levels of
detail. How you use them depends on what you want to achieve. For example, it’s
often sufficient to model a game from the perspective of a single player, even if the

NOT E appendix a
contains a tutorial
explaining how to use
the machinations Tool.

ChAptEr 5

machinaT iOns

82

Game mechanics: advanced Game desiGn

game is actually played by multiple players. Once you’ve done that, it’s fairly easy to
imagine how a diagram might be duplicated and the duplicates combined to represent the multiplayer situation.
In other cases, it’s useful to model the mechanics for one player at a higher level of
detail than other players. Or you can leave out certain aspects of the game, such as
players taking turns. At a high level of abstraction, there is often little difference in
the effects of real-time play and turn-based play.
For the examples in this book, we have tried to keep the level of detail low and the
level of abstraction high so the diagrams don’t get too complex. This way, you can
easily see the structural features of the internal economy, which will help you to
understand how these structures create emergent gameplay. For this reason, the
natural scope of a Machinations diagram is that of a single player and that player’s
individual perspective on the game system. Although it is certainly possible to
model multiplayer systems and turn-based play, the framework, as it currently
stands, does not include features designed to support multiplayer games in particular. For example, the main input device for interaction with a Machinations diagram
is the mouse; there is no support for multiple players using multiple input devices.
The tool has no means of enforcing whose turn it is to interact or to prevent one
player from clicking a part of the diagram that belongs to another player. It’s a simulation tool, not a tool for building playable games.
Finally, a word of caution: We have used Machinations diagrams to model a number
of real games, but as we said, we have intentionally simplified them in this book.
The Machinations framework and diagrams only facilitate understanding of games;
they aren’t a substitute for studying the game itself.

Machinations Diagram Basic Elements
The Machinations framework is designed to model activity, interaction, and communication between the parts of a game’s internal economy. As shown in the
previous chapter, a game’s economic system is dominated by the flow of resources.
To model a game’s internal economy, Machinations diagrams use several types of
nodes that pull, push, gather, and distribute resources. Resource connections determine
how resources move between elements, and state connections determine how the
current distribution of resources modifies other elements in the diagram. Together,
these elements form the essential core of Machinations diagrams. Let’s take a look
at these basic elements.

machinaT iOns

83

The most basic node type in a Machinations diagram is the pool. A pool is a location
in the diagram where resources gather. Pools are represented as open circles, while
the resources that are stored in a pool are represented as smaller, colored circles that
stack on them (Figure 5.2). If there are too many resources in a pool to show them
as stacks, the tool displays a number instead.


  




FIGURe 5.2
Pools and resources

  
 

Pools are used to model entities. For example, if you have a resource called money
and an entity called the player’s bank account, you would use a pool to model the
bank account. Note, however, that pools cannot store fractional values, only integers.
The bank account would have to contain only whole dollars or to be characterized
in terms of cents rather than dollars.
Machinations uses different colors to distinguish among different types of resources.
A pool can contain resources of more than one type, which means that it can
be used to model compound entities. However, until you are familiar with the
Machinations framework, it is best not to mix different resources in a single pool.
It is easier to have separate pools to, for instance, represent the health, energy, and
ammunition of a single player, than it is to have one pool with different colored
resources to represent all of them.

T I P You can change
the threshold at which
the tool switches from
displaying stacks to
displaying numbers in
a pool. With the pool
highlighted, enter a
value in the display
Limit box at the side
panel. The default is
25. if you enter a value
of zero, the pool will
always display a number, unless it is empty.
You can set a different
value for each pool you
create.

Resource Connections
Individual resources can move from node to node through a Machinations diagram
along resource connections that are represented as solid arrows connecting the nodes
of the diagram (Figure 5.3).

FIGURe 5.3
resource connections

Resource connections can transfer resources at different rates. A label beside the
resource connection indicates how many resources can move along the connection
in a single time step. If a resource connection has no label, its rate is considered
to be 1. You can also make a resource connection transfer an unlimited number of
resources in a single time step by using the word all as the resource connection’s label.
To help you see how an internal economy works, the Machinations Tool shows
the resource flow by animating the movement of the resources along the resource
connections. When the tool runs, you will see the resources traveling along the connection lines from one node to another.

ChAptEr 5

Pools and Resources

84

Game mechanics: advanced Game desiGn

inputs, outputs, sources, and tarGets
N OT E remember that
a pool is one type of
node. There are seven
other types of nodes,
each of which serves
a specialized purpose.
They are described in
the section “advanced
node Types.”

any connection leading into a node is called an input to that node, while any connection
leaving a node is called an output of that node. similarly, the origin of a connection is the
node where the connection starts, and its target is the node where it ends (Figure 5.4).






 

FIGURe 5.4 inputs, outputs, origins, and targets

random FloW rates

T I P To enter a fixed
flow rate for a resource
connection in the
machinations Tool,
select the resource connection and then type a
number or the word all
in the Label box in the
side panel.

T I P if you do not
want to watch the
resources move along
the resource connections, you can run the
machinations Tool in
quick run mode. You
will find this under the
run tab in the side
panel. This will make
the tool run much
faster.

as we have explained, games frequently use random number generators to create uncertainty. To model these kinds of games accurately, you can specify random flow rates in
machinations diagrams by entering them in the Label box. random rates are represented
in different ways. if you simply enter d, a die symbol ( ) will appear beside the resource connection to indicate an unspecified random factor. it means that the rate varies
somewhat, but you don’t want to specify the details precisely. (if you actually simulate
the diagram in the machinations Tool, it will use the default value given in the dice box
in the side panel.)
The machinations Tool can generate random numbers using the same dice notation that
is commonly used in pen-and-paper role-playing games. in these games, d6 stands for a
random number produced by a roll of one 6-sided die, whereas d6+3 adds 3 to the same
dice roll, and 2d6 adds the results of two 6-sided dice and thus will produce a number
between 2 and 12. Other types of dice can be used as well: 2d4+d8+d12 indicates the
result of two 4-sided dice added with the results of an 8- and 12-sided die. Unlike penand-paper role-playing games, the machinations Tool is not restricted to dice that are
commercially available. For example, it can use 5-, 7- or 35-sided dice.
You can also create random values using percentages. a resource connection labeled
25% indicates that there is a 25% chance that one resource can flow along that connection at each time step. When using percentages, it is possible to use percentages higher
than 100%. For example, 250% indicates a flow rate of at least two plus a 50% chance of
one more.
Figure 5.5 shows various examples of random flow rates.


FIGURe 5.5 different notations for random flow rates



machinaT iOns

85

Activation Modes
ChAptEr 5

In each iteration, the nodes in a Machinations diagram may fire. When a node
fires, it pushes or pulls resources along the connections that are connected to
it (we explain this in the next section). Whether a node fires depends on its
activation mode. A node in a Machinations diagram can be in one of four different
activation modes:
A node can fire automatically, which means it simply fires every iteration.
All automatic nodes fire simultaneously.

n

A node can be interactive, which means it represents a player action and fires in
response to that action. In a digital version of a Machinations diagram, interactive
nodes fire after the user clicks them.

n

A node can be a starting action, which means that it fires only once, before the
first iteration. In the Machinations Tool, starting actions fire immediately after the
user clicks the run button.

n

A node can be passive, which means it can fire only in response to a trigger generated by another element (we discuss triggers shortly).

n

Each type of node looks different so you can tell them apart (Figure 5.6). Automatic
nodes are marked with an asterisk (*), interactive nodes have a double outline, starting actions are marked with an s, and a passive node has no special mark.


FIGURe 5.6
activation modes

 

 

  

 

Pulling and Pushing Resources
When a pool fires, it will try to pull resources through any inputs connected to it.
The number of resources it pulls is determined by the rate of the individual input
resource connection—the number beside the line. Alternatively, a pool can be set in
push mode. In this mode, when the pool fires, it pushes resources along its output connections. Again, the number of resources pushed is determined by the flow rate of
the output resource connection. A pool in push mode is marked with a p (Figure 5.7).
A pool that has only outputs is always considered to be in push mode, in which case
the p marker is omitted.

86

Game mechanics: advanced Game desiGn

If a pool is trying to pull more resources than exist at the far end of its inputs, it will
handle it in one of two ways:
By default, a node pulls as many resources as it can, up to the flow rates of its
inputs. If not enough resources are available, it still pulls those that are.

n

Alternatively, a node can be set to pull all or no resources. In this mode, when
not all resources are available, none are pulled. Nodes that are in all or none pull
mode are marked with an & sign (Figure 5.7).

n

These rules also apply to pushing nodes: By default, a pushing node sends as many
resources as are available out along its output resource connection up to the output’s
flow rate. A pushing node in all or none mode sends resources only when it can supply all of its outputs. This means that nodes in push mode might be marked with
both a p and an &.

FIGURe 5.7
Pull and push modes






 

 

 

Figure 5.8 illustrates two situations in which there are not enough resources to
meet the demand. Node A is user-activated (which is why you see the double line).
It wants to pull three resources from its upper input and two from its lower one, but
the pools they are connected to do not contain enough resources to do it. When
clicked, node A will simply pull the resources that are available.
When node B is clicked, it tries to pull a random number, from one to six, of
resources from its input. If the random number is four, five, or six, it will pull the
three that are available.

FIGURe 5.8
Two examples showing
fewer resources than
requested









machinaT iOns

87

hourGlass example







ChAptEr 5

Using pools and resource connections, we can construct a simple hourglass (Figure 5.9).
in this case, two pools are connected by a single resource connection. The top pool (a)
is passive and contains five resources, while the bottom pool (B) is automatic and starts
without any resources. after each iteration, B will pull one resource from a until all
resources have moved from a to B. after that, there are no further changes to the state of
this diagram.
FIGURe 5.9
hour glass example








 
 



   
  

Time Modes
Games can handle time in different ways. Board games are often turn-based, while
in many video games the game is active even if the player doesn’t do anything. To
represent different types of games, a Machinations diagram can operate in one of
three different time modes:
In synchronous time mode, all automatic nodes fire at a regular interval that you
can specify for the whole system. All interactive nodes that you click fire at the next
time step, at the same time when automatic nodes fire. In this mode, all actions in
one time step take place simultaneously. It is possible for a user to activate several
different interactive nodes during a time step, but each interactive node can be activated only once in a time step.

n

In asynchronous time mode, automatic nodes in the diagram are still activated at
regular intervals of arbitrary length specified by the user. However, players can activate interactive nodes at any time within the intervals, and the resulting actions are
executed immediately, without waiting for the next time step. In this case, an interactive node can be activated multiple times during a time step. This is the default
setting of the Machinations Tool.

n

T I P You can set the
time mode of a diagram
in the machinations
Tool by using the Time
mode pull-down menu
visible in the side panel
when no element of the
diagram is selected. in
either synchronous or
asynchronous mode,
you can set the length
of the interval in the
interval box, in units of
a second. The interval
box also accepts fractional values, so 2.5
means each time step
lasts 2.5 seconds.

88

Game mechanics: advanced Game desiGn

Alternatively, a Machinations diagram can be in turn-based mode. In this mode,
time steps do not occur at regular intervals. Instead, a new time step occurs after the
player has executed a specified number of actions. This is implemented by assigning
a number of action points to each interactive node and allotting players a fixed budget of action points each turn. After all the action points are used, all the automatic
nodes fire, and a new turn starts.

n

T I P if you set the time
mode to turn-based
in the machinations
Tool, the interval box is
replaced by an actions/
Turn box, in which you
can specify the number
of action points permitted in a single turn. To
specify the number of
action points that an
interactive node consumes when clicked,
select the node and
enter a value in the
actions box in the side
panel. You may also
enter a value of zero.
When all interactive
nodes cost no action
points, except a single
interactive node named
“end turn” (that has
no other effect), this
can be used to create
a game where players
can take any number
of actions until they
indicate that they are
finished.

resolVinG pullinG conFlicts
it might happen that two pools try to pull resources from the same source simultaneously. When there are not enough resources to serve both pools, this will lead to a conflict.
For example, in Figure 5.10 every time step pool B automatically pulls one resource from
a, both c and d attempt to pull one resource from B. This means that after one time step,
B will have one resource and c and d will both try to pull it. how this is resolved depends
on the time mode. in synchronous time mode, neither c nor d can pull the resource. after
two iterations when B has pulled a second resource, both c and d will pull one resource
from B. While the diagram runs, c and d will both pull a resource once every two time
steps simultaneously. as a starts with nine resources, after nine time steps c and d will
have four resources, and one resource will remain on B. The state of the diagram will
then no longer change.
in asynchronous or turn-based mode, either c or d will pull one resource. Which pool
has priority is initially random; subsequently, the priority alternates every time step. This
means that c and d will both pull one resource from B on alternating time steps, and
eventually there will be four resources on c and five on d, or vice versa.












FIGURe 5.10 how simultaneous pulls are handled in a
machinations diagram depends on the diagram’s time mode.

machinaT iOns

89

The state of a Machinations diagram refers to the current distribution of resources
among its nodes. When the resources move from one place to another, the state
changes. In the Machinations framework, you can use state changes to modify the
flow rates of resource connections. In addition, you can trigger nodes to fire, or activate or deactivate them, in response to changes in resource distribution.
To make this possible, Machinations offers a second class of connections called state
connections. State connections indicate how changes to the current state of a node
(the number of resources in it) affect something else in the diagram. State connections are shown as dotted arrows, leading from the controlling node (called the origin)
and going to a target, which can be either a node, a resource connection, or, rarely,
another state connection. Labels on the state connection indicate how it changes
the target. There are four types of state connections that are characterized by the
type of elements they connect and their labels. The four types are label modifiers,
node modifiers, triggers, and activators. We explain them in each of the following
four sections.

LaBeL mOdiFiers
Remember that a label on a resource connection determines how many resources
may move through that connection in a given time step. Label modifiers connect
an origin node to a target label (L) of a resource connection (or even another state
connection). A label modifier indicates how state changes in the origin node (∆S)
modify the current value of the target label at a current time step (Lt ) as indicated
by the state connection’s own label (M). The new value takes effect in the next time
step (Lt+1). The amount of the change in the origin node is multiplied by the label
multiplier’s own label. So, if the label modifier says +3 and the origin node increases
by 2, then the target label will increase by 6 in the next time step (it will add 3
twice, once for each change in the origin node). However, if the label modifier says
+3 and the origin node decreases by 2, then the target label will decrease by 6. Thus,
the new value of label (Lt+1) that is the target of a single label modifier is given by
the following formula:
Lt+1 = Lt + M × ∆S
If the label is the target of multiple label modifiers, you will have to take the sum of
all the changes to find the new value:
Lt+1 = Lt + ∑ (M × ∆S)
The label of a label modifier always starts with a plus or minus symbol. For example,
in Figure 5.11, every resource added to pool A adds 2 to the value of the resource
flow between pools B and C. Thus, the first time B is activated, one resource flows to
A and three resources flow to C. The second time, one resource still flows to A, but
now five resources flow to C.

T I P it can be confusing to run the
machinations Tool and
watch a label modifier
causing its target to
decrease even though
the label modifier’s
own label is positive.
Think of it this way: a
positive label on the
label modifier causes
its target to follow the
origin node, going up
when the origin goes
up and going down
when it goes down. a
negative label on the
label modifier causes
its target to invert the
origin node, going
down when the origin
goes up, and vice versa.

NOT E This is the
first time we have
used color in a
machinations diagram.
here, it is used only for
visual clarity. however,
the diagrams can also
be color-coded, a
special feature of the
machinations Tool.
We explain colorcoding in more detail
in chapter 6.

ChAptEr 5

State Changes

90

Game mechanics: advanced Game desiGn

N OT E Figure 5.12
is not meant to be
simulated in the
machinations Tool;
it only illustrates the
principle.

Label modifiers are frequently used to model different aspects of game behavior.
For example, a pool might be used to represent a player’s accumulated property in a
game of Monopoly. The more property a player has, the more likely it is that player
will collect money from other players. This can be represented by the diagram in
Figure 5.12. Note that in this case the exact value of the label modifier is unspecified; it indicates only that the effect on the random flow rate is positive. Also note
that many mechanics of Monopoly are omitted in this diagram—for example, the
diagram does not show how a player acquires property. You will find diagrams that
paint a more complete picture of Monopoly in Chapters 6 and 8.

FIGURe 5.11
a label modifier affecting the flow rate
between two pools. at a given time
step, the flow from B to c is 3 + 2 times
the number of items in a.

N OT E notice that
node modifiers can
create and destroy
resources if their target is a pool. This
is all right for an
abstract resource such
as “threat level” but
is best avoided for
tangible and intangible resources such
as “keys” or “health.”
To create and destroy
those kinds of
resources, use other
types of nodes called
sources and drains,
described later in this
chapter.

FIGURe 5.12
in Monopoly the state of your property positively affects the chance other players’ money
flows to you.

nOde mOdiFiers
Node modifiers connect two nodes. They enable changes in the state of one node
(its origin) to modify the number of resources in another node (the target node),
according to the node modifier’s label (M). When the origin node changes, it influences the target node in the next time step. More than one origin node can modify
a target node. The formula for this is nearly identical to the formula used for label
modifiers:
Nt+1 = Nt + ∑ (M × ∆S)

node modiFiers can create shortaGes
By using negative node modifiers or redistributing resources from a node that has positive input node modifiers, it becomes possible that the number of resources on a node
becomes negative. in this case, the negative number of resources indicates a shortage.
no resources can be pulled from a node that has a shortage, and resources that flow into
a node with a shortage are used to compensate for the shortage first.

machinaT iOns

91

Figure 5.13 illustrates a node with two modifiers. The number of resources in C will
be equal to three times the number in A, minus two times the number in B.
node modifiers
affect the number of
resources in a pool.

Node modifiers can have labels that are fractions, for example +1/3 or -2/4. In this
case, the number of resources of a target node is modified by the value indicated by
the fraction’s numerator every time there is a change to the number of resources on
the origin divided by the fraction’s denominator and rounded down. Thus, when
the number of resources on an origin node changes from 7 to 8, the number of
resources on the target is lowered by 2 if the modifier is -2/4, but if the modifier is
+1/3, the number of resources on the target node does not change.
This sounds complex, but a simple example of the use of node modifiers can be
found in a real game. In The Settlers of Catan, players gain one point for every village
in their possession and two points for every city in their possession. The number of
villages is one origin node, the number of cities is a second origin node, and both
modify the target node, which is the player’s number of points.

TriGGers
Triggers are state connections that connect two nodes or connect an origin node to
the label of a resource connection. Triggers are identified by their label, which is an
asterisk (*). Triggers do not change numeric values the way label and node modifiers do. Rather, a trigger fires when all the inputs of its origin node become satisfied:
when each input brings in the number of resources to the node as indicated by its
flow rate. A firing trigger will in turn fire its target. When the target is a resource
connection, the resource connection will pull resources as indicated by its flow rate.
A node that has no inputs will fire outgoing triggers whenever it fires (either automatically or in response to a player action or to another trigger).
Triggers are commonly used in games to react to the redistribution of resources. For
example, in Monopoly players might transfer money to the bank in order to trigger
the transfer of property from the bank into their possession. This can be represented
as the diagram in Figure 5.14.

NOT E Triggers are
commonly used to fire
passive nodes that do
nothing until the trigger fires them. This
enables you to set up
a passive node that
fires only when certain
circumstances arise in
the game.

ChAptEr 5

FIGURe 5.13

92

Game mechanics: advanced Game desiGn

FIGURe 5.14
a trigger in Monopoly
enables the acquisition
of property by spending money.

acTivaTOrs
Activators connect two nodes. They activate or inhibit their target node based on the
state of their origin node and a specific condition. The activator’s label specifies this
condition. Conditions are written as an arithmetic expression (for example, ==0, <3,
>=4, or !=2) or a range of values (for example, 3-6). If the state of the origin node
meets this condition, then the target node is activated (it can fire). When the condition is not met, the target node is inhibited (it cannot fire).
Activators are used to model many different game mechanics. For example, in the
board game Caylus, players place their laborers (a resource) at particular buildings on
the board to enable them to execute special actions associated with that building.
For example, a player might place a laborer at a gold mine to collect gold (Figure
5.15). However, as indicated by the trigger in the figure, in Caylus every time a
player mines gold, the laborer then returns to the player’s Workers pool.

FIGURe 5.15
Caylus

machinaT iOns

93

Advanced Node Types
ChAptEr 5

Pools are not the only possible nodes in a Machinations diagram. In this section, we
will describe seven more types of nodes that you can use, including special nodes
for the four economic functions (sources, drains, converters, and traders) discussed
in the previous chapter. However, as you will see, some of these nodes can actually be re-created by using clever constructions of pools, resource connections, and
state connections. Dormans has created these specialized node types to make the
diagrams easier to read. If Machinations diagrams were restricted only to pools, the
diagrams would quickly become cluttered.

Gates
In contrast to a pool, a gate does not collect resources. Instead, it immediately redistributes them. Gates are represented as diamond shapes that often have multiple
outputs (Figure 5.16). Instead of a flow rate, each output is labeled with a probability or a condition. The first type of outputs are referred to as probable outputs while
the others are referred to as conditional outputs. All outputs of a single gate must be
of the same type: When one output is probable, all must be probable, and when one
output is conditional, all must be conditional.







&  '
  
  





 
  


 
   


  





  
   



!

*

* !!



!

"  # 
   $%$$

!!

"  #

   $%$$

  
 



()
&  '
 
  $%$$

FIGURe 5.16
different types of gates
in a machinations
diagram

94

Game mechanics: advanced Game desiGn

Probabilities can be represented as percentages (for example, 20%) or weights indicated by single numbers (for example, 1 or 3). In the first case, a resource flowing
into a gate will have a probability equal to the percentage indicated by each output.
The sum of these probabilities should not add up to more than 100%. If the total is
less than 100%, there is a chance that the resource will not be sent along any output
and be destroyed instead. In the case of weights, the chance that a resource will flow
through a particular output is equal to the weight of that output divided by the sum
of the weights of all outputs of the gate. In other words, if there are two outputs,
one with a weight of 1 and the other with a weight of 3, the chance that a resource
will flow out the first one is 1 in 4, and the chance that it will flow out the second
one is 3 in 4.
Gates with probable outputs can be used to represent chances and risks. For example, in Risk players put armies in danger to gain territories. This type of risk can be
represented easily by a gate with probable outputs indicating the rates for success or
failure.
An output is conditional when it is labeled with a condition (such as >3 or ==0 or
3-5). In this case, all conditions are checked every time a resource arrives at the gate,
and one resource is sent along every output whose condition is met. The conditions
might overlap; this can lead to duplication of resources or, when no condition is
met, to the destruction of the resource.
Like pools, gates have four activation modes: Gates can be passive, interactive, or
