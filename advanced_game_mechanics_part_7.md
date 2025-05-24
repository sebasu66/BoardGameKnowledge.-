and so on. at the same time, some details are omitted: how many armies are generated
by the cards and how many territories are lost to the opposition are both represented by
symbols indicating a random value (the die and the multiplayer dynamic). in addition,
the positive effect on the consumption rate of the opposition drain is not precisely specified. as long as machinations diagrams are purely static, this is not a problem. in this
case, we are just interested in the structure of the mechanics, not in the exact details. For
this structure, it is only important to know that having a continent will cause opponents
to fight more fiercely. in many cases, omitting some of the details makes the structure
easier to understand. however, to run the diagram in the machinations Tool, you would
have to specify these items.

Feedback Profiles
The first three feedback loops in Risk all are positive: More territories or cards lead
to more armies, which lead to more territories and cards. Yet they are not the same:
They have different profiles. The feedback of capturing territories to be able to build
more armies is straightforward, is fairly slow, and involves a considerable investment of armies. Often players lose more armies in an attempt to conquer territories
than they regain with one build. This leads to the common strategy to build during
multiple, consecutive turns. The feedback of cards is much slower than the feedback
of territories. A player can get only one card each turn, and she needs at least three
to create a complete set. At the same time, the feedback of the cards is also much
stronger: A player might get between four and ten armies depending on the set she
collects. Feedback from capturing continents operates faster and more strongly still,
because it generates bonus armies every turn. This feedback is so strong and obvious
that it typically inspires fierce countermeasures from other players.
These properties are important characteristics of the feedback loops that have a
big impact on the dynamics of the game. Players are more willing to risk an attack
when it is likely that the next card they will get completes a valuable set: It does not
improve their chances of winning a battle, but it will increase the reward if they do.
Likewise, the chance of capturing a continent can inspire a player to take more risk
than the player should. In Risk the player’s risks and rewards constantly shift, making the ability to understand these dynamics and to read the game a critical skill.
These three positive feedback loops play an important role, but simply classifying
them as positive does not do justice to the subtlety of the mechanics. It is important
to understand how quickly and how strongly each operates.

ChAptEr 6

leVel oF detail

122

Game mechanics: advanced Game desiGn

Seven Feedback Characteristics
Table 6.1 lists seven characteristics that, together with the determinability characteristic discussed next, form a more detailed profile of a feedback loop. At first
glance, some of these characteristics might seem as if they overlap, but they do not.
It is easy to confuse positive feedback with constructive feedback and negative feedback with destructive feedback. However, positive destructive feedback does exist.
For example, losing pieces in a game of chess will increase the chance of losing more
pieces and losing the game. Likewise, in Civilization, the growth of a city is slowed
down by the corruption that is caused by large cities: negative feedback on a constructive effect.

TAble 6.1
seven characteristics
of Feedback

cOmmOn mechanisms

123

The strength of a feedback loop is an informal indication of its impact on the game.
Strength cannot be attributed to a single characteristic; it is created by the interactions of several. For example, permanent feedback with a little return can have a
strong effect on the game.

The profile of feedback created by direct interaction in a multiplayer game, such
as the ability to target specific players for an attack in Risk, can change depending
on the players’ strategies. Feedback from direct interaction often is negative and
destructive: Players act against, or even conspire against, the leader. At the same
time, it can turn into positive and destructive feedback when someone starts to prey
on the weaker players.
Feedback characteristics can be read from a Machinations diagram, although this
is easier for some characteristics than it is for others. In general, use the following
guidelines:
To determine a feedback loop’s effect, look at how it is connected to different
end conditions. If the feedback mechanism is directly connected to a winning condition, it is probably constructive; if it is directly connected to a losing condition,
it is probably destructive.

n

A feedback loop’s investment can be determined by looking at how many
resources are consumed to activate the mechanism. In addition, feedback mechanisms that require players to activate many elements usually have a high
investment, as these mechanisms generally require more time or turns to activate.

n

A feedback loop’s return can be determined by looking at how many resources
are produced by the mechanism. Return must be compared to investment to paint
a complete picture.

n

n The speed of a feedback loop is determined by the number of actions and elements involved to activate the feedback loop. Feedback loops that contain delays
and queues are obviously slower than those loops that do not include these elements. Feedback loops that involve only automatic nodes tend to be faster than
feedback loops that include many interactive nodes. Likewise, in most cases, feedback loops that consist of mostly state connections tend to be faster than feedback
loops that consist of mostly resource connections.

The range of a feedback loop is easily determined by the number of elements it
consists of. Feedback loops that consist of many elements have a high range.

n

ChAptEr 6

Changes to the characteristics of a game’s feedback loops can have a dramatic effect
on the game. Feedback that is indirect and slow but with a lot of return and not
durable has a strong destabilizing effect. In this way, even negative feedback can be
used to destabilize a system if it is applied erratically or when its effects are strong
but slow and indirect. It means that at a much later point in the game something
big will happen that is difficult to predict or prevent.

124

