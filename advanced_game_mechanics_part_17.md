SimCity is a good example of engine building. The energy in SimCity is money, which
is used to activate most building mechanisms. The mechanisms consist of preparing building sites, zoning, building infrastructure, constructing special buildings,
and demolition. The core engine of SimCity is quite complex with many internal
resources such as people, job vacancies, power, transportation capacity, and three
different types of zones. Feedback loops within the engine cause all sorts of friction
and effectively balance the main positive feedback loop, up to the point that the
engine can collapse if the player is not careful and manages the engine poorly.
In the board game Puerto Rico, each player builds up a New World colony. The colony
generates different types of resources that can be reinvested or converted into victory
points. The core engine includes many elements and resources such as plantations,
buildings, colonists, money, and a selection of different crops. Puerto Rico is a multiplayer game in which the players compete for a limited number of positions that
allow different actions to improve the engine; they compete for different building
mechanics. This way, a strong multiplayer dynamic is created that contributes much
of its gameplay.

related Patterns
Applying multiple feedback to the building mechanisms is a good way to increase
the difficulty of the engine building pattern.

n

All friction patterns are suitable to balance the typical positive feedback created
by an implementation of engine building that consumes energy to activate building
mechanisms.

n

The dynamic engine is one of the simplest possible implementations of an engine
building pattern.

n

n

The engine building pattern elaborates the dynamic engine and converter engine patterns.

n

The engine building pattern can be elaborated by the worker placement pattern.

Online Appendix B

The upgrade mechanism in a dynamic engine pattern also is an example of a building
mechanism. In fact, the dynamic engine is a simple and common implementation
of an engine building pattern. However, its simplicity means that a dynamic engine
allows only one or maybe two kinds of upgrades. The typical core engines in a game
that follow the engine building pattern allow for many more upgrade options.

B-12

GAme meChAniCS: AdvAnCed GAme deSiGn

Static Friction
n

Type: Friction

n

Intent: A drain automatically consumes resources produced by the player.

Motivation: The static friction pattern counters a production mechanism by
periodically consuming resources. The rate of consumption can be constant or subjected to randomness.

n

Applicability
Use static friction when:
You want to create a mechanism that counters production but can eventually be
overcome by the players.

n

You want to exaggerate the long-term benefits from investing in upgrades for a
dynamic engine.

n

Structure

Participants
n

A resource: energy

n

A static drain that consumes energy

A production mechanism that produces energy

n

n

Other actions that consume energy

Collaborations
The production mechanism produces energy that players need to use to perform
actions. The static drain consumes energy outside players’ direct control.

Consequences
The static friction pattern is a relatively simple way to counter positive feedback
created by engine patterns. However, it tends to emphasize the long-term strategy
inherent to the dynamic engine because it reduces the initial output of the dynamic
engine but does not affect any upgrades.

implementation
An important consideration when implementing static friction is whether the consumption rate is constant or subject to some sort of randomness. Constant static
friction is the easiest to understand and most predictable, whereas random static
friction can cause more noise in the dynamic behavior of the game. The latter can

deSiGn PAt tern LibrAry

B-13

be a good alternative to using randomness in the production mechanism. The frequency of the friction is another consideration: When the feedback is applied at
short intervals, the overall system will be more stable than when the feedback is
applied at long or irregular intervals, which might cause periodic behavior in the
system. In general, the effects of a continual loss of energy on the dynamic behavior
of the system are less powerful than a periodic loss of the same amount of energy.

examples

Online Appendix B

In the Roman city-building game Caesar III, the player must pay tribute to the
emperor at particular moments during each mission. The schedule of the tribute
payments is fixed for each mission and not affected by the player’s performance.
In effect, they cause a very infrequent and high form of static friction that causes a
huge tremor in the game’s internal economy. See Chapter 9, “Building Economies,”
for a more detailed discussion of this game.
The dynamic engine in Monopoly is countered by different types of friction, including static friction (Figure B.6). The main mechanism that implements static friction
is the Chance cards through which the player infrequently loses money. Although
some of these cards take into account the player’s property, most of them do not.
You might think that paying rent to other players is also a form of static friction because
the frequency and severity of the payments are far beyond the direct control of the
player who has to pay. However, paying rent is an example of the attrition pattern, not
static friction. The rate of the friction does change over time, and players have some
indirect effect on it: When a player is doing well, chances are that his opponents
are not, which negatively affects this friction. The diagram in Figure B.8 does not
include this aspect because it is made from the viewpoint of an individual player.

Figure B.6
Static friction in
Monopoly

related Patterns
n Static friction exaggerates long-term investments, and therefore it is best suited to
be used in combination with a static engine, converter engine, or an engine building pattern.
n

Static friction is elaborated by the dynamic friction or the slow cycle pattern.

B-14

GAme meChAniCS: AdvAnCed GAme deSiGn

Dynamic Friction
n

Type: Friction

Intent: A drain automatically consumes resources produced by the player; the
consumption rate is affected by the state of other elements in the game.

n

