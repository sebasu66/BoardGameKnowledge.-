automatic, or they can be a starting action. Interactive gates have a double outline,
automatic gates are marked with a star, and gates that are activated once before the
diagram starts are marked with an s. When a gate has no inputs, it triggers every
time it fires. This way gates can be used to produce triggers either automatically or
in response to player actions.

T I P When you place a
gate in a machinations
diagram in the tool, you
may set the gate’s type
by clicking one of the
Type icons in the side
panel. The hollow diamond (the default) is a
deterministic gate. The
die symbol converts it
to a random gate.

Gates have one of two distribution modes: deterministic distribution and random
distribution. A deterministic gate will distribute resources evenly according to the distribution probabilities indicated by percentages or weights if it has probable outputs.
When it has conditional outputs, it will count the number of resources that have
passed through it every time step and will use that number to check the conditions
of its outputs. (It can be convenient to think of a deterministic gate with conditional outputs as a counting gate.) A deterministic gate has no special symbol and is
represented as a small open diamond.
A random gate generates a random value to determine where it will distribute incoming resources. When it has probable outputs, it will generate a suitable number
(either a value between 0% and 100% or a number below the total weights of the
outputs). When its outputs are conditional, it will produce a value between 1 and 6
to check against the conditions, just as if the diagram rolled a normal six-sided die
(later we will show you how this value can be changed to represent other types of
random distribution). Random gates are marked with a die symbol.

machinaT iOns

95

All output state connections from a gate are triggers; gates do not accumulate
resources, and therefore label modifiers, node modifiers, and activators originating
from a gate serve no purpose. These triggers can also be conditional or probabilistic.
In this way, gates can be used to control the flow of resources (Figure 5.17).

FIGURe 5.17
an automatic, random gate controlling
the flow of resources
between two passive
pools. in this case,
there is a 30% chance
that three resources
will flow from a to B
every time step.










Sources
Sources are nodes that create resources. They are represented as a triangle pointing
upward (Figure 5.18). Any node in a Machinations diagram can be automatic (the
default), interactive, or passive, or it can activate once before a diagram starts. An
example of an automatic source is the steady regeneration of the protective shields
of the player’s star fighter in Star Wars: X-Wing Alliance. The action to build armies
in Risk would be modeled as an interactive source of armies, and passing Go in
Monopoly would be a passive source of money that is triggered by a game event. The
rate at which a source produces resources is a fundamental property of a source and
is indicated by the flow rates of its outputs.








 

FIGURe 5.18



In many ways, a source acts just as a pool without inputs that starts with a sufficiently large (or even infinite) supply of resources. However, to model limited
sources (see the section “Four Economic Functions” in Chapter 4), it is better to use
a pool with a specified number of resources in it.

Drains
Drains are nodes that consume resources; a resource that goes into a drain disappears permanently. The Machinations framework includes a special drain node
represented as a triangle pointing downward (Figure 5.19). The rate of a drain is
determined by the flow rate of its input resource connection. Some drains consume

Unlimited and limited
sources

ChAptEr 5

Gates might have only one output. Gates with one output act the same way as gates
with multiple outputs. The gates on the middle row of Figure 5.16 will (from left to
right) randomly let 30% of all the resources pass, immediately pass the resource to the
output regardless of the output’s flow rate, and let only the first two resources pass.

96

Game mechanics: advanced Game desiGn

resources at a steady rate, while others consume resources at random rates or intervals. You can also make a drain consume everything its input resource connection is
attached to by labeling the resource connection with all. (A toilet is a good example:
When flushed, it drains all the water in the cistern, no matter how much it is.) You
could in principle represent a drain as a pool with no outputs, but to indicate that
the resources that flow to a drain are consumed and have no further impact on the
game, it is better to use a drain node.

FIGURe 5.19
drains


   

Drains are useful for representing processes that remove resources from an economy
permanently. This might include the effect of wear or friction in a physical system
or the consumption of ammunition when a weapon is fired in a shooter game.

Converters
Converters convert one resource into another. They are represented as a triangle
pointing to the right with a vertical line through it (Figure 5.20). Converters are
designed to model things like factories that turn raw materials into finished products. A windmill, for example, turns wheat into flour. Converters act exactly as a
drain that triggers a source, consuming one resource to produce another. As with
sources and drains, converters can have different types
of rates to consume and produce resources as specified by their inputs and outputs.
For example, a converter representing a sawmill might turn one tree into 50 boards
of lumber.

FIGURe 5.20
converters








Since converters are constructed from drains and sources, it is possible to create a
special construction that might be called a limited converter that can produce only a
limited amount of something as its output. A limited converter is the combination
of a drain and a limited source. Figure 5.21 shows two equivalent alternatives to
construct a limited converter.

FIGURe 5.21
Two ways to build a
limited converter







machinaT iOns

97

Traders
ChAptEr 5