Game mechanics: advanced Game desiGn

Most feedback loops are fundamental parts of their game’s economy, so their
durability is extended or permanent. To identify a feedback loop with limited durability, see whether any part of the loop depends on limited resources that can never
be recovered or are recovered only at long intervals.

n

The feedback loop’s type is probably the trickiest characteristic to determine
simply by looking at a Machinations diagram. Positive label modifiers affecting the
flow of production mechanisms create positive feedback, but positive label modifiers affecting the flow toward a drain or a converter tend to create negative feedback.
The type of feedback is much harder to determine when the feedback loop involves
activators. To determine the type of a feedback mechanism, you must really consider the entire mechanism and all its details.

n

Determinability
In many games, the strength of a feedback loop is affected by factors such as chance,
player skill, and the actions of other players. Machinations diagrams represent these
factors by different symbols that stand for nondeterministic mechanisms. Table 6.2
lists the symbols used to indicate different types of nondeterministic behaviors.
You can use these icons to annotate connections and gates in a diagram. A single
feedback loop can be affected by multiple and different types of nondeterministic
resource connections or gates. For example, the feedback through cards in Risk
(Figure 6.25) is affected by a random gate and a random flow, increasing its unpredictability. The loss of territories is affected by a multiplayer dynamic, namely,
attacks by other players.

TAble 6.2
Types of
determinability

cOmmOn mechanisms

125

FIGURe 6.29
Tetris

usinG nondeterministic symbols
in the machinations tool
You can use the symbols for deterministic behavior in digital machinations diagrams.
if you set the label of a connection to D, it will display a dice symbol. The multiplayer
symbol is created by setting the label to M, the player skill symbol is created by setting
the label to S, and the strategy symbol is created by setting the label to ST (for strategy).
Because the machinations Tool cannot actually simulate the effects of player skill or
other players’ actions, functionally these symbols all work the same way when the tool
is running: They produce a random value from 1 to 6. By changing the diagram settings,
you can specify other values as you wish. even though they work the same way, Joris
dormans has provided the nondeterministic symbols so that the diagrams are easier to
read. When you see the joystick symbol, you know that it stands for effects influenced by
variations in player skill.

ChAptEr 6

The skill of a player in performing a particular task can also be a decisive factor in
the nature of feedback, as is the case in many computer games. For example, Tetris
gets more difficult as the blocks pile up, and the rate at which players can get rid
of the blocks is determined by their skill. Figure 6.29 shows this as an interactive gate that controls a converter. Skillful players will be able to keep up with the
game much longer than players with less skill. Here player skill is a factor on the
operational or tactical level of the game. In games of chance, tactics, or games that
involve only deterministic feedback, a whole set of strategic skills can be quite decisive for the outcome. This feedback loop in Tetris is also affected by randomness.
The shape of the block is randomly determined by the game. Although the skill is
generally more decisive in Tetris, the player just might get lucky.

126

Game mechanics: advanced Game desiGn

Randomness vs. Emergence
Games with many random factors become hard, if not impossible, to predict. In
games that have too many random factors, players often feel that their actions have
little impact on the game. One of the strengths of creating games with emergent
gameplay is that most of the dynamic behavior of the game arises from the complexity of the systems, not from the number of dice rolled.
It is our conviction that a well-designed game relies on pure chance only sparingly.
A game with only a few deterministic feedback loops can show surprisingly dynamic
behavior. When you use emergence rather than randomness to create dynamic
gameplay with uncertain outcomes, all decisions made by the player will matter.
This encourages her to pay attention and engage with the game.

Frequency and impact oF randomness
When using randomness, you should be aware of how its frequency and impact affect
the game. The impact of the randomness of a mechanic is often related to the range and
distribution of random numbers created. For example, in some board games, players roll
one die to move, and in others they roll two. With one die, they have an equal chance of
moving from 1–6 spaces. With two, they can move much farther, from 2–12 spaces, but
the probability distribution is not equal; they are more likely to roll a 7 than any other
number.
When designing games of emergence, it is almost always best to aim for random mechanics that operate frequently but have a relatively low impact on the game. increasing
the frequency of a random mechanism is generally a good way of reducing its impact:
You can expect that in the long run the odds even out.

There are two situations in which adding randomness is a useful design strategy:
It can force players to improvise, and it can help counter dominant strategies.

Use Randomness to Force Improvisation
Many games use randomness to create a situation in which the player is forced to
improvise. For example, the random maps generated for games such as Civilization
and SimCity create new and unique sets of challenges each time players start a new
game. In the collectible trading card game Magic: The Gathering, each player builds
his own deck by selecting 40 or so cards from his collection. But every time he starts
a new game, he needs to shuffle them. Players might control the cards in the deck,
but they must deal with them in a random order. Planning and building your deck
is one part of the skill that goes into playing Magic: The Gathering. Improvising and
spotting opportunities as they occur while the game develops is another.

cOmmOn mechanisms

127