Motivation: Dynamic friction counteracts production but adapts to the performance of the player. Dynamic friction is a classic application of negative feedback in
a game.

n

Applicability
Use dynamic friction when:
n

You want to balance games in which resources are produced too fast.

You want to create a mechanism that counters production and automatically
scales with players’ progress or power.

n

You want to reduce the effectiveness of long-term strategies created by a dynamic
engine in favor of short-term strategies.

n

Structure

Participants
n

A resource: energy

n

A dynamic drain that consumes energy

n

A production mechanism that produces energy

n

Other actions that consume energy

Collaborations
The production mechanism produces energy that players need to perform actions.
The dynamic drain consumes energy outside players’ direct control but is affected
by the state of at least one other element in the game system.

deSiGn PAt tern LibrAry

B-15

Consequences
Dynamic friction is a good way to counter positive feedback created by engine patterns. Dynamic friction adds a negative feedback loop to the game system.

implementation

Online Appendix B

There are several ways of implementing dynamic feedback. An important consideration is the choice of the element that causes the consumption rate to change.
In general, this can be either the amount of available energy itself, the number of
upgrades to a dynamic engine or a converter engine, or the player’s progress toward a
goal. When the amount of available energy changes the friction, the negative feedback tends to be fast. When progress or production power is the cause, the feedback
is more indirect and probably slower.
When dynamic friction is used to counter a positive feedback loop, it is important
to consider the difference in characteristics of the positive feedback loop and the
negative feedback loop implemented through the dynamic friction. When the characteristics are similar (equally fast, equally durable, and so on), the effect is far more
stable than when the differences are large. For example, when a slow and durable
dynamic friction is acting against a fast but nondurable positive feedback that initially yields a good return, players will initially make a lot of progress but might
suffer in the long run. Fast positive feedback and slow negative feedback seems to be
the most frequently encountered combination.

examples
The mechanics of tower defense games typically revolve around a dynamic drain
on the player’s life points caused by enemies that the player must keep under control by building towers (Figure B.7). In this case, the goal of the game is to prevent
dynamic friction from taking effect. In real tower defense games, placing the right
types of towers involves a strategy that is omitted from this diagram.

Figure B.7
dynamic friction in
tower defense games

B-16

GAme meChAniCS: AdvAnCed GAme deSiGn

Dynamic friction is used in the city production mechanism in Civilization (Figure B.8).
In this game, the player builds cities to produce food, shields, and trade. As cities
grow, they need more and more food for their own population. Players have some
control over how much food is produced compared with other resources, but the
players’ options are limited by the surrounding terrain. By choosing to produce a lot
of food early, cities initially produce fewer other resources but grow faster because
of great potential. Fast growth creates a problem, however, because the happiness
rating of a city must stay equal to or higher than half the population, or else the
production stops due to of civil unrest. Initially, a city has a happiness value of two.
Players can create more happiness by building special buildings or by converting trade
into culture. Both approaches cause more dynamic friction with different profiles on
the production process. Constructing special buildings is slow and requires a high
investment but is highly durable and has a relatively high rate of return. Converting
trade to culture is fast but has a relatively low return for the investment required.

Figure B.8
the city economy of
Civilization. dynamic
friction mechanisms
are printed in color.
the player can freely
adjust the culture and
research settings to
control unrest and
research production.
these settings are
global and affect all
cities equally.

related Patterns
Dynamic friction is a good way to balance any pattern that causes positive feedback and often is part of the multiple feedback pattern.

n

n

Attrition elaborates dynamic friction that is the result of multiplayer interaction.

n

Dynamic friction is elaborated by a stopping mechanism.

deSiGn PAt tern LibrAry

B-17

Stopping Mechanism
n

Type: Friction

n

Intent: Reduce the effectiveness of a mechanism every time it is activated.

n

Also known as: Law of diminishing returns.

Motivation: To prevent a player from abusing a powerful mechanism, the mechanism’s effectiveness is reduced every time it is used. In some cases, the stopping
mechanism is permanent, but usually it’s not.

n

Use a stopping mechanism when:
n

You want to prevent players from abusing particular actions.

n

You want to counter dominant strategies.

n

You want to reduce the effectiveness of a positive feedback mechanism.

Structure

Participants
n

An action that might produce some sort of output

n

A resource energy that is required for the action

The stopping mechanism that increases the energy cost or reduces the output
of the action

n

Collaborations
For a stopping mechanism to work, the action must have an energy cost, produce
resources, or both. The stopping mechanism reduces the effectiveness of an action
mechanism every time it is activated by increasing the energy costs or reducing
the output of resources.

Online Appendix B

Applicability

B-18

GAme meChAniCS: AdvAnCed GAme deSiGn

Consequences
Using a stopping mechanism can reduce the effect of a positive feedback loop considerably and even make its return insufficient.