Traders are nodes that cause resources to change ownership when fired: Two players
could use a trader to exchange resources. Machinations diagrams represent a trader
as a vertical line over two triangles that point left and right (Figure 5.22). Use traders when a given number of resources of one type is exchanged for (not converted
into) a given number of another type. This is ideal for any situation that resembles
shopping: the merchant receives money, and the customer receives goods in a stated
proportion (the price). If either the merchant or the customer does not have the
necessary resources, the trade cannot take place. Fallout 3, in which all traders’ supplies are limited, is a good example. A trading mechanism can be constructed by
two gates connected by a trigger ensuring that when one resource is received, the
other is returned in exchange.

FIGURe 5.22
Traders

conVerters Vs. traders
From the perspective of a player, converters and traders have almost the same function:
Pass a number of resources to it and get a number of other resources in return. From
the designer’s perspective, however, they are definitely not the same. The difference becomes clear from looking at their equivalent constructions in a machinations diagram. a
converter is a combination of a drain and a source. When activating a converter, resources are actually consumed and produced, and therefore the total number of resources in
the game might change. in contrast, activating a trader leads only to an exchange; the
number of resources in the game always stays the same.

end Conditions
Games end when certain conditions are fulfilled. Sometimes they end when a
player reaches a certain goal or when time runs out or when all players but one
are eliminated. Machinations diagrams use end conditions to specify end states. The
Machinations Tool checks the end conditions in a diagram at each time step and
stops running immediately when any end condition is fulfilled. End conditions are
square nodes with a smaller, filled square inside (the same symbol that is used to
indicate the stop button on most audio and video players). End conditions must
be activated by an activator. The activators are used to specify the end state of the

NOT E This is an
example of a colorcoded diagram, which
uses color to represent different kinds of
resources. in Figure
5.22, think of red as
representing money
and blue as representing goods. When
the interactive Trader
icon is clicked, three
money resources are
exchanged for two
goods resources. We
explain color-coded
diagrams in more detail
in chapter 6.

98

Game mechanics: advanced Game desiGn

game. Figure 5.23 shows a couple of examples. The diagram on the left stops after
the 25 resources are drained automatically. In the example on the right, you win by
growing more than three apples and oranges.

FIGURe 5.23
end conditions

Modeling Pac-Man
Let’s see how you can use Machinations diagrams to simulate the mechanics of a
simple game—the arcade classic Pac-Man. We’ll break down the process of modeling
Pac-Man into six steps and add them to a Machinations diagram, one at a time to
show how they work. First we’ll identify the game’s most important resources, and
then we’ll model the individual mechanisms. We’ll give each major mechanism its
own color for ease of identification. The last of these mechanisms ties everything
together into a full diagram for Pac-Man.
We have to warn you that our model is an approximation, not a literal simulation
of what Pac-Man’s software does. For example, we implemented a system in which
the ghosts come out of the ghost house at a regular rate, one every five time steps.
The real game uses a more complex algorithm to determine when they come out.
We could have modeled it, but it would have made the diagram too complex. Our
goal here is to teach you to use the Machinations framework, not to create an exact
copy of the real game, so we have simplified it a bit.

Resources
We will use the following resources to model Pac-Man:
Dots. Scattered along the maze are the dots that Pac-Man must eat to complete a
level. Dots are tangible resources in Pac-Man that must all be destroyed to win. The
game starts with a fixed number of dots. Dots are not produced during play (except
when going to the next level).

n

machinaT iOns

99

Power Pills. Every level starts with four power pills, which Pac-Man can eat to be
able to eat the ghosts. These power pills are a scarce but tangible resource the player
must use wisely. Like dots, they are only consumed, never produced during play.

n

Fruits. Occasionally a fruit appears in the maze. Pac-Man can eat the fruit to
score extra points.

ChAptEr 5

n

Ghosts. There are four ghosts that chase Pac-Man around the maze. The ghosts
can be in one of two locations: Either they are in the “ghost house” (the area in the
middle of the screen) or they are in the maze giving chase. The ghosts are also a tangible resource. (Notice that resources are not always positive things for the player!)

n

Lives. Pac-Man starts the game with three lives. Lives are intangible resources in
Pac-Man. If Pac-Man loses all lives, the game ends.

n

Threat. To simulate the effect of the ghosts giving chase, we will model an
abstract resource called threat. When the threat passes a certain threshold, Pac-Man
is caught, and he loses a life. Note that we are not modeling the shape of the maze
itself (which Machinations cannot do), only the flow of resources and states the
game can be in.

n

Points. Every time Pac-Man eats a dot, a fruit, or a ghost, he will consume them
and score a number of points. The objective of the game is to score as many points
as possible. Points are intangible resources.

n

These are all the obvious resources in the Pac-Man economy, and we’ll start our
model by constructing systems around them. Notice that threat is one we made up
for the purposes of the simulation, and our decisions about how to model threat are
subjective and not part of the original game.

