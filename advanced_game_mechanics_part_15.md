Motivation: Dynamic friction counteracts production but adapts to the performance of the player. Dynamic friction is a classic application of negative feedback in
a game.

n

applicability
Use dynamic friction when:
n

You want to balance games in which resources are produced too fast.

You want to create a mechanism that counters production and automatically
scales with players’ progress or power.

n

You want to reduce the effectiveness of long-term strategies created by a dynamic
engine in favor of short-term strategies.

n

structure

Participants
n

A resource: energy

n

A dynamic drain that consumes energy

n

A production mechanism that produces energy

n

Other actions that consume energy

collaborations
The production mechanism produces energy that players need to perform actions.
The dynamic drain consumes energy outside players’ direct control but is affected
by the state of at least one other element in the game system.

desiGn PaT Tern LiBrarY

317

consequences
Dynamic friction is a good way to counter positive feedback created by engine patterns. Dynamic friction adds a negative feedback loop to the game system.

implementation

AppEnDIx B

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

FIGURe b.7
dynamic friction in
tower defense games

318

Game mechanics: advanced Game desiGn

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

FIGURe b.8
The city economy of
Civilization. dynamic
friction mechanisms
are printed in color.
The player can freely
adjust the culture and
research settings to
control unrest and
research production.
These settings are
global and affect all
cities equally.

related Patterns
Dynamic friction is a good way to balance any pattern that causes positive feedback and often is part of the multiple feedback pattern.

n

n

Attrition elaborates dynamic friction that is the result of multiplayer interaction.

n

Dynamic friction is elaborated by a stopping mechanism.

desiGn PaT Tern LiBrarY

319

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

applicability
n

You want to prevent players from abusing particular actions.

n

You want to counter dominant strategies.

n

You want to reduce the effectiveness of a positive feedback mechanism.

structure

Participants
n

An action that might produce some sort of output

n

A resource energy that is required for the action

The stopping mechanism that increases the energy cost or reduces the output
of the action

n

collaborations
For a stopping mechanism to work, the action must have an energy cost, produce
resources, or both. The stopping mechanism reduces the effectiveness of an action
mechanism every time it is activated by increasing the energy costs or reducing
the output of resources.

AppEnDIx B

Use a stopping mechanism when:

320

Game mechanics: advanced Game desiGn

consequences
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

FIGURe b.9
The stopping mechanism in Warcraft III:
The production rate for
each peasant will drop
to 0.4 when the forest
is almost cleared.

The price mechanism of the fuel market in Power Grid involves a stopping mechanism (Figure B.10). In Power Grid, players use money to buy fuel and burn fuel to
generate money. This positive feedback loop is counteracted by the fact that buying
a lot of fuel actually drives up the price for all players. Because the leading player
acts last in Power Grid, this stopping mechanism causes powerful negative feedback
for the leading player.

desiGn PaT Tern LiBrarY

321

FIGURe b.10

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

applicability
Use attrition when:
n

You want to allow direct and strategic interaction between multiple players.

You want to introduce feedback into a system whose nature is determined by the
strategic preferences and/or whims of the players.

n

AppEnDIx B

The stopping mechanism in Power Grid
drives up the price
of fuel and causes
negative feedback,
especially for leading
players.

322

Game mechanics: advanced Game desiGn

structure

Participants
n

Multiple players who have the same (or similar) mechanics and options.

A strength resource. A player who loses all his strength is eliminated from the
game.

n

n

A special attack action that drains or steals the other player’s strength.

collaborations
By performing attack actions, players can drain each other’s strength. Attacking
may, or may not, cost strength to perform. If attacking doesn’t cost strength, it
should require time to perform or involve some measure of skill or randomness.
The balance between the attack costs, its effectiveness, and how beneficial the other
actions in the game are determine the effectiveness of the attack and the dominance
of the attrition pattern.

consequences

N OT E remember that
the terms constructive
and destructive
describing feedback
are not the same as
positive and negative.
see the section
“seven Feedback
characteristics” in
chapter 6, “common
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

desiGn PaT Tern LiBrarY

323