implementation
When implementing a stopping mechanism, it is important to consider whether to
make the effects permanent. When the accumulated output is used to measure the
strength of the stopping mechanism, the effects are not permanent. In that case, it
requires players to alternate frequently between creating the output and using the
output in other actions.
A stopping mechanism can apply to each player individually or can affect multiple
players equally. In the latter case, the game will reward players that use the action
before other players do. This means that the stopping mechanism can create a form
of feedback depending on whether leading or trailing players are likely to act first.

examples
A subtle stopping mechanism can be found in the timber-harvesting mechanism
in Warcraft III. In Warcraft III, players can assign peasants to cut wood and produce
lumber. Because the peasants have to transport the lumber back from the forest to
the player’s base and cannot cut wood while transporting, the distance to the forest
has an effect on effectiveness of the production mechanism. Because cutting wood
clears the forest, the distance increases as the player cuts more and more wood.
Figure B.9 represents these mechanics.

Figure B.9
the stopping mechanism in Warcraft III:
the production rate for
each peasant will drop
to 0.4 when the forest
is almost cleared.

The price mechanism of the fuel market in Power Grid involves a stopping mechanism (Figure B.10). In Power Grid, players use money to buy fuel and burn fuel to
generate money. This positive feedback loop is counteracted by the fact that buying
a lot of fuel actually drives up the price for all players. Because the leading player
acts last in Power Grid, this stopping mechanism causes powerful negative feedback
for the leading player.

deSiGn PAt tern LibrAry

B-19

Figure B.10

related Patterns
n

Stopping mechanisms are often found in systems that implement multiple feedback.

n

A stopping mechanism elaborates the dynamic friction pattern.

n

A stopping mechanism might be elaborated by a slow cycle pattern.

Attrition
n

Type: Friction

Intent: Players actively steal or destroy resources of other players that they need
for other actions in the game.

n

Motivation: By allowing players to directly steal or destroy each other’s
resources, players can eliminate each other in a struggle for dominance.

n

Applicability
Use attrition when:
n

You want to allow direct and strategic interaction between multiple players.

You want to introduce feedback into a system whose nature is determined by the
strategic preferences and/or whims of the players.

n

Online Appendix B

the stopping mechanism in Power Grid
drives up the price
of fuel and causes
negative feedback,
especially for leading
players.

B-20

GAme meChAniCS: AdvAnCed GAme deSiGn

Structure

Participants
n

Multiple players who have the same (or similar) mechanics and options.

A strength resource. A player who loses all his strength is eliminated from the
game.

n

n

A special attack action that drains or steals the other player’s strength.

Collaborations
By performing attack actions, players can drain each other’s strength. Attacking
may, or may not, cost strength to perform. If attacking doesn’t cost strength, it
should require time to perform or involve some measure of skill or randomness.
The balance between the attack costs, its effectiveness, and how beneficial the other
actions in the game are determine the effectiveness of the attack and the dominance
of the attrition pattern.

Consequences

N OT E remember that
the terms constructive
and destructive
describing feedback
are not the same as
positive and negative.
See the section
“Seven Feedback
Characteristics” in
Chapter 6, “Common
mechanisms,” for an
explanation of the
distinction.

Attrition introduces a lot of dynamism into a system because players directly control
the measure of the destructive force applied to each other. Often, this introduces
destructive feedback because the current state of a player will cause reactions by
other players. Depending on the nature of the winning conditions and the current
state of the game, this feedback might be negative when it stimulates players to act
and conspire against the leader, but it also might cause positive feedback when players are stimulated to attack and eliminate weaker players.

implementation
For attrition to work well, players should be required to invest some sort of resource
in attacking that could also be spent otherwise. If they don’t have to make this
investment, in a two-player game attrition simply becomes a race to destroy the
opponent with few or no strategic choices. In a multiplayer game that facilitates
social interaction between the players, attacking without investment works a little
better because the players need to choose whom to attack.

deSiGn PAt tern LibrAry

B-21

It is quite common to implement attrition using two resources, life and energy, instead
of just one, strength. Players use energy to perform actions and lose the game when
they run out of life. When using these two resources, it is important that they be
somehow related. Often, players are allowed to spend energy to gain more life.
Sometimes the relationship between life and energy is implicit. For example, when
a player must choose between spending energy or gaining life, there is an implicit
link between the two because players generally cannot do both at the same time.

Online Appendix B

In a two-player version of attrition, the game must include other actions, and
games for more than two players often allow other actions that the players can
perform. Most of the time these actions constitute some sort of production mechanism for strength, which increases the effectiveness the players’ defensive or
offensive capabilities (and thus elaborates the attrition pattern to an arms race
pattern). Most real-time strategy games include all these options, often with multiple variants for each.
The winning conditions and effects of eliminating another player have a big impact
on the attrition pattern. The winning condition does not need to be elimination,
however. Players might score points, or reach a particular goal outside the attrition
pattern, which automatically widens the number of strategies available. When there
is a bonus for attacking or eliminating players, the pattern can be made to stimulate
the elimination of weaker players.

examples
The trading card game Magic: The Gathering implements an elaborate version of the
attrition pattern. Figure B.11 presents this implementation, although it shows the
details from the perspective of a single player only.