Dots
We start with a simple mechanic: Pac-Man eats dots, converting them into points.
It can be represented with two pools and a converter (Figure 5.24). One pool starts
with 50 resources in it representing the dots in the maze. The pool that collects
points starts empty. We also added an end condition that determines that you have
completed a level after eating all the dots. The converter representing the eating
action is an interactive node. You can click it to eat the dots. Notice, however, that
the input of the converter has a random flow rate. Every time you click, there is
only a partial chance that the action succeeds. The more dots there are, the easier
it is to eat them. Initially the chance to eat a dot starts at 100%, but every iteration,
for every dot that is eaten, the chance is lowered by 1%. This reflects the challenge
to the player in moving around the maze and eating every single dot.

NOT E The real game
has exactly 240 dots on
every level. We reduced
this to 50 to make the
game shorter.

100

Game mechanics: advanced Game desiGn

FIGURe 5.24
eating dots to score
points

T I P don’t be confused
by the fact that the
probability of successfully eating a dot goes
down even though the
state connection that
controls it is labeled
+1%. remember that
the function of the state
connection is to transmit the change in its
origin pool (multiplied
by its label). Because
in this case the change
is always negative,
the state connection
actually transmits a
negative value.

In the real game, Pac-Man eats dots 100% of the time until he returns to a place he
has already been, at which point he eats dots 0% of the time. We had to approximate this somehow, so we used a diminishing probability of successfully eating a
dot every time the Eat Dot converter is clicked. In our model, the probability of eating a dot is initially set to 100%, modified by a label modifier that reflects changes
in the Dots pool. If the number of dots in the Dots pool changes between one time
step and the next, that change is multiplied by the label on the state connection,
and the result is applied to the percentage on the resource connection. When a dot
is consumed (say, from 50 dots to 49), the change in the state of the Dots pool is -1.
Multiply that by +1% and you get -1%, and that reduces the probability of successfully eating a dot by 1% on the next time step.
The process of creating these approximations is one of the trickier aspects of modeling a game with Machinations, and you have to think carefully about what your
decisions mean. We chose numbers that feel good to us, but we could have used
others. For example, we could have chosen a rate of change of 0.25% instead of 1%
for successfully eating a dot. This would represent a very skilled player who spends
little time in parts of the maze where he has already been—he’s eating new dots
most of the time.
In some respects, it’s easier to model a new game than an existing one. When you
use Machinations to design a new game, you can set up anything you want. The
tool’s greatest strength is that you can experiment and adjust the details as much
as you like.

The Fruit Mechanism
N OT E in the real
game, fruit appears
only twice in a level
and offers an escalating
number of bonus points
depending on which
level it is. We don’t
implement multiple levels of the game, so we
made the fruit process
shorter, simpler, and
more frequent so that it
is easier to observe.

The fruit mechanism (Figure 5.25) works similarly to the dot mechanism. However,
in contrast to dots, a fruit will appear from time to time and disappear automatically if Pac-Man doesn’t eat it. These extra mechanics are represented by the source
and the drain that are connected to the fruit pool. The fractional rates indicate that
the fruit source produces a fruit once every 20 iterations and is drained once every
5 iterations. This means a fruit will appear once every 20 iterations and disappear 5
iterations later. The interactive node that represents the Eat Fruit action has a fixed
chance of 50% to actually succeed. This approximates the difficulty of catching the
fruit as it moves through the maze. However, eating a fruit will produce 5 points
instead of 1 as eating a dot does.

machinaT iOns

101

FIGURe 5.25

ChAptEr 5

Fruit mechanism
(purple) added to the
diagram

Ghosts Produce Threat
The four ghosts start in the ghost house, and they enter the maze at a fixed rate of
one ghost every five iterations. Each ghost that is in the maze will produce a threat,
which we represent as a black resource generated by an automatic source. Figure 5.26
represents these mechanics. In this diagram, the Maze pool pulls one ghost every
five iterations. Each ghost in the maze increases the output of the source that produces the threat. The player has a chance to lower the threat by clicking the random
interactive Evade gate. When clicked, it has a 50% percent chance of triggering a
drain that drains nine threat resources. (If this fails, the Evade gate does nothing, but
the player may click it again to try again.) We arbitrarily chose this value to indicate
that trying to evade the ghosts doesn’t always work. If you wanted to change the
diagram to represent a more skilled player, you could increase this percentage.

NOT E in the real
game, the algorithm
that determines when
ghosts leave their
house is quite complex.
We made it simpler
for teaching purposes.
also, the ghosts have
limited artificial intelligence that governs how
they move; that doesn’t
appear in our diagram
because we don’t simulate the layout of the
maze.

FIGURe 5.26
Ghosts create threat
but can be evaded.

Capture and loss of life
When the number of threat resources in the Threat pool passes 100, Pac-Man is
caught, and the player loses a life (Figure 5.27). In the meantime, the ghosts return
to the ghost house, and the player can start again, unless it was his last life in which
case the game is over. This process is represented by an automatic trigger (the black
dotted line) that is activated when the number of threat resources passes the threshold of 100. It goes to a Reset gate, which passes the trigger on in three directions

102

Game mechanics: advanced Game desiGn

(the green dotted lines): to a drain that drains a life, to a resource connection that
returns the ghosts from the maze to their house, and to a drain that drains all the
built-up threat.

FIGURe 5.27
reset when caught