Improvisation works very well in a game that offers a random but level playing field
for all players. If a game generates random events that affect all players equally, the
decisive factor in dealing with the events comes from the players’ reaction to and
preparation for these events. Many modern, European-style board games tend to use
randomness in this way.

FIGURe 6.30

ChAptEr 6

Power Grid, German
edition. image courtesy of Jason Lander
under a creative
commons (cc BY 2.0)
attribution license.

128

Game mechanics: advanced Game desiGn

randomness Vs. emerGence in modern board Games
modern, european-style board games are often designed to create dynamic systems in
which players’ skill and strategy are more decisive than luck is. an excellent example is
the game Power Grid (Figure 6.30). in this game, players buy fuels to produce energy and
sell the energy to a growing network of cities connected to their power grid. There are
only two random factors in the game: The initial player order is randomly determined,
and a shuffled deck of cards determines what power plants are available for players to
buy. The game has mechanisms in place to counter the effects of this initial randomness:
With each turn the player order is changed in such a way that is disadvantageous to the
players in the lead (a form of negative feedback), and for the most part, only the cheaper
power plants are available, and the most expensive ones are returned to the deck (to
come back for the end game). none of the decisions players make during a game involves
rolling dice or other random factors. Buying power plants requires a player to outbid
her opponents, which is a multiplayer dynamic mechanism but not a random one. many
other popular and critically acclaimed board games, such as Puerto Rico, Caylus, and
Agricola, are similar in this respect. each of these games’ mechanics are worth analyzing.

Use Randomness to Counter Dominant Strategies
A dominant strategy is a course of action that is always the best one available to a
player in all circumstances. (It doesn’t guarantee that the player will win; it’s just his
best option.) As a designer, it is essential to avoid setting up mechanics that establish
a dominant strategy. Games with a dominant strategy aren’t any fun to play, because
the players end up doing the same thing over and over again. If you have a dominant strategy in your game, you need to balance your mechanics better (which we’ll
discuss in Chapter 8). Sometimes this is too difficult or too time-consuming. In that
case, adding more randomness to the mechanism can be an easy way out.
For example, consider the following simple two-player, energy-harvesting game.
Each player starts with a harvester that collects 0.1 energy every turn. Players can
buy an additional harvester by spending three energy, which increases their harvesting rate. The goal is to collect 30 energy, and whoever collects it first wins. In Figure
6.31, two players (red and blue) are playing. Red’s strategy is to spend all energy
to build seven new harvesters before starting to collect energy. Blue’s strategy is to
build two new harvesters before collecting.
Because this game is completely deterministic, the outcome is always the same: Red
wins every time. With her strategy, it will take her 119 turns to collect 30 energy,
while it will take blue, with his strategy, 146 turns to collect 30 energy. In fact, if we
use a Machinations diagram to determine the time it takes to collect 30 energy for
all possible options to build between 0 and 11 harvesters, it should become clear
that building 7 extra harvesters is the dominant strategy: It simply allows the player
to get to the goal the fastest (Table 6.3).

cOmmOn mechanisms

129

FIGURe 6.31

NOT E You might
recognize the pattern
in the chart from
the section “Longterm investments vs.
short-term gains” in
chapter 4. it’s the same
phenomenon.

S T R AT EG y ( N u m b e r o f
Additional Harvesters Built)

T u R N S R EQ u I R E D
T O CO M P l E T E G O A l

0

300

1

181

2

146

3

133

4

125

5

121

6

120

7

119

8

120

9

120

10

121

11

121

12

122

TAble 6.3
comparison of the
different strategies
in the deterministic
harvesting Game

Randomness can be used to break this pattern. If the same game were played but
instead of harvesting 0.1 energy every turn, a harvester would increase the chance
that energy is harvested by 10%, the results completely change. Figure 6.32 shows
a sample run of the harvesting game set up in this way. From simulating and running this game 1,000 times, we determined that now blue has roughly a 15%
chance to win.

ChAptEr 6

a simple deterministic
harvester game. red
wins all the time.

130

Game mechanics: advanced Game desiGn

FIGURe 6.32
The random harvester
game. now blue has a
15% chance to win.

Example Mechanics
In this section, we’ll discuss some mechanics commonly found in games across different genres. We’ll use Machinations diagrams to show how these mechanics can
be modeled, but we’ll also use the diagrams to discuss the mechanisms themselves
in more detail. You can also find digital versions of all these examples online.
When reading through the example mechanics, you will notice that we often isolate
and model different mechanisms individually. This is done partly because models of
complete games grow complex very quickly. It would be difficult to grasp all these
mechanics from a single diagram for a game, especially because the printed diagrams in the book are static. In many cases, it is simply not necessary to look at all
the mechanics in a game to understand the most important ones. After all, games
are often built from several dynamic components. Thoroughly understanding each
component is the first and most important step toward understanding the dynamic
behavior of a game as a whole, even when (as in most games of emergence) the
whole is definitely more than the sum of its parts.

cOmmOn mechanisms

131