Figure B.11
the attrition mechanism in Magic: The
Gathering

B-22

GAme meChAniCS: AdvAnCed GAme deSiGn

In Magic: The Gathering, players can play one card every turn. These cards allow
players to add lands, summon creatures, cast spells to heal, or deal direct damage to
their opponent or their opponent’s creatures. But all actions except playing lands
cost mana (magical energy). The more mana players have, the more they can spend
each turn and the more powerful actions they can play. Creatures will fight other
creatures, and when there are no more enemy creatures, they will damage the opponent directly. Players who lose all their life points are eliminated from the game.
Magic: The Gathering is an example of a game that implements attrition using separate resources for life and energy (or in this case, life and mana).
The different gameplay options in Magic: The Gathering illustrate how attrition can
work differently. Direct damage briefly triggers a drain. As its name implies, it is fast
and direct. On the other hand, summoning creatures activates a permanent drain
on the opponent’s creatures and life. The effects usually are not as powerful as direct
damage, but because they accumulate over time, they can be quite devastating. The
cards in the player’s hand determine which options are available to him and exactly
how powerful those options are. Because players build their own decks from a large
collection of cards, deck building is an important aspect of Magic: The Gathering.
The most obvious way to implement attrition is in a symmetrical game. However,
many single-player games and even certain types of multiplayer games use asymmetrical attrition. An example of asymmetrical attrition can be found in the board
game Space Hulk in which one player, controlling a handful of space marines, tries
to accomplish a mission while the other player, controlling an unlimited supply of
alien “genestealers,” tries to prevent that. The genestealer player tries to reduce the
number of space marines to stop them from accomplishing their goals and wins
when the genestealers have destroyed enough space marines. The space marine
player usually cannot win by destroying genestealers but must keep the number of
genestealers under control to survive, because the genestealers become more effective as their numbers grow. Figure B.12 is a rough illustration of the mechanics in
Space Hulk.

Figure B.12
Asymmetrical attrition
in Space Hulk

deSiGn PAt tern LibrAry

B-23

related Patterns
Attrition works well with any sort of engine pattern. Trade can be used as an alternative form of multiplayer feedback that is constructive instead of destructive and is
nearly always negative.

n

n

Attrition elaborates the dynamic friction pattern.

n

Attrition can be elaborated by the arms race and worker placement patterns.

n

Type: Escalation

n

Intent: Progress toward a goal increases the difficulty of further progression.

Motivation: A positive feedback loop between player progress and the game’s difficulty makes the game increasingly harder for players as they get closer to achieving
their goals. This way, the game quickly adapts to the player’s skill level, especially
when the good performance allows the player to progress more quickly.

n

Applicability
Use escalating challenge when:
You want to create a fast-paced game based on player skill (usually physical skill)
in which the game gets harder as the player advances; his ability to complete tasks is
inhibited as he goes.

n

You want to create emergent mechanics that (partially) replace predesigned
level progression.

n

Structure

Online Appendix B

Escalating Challenge

B-24

GAme meChAniCS: AdvAnCed GAme deSiGn

Participants
n

Targets represent unresolved tasks.

n

Progress represents the player’s progress toward a goal.

n

A task either reduces the number of targets or produces progress.

A feedback mechanism makes the game more difficult as the player progresses
toward the goal or reduces the number of targets.

n

Collaborations
The task reduces targets, produces progress, or does both. The feedback mechanic
increases the difficulty of the task as the player gets closer to achieving the goal.

Consequences
Escalating challenge is based on a simple positive feedback loop affecting the difficulty of the game. Its mechanism quickly adjusts the difficulty of the game to the
skill level of the player. If failure at the task ends the game, escalating challenge
ensures a very quick game.

implementation
The task in a game that implements the escalating challenge pattern is typically
affected by player skill, especially when the escalating challenge pattern makes up
the most of the game’s core mechanics. When the task is a random or deterministic mechanic, players will have no control over the game’s progress. Only when
the escalating challenge pattern is part of a more complex game system and players have some sort of indirect control over the chance of success does a random or
deterministic mechanic become viable. Using multiplayer dynamic mechanisms is
an option but probably works better in a more complex game system as well.

examples
Space Invaders is a classic example of the escalating challenge pattern. In Space
Invaders, the player needs to destroy all the invading aliens before they can reach
the bottom of the screen. Every time the player destroys an alien, all other aliens
speed up a little, making it more difficult for the player to shoot them.
Pac-Man is another example. In Pac-Man, the task is to eat all the dots in a level, while
the chasing ghosts make it more and more difficult to get to the last remaining dots
(see Chapter 5, “Machinations,” for a detailed discussion and diagram of Pac-Man).

related Patterns
By combining escalating challenge with static friction or dynamic friction, a game can
be created that quickly matches its difficulty to the ability of the player.

deSiGn PAt tern LibrAry

B-25

Escalating Complexity
n

Type: Escalation

Intent: Players act against growing complexity, trying to keep the game under
control until positive feedback grows too strong and the accumulated complexity
makes them lose.