T I P note the label
reading >100 on the
state connection to
the reset gate. This
indicates that the state
connection is an activator. activators connect
two nodes. The first
node activates the
second node when the
condition is met, which,
in this case, is when the
Threat pool contains
more than 100 threat
resources.

N OT E Because we
don’t simulate the
layout of the maze, we
arbitrarily assigned
a value of 100 to the
threat level to determine when the player
is caught by a ghost.
But as in the real game,
the player can evade
(using the interactive
evade gate), which lowers the threat.

Power Pills
The last mechanism to be added to the diagram is the mechanism that allows players to eat the ghosts by eating power pills. Figure 5.28 adds this mechanism (light
blue) to the diagram and represents the full game. Power pills start as a limited supply. The player can choose to use them by clicking the Eat Power Pill converter to
convert a power pill into power-up time, an abstract resource that is automatically
drained. While some power-up time remains, the ghosts stop producing threat,
and a drain on the threat is activated. At the same time, a new action to eat a ghost
becomes available. Eating ghosts returns a ghost to the ghost house and also produces five bonus points.

The Complete Diagram
Figure 5.28 represents a playable approximation of Pac-Man. As we have said,
certain mechanisms have been omitted, and the game is different in various details.
It is possible to add these details to a Machinations diagram, but you would be
unlikely to learn anything new from them. However, you can discover a few important things from studying even this simplified diagram. For one thing, players of
Pac-Man must balance their activities among different tasks: eating dots, evading

machinaT iOns

103

ChAptEr 5

ghosts, and eating fruit. One of these actions, eating fruit, is fairly isolated from the
rest of the game. Eating fruit scores bonus points but doesn’t help with anything
else, which means that novice players who have their hands full with the tasks of
eating and evading can safely ignore the fruit. The power pills are an important
resource that must be spent wisely.
Playing around with the digital version of the Pac-Man diagram even gives you a feel
of some of the strategic options available in the real game: You can use power pills
to eat ghosts and score bonus points, but you can also use power pills to safely go
for the final dots and progress faster.

FIGURe 5.28
complete diagram for

Pac-Man

NOT E in the real
game, the duration
of the power pill and
the number of points
earned for eating a
ghost are level-dependent factors, so we
simplified those
aspects.

104

Game mechanics: advanced Game desiGn

Summary
In this chapter, we described the Machinations framework in some detail.
Machinations diagrams consist of nodes that perform functions on resources. The
most basic type of node is the pool, which stores resources. Nodes are joined to each
other by arrows called resource connections, which govern where, when, and how
many resources travel from one node to another. State connections, shown as a dotted arrow, permit the operation of the mechanics to change the behavior of resource
connections and the number of items in a pool and to trigger (or inhibit) events.
A number of specialized nodes perform common functions within an internal
economy: Sources create new resources, while drains destroy them again, and converters turn one kind of resource into another. Gates distribute the flow of resources
through them and can also be used to produce triggers.
At the end of the chapter, we built a Machinations model of Pac-Man, adding systems one at a time to show you how they work. As we have shown, you can use
Machinations to simulate many, many kinds of game mechanics and economies,
even those of action games.
In the next chapter, we’ll introduce a few more specialized nodes and then show
you how to use Machinations to model feedback and randomness. We also discuss
how you can apply Machinations to several different game genres, with numerous
examples.

Exercises
The following exercises are designed to test your familiarity with the Machinations
framework and your understanding of how the tool operates. For clarity, we have
drawn the diagrams so that all pools show how many resources they contain in
digits, rather than in stacks.

machinaT iOns

105

1. In each of the following eight diagrams, how many resources will be in pool A
after one click?










ChAptEr 5

















2. In each of the following six diagrams, what is the minimum number of clicks
required to move all resources to pool A?




















































106

Game mechanics: advanced Game desiGn

3. In each of the following six diagrams, what is the minimum number of clicks
required to move all resources to pool A?



















































4. In each of the following six diagrams, what is the minimum number of clicks
needed to win the game? Note that some diagrams have more than one interactive
element.


































































ChAptEr 6
Common Mechanisms

ChAptEr 6

In the previous chapter, we introduced the Machinations framework and showed
how you can use Machinations diagrams to model the internal economy of games.
In this chapter, we introduce some advanced features of the Machinations framework
that will permit you to simulate and study more complex economies. We also discuss how feedback structures can be read from a Machinations diagram. As we
discussed in Chapter 3, “Complex Systems and the Structure of Emergence,” feedback plays an important role in the creation of emergent behavior, and in this
chapter we outline seven important characteristics of feedback structures. Finally,
we address ways you can use randomness to add unpredictability and variation to
the behavior of your internal economy. This way, Machinations diagrams, both
static and digital versions, become an essential tool to help designers understand
the nature of the dynamic system of game mechanics that drives the gameplay of
their game.

More Machinations Concepts
To start with, we introduce a few additional features of digital Machinations diagrams that we didn’t include in Chapter 5, “Machinations.” In this section, we’ll
explain these extra features.