Power-Ups and Collectibles in Action Games
The gameplay of action games emerges primarily from interesting physics and good
player interaction. The levels of many action games are fairly linear: The player
simply needs to perform a number of tasks, each with a certain chance to fail. His
objective is to reach the end of a level before running out of lives. Figure 6.33
represents a small level for an action game with three tasks (A, B, and C). Each is
represented by a skill gate that generates a number between 1 and 100. The player
is represented by a resource that moves from pool to pool. If the player fails to perform a task, there are two options: Either he dies (as is the case with tasks A and C)
or he is sent back to a previous location in the level (as is the case with task B).
Level progression in an
action game

Most action games are more than just a series of tasks, however. They usually have
an internal economy that revolves around power-ups and collectible items. For
example, in Super Mario Bros., the player can collect coins to gain extra points and
lives, while power-ups grant the player special powers, some of which have a limited
duration. Power-ups and collectibles can be represented in Machinations diagrams
by resources that are harvested from certain locations. Figure 6.34 shows how this
might be modeled using different colored resources to indicate different power-ups
or collectibles. In this diagram, the player must be present at a certain location to
be able to collect the power-up. This diagram also shows how power-ups and collectibles can be used to offer players different strategic options. In this case, the
player can progress through the level quickly and fairly easily if she goes from location I to II and V immediately. However, she can also opt for the more dangerous
route through III and IV, in which case she can collect one red and two extra yellow
resources.

ChAptEr 6

FIGURe 6.33

132

Game mechanics: advanced Game desiGn

FIGURe 6.34
collecting power-ups
from different locations
in an action game
(lives are omitted from
this diagram)

T I P in Figure 6.34,
the blue power-up and
the task that requires it
constitute an example
of a lock-and-key
mechanism. Lockand-key mechanisms
are the most important mechanisms that
games of progression
use to control how
a player progresses
through a level. Lockand-key mechanisms
rarely incorporate
feedback loops and
so seldom exhibit
emergent behavior. We will examine
lock and key mechanisms in more detail in
chapter 10, “integrating
Level design and
mechanics.”

Power-ups might be needed to progress through a game, and in that case, finding
the right power-ups is a requirement to complete a level. Other power-ups might
not be needed but are helpful all the same; in this case, the player must decide how
much risk she will take to collect one and how much she stands to gain from it. For
example, in Figure 6.34, the blue power-up is required to perform the final task to
complete the level, while the red power-up makes that task a little easier.

limited-duration poWer-ups
Power-ups frequently operate for only a limited amount of time. The construction in
Figure 6.35 shows how you can use delays to create a temporal power-up to aid in a task.
The power-up respawns to be available again after it has been consumed.

FIGURe 6.35 Limited-duration power-up

cOmmOn mechanisms

133

Collectibles also offer a player a strategic option. For example, if the player must risk
lives to collect coins and must collect coins to gain lives, the balance between the
effort and risk the player takes and the number of coins to be collected is crucial. In
this case, if a player has collected nearly enough coins to gain an extra life, taking
more risk becomes a viable strategy. Figure 6.36 represents this mechanism. Note
that it forms a feedback loop. In this case, the feedback is positive, but the player’s
skill determines whether the return on the investment is enough to balance the risk
she takes.

FIGURe 6.36

ChAptEr 6

Feedback in collecting coins that gain new
lives

Racing Games and Rubber banding
Racing games can be easily framed in economic terms as a game where the player’s
objective is to “produce” distance. The first player to collect enough distance wins
the game. Figure 6.37 illustrates this mechanism. Depending on the implementation, the production mechanism might be influenced by chance, skill, strategy, the
quality of the player’s vehicle, or any combination of these factors. The Game of
Goose is an example of a racing game in which chance exclusively determines the
outcome of the game. Most arcade racing video games rely heavily on skill to determine a winner. More representative racing games that include vehicle tuning will
probably involve some long-term strategy as well.

FIGURe 6.37







A simple racing mechanism as represented in Figure 6.37 has a huge disadvantage. If
skill or strategy is the decisive factor, the outcome of the game will nearly always be
the same. Consider the mechanisms in Figure 6.38. It shows two players racing, and
their skill is represented by different chances to produce distance. The chart displays

racing mechanism

134

Game mechanics: advanced Game desiGn

a typical game session and indicates spreads of possible outcome. Obviously, the
blue player is going to win nearly all the time.

FIGURe 6.38
an unequal race

N OT E We have intentionally implemented
an extreme form of rubber banding to make
it more visible. real
games would use more
subtle boosting.

FIGURe 6.39
rubber banding with
strong and durable
negative feedback

Many racing games use a technique called rubber banding to counter this effect.
Rubber banding is a technique of applying negative constructive feedback based on
the distance between the player and his artificial opponents in order to make sure
that they stay close. We have seen a construction like this already with LeBlanc’s
example of negative feedback basketball. In that discussion, we pointed out that
while negative feedback used like this might keep the players close together, it will
not really make a poorer player win more often. However, there are adjustments
that can be made to the rubber-banding mechanism to change that. If the negative feedback is made stronger and lasts for a time, its effects are changed. Figure
6.39 represents this type of rubber banding. The blue player has a skill level of 60%,
while the red player has a skill level of 40%, so blue generates distance more quickly
than red. The register at the right computes the difference in distance and, depending on which one is ahead, will signal their Boost source to generate a boost. The
boost lasts for 20 time steps, and each boost will improve the player’s performance
by 5%. The chart displays a typical game session that results from this mechanism.
Note that the chart shows a race in which red and blue take the lead alternately.