n

Motivation: Players are tasked to perform an action that grows more complex
if the players fail and in which complexity contributes to the difficulty of the task.
As long as players can keep up with the game, they can keep on playing, but once
the positive feedback spins out of control, the game ends quickly. As the game progresses, the mechanism that creates the complexity speeds up, ensuring that at some
point players can no longer keep up and eventually must lose the game.

Applicability
Use escalating complexity when:
n

You aim for a high-pressure, skill-based game.

You want to create emergent mechanics that (partially) replace predesigned
level progression.

n

Structure

Participants
The game produces complexity that
must be kept under a certain limit by the
player.

n

A task performed by the player
reduces complexity.

n

A progress mechanism increases
the production of complexity over
time.

n

Collaborations
Complexity immediately increases the production of more complexity, creating
a strong positive feedback loop that must be kept under control. The player loses
when complexity exceeds his ability to manage it.

Online Appendix B

n

B-26

GAme meChAniCS: AdvAnCed GAme deSiGn

Consequences
Given enough skill, players can keep up with the increase in complexity for a long
time, but when players no longer keep up, complexity spins out of control and the
game ends quickly.

implementation
The task in a game that implements the escalating complexity pattern is typically
affected by player skill, especially when escalating complexity makes up most of the
game’s core mechanics. When the task is governed by a random or deterministic
mechanism, players will have no control over the game’s progress. Random or deterministic mechanics work a little better in more complex game systems in which
players have some control over their chance of success. Using a multiplayer task is
an option, but it probably also works better in a more complex game system.
Randomness in the production of complexity creates a game with a varied pace,
where players might struggle to keep up with production at its peak but get a chance
to catch their breath when complexity production slows down a little.
There are many ways to implement the progress mechanic, from a simple timebased increase of the production of complexity (as is the case in the previous sample
structure) to complicated constructions that rely on other actions by the player or
by other players. This way, it is possible to combine escalating complexity with escalating challenge by introducing positive feedback to the progress mechanic as a result
of the execution of the task.
Escalating complexity lends itself well to serve as part of a multiple feedback structure
in which the complexity feeds into several feedback loops with different signatures.
For example, escalating complexity can be partially balanced by having the task feed
into a much slower negative feedback loop governing the production of complexity.

examples
In Tetris, a steady flow of falling tetrominoes produces complexity. There is a slight
randomness in this production as the different types of tetrominoes are created
over time. Players need to place the tetrominoes in such a way that they fit together
closely. When a line is completely filled, it disappears, making room for new tetrominoes. When players fail to keep up, the tetrominoes pile up quickly, and they will
have less time to place subsequent tetrominoes. This can quickly increase the complexity of the field when players are not careful and cause them to lose the game
if the pile of tetrominoes reaches the top of the screen. In Tetris, levels create the
progression mechanism. Every time the player clears ten lines, the game advances to
the next level and the tetrominoes start falling faster, making it more and more difficult to place them accurately. In this case, the level mechanism is also an example
of the escalating challenge pattern.
Figure B.13 represents these mechanics of Tetris. In this diagram, tetrominoes are
converted into points. The number of points goes up when there are more tetrominoes

deSiGn PAt tern LibrAry

B-27

in the game. This represents the possibility to clear more lines at once and enables a
high-risk, high-reward strategy. The chart in Figure B.13 clearly shows that once the
pace grows too great for the player to keep up, the game rapidly spins out of control.

Figure B.13

Online Appendix B

escalating complexity
in Tetris

In the independently developed action shooter Super Crate Box, players are required
to pick up crates containing different weapons, while keeping the number of enemies under control by shooting them. As soon as the player touches an enemy, he is
killed. Enemies spawn at the top of the screen and run down the level to disappear
at the bottom. An enemy that makes it to the bottom respawns at the top of the
screen but moves much faster the second time. The player carries only one weapon
at a time, and not all weapons are equally powerful. However, because the only way
to get ahead is to pick up crates and change weapons, the player is forced to make
the best use of whatever he picks up. The player has to alternate between killing
enemies to keep their numbers under control and picking up boxes to score more
points. Figure B.14 represents a diagram for Super Crate Box.

Figure B.14
Super Crate Box has
the players alternate between scoring
points and keeping
enemy numbers under
control.

B-28

GAme meChAniCS: AdvAnCed GAme deSiGn

related Patterns
n

Any type of engine pattern can be used to implement the progress mechanism.

It is common to find the progression mechanism implemented as an escalating
challenge pattern.

n

Arms Race
n

Type: Escalation

Intent: Players can invest resources to improve their offensive and defensive
capabilities against other players.

n

Motivation: Allowing players to invest in their offensive and defensive capabilities introduces many strategic options into the game. The player can choose
strategies that fit his skills and preferences.

n

Applicability
Use arms race when:
You want to create more strategic options or avoid dominant strategies in games
that use the attrition pattern.

n

n

You want to lengthen the playing time of your game.

You want to encourage players to develop strategies and playing styles that suit
their individual skills and preferences.