Registers
Sometimes you’ll want to make simple calculations in a Machinations diagram
or use numeric values that come from player input. While it is possible to model
most of these features with pools, interactive sources, interactive drains, and state
connections, the resulting diagram is awkward to read. To simplify things, digital
Machinations diagrams offer an additional node type: registers. Registers are represented as solid squares with a number indicating their current value.
In many ways, a register acts just like a pool that always displays its value as a number. A register can be passive or interactive. A passive register has a value that is set
by input state connections. When a diagram is not running, this value is displayed
as x because it is not yet determined. An interactive register has an initial value that
you can set while designing the diagram. In addition, it has two buttons that allow
the user to modify its value while the diagram is running. An interactive register is
the equivalent of a pool connected to an interactive source and an interactive drain
(Figure 6.1).

107

108

Game mechanics: advanced Game desiGn

FIGURe 6.1



an interactive register and its equivalent
construction













     

      
   

     
     
   

Registers do not collect resources like pools do, so you should not connect resource
connections to a register. You can connect node modifier state connections to registers in the same way you can connect state connections to a pool.
Passive registers allow you to perform more complex calculations. Every state connection that you connect to a register as an input is assigned a letter automatically.
You can give the register a formula that uses these letters to determine the value of
the register (Figure 6.2). In addition, you can also use the labels max and min to set
a passive register to the maximum or minimum value of its inputs.

FIGURe 6.2



Performing calculations using passive
registers



























Intervals
Sometimes you want a node in a Machinations diagram to be activated less often
than every time step. You can accomplish this by creating flow rates with an interval. Intervals are created by using a slash (/) in the flow rate: A source that has an
output rate of 1/5 will produce 1 resource every 5 time steps. (See Figure 6.3 for
three examples.) A similar effect can be created when the output rate is set to 0.2.
However, using intervals allows you more control over the interval and allows you
to produce resources in bursts. For example, a production rate of 5/10 would produce 5 resources at once every 10 steps.

FIGURe 6.3
intervals




 




  
 



  
  
 

cOmmOn mechanisms

109

You can use random flow rates with intervals. A production rate of D6/3 will produce between one and six resources every three steps. Intervals can be random as
well. A production rate of 1/(D4+2) indicates that one resource is produced every
three to six steps. Random intervals can be a good way to keep the player’s attention
on the game (see the “Random Intervals in Games” sidebar). You can even use a production rate of D6/D6, which indicates between one and six resources are produced
every one to six steps.

random interVals in Games

ChAptEr 6

in his article “Behavioral Game design,” John hopson (2001) reports that experiments in
behavioral psychology suggest that player behavior is affected by chance and the interval
at which the player is rewarded for actions. When a player has a chance to be rewarded
at regular intervals, the player’s attention and activity will spike at those intervals. When
those intervals have random lengths, players will be active most of the time because they
never quite know when their next action might lead to a new reward. Use this powerful
knowledge with caution.

Intervals can also be modified dynamically. Label modifiers that have an i as a unit
of their modification (for example, +1i or -3i) will change their target’s interval. For
example, in Figure 6.4, the interval of the output of the source A is increased as
more resources arrive in pool B.





FIGURe 6.4
dynamic intervals




Multipliers
When working with random flow rates, it is often useful to combine multiple
chances into one value. For example, a source might have two chances to produce
a resource during every time step. You can represent this with two outputs with a
probable flow rate for each (Figure 6.5, left side), but as long as the probabilities are
equal for each chance, using a multiplier is more convenient. A multiplier is created
by adding n* before the flow rate, for example 3*50%, 2*10%, or 3*D3 (Figure 6.5,
right side). The two constructions are equivalent, but the one on the right is less
cluttered. If you need to use different probabilities, however, you will have to create
a construction like the one on the left.









FIGURe 6.5
multiplying a flow rate


110

Game mechanics: advanced Game desiGn

Like intervals, multipliers can also be modified dynamically. Label modifiers that
have an m as a unit of their modification (for example, +2m or -1m) will change
their target’s multiplier. For example, the multiplier of the input of the drain A in
Figure 6.6 is controlled by the register B. If you run this diagram in the tool and
click A (an interactive drain), it will attempt to drain two items from the pool, with
a 50% chance of success for each one. If you change the value in the B register, you
can raise or lower the number of items that A attempts to drain.
Just like any other label modifier, a label modifier with an m on its own label transmits the change in the source node. Although the value of register B in Figure 6.6 is
the same as that on the resource connection, it doesn’t have to be. If the label modifier’s connection were +2m, it would transmit double the change in B.

FIGURe 6.6
a dynamic multiplier










Delays and Queues
In many games, producing, consuming, and trading resources takes time. The
time it requires to complete an action might be crucial for the game balance. In a
Machinations diagram, a special node can be used to delay the flow of resources as
they travel. A delay is represented as a small circle with an hourglass inside (Figure
6.7).

FIGURe 6.7
Producing soldiers takes time and
resources.