cOmmOn mechanisms

135

RPG elements
Many games allow players to build up and customize the attributes of their avatars or of a party of characters. Often the mechanics involved are referred to as RPG
elements of the game. In this economy, skills and other attributes of player characters are important resources that affect their ability to perform particular tasks. The
most important structure of the RPG economy is a positive feedback loop: Player
characters must perform tasks successfully to increase their abilities, which in turn
increases their chance to perform more tasks successfully.

ChAptEr 6

In classic role-playing games, experience points and character levels act as separate
resources that structure the economy. Figure 6.40 shows how these mechanics might
be modeled for a typical fantasy role-playing game. In this case, the player can perform
three different actions: combat, magic, and stealth. Successfully executing these
actions will produce experience points. When a player has collected 10 experience
points, he can level up. The experience points are converted into a higher character level and two upgrades that he can use to increase his abilities. (In some games,
experience points are not consumed, but trigger upgrades at stated thresholds. You
can do this with a source that produces upgrades and an activator to fire it.) To spice
up things a little, this diagram also contains a construction that occasionally increases
the difficulty of the tasks. Using color-coding, the difficulty of each different task progresses differently. Normally a dungeon master (in the case of a tabletop role-playing
game) or the game system would make sure players are presented with suitable tasks.

FIGURe 6.40
rPG economy with
experience points
and levels

136

Game mechanics: advanced Game desiGn

In Figure 6.40, the positive feedback loop is countered partially by a negative feedback loop that is created by increasing the number of experience points required to
reach the next level every time the player levels up. This is a common design feature
in the internal economies of many role-playing games. Such a structure strongly
favors specialization: As players need more and more experience points to level
up, they will favor the task they are better at, because these tasks will have a bigger
chance to produce new experience points. This can be countered by applying negative feedback to the upgrade cost or impact for each ability separately (Figure 6.41),
either instead of, or in addition to, the increasing costs to level up.

FIGURe 6.41





alternative ways of
applying negative
feedback in an rPG
economy











 



  

Some RPG economies work differently; they give experience points whether an
action succeeds or not. For example, in The Elder Scrolls series, performing an action
often increases the player character’s ability, even if that action is unsuccessful. In
The Elder Scrolls, negative feedback is applied by requiring the action to be performed more times in order to advance to the next level of ability. This type of
mechanism is illustrated in Figure 6.42.

FIGURe 6.42


  

an rPG economy
without experience
points controlled by
the player















FPS economy
At the heart of the economy of most first-person shooters there is a direct relationship between fighting aggressively (thus consuming ammo) and losing health. To
compensate for this, enemies might drop ammo and health pick-ups when they are

cOmmOn mechanisms

137

killed. We’ll show how to model this structure in a Machinations diagram in two
steps (Figure 6.43 and Figure 6.44).

FIGURe 6.43
ammunition and enemies in an FPs game

Figure 6.44 adds player health to the diagram. In this case, poor performance by
the player when engaging an enemy (such as when a number below 75 is generated
by the skill gate) activates a drain on the player’s health. In addition to dropping
ammunition, there now is also a 20% chance a killed enemy drops a medical kit
(medkit) that the player can use to restore health.

FIGURe 6.44
health added to the
FPs game economy.
skill gates and random gates generate
numbers between 1
and 100.

ChAptEr 6

In the first step, ammunition is represented by a pool of resources. When the player
chooses to engage an enemy, he wastes between two and four ammunition units
and has a chance to kill an enemy. This is modeled by the skill gate between the
Engage and Kill drains. In this case, the skill gate is set to generate a random number between 1 and 100 every time it fires. If the generated value is larger than 50,
the Kill drain is activated, and one enemy is removed. The register labeled Skill can
be used to increase or decrease this chance; it can be used to reflect more or less
skilled players. Once an enemy is killed, a similar construction is used to create a
50% chance that five more ammunition resources are generated by the Drop Ammo
source, which go into the Ammo pool. To keep things interesting, new enemies are
spawned occasionally.

138

Game mechanics: advanced Game desiGn

Analyzing the mechanics in Figure 6.44 reveals that in the basic FPS game economy
there are two related positive feedback loops. However, the effectiveness of the return
of each feedback loop depends on the skill of the player. A highly skilled player
will waste less ammunition, lose less health, and gain ammunition from engaging
enemies, whereas a poorly skilled player might be better off avoiding enemies. The
amount of ammunition a player needs to kill an enemy and the chance that killed
enemies drop new ammunition or medkits obviously is vital for this balance.
You could add a number of additional feedback loops to make this basic game
economy more complex. For example, the number of enemies might increase the
difficulty of killing enemies or increase the chance players will lose health fighting
them, thus creating positive destructive feedback (a downward spiral). Negative
constructive feedback could be created by having the player’s ammunition level
negatively impact the player’s chance of killing an enemy. Players with little ammunition would magically fight a bit better, while those with a lot wouldn’t fight quite
so well. This would tend to damp down the effect of large fluctuations in ammunition availability.