It is quite common to implement attrition using two resources, life and energy, instead
of just one, strength. Players use energy to perform actions and lose the game when
they run out of life. When using these two resources, it is important that they be
somehow related. Often, players are allowed to spend energy to gain more life.
Sometimes the relationship between life and energy is implicit. For example, when
a player must choose between spending energy or gaining life, there is an implicit
link between the two because players generally cannot do both at the same time.

AppEnDIx B

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

FIGURe b.11
The attrition mechanism in Magic: The
Gathering

324

Game mechanics: advanced Game desiGn

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

FIGURe b.12
asymmetrical attrition
in Space Hulk

desiGn PaT Tern LiBrarY

325

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

applicability
Use escalating challenge when:
You want to create a fast-paced game based on player skill (usually physical skill)
in which the game gets harder as the player advances; his ability to complete tasks is
inhibited as he goes.

n

You want to create emergent mechanics that (partially) replace predesigned
level progression.

n

structure

AppEnDIx B

Escalating Challenge

326

Game mechanics: advanced Game desiGn

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

collaborations
The task reduces targets, produces progress, or does both. The feedback mechanic
increases the difficulty of the task as the player gets closer to achieving the goal.

consequences
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

desiGn PaT Tern LiBrarY

327

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

applicability
Use escalating complexity when:
n

You aim for a high-pressure, skill-based game.

You want to create emergent mechanics that (partially) replace predesigned
level progression.

n

structure

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

collaborations
Complexity immediately increases the production of more complexity, creating
a strong positive feedback loop that must be kept under control. The player loses
when complexity exceeds his ability to manage it.

AppEnDIx B

n

328

Game mechanics: advanced Game desiGn

consequences
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

desiGn PaT Tern LiBrarY

329

in the game. This represents the possibility to clear more lines at once and enables a
high-risk, high-reward strategy. The chart in Figure B.13 clearly shows that once the
pace grows too great for the player to keep up, the game rapidly spins out of control.

FIGURe b.13

AppEnDIx B

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

FIGURe b.14
Super Crate Box has
the players alternate between scoring
points and keeping
enemy numbers under
control.

330

Game mechanics: advanced Game desiGn

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

applicability
Use arms race when:
You want to create more strategic options or avoid dominant strategies in games
that use the attrition pattern.

n

n

You want to lengthen the playing time of your game.

You want to encourage players to develop strategies and playing styles that suit
their individual skills and preferences.

n

structure

desiGn PaT Tern LiBrarY

331

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

consequences
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

AppEnDIx B

collaborations

332

Game mechanics: advanced Game desiGn

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

FIGURe b.15
an asymmetrical
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

desiGn PaT Tern LiBrarY

333

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

applicability
Use playing style reinforcement when:
You want players to make a long-term investment in the game that spans multiple play sessions.

n

You want to reward players for building, planning ahead, and developing personal strategies.

n

n

You want players to grow into a specific role or strategy.

structure

AppEnDIx B

n

334

Game mechanics: advanced Game desiGn

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

collaborations
n

Ability affects the success rate of actions.

Attempting actions generates experience points or directly improves abilities.
Some games require the action to be successful, while others do not.

n

n

Experience points might be spent to improve abilities.

consequences
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

desiGn PaT Tern LiBrarY

335

implementation

Role-playing games are the quintessential example of games built around the play
style reinforcement pattern. In these games, the feedback loops are generally quite
slow and balanced by an escalating challenge, dynamic friction, or a stopping mechanism
to make sure avatars do not progress too fast. In fact, most of these games are balanced
in such a way that progression is initially fast and gradually slows down, usually
because the required investment of experience points increases exponentially.
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

AppEnDIx B

Whether or not to use experience points is an important decision when implementing play style reinforcement. When using experience points, there is no direct
coupling between growth and action, allowing the player to harvest experience
with one strategy to develop the skills to excel in another strategy. On the other
hand, if you do not use experience points, you have to make sure that the feedback
is balanced for the frequency of the actions; actions that are performed more often
should have weaker feedback than actions that can be practiced infrequently.

336

Game mechanics: advanced Game desiGn