The label on the delay’s output indicates how many time steps a resource is delayed.
(Note that this is different from most labels on resource connections, which ordinarily represent a flow rate.) This time is dynamic. Other elements in the diagram
can change the delay setting through label modifiers. You can also specify a random
delay time using dice notation. A delay can process multiple resources simultaneously. This means that all incoming resources are delayed for the specified number
of time steps irrespective of the number of resources currently being delayed.
A delay can also be turned into a queue. A queue has two hourglass symbols instead
of one. Queues process only one resource at a time. For Figure 6.8, this would mean
that only one resource is passed every five time steps.

cOmmOn mechanisms

111

FIGURe 6.8
Building orders are
queued and executed
one at a time.

Delays and queues can use state connections that communicate the number of
resources they are currently processing (including the number of resources waiting
in a queue to be processed). This can be useful to create timed effects. For example
in Figure 6.9, activating delay A will activate source B for 10 steps. You can activate
the delay as long as there are resources on pool C. A construction like this can be
used to improve the construction discussed for power pills in Pac-Man in the section
“Power Pills” in Chapter 5.

FIGURe 6.9



Using a delay to create
a timed effect







Reverse Triggers
In some games, bad things happen when the player doesn’t have the resources
required by an automatic or randomly triggered element. For example, in Civilization
when the player runs out of gold to pay the upkeep for his cities’ improvements,
the game automatically sells some of them. To simulate this type of event, the
Machinations diagrams include a reverse trigger. A reverse trigger is a state connection that is labeled with a !. If its source node tries to pull resources but cannot pull
all resources as indicated by the source’s input connections, the reverse trigger will
fire its target node. Figure 6.10 illustrates how a reverse trigger can be used to model
the automatic sale of city improvements in Civilization.






FIGURe 6.10







   

automatic sale of a city
improvement when the
player runs out of gold
in Civilization

ChAptEr 6



112

Game mechanics: advanced Game desiGn

Reverse triggers can also be used to trigger end conditions to make a game stop. For
example, in Figure 6.11 this construction is used to end a game when a player takes
more damage after she has lost all hit points. (In the figure the damage is caused by
the user clicking the interactive damage drain. Obviously in most games damage will
be caused by triggers produced by other mechanisms.)

FIGURe 6.11
ending a game when
a player takes damage
when she is out of
hit points.

Color-Coded Diagrams
Machinations diagrams can include color coding to help you distinguish among different types of resources as they flow around. To create a color-coded diagram in the
online tool, simply select the Color-Coded option in the diagram settings dialog in
the side panel.

T I P if you don’t check
the color-coded option
in the tool, you can still
color elements of your
diagram for illustration purposes, but the
simulation will act as
if everything is all the
same color.

In a color-coded Machinations diagram, the color of resources and connections is
meaningful. If a resource connection has a different color than its source, it will
pull only resources of its own color. Likewise, if a state connection has a different
color from its source, it will respond only to the resources of that color and ignore
all other resources. Color-coding allows you to store different resources in the same
pool, and for certain games this is very useful. Later in this chapter, we’ll show how
color-coding can be used to effectively model different unit types in a strategy game.
In a color-coded diagram, one source or converter can produce different colored
resources if its outputs are of a different color than the source or converter itself.
Gates can use different colored outputs to sort resources of different colors.
Figure 6.12 illustrates how color coding can be used. In this figure, source A produces a random number of orange and blue resources every time it is activated. Both
are collected at pool B. The number of orange resources in B increases the number
of blue resources produced at A, and vice versa. The user can activate drain C only
when there are at least 20 orange and 20 blue resources in pool B.

FIGURe 6.12
a color-coded diagram

In a color-coded diagram, a gate can be used to change the colors of resources that
pass it. If the gate has color-coded outputs, it will try to sort resources by their
color, sending red resources along a red output, and so on. However, if the incoming resource color doesn’t match any of the outputs, the gate selects an appropriate
output (based on random numbers if it is a random gate or spreading the resources
according to the weighting of the outputs if it is a deterministic gate) and changes

cOmmOn mechanisms

113

the resource to that color. For example, Figure 6.13 uses this construction to randomly produce red and blue resources with an average proportion of 7/2.

FIGURe 6.13

Delays and queues can use color coding. By giving them outputs with different colors, they will delay resources of the corresponding color by a number of time steps
indicated by that output. For example, Figure 6.14 represents the mechanics of a
game where players can build knights and soldiers. Knights are represented as red
resources, and soldiers are represented as blue resources. Knights cost more gold and
take more time to build.

FIGURe 6.14
Using color coding to
build different units
with one building
queue

Feedback Structures in Games
The structure of a game’s internal economy plays an important role in a game’s
dynamic behavior and gameplay. In this structure, feedback loops play a special
role. A classic example of feedback in games can be found in Monopoly where the
money spent to buy property is returned with a profit because more property will
generate more income. This feedback loop can be easily read from the Machinations
diagram of Monopoly (Figure 6.15): It is formed by the closed circuit of resource and
state connections between the Money and Property pools.

FIGURe 6.15
Monopoly

ChAptEr 6

Producing resources
with random colors

114

Game mechanics: advanced Game desiGn