RTS Harvesting
In a real-time strategy game, you typically build workers to harvest resources.
Figure 6.45 represents a simple version of this mechanism with only one resource:
gold. In this case, gold is a limited resource. Instead of using a source, the available
gold is represented with a pool named Mine that starts with 100 resources. Note that
the pool is made automatic so that it starts pushing gold toward the player’s inventory (the pool named Gold). The flow rate is determined by the number of workers
the player has. Building workers costs two gold units. Note that the converter to
build workers pulls gold only when there are two gold available: It is in “pull all”
mode as indicated by the & sign.
S

cOmmOn mechanisms

139

Most real-time strategy games have multiple resources to harvest, forcing players
to assign different tasks to their workers. Figure 6.46 expands upon the previous
one to include a second resource: timber. In this diagram, players can move workers between two locations by activating the two pools representing those locations.
Workers in each location contribute to the harvesting of one of the resources. In
this case, timber is also a limited resource (the Forest pool). The initial harvesting
rate for timber is slightly higher than the harvesting rate for gold. However, as the
workers clear the forest, the harvesting rate drops because they have to travel longer distances (you might recognize this situation from Warcraft). This mechanism
is modeled by applying a little negative feedback on the harvesting rate of timber
based on the number of resources left in the forest.
mining gold and harvesting timber

RTS building
In real-time strategy games, all those resources are harvested for a reason: You need
them to build your base and military units. Figure 6.47 illustrates how resources
can be used to construct a number of buildings and units. The diagram uses colorcoding, and each unit type has its own color. Soldiers are blue, and archers are
purple. Building types have their own color too: Barracks are blue, the mill is purple,
and towers are red. Different colored activators are used to create dependencies
between the building options: You need a barracks to be able to build units and a
mill to produce archers and towers.

ChAptEr 6

FIGURe 6.46

140

Game mechanics: advanced Game desiGn

FIGURe 6.47
rTs building
mechanics

RTS Fighting
N OT E remember
that a state connection always tracks
changes in the node
that is its origin. in
Figure 6.48, the state
connections reduce the
multipliers that they
point to because their
origin pools are being
drained.

An efficient way of modeling mechanics for combat between units is to give every
unit a chance to destroy one unit of the opposition in each time step. This is best
implemented with a multiplier. Figure 6.48 illustrates this mechanism. It features
generic units from two armies (red versus blue), each in a pool; blue has 20 units,
and red has 30. Every unit has a 50% chance of destroying an enemy unit in each
time step. This is implemented with a state connection from the pool (the dotted line marked +1m) that controls how many units the blue army will try to drain
from the red army, and vice versa. As blue has 20 units at the beginning of the run,
the resource connection between the red pool, and its drain reads 20*50%—that is,
the 20 blue units each have a 50% chance of killing (draining) a red unit. Similarly,
the 30 red units each have a 50% chance of killing a blue unit. In the first time step,
the calculation will run, and some number of each armies units will be drained. The
state connection will then update the flow rate of the resource connection to reflect
the new number of units in each pool.

cOmmOn mechanisms

141

FIGURe 6.48

playinG around With numbers
You should take some time to play around in the machinations Tool with simple constructions like the fighting mechanism of Figure 6.48. it trains your understanding of dynamic
systems. For example, can you predict whether blue’s chances of winning increase when
each side’s chance to destroy an enemy each time step is lowered to 10% per unit? Or
if blue’s chances increase if there are fewer units on each side, even if their relative
strength is the same?
Figure 6.49 was produced from a run with both sides starting with 20 units and a 10%
chance of destroying an enemy. studying this chart reveals a widening gap between
the red and blue units starting roughly halfway through. By now, you should be able to
attribute this shape to a positive feedback loop kicking in after blue takes a decisive lead
in the battle. in some runs of this diagram, the feedback takes effect immediately leaving
the winner with many units; in other runs, the feedback never matters much, and the two
sides stay close until the very end, leaving the winner with only a few units.

FIGURe 6.49 a chart mapping the battle between 20 red and blue units

ChAptEr 6

Basic combat in a realtime strategy game

142

Game mechanics: advanced Game desiGn

We can expand this basic combat construction in two ways. First, we can take into
account different unit types by using color coding. For example, we might distinguish between stronger and weaker offensive units by having each type of unit
activate a different drain. This is illustrated in Figure 6.50. Blue units have more
offensive power than green units, because they have a higher chance of destroying
an enemy.