In Civilization III, there are different ways in which a player can win the game.
A player reinforces his chosen strategy of military, economic, cultural, or scientific
dominance (or any combination) by building city improvements and wonders of
the world that favor that strategy. In Civilization III, several resources take the role of
experience points; money and production are prominent examples. These resources
are not necessarily tied to one particular strategy in the game. Money generated by
one city can be spent to improve production in another city in the game.

related Patterns
When playing style reinforcement depends on the success of actions, it creates a
powerful feedback. In that case, a stopping mechanism is often used to increase the
price of new upgrades to an ability.

Multiple Feedback
A full description of the multiple feedback pattern is included in the online version of
Appendix B, which you can find at www.peachpit.com/gamemechanics.

Trade
A full description of the trade pattern is included in the online version of Appendix B,
which you can find at www.peachpit.com/gamemechanics.

Worker Placement
A full description of the worker placement pattern is included in the online version of
Appendix B, which you can find at www.peachpit.com/gamemechanics.

Slow Cycle
A full description of the slow cycle pattern is included in the online version of
Appendix B, which you can find at www.peachpit.com/gamemechanics.

AppEnDIx C
Getting started
with Machinations

AppEnDIx C

You can create and simulate Machinations diagrams in the Machinations Tool, a
graphical editor and simulator created by Joris Dormans. Appendix C, which you
can find online at www.peachpit.com/gamemechanics, contains a tutorial that will get
you up to speed creating diagrams in the tool. In the tutorial you will learn about the
user interface of the tool, and we’ll show you, step by step, how to create a diagram.

337

references
Adams, Ernest. 2009. Fundamentals of Game Design, Second Edition. Berkeley, CA:
Peachpit Press/New Riders.
Alexander, Christopher, et al. 1977. A Pattern Language: Towns, Buildings, Construction.
Oxford: Oxford University Press.
Ashmore, Calvin, & Nitsche, Michael. 2007. “The Quest in a Generated World.”
In Situated Play: Proceedings of the 2007 Digital Games Research Association Conference,
Tokyo, Japan, September 2007, pp. 503–509.
Ball, Philip. 2004. Critical Mass: How One Thing Leads To Another. New York, NY:
Farrar, Straus and Giroux.
Beck, John C., and Wade, Mitchell. 2006. The Kids are Alright: How the Gamer
Generation is Changing the Workplace. Boston, MA: Harvard Business Review Press.
Björk, Staffan, and Holopainen, Jussi. 2005. Patterns in Game Design. Boston, MA:
Charles River Media.
Bogost, Ian. 2006. Unit Operations: An Approach to Videogame Criticism. Cambridge,
MA: The MIT Press.
Caillois, Roger. 1958. Man, Play, and Games. Translated by Meyer Barash. Urbana, IL:
University of Illinois Press.
Chomsky, Noam. 1972. Language and Mind, Enlarged Edition. New York, NY: Harcourt
Brace Jovanovich Inc.
Church, Doug. 1999. “Formal Abstract Design Tools.” Article in the Gamasutra
webzine, 16 July 1999. Available at www.gamasutra.com/features/19990716/design_
tools_01.htm (referenced May 18, 2012).
Cook, Daniel. 2007. “The Chemistry of Game Design.” Article in the Gamasutra
webzine, July 19, 2007, at www.gamasutra.com/view/feature/1524/ (referenced
May 9, 2012).
Crawford, Chris. 1984. The Art of Computer Game Design. Berkeley, CA: McGraw-Hill/
Osborne Media.
Eco, Umberto. 1976. A Theory of Semiotics. Bloomington, IN: Indiana University Press.
Eco, Umberto. 2004. On Literature. Translated by Martin McLaughin. London: Secker
& Warburg.
Elrod, Corvus. 2011. “So You Wanna Call Yourself a Game Designer?” Semionaut’s
Notebook website. Available at http://corvus.zakelro.com/2011/08/so-you-wannacall-yourself-a-game-designer/ (referenced May 5, 2012).

338

339