Closed Circuits Create Feedback
A feedback loop in a Machinations diagram is created by a closed circuit of connections. Remember that feedback occurs when state changes create effects that
ultimately feed back to the original element. A closed circuit of connections will
cause this effect.
A closed circuit of only resource connections (as in Figure 6.16) cannot display very
complex behavior. The resource is pulled through the pools in circles creating a simple periodic system, but nothing more interesting can happen.

FIGURe 6.16
Feedback created by
only resource connections. The resource
simply goes round
and round.









The most interesting feedback loops consist of a closed circuit that mixes resource
connections and state connections. The loop should contain at least one label modifier or activator. For example, the mechanism in Figure 6.17 uses an activator to
maintain the resources in the pool at about 20. It acts the way a heating system does
to keep a room warm in cold climates: It turns on a heater with a fixed output when
the temperature drops below 20. The graph in the same figure displays the temperature over time.

FIGURe 6.17
heater feedback
mechanism using
an activator

charts in machinations diaGrams
Using the online tool for machinations diagrams, it is very easy to produce charts tracking the number of resources in a pool over time. The chart in Figure 6.17 is produced by
the tool. You can add a chart to a diagram like any other element. To start measuring the
number of resources, simply connect a pool to the chart with a state connection. When
selected, this connection is displayed as normal, but when it is not selected, it is reduced
to two small arrows to avoid visual clutter.

cOmmOn mechanisms

115

You can build a similar system using a label modifier instead (Figure 6.18). In this
case, the heater’s output rate is adjusted by the actual temperature, creating a more
subtle temperature curve. This simulates a heater that can produce varying amounts
of heat rather than a fixed amount, as in Figure 6.17.

FIGURe 6.18

ChAptEr 6

heater feedback
mechanism using a
label modifier

Feedback by Affecting Outputs
A feedback loop can also be created by a circuit of connections that affects the output
of an element. For example, consider a Machinations diagram for an air conditioner
(Figure 6.19). The higher the temperature, the faster the temperature is drained.

FIGURe 6.19
an air conditioner
in machinations

Any changes that affect the output of a node can also close a feedback loop. In this
case, output can be affected directly by a label modifier or by a trigger or activator
affecting an element at the end of the resource that is able to pull resources (such as
a drain, converter, or gate, as in Figure 6.20).







FIGURe 6.20





closing a feedback
loop by affecting
the output

116

Game mechanics: advanced Game desiGn

Positive and Negative Feedback basketball
In Chapter 4, we briefly introduced Marc LeBlanc’s concept of positive and negative feedback basketball to explain the effects of positive and negative feedback on
games. In this section, we’ll discuss the idea in more detail and show how to model
it in Machinations.
Positive feedback basketball is played like normal basketball but with the following extra rule: “For every N points of difference in the score, the team that is ahead
may have an extra player in play.” Figure 6.21 shows a model of positive feedback
basketball. It uses a very simple construction to model basketball itself: Every player
on a team has a particular chance to score every time step. Teams initially consist of
five players, so their chance to score is represented as a source with an initial production rate of five (for simplicity, we assume that a basket is worth one point, not
two, and we ignore three-point shots and free throws). Next comes a gate with a
percentage; this indicates the percentage of player attempts that actually succeed in
scoring. As you can see, the blue team is much better than the red team is; the blue
team’s chance of scoring is 40% while the red team’s chance is only 20%. A pool
called Difference keeps track of the difference in the points scored, because every time
blue scores, a point is added to the Difference pool, and every time red scores, a point
is subtracted. Each team can field one more player for every five points that it leads
by—if it’s ahead by five, it gets one more player; if it’s ahead by 10, it gets two; and
so on. The development of the scores and the difference in the scores are plotted
over time in the chart. As you can see, the score of the better team quickly spirals
upward as the difference increases, allowing them to field more and more players.

FIGURe 6.21
Positive feedback
basketball. Team sizes
are prevented from
dropping below 5 by
setting their minimal
value to 5.

In negative feedback basketball, the extra rule is reversed: The losing, rather than
the leading, team can field an extra player for every N points of difference. Again,
this can be easily modeled as a Machinations diagram, simply by reversing the signs
of a few state connections. The chart that is produced by running the diagram is

cOmmOn mechanisms

117

harder to predict. Without looking at Figure 6.22, can you guess what happens to
the points of both teams and the difference in scores?

FIGURe 6.22

ChAptEr 6

negative feedback
basketball

The chart in Figure 6.22 surprised us when we first produced it. Where you might
expect the negative feedback to cause the poorer team to get ahead of the better
team, it never does. What happens is that the negative feedback stabilizes the difference between the two teams. At some point, the poorer team is so far behind that
their lack of skill is compensated for by their team size, and beyond this point, the
difference doesn’t change much.
Another interesting effect of feedback occurs when you have two teams of similar
skill play positive feedback basketball. In that case, both teams will score at a more
or less equal rate. However, once one of the teams by chance takes a lead, the positive feedback kicks in, and they can field more and more players. The result might
look something like Figure 6.23.

FIGURe 6.23
Positive feedback basketball between two
equal teams. notice
the distinctive slope
in the line that depicts
the difference between
the scores after
roughly 30 steps.