orthoGonal unit diFFerentiation
ideally, every type of unit in a real-time strategy game should be unique in some way
and not just a more powerful (but otherwise identical) version of another unit. This
design principle is called orthogonal unit differentiation and was first introduced by
designer harvey smith at the 2003 Game developers’ conference (smith 2003). in Figure
6.50, the blue units have a greater chance of defeating an enemy than the green units,
but they are otherwise identical, so they violate this principle. One way to (slightly)
improve the design would be to lower the price of the blue units but also to make them
available only after constructing an expensive building. This would differentiate their
impact on the game: investing in the blue units presents the player with a considerable
risk and with a potential high reward against the fairly low-risk and low-gain strategy of
going for green units.

FIGURe 6.50
combat with different
unit types

We can also add the ability to switch between offensive and defensive modes. This
can be modeled using two different pools for attack and defense (Figure 6.51). By
moving units from the defense to the attack, you start attacking your enemy. In this
case, color coding can be used to prevent immobile units (such as towers or bunkers)
from rushing toward the attack.

cOmmOn mechanisms

143

FIGURe 6.51
Offensive and defensive modes

ChAptEr 6

Technology Trees
Real-time strategy games, but also simulation games like Civilization, often allow the
player to spend resources to research technological advances that will give him an
extra edge in the game. These constructions are usually referred to as technology trees
and often add interesting long-term investments to a game’s economy. More often
than not, the technology tree involves multiple steps and many possible routes to
various advancements; these technology trees constitute interesting internal economies in their own right.
To model technology trees, you should use resources to represent technological
advances and have these resources unlock new game options or improve old ones.
Figure 6.52 illustrates how a technology tree can be used to unlock and improve the
abilities of a new unit type in a strategy game. The player can start building knights
only after he researches one level of knight lore. Every level of knight lore also
increases the effectiveness of the knights, although the research gets more and more
expensive for every level. In this example, researching knight lore requires a considerable investment but rewards the player with stronger units.

FIGURe 6.52
adding research to a
strategy game

144

Game mechanics: advanced Game desiGn

In some technology trees, players can research each technology only once; however,
many technologies require the player to have researched one or more technologies
before. For example, Figure 6.53 represents a technology tree that is not unlike the
one found in Civilization. Keep in mind that the effect of having a particular technology is omitted from this diagram. However, it is easy to imagine that technologies
such as the alphabet and writing increase the resources available for research. In
this diagram, the red connections enforce the order in which technologies must
be researched, while the blue construction keeps track of the number of resources
developed and adjusts the research prices accordingly.

FIGURe 6.53
a Civilization-style
technology tree

Summary
In this chapter, we introduced a few additional features of the Machinations
Tool and then took a much closer look at two important mechanics design tools:
feedback loops and randomness. We explained seven different characteristics of
feedback: type, effect, investment, return, speed, range, and durability. Each of these
has a distinct effect on the behavior of an internal economy.
In the section “Randomness vs. Emergence,” we showed how you can use randomness to create unique situations that force players to improvise. We also explained
that randomness can help prevent dominant strategies: Because randomness
changes a game’s state unpredictably, you are less likely to create a game in which
one strategy is always the best one.
We ended the chapter with an extensive discussion of ways to use Machinations
diagrams to model economic structures in traditional genres of video games.

cOmmOn mechanisms

145

Machinations can simulate some of the key economies found in action games,
role-playing games, first-person shooters, and real-time strategy games.
In the next chapter, we’ll discuss the important topic of design patterns, which are
familiar structures that you can use to create and test mechanics quickly.

Exercises
1. Find a way to include an extra negative feedback loop in Monopoly.
2. Create a game in which all random effects affect all players equally.
feedback yet remains fair.

4. Create a diagram for the major feedback loops in a published game.
5. Prototype and playtest a game with one feedback loop. Keep adding feedback
loops of different signatures until you have an enjoyable, well-balanced game that
exhibits emergent behavior. Prototype and play test every step. How many feedback
loops are required?

6. In each of the following four diagrams, what will be the production rate of the
automatic source at the upper left after clicking the interactive node A exactly once?








































 
















 



 

















ChAptEr 6

3. Design the mechanics for a racing game that involves positive, constructive

146

Game mechanics: advanced Game desiGn

7. In each of the following five turn-based diagrams, how many turns will it take
to accumulate 10 resources in pool A? (In the Machinations Tool, you would also
need an interactive node labeled End Turn to end a turn, but try to figure it out
for yourself.)











































8. In each of these two color-coded diagrams, what is the minimum number of
clicks required to win the game?

ChAptEr 7
Design patterns
In this chapter, we address the concept of design patterns and show how you can
use the Machinations Tool to build a library of useful patterns. Because there have
been many efforts to identify design patterns in the past, the first part of the chapter gives some of the history and theory of the subject. Next, we’ll show you how
Machinations diagrams are effective tools to capture and represent these patterns.
Finally, we’ll discuss how you can use these patterns to become a better game designer.

Introducing Design Patterns

FIGURe 7.1 Monopoly

ChAptEr 7