Fiske, John. 2011. Introduction to Communication Studies, Third Edition. New York,
NY: Routledge.
Fromm, Jochen. 2005. “Types and Forms of Emergence.” Cornell University Library
website at http://arxiv.org/abs/nlin.AO/0506028 (referenced May 14, 2012).
Gamma, Erich, et al. 1995. Design Patterns: Elements of Reusable Object-Oriented
Software. Boston, MA: Addison-Wesley.
Grünvogel, Stefan M. 2005. “Formal Models and Game Design.” Game Studies, 5 (1).
Available at gamestudies.org/0501/gruenvogel/ (referenced May 16, 2012).
Guttenberg, Darren. 2006. “An Academic Approach to Game Design: Is It Worth
It?” Article in the Gamasutra webzine, April 13, 2006, at www.gamasutra.com/view/
feature/131070/student_feature_an_academic_.php (referenced May 9, 2012).
Hopson, John. 2001. “Behavioral Game Design.” Article in the Gamasutra webzine,
April 27, 2001, at www.gamasutra.com/view/feature/3085/behavioral_game_design.
php (referenced May 9, 2012).

Järvinen, Aki. 2003. “Making and Breaking Games: A Typology of Rules.” In M.
Copier, & J. Raessens (Eds.) Level Up Conference Proceedings: Proceedings of the 2003
Digital Games Research Association Conference, Utrecht, The Netherlands, November
2003, pp. 68–79.
Jenkins, Henry. 2004. “Game Design as Narrative Architecture.” In N. Wardrip-Fruin,
& P. Harrigan (Eds.) First Person: New Media as Story, Performance and Game,
(pp. 118–130). Cambridge, MA: MIT Press.
Juul, Jesper. 2002. “The Open and the Closed: Games of Emergence and Games of
Progression.” In F. Mäyrä (Ed.) Proceedings of Computer Games and Digital Cultures
Conference, Tampere, Finland, June 2002, pp. 323–329.
Juul, Jesper. 2005. Half-Real: Video Games between Real Rules and Fictional Worlds.
Cambridge, MA: MIT Press.
Koster, Raph. 2005a. “A Grammar of Gameplay: Game Atoms—Can Games
Be Diagrammed?” Lecture delivered at the Game Developers Conference,
San Francisco CA, March 2005. Available at www.raphkoster.com/gaming/atof/
grammarofgameplay.pdf (referenced May 18, 2012).
Koster, Raph. 2005b. A Theory of Fun for Game Design. Scottsdale, AZ: Paraglyph Press.
Kreimeier, Bernd. 2002. “The Case For Game Design Patterns.” Article in the
Gamasutra webzine, March 13, 2002, at www.gamasutra.com/view/feature/4261/
the_case_for_game_design_patterns.php (referenced May 9, 2012).

rEfErEnCEs

Jakobson, Roman. 1960. “Closing Statement: Linguistics and Poetics.” In T. A.
Sebeok (Ed.) Style in Language, pp. 350–378. Cambridge, MA: MIT Press.

340

Game mechanics: advanced Game desiGn