n

Structure

deSiGn PAt tern LibrAry

B-29

Participants
n

Multiple players that can activate the same (or similar) attack mechanisms.

A strength resource. A player that loses all his strength is eliminated from the
game.

n

An optional energy resource that is consumed by upgrades. In some cases, energy
and strength are the same.

n

At least one upgrade mechanisms to improve the offensive or defensive capabilities of each player.

n

The attack mechanisms allow players to drain or steal each other’s strength.
Activating the attack and upgrade mechanisms require the player to invest energy or
time. The upgrade mechanisms improve the player’s offensive or defensive capabilities or restore the player’s strength.

Consequences
Arms race introduces many strategic options for players to explore, which can
make the game difficult to balance. In general, it is best to implement an intransitive (rock-paper-scissors) mechanism in the upgrade options so that every strategy
has a counter-strategy. For example in many medieval war games, heavy infantry
beats cavalry, while cavalry beats artillery, and artillery beats infantry. In this case,
the best strategy and most effective army composition is partially determined by
the choices made by your opponent.
Many strategic options allow players to develop their own playing styles and strategies. For example, if a player likes a particular mechanism, she can use it more often,
while if she dislikes a mechanism, she might ignore it.
Using an arms race pattern typically lengthens a game, because players always have
the option to play defensively at first. This can even delay confrontation and conflict for a long time.

implementation
What resources are required to pay for upgrades is an important design decision
when implementing an arms race. When strength and energy are the same, the
player might over-invest and make himself vulnerable, especially if the upgrades
take time to take effect. When energy is separate from strength, you need to consider carefully what the relationship between strength and energy actually is.
Strength might determine the production rate of energy. This would create a strong
positive, destructive feedback loop. Energy might also be converted into strength, or
energy might be invested to produce strength over time. There are many options.

Online Appendix B

Collaborations

B-30

GAme meChAniCS: AdvAnCed GAme deSiGn

A good way to prevent an arms race from lengthening the game too much is to
make the resource to activate upgrades heavily contested, either because all players
are trying to harvest the same resources or because upgrades require the player to
invest strength.
An arms race doesn’t have to be symmetrical. It is possible to create an arms race
with two different sides, although this would be more difficult to balance.

examples
Many real-time strategy games implement the arms race pattern. For example,
StarCraft II and Warcraft III allow the player to investigate technology to improve the
fighting capabilities of his units. In these games, strength is measured as the sum of
the player’s units and buildings, whereas energy is harvested by worker units and is
used to upgrade and build new units.
An arms race is also often found in tower defense games, although in those games
it is an asymmetrical implementation of the pattern. For example, the green and
blue mechanisms in Figure B.15 represent two different mechanisms that increase
the offensive capacities of the player (blue) and the enemies (green). In most tower
defense games, there are many more upgrade mechanisms: Players can upgrade towers or choose between different towers for different effects, while the enemy waves
will include other types of enemies that require a different type of response by the
player.

Figure B.15
An asymmetrical
arms race in a tower
defense game

related Patterns
Arms race combines well with a dynamic engine to produce energy and strength.
This combination is found in many real-time strategy games.

n

n

Arms race elaborates the attrition pattern.

n

Arms race can be elaborated by the worker placement pattern.

deSiGn PAt tern LibrAry

B-31

Playing Style Reinforcement
n

Type: Miscellaneous

Intent: By applying slow, positive, constructive feedback on player actions, the
game encourages specialization and gradually adapts to the player’s preferred playing style.

n

n

Also Known As: Role-playing game (RPG) elements.

Motivation: Slow, positive, constructive feedback on player actions (actions that
have another effect on the game) causes the player’s avatar or units to develop over
time. As the actions themselves feed back into this mechanism, the avatar or units
specialize over time, getting better at performing a particular task. As long as there
are multiple viable strategies and specializations, the avatar and the units will, in
time, reflect the player’s preferences and style.

Applicability
Use playing style reinforcement when:
You want players to make a long-term investment in the game that spans multiple play sessions.

n

You want to reward players for building, planning ahead, and developing personal strategies.

n

n

You want players to grow into a specific role or strategy.

Structure

Online Appendix B

n

B-32

GAme meChAniCS: AdvAnCed GAme deSiGn

Participants
Actions players can perform whose success depends in part on the attributes of
the player’s character or the units involved in the action.

n

A resource ability that affects the chance that actions succeed and that can grow
over time.

n

An optional resource experience points that can be used to increase an ability.
Some games call these skill points and include a different resource called experience
points that cannot be traded.

n

Collaborations
n

Ability affects the success rate of actions.

Attempting actions generates experience points or directly improves abilities.
Some games require the action to be successful, while others do not.

n

n

Experience points might be spent to improve abilities.