In earlier chapters, you looked at diagrams representing many different games.
You might have noticed that some diagrams look remarkably similar. For example,
we used Figure 7.1 to illustrate a feedback loop in Monopoly, and Figure 7.2 shows
a single player version of the Harvester game we described in Chapter 6, “Common
Mechanisms.” If you ignore the Pass Go source and Pay Rent drain in Figure 7.1 and
rotate the remaining nodes 90 degrees counter-clockwise, you will discover that
although the details in the labels are different, both feedback loops are the same:
A source feeds a pool at a particular production rate. Resources from the pool can be
converted into a new type of resource that increases the production rate of the source.

FIGURe 7.2 The harvester game

If you look closely at the other examples in Chapter 6, you might spot similar
structures a few more times. Risk contains a similar feedback loop, too. This is not a
coincidence, nor is it likely that the designers of Risk deliberately stole the mechanics of Monopoly. The similarity between the structures simply means that this particular
pattern in game mechanics works for many games. There are many more patterns in
game mechanics that are found across many different kinds of games.

147

148

Game mechanics: advanced Game desiGn

We call recurrent patterns in the structure of game mechanics design patterns. The
architect Christopher Alexander first introduced the idea of design patterns in his
book A Pattern Language (1979). That work inspired others to create design patterns
for software engineering, and they have become a popular tool in that field. Design
patterns for games, as we describe them here, follow the same lines as those used in
architecture and software engineering.

A brief History of Design Patterns
Alexander and his colleagues originally identified design patterns in an attempt to
capture objective standards of quality in architecture. They documented the patterns
they found to help architects design good buildings. As Alexander himself put it,
“There is a central quality which is the root criterion of life and spirit in a man, a
town, a building, or a wilderness. This quality is objective and precise but it cannot
be named” (Alexander 1979, p. ix).

Good desiGn
People call things good when they like them. “Good“ is often thought to be a personal
and subjective value judgment. What one person calls a “good game” might not appeal
to another. however, many critics of games, films, books, or architecture feel that certain
products are objectively better than others. They think their evaluations are more than
just matters of personal taste (and if they don’t, they should reconsider their choice of
profession). in all fields of art and design, games included, we work with assumption that
at least some aspects of a game can be evaluated objectively. Our opinions might not be
universally accepted, but they’re more than a simple matter of personal taste. Learning
about design patterns for games will help you understand the characteristics that good
games possess.

Alexander describes an entire library of patterns for architecture, which he calls a
pattern language. Each pattern represents a solution to a common design problem.
These solutions are described as generically as possible so that they may be used
in different circumstances. The patterns are all described in the same format. Each
pattern also has connections to larger and smaller patterns within the language.
Smaller patterns help to complete larger patterns. The works of Alexander describe
more than 100 different patterns across a few different domains within architecture
(from urban planning to individual buildings).

desiGn PaT Terns

149

This idea was transferred to the domain of software design by Erich Gamma, Richard
Helm, Ralph Johnson, and John Vlissides (known to the software engineering community as the “Gang of Four”) in their seminal book Design Patterns: Elements of
Reusable Object-Oriented Software (1995). Within software engineering, the principles
of object-oriented programming take the place of Alexander’s unnamed quality. By
identifying software design patterns, they created a common vocabulary for programmers to discuss object-oriented software features that they all knew about but
had no names for. This made it easier for developers to work together but also to
create better code. The Gang of Four also organized their pattern language into a set
of interrelated patterns that describe generic solutions to common design problems.
The original set contained about 20 patterns. Over the years, a number of patterns
have been added, while a few have been removed. Today the set of core patterns for
software design remains relatively small.

We are not the first to draw inspiration from Alexander and apply the idea of design
patterns to game design. Many designers and researchers have noted that game
designers have no generally accepted design vocabulary that efficiently allows them
to share and discuss ideas. In a 1999 Gamasutra article “Formal Abstract Design
Tools, ” designer Doug Church set out to create a framework for a common vocabulary for game design. According to Church, “formal” indicates that the vocabulary
needs to be precise, and “abstract” indicates the vocabulary must transcend the particular details of a single game. For Church the vocabulary should function as a set
of tools, in which different tools are suited for different tasks, and not all tools are
applicable for a given game.

desiGn patterns Vs. desiGn Vocabularies
The notions of design patterns and design vocabularies are sometimes used interchangeably. The approaches are similar but not identical. design patterns and design
vocabularies try to both capture and objectify essential characteristics of games, but
design patterns are intended to help people create good games (or program code or
buildings), while design vocabularies try to remain more neutral and less prescriptive
(especially when they are used in an academic context). There is something to say for
both approaches, but in this book we choose the design pattern approach because it is
of more practical use to designers. We don’t just look at design patterns as interesting
phenomena found in games; they’re tools for making better games. however, some might
point out that, because of its more prescriptive nature, a pattern language can be more
restrictive. We’ll address this issue in the sidebar “Two criticisms of Formal methods”
later in this chapter.

ChAptEr 7

Design Vocabularies in Games

150

Game mechanics: advanced Game desiGn

As a starting point for his full set of formal abstract design tools, Church describes