Kreimeier, Bernd. 2003. “Game Design Methods: A 2003 Survey.” Article in the
Gamasutra webzine, March 3, 2003. Available at www.gamasutra.com/view/
feature/2892/game_design_methods_a_2003_survey.php (referenced May 18, 2012).
LeBlanc, Marc. 1999. “Formal Design Tools: Feedback Systems and the Dramatic
Structure of Completion.” Lecture delivered at the Game Developers’ Conference,
San Jose CA, March 1999. Slides available at http://algorithmancy.8kindsoffun.com/
cgdc99.ppt (referenced May 16, 2012).
Peirce, Charles Sanders. 1932. Collected Papers of Charles Sanders Peirce, Volume 2,
Elements of Logic. Cambridge, MA: Harvard University Press.
Poole, Steven. 2000. Trigger Happy: The Inner Life of Videogames. London, UK:
Fourth Estate.
Rand, Ayn. 1964. The Virtue of Selfishness. New York, NY: Signet.
Saint-Exupéry, Antoine de. 1939. Wind, Sand and Stars. London: Heinemann.
Saussure, Ferdinand de. 1915. Cours de Linguistique Générale. Translated in 1983 as
Course in General Linguistics. Chicago, IL: Open Court Publishing Company.
Shannon, Claude E. 1950. “Programming a Computer for Playing Chess.”
Philosophical Magazine, 41 (314), pp. 256–275.
Sheffield, Brandon. 2007. “Defining Games: Raph Koster’s Game Grammar.”
Article in the Gamasutra webzine, October 19, 2007, at www.gamasutra.com/view/
feature/1979/defining_games_raph_kosters_game_.php (referenced May 9, 2012).
Smith, Harvey. 2001. “The Future of Game Design.” International Game Developers’
Association website. Available at www.igda.org/articles/hsmith_future (referenced
May 9, 2012).
Smith, Harvey. 2003. “Orthogonal Unit Differentiation.” Lecture delivered at
the Game Developers’ Conference, San Francisco, CA, 2003. Slides available in
PowerPoint format at www.planetdeusex.com/witchboy/gdc03_OUD.ppt
(referenced May 9, 2012).
Vogler, Christopher. 1998. The Writer’s Journey: Mythic Structure for Writers,
Second edition. Studio City, CA: Michael Wiese Productions.
Wardrip-Fruin, Noah. 2009. Expressive Processing. Cambridge, MA: MIT Press.
Wolfram, Stephen. 2002. A New Kind of Science. Champaign, IL: Wolfram Media.
Wright, Will. 2003. “Dynamics for Designers.” Lecture delivered at the Game
Developers’ Conference, San Jose CA, March 2003. Slides available at
www.slideshare.net/geoffhom/gdc2003-will-wright-presentation (referenced
May 19, 2012).

400 Project, 150

A
abstraction
elimination, 286–287
in Machinations diagrams,
81–82
process of, 286–287
simplification, 286–287
in simulations, 286–287
action games
level progression, 131
mechanics, 8
power-ups and collectibles in,
131–133
actions
challenges associated with,
43–44
effect of, 43
unexpected, 44
Adams, Ernest
definition of games, 1
Fundamentals of Game Design,
59
hierarchy of challenges, 229
player-centric design, 169, 292
adventure games, mechanics, 8
Alexander, Christopher, 148
America’s Army, 287, 299
analogous simulation, 288–289,
291–293
Angry Birds, 31
physics, 6
strategy in, 10
vs. World of Goo, 10–11
AP (artificial player). See artificial
players; players
arms race pattern
applicability, 330
collaborations, 331
consequences, 331
examples, 332
implementation, 331–332
intent, 330
participants, 331
related patterns, 332

structure, 330
type, 330
Art of Computer Game Design, 232
artificial players. See also direct
commands; Machinations
diagrams; players
activate(parameter) command,
175
adding to Machinations
diagrams, 172
additive script condition, 174
color-coded, 175
deactivate() command, 175
defining in SimWar, 191–192
designing strategies, 177
diagram with, 171
direct commands, 172–173
endTurn() command, 175
equality script condition, 174
if statements, 173–175
linking, 178
logical and script condition,
174
logical or script condition, 174
in Monopoly, 179
multiplicative script condition,
174
nonequality script condition,
174
purpose of, 177
Quick Run option, 176–177
relational script condition, 174
removing randomness,
177–178
script box, 172
script conditions, 173–174
selecting node for, 172
stopDiagram(message)
command, 174
values in conditions, 175
Ashmore and Nietsche, 35
attrition pattern
applicability, 321
collaborations, 322
consequences, 322
examples, 323–324
implementation, 322–323

intent, 321
motivation, 321
participants, 322
related patterns, 325
structure, 322
type, 321
avatars, customizing attributes of,
135–136

B
basketball
Difference pool, 116
negative feedback, 70, 116–117
positive feedback, 70–71,
116–117
battle, mapping, 141
Beck, John, 272
“Behavioral Game Design,” 109
Bioshock
moral layer, 295
physical layer, 295
political layer, 295
as satire, 295
Björk, Staffan, 151
blackjack game, length of, 2
board games
randomness vs. emergence in,
128
reliance on emergent
progression, 259
Bogost, Ian, 287
bombling keys, example of, 254
Boulder Dash, 9, 26
Brathwaite, Brenda, 297
breadcrumbs, defined, 72