Consequences
Playing style reinforcement works best in games that are played over multiple sessions and over a long time.
Playing style reinforcement works well only when multiple strategies and play styles
are viable options in the game. When there is only one, or only a few, all the players
will use the same strategy, which makes the game uninteresting.
Playing style reinforcement can inspire min-maxing behavior with players. This
refers to a strategy in which players seek the best possible options that will allow
them to gain powerful avatars or units as fast as possible. If min-maxing is successful, it usually becomes a dominant strategy. This can happen when the strength of
the feedback is not distributed evenly over all actions and strategies.
Playing style reinforcement favors experienced players over inexperienced players,
because the experienced ones will have a better understanding of their options and
the long-term consequences of their actions.
Playing style reinforcement rewards the player who can invest the most time in
playing the game. In this case, time spent playing can compensate for different levels of skill among players, which can be a wanted or an unwanted side-effect.
It can be ineffective for a player to change strategies over time in a game with
playing style reinforcement, because the player will lose the benefit of previous
investments in another play style.

implementation
Whether or not to use experience points is an important decision when implementing play style reinforcement. When using experience points, there is no direct

deSiGn PAt tern LibrAry

B-33

coupling between growth and action, allowing the player to harvest experience
with one strategy to develop the skills to excel in another strategy. On the other
hand, if you do not use experience points, you have to make sure that the feedback
is balanced for the frequency of the actions; actions that are performed more often
should have weaker feedback than actions that can be practiced infrequently.

You must also decide whether the action needs to be executed successfully to generate the feedback. How you decide this issue can dramatically affect player behavior.
When success is required, the feedback loop gains influence. In that case, it is probably best to have the difficulty of the player’s tasks also affect the success of an action
and to challenge the player with tasks of varying difficulty levels, thus allowing
them to train their avatars. When success is not required to earn experience points,
players have more options to improve neglected abilities during later and more difficult stages. However, it might also encourage players to perform a particular action
at every conceivable opportunity, which could lead to some unintended, unrealistic,
or comic results, especially when the action involves little risk.

examples
Many pen-and-paper role-playing games implement playing-style reinforcement.
For example, in Warhammer Fantasy Role-Play and Vampire: The Masquerade, players are awarded experience points for achieving goals in the game. They can spend
experience points on improving their character’s abilities. Curiously, the original
role-playing game Dungeons & Dragons doesn’t have playing-style reinforcement. In
Dungeons & Dragons, players are awarded experience points that they need to accumulate to advance to the next level. However, the player has no influence over how
her character’s abilities improve when she levels up; the character’s abilities do not
adapt to the playing style or preferences of the player.
In the computer role-playing game The Elder Scrolls IV: Oblivion, the avatar’s progress
is directly tied to her actions. The avatar’s ability corresponds directly to the number
of times she has performed the associated actions. Oblivion implements playing-style
reinforcement without experience points.
In Civilization III, there are different ways in which a player can win the game. A
player reinforces his chosen strategy of military, economic, cultural, or scientific
dominance (or any combination) by building city improvements and wonders of
the world that favor that strategy. In Civilization III, several resources take the role of
experience points; money and production are prominent examples. These resources
are not necessarily tied to one particular strategy in the game. Money generated by
one city can be spent to improve production in another city in the game.

Online Appendix B

Role-playing games are the quintessential example of games built around the play
style reinforcement pattern. In these games, the feedback loops are generally quite
slow and balanced by an escalating challenge, dynamic friction, or a stopping mechanism
to make sure avatars do not progress too fast. In fact, most of these games are balanced
in such a way that progression is initially fast and gradually slows down, usually
because the required investment of experience points increases exponentially.

B-34

GAme meChAniCS: AdvAnCed GAme deSiGn

related Patterns
When playing style reinforcement depends on the success of actions, it creates a
powerful feedback. In that case, a stopping mechanism is often used to increase the
price of new upgrades to an ability.

Multiple Feedback
n

Type: Miscellaneous

Intent: A single gameplay mechanism feeds into multiple feedback mechanisms,
each with a different profile.

n

Motivation: A player action activates multiple feedback loops at the same time.
Some feedback loops will be more obvious than others. This creates a situation
where the exact outcome or success of an action might be predictable in the short
term but can have unexpected results in the long run.

n

Applicability
Use multiple feedback when:
n

You want to increase a game’s difficulty.

n

You want to emphasize the player’s ability to read the current game state.

Structure

Participants
An action that can be activated by
the player

n

N OT E in the example
structure, there are two
feedback mechanisms.
the action (black)
activates one feedback
mechanism (red) that
is positive, limited in
duration, and strong,
but it also activates a
secondary feedback
mechanism (blue) that
is negative, permanent, and weak. this
illustrates just one way
of setting up multiple
feedback loops. there
are many more.

Multiple feedback mechanisms
that are activated by the action

n

Collaborations
The action activates multiple feedback mechanisms that ultimately feed back into
the action.

Consequences
For the player, multiple feedback loops are more difficult to understand than single
feedback loops. As a result, using this pattern makes a game more difficult.

deSiGn PAt tern LibrAry

B-35

If the feedback loops that the action activates can have dynamic profiles that
change during play (which they often do), it is very important for the player to be
able to read the current profile, because their balance might shift considerably during the game.
Finding the right balance between the multiple feedback loops is an important issue
in a game that uses this pattern.