118

Game mechanics: advanced Game desiGn

Multiple Feedback loops

T I P Like Monopoly,
Risk is a classic board
game that illustrates
certain principles of
mechanics design well.
if you are not familiar with Risk, you can
download a copy of the
rules at www.hasbro.
com/common/instruct/
risk.pdf. The Wikipedia
entry for Risk also
includes an extensive
analysis.

In the section “Categorizing Emergence” in Chapter 3, we discussed Jochen Fromm’s
typology of emergent systems. According to Fromm, systems with multiple feedback
loops display more emergent behavior than systems with only one feedback loop.
This is also true for games. Most games need more than one feedback loop to provide interesting emergent behavior. The board game Risk is an excellent example of
this. In Risk, no fewer than four feedback loops interact.

the ideal number oF Feedback loops
it is clear that games with multiple feedback loops exhibit more emergence than games
with only one or even no feedback loop at all. however, the ideal number of feedback
loops is much harder to determine. We have found that somewhere between two and
four major feedback loops seems to be sufficient for most types of games. depending on
how complex you want the game to be, you can try more feedback loops, but you have
to be careful not to create a game that is too hard to understand. remember that as a
designer you have a good grasp over the feedback loops that operate within your game,
but your players do not.
another important distinction here is the difference between major and minor feedback
loops. sometimes a feedback loop acts only locally and has little effect on any other
mechanism—a minor feedback loop. in contrast, a major feedback loop involves multiple
important mechanisms of your game and has a much greater impact on the gameplay.
You might have more than four minor feedback loops without complicating the rules too
much, but including more than four major feedback loops will make your game difficult
to master.

The core feedback loop in Risk involves the resources armies and territories: The more
territories a player holds, the more armies he can build. Figure 6.24 depicts this core
feedback loop. The player expends armies to gain territories by clicking the interactive Attack gate. The armies that succeed pass to the converter, which turns them
into territories. The label +1/3 of the label modifier that sets the output flow rate of
the interactive source Build indicates that the output of the source goes up by one
for every three territories the player has.

FIGURe 6.24
The core feedback loop
involving armies and
territories in Risk

When a player gains a territory, he receives a card. These may be collected into sets
and exchanged for more armies. The second feedback loop in Risk is formed by the
cards that are gained from a successful attack (Figure 6.25). Only one card can be
gained every turn, so the flow of cards passes through a limiter gate first. Collecting
a set of three cards can be used to generate new armies. The interactive converter
Trade Cards changes three cards into a random number of armies.

FIGURe 6.25
The second feedback loop in
Risk, involving cards and armies

The third feedback loop is activated when a player manages to capture an entire
continent, which will give the player bonus armies every turn (Figure 6.26). In Risk,
predefined groups of territories form continents as indicated by the design of the
game board. In the diagram, this level of detail is not possible, so instead the construction is represented as a pool connected to another pool with a node modifier.
In this particular case, five territories count as one continent, which will in turn
activate the bonus source.

FIGURe 6.26
The third feedback loop in
Risk : bonus armies through
the possession of continents

Finally, the fourth feedback loop is activated by the loss of territories because of the
actions of other players. Which player chooses to attack which other player depends
on many factors, including the attacker’s position, strategy, and preferences.

119

NOT E in the real
game, not every trio of
cards generates armies,
and some trios generate more armies than
others. We have simplified this by making the
exchange rate of cards
for armies random. in
Figure 6.25, this is indicated by the die symbol
labeling the output
of the Trade cards
converter.

ChAptEr 6

cOmmOn mechanisms

120

Game mechanics: advanced Game desiGn

Sometimes it makes sense to prey on weaker players in order to gain territories or
cards, and sometimes it is important to oppose stronger players to keep them from
winning. The number of continents a player holds has a strong influence on this.
Because continents generate bonus armies, players will generally attack aggressively
to prevent others from keeping a continent (Figure 6.27). The important thing is
that in Risk there is some form of friction caused by other players, and the influence
of this friction increases when the player has captured continents. This type of friction is a good example of the negative feedback that can almost always be found in
multiplayer games where players can act against each other, especially if they are
allowed to collude against the lead player.

FIGURe 6.27
The fourth feedback
loop in Risk : capturing
continents provokes
increased attacks by
other players.

N OT E in the diagram,
the loss of territories
taken by other players’ attacks is indicated
by the multiplayer
dynamic label (an icon
depicting two pawns)
affecting the resource
flow to the Opposition
drain. see table 6.2 for
more information about
this and other types
of nondeterministic
behavior.

FIGURe 6.28
The complete
Risk diagram

Figure 6.28 shows the entire Risk diagram. It does not model the entire game
exactly; like our Pac-Man example in Chapter 5, this is an approximation. See the
“Level of Detail” sidebar.

cOmmOn mechanisms

121

You might have noticed that in the diagram in Figure 6.28, we use different levels of
detail. many of the game’s details are specified by the diagram: You can build one more
army for every three territories, continents give you a bonus of two armies every turn,