C
Caesar III
advantages, 200
buildings, 204–205
city economy, 199
connecting components, 206
connections between
elements, 200–201
converter engine, 202

341

InDEx

InDEx

342

Game mechanics: advanced Game desiGn

Caesar III (continued)
described, 199
design patterns, 202
dominant economic structure,
202–203
dynamic friction, 202
economic buildings, 201
economic relationships, 200
engine building, 202
farms, 204
as game of emergence, 206
landscape, 202–203
maps, 203
markets, 205
mechanisms, 201
missions, 203
money for building, 203
multiple feedback, 202
negative feedback, 203–204
phases of progression, 206
players, 200
progress in, 224
residences, 204
resources, 199
restricting players, 202–203
Caillois, Roger, 222
cartoon physics, explained, 6
“The Case for Game Design
Patterns,” 150
Caylus board game, activators in,
92, 128
cellular automata
Game of Life, 53
generation, 48
study of, 48
threshold for complexity, 50
tower defense games, 50
Wolfram’s, 48–49
challenge to adventure, example
of, 36
challenges
adding to improve experience,
231–232
atomic, 229
focusing on, 229
relationship to actions, 43–44
chance, relying on, 126
chaos vs. order
emergent systems, 45–47
periodic systems, 45–46
characters, customizing attributes
of, 135–136

charts, using, 63
chess game
charting patterns, 65
endgame, 65
long-term trend, 65
material number, 64
middle game, 65
opening stage, 65
shape of, 64–65
strategic advantage, 64–65
choice, creating via enemies, 231
Chomsky, Noam, 293
Church, Doug, 149–150
Civilization, 28–30
city economy of, 318
development phases in, 47
discrete mechanics, 29
economies in, 197–198
economy construction, 77
gameplay phases, 30
golden ages, 30
historical periods, 30
phases, 29–30
random maps in, 126
reverse triggers in, 111
vs. StarCraft, 40
strategies, 29
technology tree, 144
Civilization V, negative feedback
in, 52
closed circuits, creating feedback
with, 114–115
cognitive effort vs. speed, 232
collectibles, indicating, 131–133
color-coding
delays and queues, 113
Machinations diagrams,
112–113
combat construction
example of, 141–142
in SimWar, 189
Command & Conquer: Red Alert, 69
communication
interactivity of, 278
model of, 276
communication theory
art and entertainment, 277
channel, 276
design challenges, 280–281
functions, 277

mechanics sending messages,
279–280
medium and message, 277–279
message, 276
poetic function, 277
receiver, 276
sender, 276
signal, 276
complex systems. See also
emergence; science of
complexity
active and interconnected
parts, 48–51
behavioral patterns, 53–56
behaviors, 46
categorizing emergence, 56–57
cell activity, 50
cellular automata, 48
defined, 45
destabilizing, 51–53
dynamic behavior, 49–50
ecosystems, 51–53
emergence in, 47
feedback loops, 51–53
intentional emergence, 56
long-range communication, 49
multiple emergence, 56
nominal emergence, 56
simple cells, 49
simple parts in, 26–27
stabilizing, 51–53
strong emergence, 57
weak emergence, 56
weather, 47
complexity
of game behavior, 45
of rules, 45
complexity barrier, explained, 37
complexity theory, applying to
phase transitions, 267
concept stage, 13
Connect Four
gravity in, 28
vs. tic-tac-toe, 27
consistency vs. realism, 44
continuous mechanics, 9
converter element, elaborations
for, 164
converter engine
applicability, 308
in Caesar III, 202

collaborations, 308
consequences, 309
examples, 309–311
implementation, 309
intent, 308
motivation, 308
participants, 308
related patterns, 311
structure, 308
type, 308
converters
explained, 62
vs. traders, 97
using with resources, 96
Conway, John, 53, 56
Cook, Daniel, 238–239
Copenhagen Games Collective, 5
core mechanics
explained, 4
of video games, 4
Counter-Strike, gun fights in, 24
Crash Bandicoot
Kata stage, 242
Kihon stage, 241–244
Kihon-kata stage, 241
Kumite stage, 242
Crawford, Chris, 25, 232

D