When creating a game with multiple feedback, it is very important to make sure
that the profiles of the different feedback loops are different. In particular, the speed
of the feedback needs to vary if this pattern is going to be effective. Alternatively,
varying the profile of the feedback over time can work well. To this end, adding
playing style reinforcements and stopping mechanisms to one or more of the feedback
loops is a good design strategy.
The most common combination for multiple feedback seems to be fast, constructive, positive feedback coupled with slow, negative feedback. This creates a trade-off
between short-term gains and long-term disadvantages.

examples
The economy of SimCity includes many multiple feedback mechanisms. For example, the city requires energy, so the player needs to build an energy plant. In the
short term, the plant will spur economic growth as it powers residential, commercial, and industrial zones. However, in the long term, power plants also cause
pollution and will have negative effects on surrounding zones. Likewise, infrastructure like roads are required to make a city grow, but in the long term, as they are
used more frequently, they also cause problems such as traffic jams and pollution.
Attacking in Risk feeds into three positive feedback loops of varying speeds and
strengths (see the discussion of Risk in Chapter 6, “Common Mechanisms”). Most
obviously, using armies to capture more lands allows the player to build more
armies. The cards implement a slower form of feedback; a player who successfully
attacks gains a card, and certain combinations of three cards allow him to gain extra
armies. The last type of feedback is created by capturing continents. A continent will
give a player a number of bonus armies each turn; this is a very fast and strong feedback loop, but one that requires a higher investment by the player to achieve.

related Patterns
Playing style reinforcements and stopping mechanisms are good ways to ensure that the
profile of the feedback loops that an action feeds into changes over time.

Online Appendix B

implementation

B-36

GAme meChAniCS: AdvAnCed GAme deSiGn

Trade
n

Type: Miscellaneous

Intent: Allow trade between players to introduce multiplayer dynamics and negative, constructive feedback.

n

Motivation: Players are allowed to trade important resources. Usually this means
that leading players will face tougher negotiations, while trailing players can help
each other to catch up. Trade works especially well when the flow of resources is
unstable and/or not equally distributed among players.

n

Applicability
Use trade when:
n

You want to introduce multiplayer dynamics to the game.

n

You want to introduce negative, constructive feedback.

You want to introduce a social mechanic that encourages players to interact with
one another via commerce (as opposed to combat).

n

Collaborations
The tradable resources can be exchanged by the players using the trading mechanism.

Structure

Participants
A trading mechanism that allows
resources to be traded among players

n

Multiple tradable resources that
can be exchanged or used in various
ways

n

Actions that require using tradable
resources

n

Consequences
Trade introduces negative feedback that does not really slow down the game but
usually helps trailing players catch up (because it is not destructive).
Trade favors players with good social and bartering skills.

deSiGn PAt tern LibrAry

B-37

implementation

To implement a successful trading mechanism, multiple tradable resources are
required, and the production rates of these resources must fluctuate or at least be
different among players. Trading works only when there is an imbalance in the
distribution of resources among the trading parties. It also helps to include many
actions that consume the tradable resources and to create actions that consume
resources of multiple types at once, because this further exaggerates the imbalance
when players choose different courses of action.

examples
In The Settlers of Catan, players build up an uncertain dynamic engine: villages and
cities that produce the resources used to build more villages and cities. The randomness of these engines is partly countered by allowing all players to trade resources
with the player who is currently taking her turn. The exchange rate is set by mutual
agreement and usually determined by the availability of the resource and the position of the player. Players who are in the lead can afford to pay more for their
resources. When close to winning, players might find it impossible to make a deal.
In Civilization III, players can exchange strategic resources, money, and knowledge.
This mutually benefits both parties and allows weaker civilizations to catch up fairly
quickly.

related Patterns
Attrition can be an alternative source of multiplayer feedback that is not constructive
but destructive in nature.

Worker Placement
n

Type: Miscellaneous

Intent: The player controls a limited resource (workers) that she must commit to
activate or improve different mechanisms in the game.

n

Motivation: A set of mechanisms create a complex and dynamic core of the
game. The player must choose how to distribute a limited resource (workers) to
activate these mechanisms. The limited number requires the player to change the
distribution of the workers to operate the game mechanisms most effectively.

n

Online Appendix B

In board games, trade is very easy to implement. The game simply needs to specify
how and when players can trade resources. In a multiplayer computer game, trade is
also easy. However, creating a trading mechanism that involves computer-controlled
characters is far from trivial.

B-38

GAme meChAniCS: AdvAnCed GAme deSiGn

Applicability
Use worker placement when:
n

You want to introduce constant micromanagement as a player task.

n

You want to encourage players to adapt to changing circumstances.

n

You want to introduce timing as a crucial factor in successful strategies.

n

You want to create a subtle mechanism for indirect conflict.

Structure

Participants
The core mechanisms, usually a
complex structure combining multiple
mechanisms

n

N OT E the structure
