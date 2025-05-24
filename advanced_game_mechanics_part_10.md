resources arriving, and while there, labor resources help pull olives from elsewhere
and store them in a local pool. The labor also helps convert the olives into oil. The
oil is stored in another pool until pulled from elsewhere, and the labor resources drain.

ChAptEr 9

n

Markets work like farms and workshops in that they use labor to pull in resources
from elsewhere. However, all they do is store the resources in a pool until required
by an outside process. A market disables its input after it has pulled a certain number of resources, reflecting the fact that it can hold only so many.

n

FIGURe 9.7
detailed mechanics
for residences, farms,
workshops, and
markets in Caesar III

206

Game mechanics: advanced Game desiGn

An important aspect of these economic components is that they can be hooked
up in various ways. Olive farms and markets both need to tap into the general
flow of labor resources to function. Farms produce resources that are stored at the
farm and in that way are made available for other components in the economy.
Another point you should note is that all these components have inputs and outputs, expanding the number of ways they can be hooked to other components and
creating more opportunities to create long economic chains and loops. This way,
the player is free to create many different constructions in the economy. For certain
games, this might even mean there are different dominant economic structures
that the player can build from its components.

III
Games in which players build an internal economy clearly fall into the category of games
of emergence. still, playing these games does offer some experience of progression.
Caesar III for example, provides a series of scenarios, each with its own particular
challenges and goals, and within each scenario there are a number of scripted events.
But even without these events, the process of building a city goes through a number of
stages. in the initial planning stage, players still have enough money to build anything
they might need. Later they find themselves managing crises or the city’s defense and,
finally, fine-tuning the city’s economy to reach tough economic goals during the end
stages of the later levels.
an important mechanism that contributes to this sense of progression is that, initially,
wealthier residences increase labor output, but after a certain point the labor produced
by a residence actually decreases as its inhabitants grow wealthier. This means that beyond a certain wealth threshold the city starts losing labor, reducing the effects of many
production buildings, which could destroy the economy. This creates phase transitions or
barriers in the city’s growth that are hard to negotiate.
Caesar III, as many other games of emergence, has its own rhythm and progression that
partly emerges from its dynamic game economy and partly from the scripted events that
are unique for every scenario.

Designing Lunar Colony
In the second part of this chapter, we will take the lessons learned from analyzing
Caesar III and apply them toward designing a new economy building game called
Lunar Colony. Lunar Colony is a multiplayer tabletop game that can be played with a
set of poker chips, a few playing cards, and a single (six-sided) die. You don’t need
a board to play; any flat surface will do. You can also use any other set of tokens as
long as they are all of the same size (for one play test we used LEGO blocks, and that
worked just fine). Depending on the number of colors of tokens you have access
to, you can play with any number of players. You will need to keep track of each

BUiLdinG ecOnOmies

207

Throughout this section, we place more emphasis on human play testing than on
simulating the game in the Machinations tool, although we still use Machinations
diagrams to explain the game’s economy. Simulations can complement, but never
replace, human play testing.

Rules (First Prototype)
In Lunar Colony each player develops a research colony on the moon. The players
compete for ore and ice, trying to build as many stations as possible. To do this, they
must build an infrastructure, research new technologies, and manage their economy.

Game maTeriaL
To play this game, you will need the following:
n

One playing card (used to measure distances).

n

One six-sided die.

n

At least 10 white tokens per player to represent ice.

n

At least 10 black tokens per player to represent ore.

n

At least 20 green tokens to represent energy points.

About 20 tokens, all of the same color, to represent one player’s stations, and 20
more of a different color for each additional player. You need as many different colors as there are players. (Most poker chip sets include blue and red chips, suitable for
two-player games.)

n

n

A flat playing surface.

seTUP
To set up the game, the players must first create a playing area. (Like Civilization and
SimCity, Lunar Colony starts with a “randomly generated” map.) Use the following
procedure for this first prototype of the game:
For each player in the game, set aside 10 ice tokens and 10 ore tokens. Create a
single pile for all ice tokens and a single pile for all ore tokens. More may be needed
during play, so keep them accessible too.

n

The players take turns setting up the playing area. The first player starts the setup
by rolling a die. If he rolls a 1, 2, 3, or 4, he takes that many ore tokens from the
ore pile and places them anywhere on the playing surface in a single stack to form
an ore lode. If he rolls a 5 or 6, he takes that many ice tokens from the ice pile and
places them anywhere on the surface in a single stack to form an ice lode.

n

NOT E We designed
Lunar Colony as a
tabletop game made
from simple materials. This way, you can
both play and extend
it easily. Throughout
this section, you will
find design challenges
that suggest directions for you to explore.
We encourage you to
explore these ideas but
also any other interesting mechanics you
might think of.

ChAptEr 9

player’s technology level on a piece of paper. A two-player game of Lunar Colony
should take 15 to 20 minutes to complete.

208

Game mechanics: advanced Game desiGn

The next player rolls the die and does the same thing, placing ore or ice tokens
somewhere on the table. Players keep placing tokens until both piles are depleted
and all the tokens are on the table (if the die roll is higher than the number remaining, simply put all the remaining tokens of that color into play).

n

Figure 9.8 displays what a two player setup might look like. Note that it is permissible to place lodes adjacent to each other.

FIGURe 9.8
ice and ore lodes
spread across the
“surface of the moon”

Once all the ice and ore tokens are placed on the table, the first player sets up his
starting colony with three tokens of his color. These tokens represent stations. He
must place one token so that it touches exactly one ice lode and one token so that
it touches exactly one ore lode. This claims those lodes for him, and no other player
may set up a station touching his lode. He may place the third token anywhere
he likes, including to claim another lode. If it does not touch a lode, it is called a
way station (see the next section, “Stations”) and is used to help transport ice and
ore. Initially, these materials cannot be transported farther than the length of the
short side of the playing card, so it is best to keep the stations relatively close to one
another. Way stations are used to close larger gaps.
When the first player is finished, the next player sets up his colony in the same way,
and so on, until all players have set up their colonies. Figure 9.9 shows how two
players placed their colonies and are now ready to start playing.

FIGURe 9.9
The game is set up,
and two players (red
and blue) are ready
to play.

BUiLdinG ecOnOmies

209

In the game, the players build different types of stations. Stations are represented
by stacks of tokens (initially just one) of their own color. Any station can store ice,
ore, or both by stacking them. If a station is a mine, it stores whichever substance
it mines, but any station can also store ice or ore received through transportation.
Players can build the following stations:
n

Ice mines. A station that touches an ice lode is an ice mine.

n

Ore mines. A station that touches an ore lode is an ore mine.

Way station. A station that doesn’t touch either an ice or an ore lode is a way
station. Ice mines and ore mines whose lode is depleted automatically change into
way stations.

n

PLaYinG The Game
Players take turns, and in each turn they may perform a number of actions. To
determine the number of actions a player may perform, divide the number of stations he has by two and round up any fractions. Because the game always starts
with three stations for each player, in the first turn each player will always get two
actions. In each action, the player may choose to do one of the following:
Mine for ice. Take one ice token from the ice lode next to one of his ice mines and
store it on the mine (a station can have any number of ice or ore tokens stacked on it).

n

Mine for ore. Take one ore token from the ore lode next to one of his ore mines
and store it on the mine.

n

Transport resources. Move one ice or one ore token between two of his stations.
The two stations cannot be farther apart than the short side of a playing card.

n

Build a new station. Remove an ore token stored in any station and discard
it. Place a new station of the player’s color somewhere on the surface, close to the
station from which the ore came. The distance between the new station and the
original station cannot be longer than the short side of a playing card.

n

Expand station. Remove an ice and an ore token from a station (it must have at
least one of each), discard them, and add an additional station token to the stack.
The size of a station is the number of tokens of the player’s color in its stack.

n

Produce energy. As a single action, any station with ice stored in it can produce
energy. To produce energy, remove any number of ice tokens from the station and
discard them. For each ice token removed, the player receives as many energy tokens
as the size of the station. (In other words, if the station is two tokens big and he
removes three ice tokens from it, he will get six energy tokens.) Energy tokens are
not stored in the playing area but held by the player.

n

Research. Players can spend energy points to buy a technology (see the next
section, ”Technology”).

n

ChAptEr 9

sTaTiOns

210

Game mechanics: advanced Game desiGn

During one turn, any station can be used in action only once, so a station can be
used only to mine, build, expand, or produce energy in a given turn. Transporting
resources and doing research (buying a technology) are considered actions, but they
do not involve a station in an action. Any number of resources may be moved to
and from a station after which it can still be involved in another action.

TechnOLOGY
Players can spend their energy points to buy any one of the following technologies
as a single action. Each technology costs three energy points:
Fast Ice Mining. When mining for ice, the player can take two tokens from the
mine’s supply instead of one.

n

Efficient Ore Mining. For every ore the player mines from a lode, he can take
one additional ore token from the unused ore tokens that are not on the map.

n

Transportation Capacity. The player can move two substance tokens, instead of
one, from one station to another station as a single action.

n

Long Range Shuttles. The player can use the long side of the playing card
instead of the short side to determine how far he can transport resources or at what
distance he can build new stations.

n

Luxurious Habitats. This technology comes into effect only when counting up
the score. A player who has the Luxurious Habitats technology gains additional
points for large stations. See the next section, “Winning the Game,” for details.

n

When a player purchases one of these technologies, he should write it down on a
piece of paper as public record that he has done so.

WinninG The Game
When any player mines either the last ore or the last ice from the surface of the
moon, the game ends after he finishes his turn. The players then score the game
as follows: Players who do not have the Luxurious Habitats technology score
exactly one point for every station they hold of size two or more. Players who have
purchased Luxurious Habitats count differently: They get extra points for larger stations: one point for each expansion above two. In other words, a size three station
earns them two points, size four earns three points, and so on.
The player with the most points wins.

BUiLdinG ecOnOmies

211

basic economic Structure
ChAptEr 9

Figure 9.10 shows the basic economic structure of Lunar Colony. It is a color-coded
and turn-based diagram. Mine Ice and Mine Ore are interactive nodes that pull these
resources from their respective pools when clicked. (Mine Ice is a gate, while Mine
Ore is a converter for reasons we’ll explain in a moment.) Buying the technology
upgrades for ice and ore mining improves their productivity: Fast Ice Mining causes
the Mine Ice gate to pull two ice resources instead of one. Efficient Ore Mining does
not cause Mine Ore to pull two ore resources; rather, it causes the Mine Ore node to
turn one incoming ore resource into two, which has to be done with a converter
rather than a gate.

FIGURe 9.10
The basic economy of
Lunar Colony. This
diagram requires
additional details
to work in the
machinations Tool.

Once ice and ore resources have been mined, they go into a common pool labeled
Resources. From this pool, ore is used to build stations, ice is used to produce energy,
and both ore and ice are required to expand a station. The diagram also includes
a very simple mechanism to simulate the fact that resources are distributed across
the tabletop in the real game. The player starts with limited access to resources—he
can use only the ones in the Accessible Ice and Accessible Ore pools. By building extra
stations, he has a 50% chance of making more ore accessible and a 25% chance of
making more ice accessible. These probabilities are taken from the density of the
resources on the table, which was established during the setup phase.

NOT E Figure 9.10
has a register labeled
Actions. in a turnbased diagram, a
register with that label
can be used to change
the number of actions
a player can take every
turn. in this case, it is
used to increase the
number of actions as
the player builds more
stations.

212

Game mechanics: advanced Game desiGn

The diagram omits a number of mechanics. It doesn’t show how ice and ore must
be transported across the table, and it doesn’t show the Transportation Capacity
and Long-Range Shuttles technology upgrades that affect that part of the game.
Some of the mechanics are unspecified: The Luxurious Habitats technology has a
positive effect on the number of points, but this depends on the size of the players’
stations. Similarly, having more enlarged stations is likely to increase the energy
production, but this also depends on factors such as station positioning and other
player decisions.
The game features two design patterns. First there is a dynamic engine: ore and ice are
used to produce research stations and energy points. The energy points in turn are
used to improve the production of ore and ice. It’s easiest to spot this by looking at
the loop for ice. A second dynamic engine increases the number of actions available
per turn as the result of spending ore to build more stations. The second pattern is
the engine-building pattern. Through technology research, the player has some control over what parts of her engine to improve (actions per turn or production rates).
Two things to notice about this economic structure are that it includes only positive
feedback, and the game allows little direct interaction between the players. There’s
no concept of attacking other players or stealing their resources. The most important source of friction in the game comes from having to build way stations, which
occurs if the distance between the resources on the tabletop is large. However, this
friction is mostly static (it doesn’t change with the state of the engine) and is determined by the initial setup. As the game progresses, the friction may increase as the
players need to build more way stations to get to the last resources on the table.
The basic game is already fairly balanced between the players in this initial prototype, although the starting positions they choose matter a great deal. The player
who picks the best starting position is very likely to win, as you might have guessed
from the lack of negative feedback in the economy.

desiGn challenGe
The end conditions for Lunar Colony might not be the best. can the game continue until
all resources are removed from the surface or when all of them are consumed? What would
happen if the game ends when somebody collects four or five points? What would be a
better number of points, and why? design a different type of end condition for the game.

desiGn challenGe
By looking at the basic economic structure of the first prototype for Lunar Colony, think of
a way to add negative feedback to the game. as a place to start, you might want to start
by going over the design patterns in appendix B.

BUiLdinG ecOnOmies

213

building blocks
ChAptEr 9

The first prototype has only one building block: stations. Figure 9.11 illustrates
this building block. Mining stations act just like way stations with one exception:
Mining stations can pull resources from the board. The mechanics for this building
block fulfill the requirement that it can hook up with other blocks in the game in
several ways. However, in the initial prototype, all the stations function in more or
less the same way. The player needs to think about where to place stations to ensure
that they are all close enough to one another to permit transportation. The only
other consideration is which stations to expand. In general, the best choices for
expansion are the stations that are close to ice and (to a lesser extent) close to ore.

FIGURe 9.11
The mechanics for
a station in Lunar

Colony

With effectively only one building block, there won’t be much variation in the way
players build up the economy. What the game needs is more types of stations to
give the players more interesting choices.
To improve the game, we’ve designed three new stations: purifiers, refineries, and
transporters. This second version of the game now requires two additional colors
of tokens to represent purified ice or refined ore, respectively. We also changed the
rule that states that the number of actions available is determined by the number
of stations that a player has. Instead, every player starts the game with two actions,
but one of our new stations will change that during the course of play. Figure 9.12
shows the new types of stations (note each has a different color token placed under
the player’s color):

FIGURe 9.12
new types of stations
in Lunar Colony

Purifiers take normal ice and turn it into twice as much purified ice by expending energy. Purifiers can’t be built from scratch or at the beginning of the game.
Instead, they must be converted during the game from existing size 1 stations. To

n

214

Game mechanics: advanced Game desiGn

N OT E ideally, the
purified ice and purified ore tokens should
be similar in color to
their original forms, for
example, white for ice
and gray for purified
ice. in our playtests,
we didn’t have more
colors, so we tacked
small Post-it notes to
the original tokens to
indicate their changed
states.

build a purifier from an ordinary size 1 station (ice mine, ore mine, or way station),
the player must have at least one ice token stored in the station and pay two energy
tokens. Place the ice token used under the station to indicate its new type. A purifier can no longer be used to mine or produce energy and cannot expand. However,
as a single action, the player can purify all the ice stored on the purifier (or as much
as desired) by spending one energy token per ice token purified. To do this, replace
each ice token to be purified in the station with two purified ice tokens from the
reserves off the table. Purified ice cannot be purified further. Purified ice is not really
different from, or more valuable than, ordinary ice. It is used in the same way, and
all other stations can use purified ice instead of normal ice in their operations. The
function of a purifier is simply to double the amount of ice available by expending
energy.
Refineries work on ore exactly as purifiers do on ice; the only difference is that the
refining process costs more. As with purifiers, to build a refinery, take an ore token
from the station, put it underneath the station as identification, and pay two energy
tokens. When converting ore on the station, pay two energy tokens per ore token
refined, and replace the ore token with two purified ore tokens.

n

Transporters increase the number of actions the player can take in a turn and
transport resources rapidly by expending energy. A player can change any ordinary
size 1 station (ice mine, ore mine, or way station) into a transporter. To build a
transporter, the player pays two energy tokens. Place one energy token under the
station to indicate its new type. Like purifiers and refineries, a transporter can no
longer be used to mine or produce energy and cannot expand. For each transporter
the player builds, he gains one action per turn. In addition, the player can transport
any or all resource tokens stored in a transporter to a single destination station
anywhere on the surface for the price of one energy token.

n

Why make reFininG more expensiVe?
You might wonder why we made refining ore cost more energy than purifying ice. The
reason is that if a player has the efficient Ore mining technology, he can already produce
two ore resources out of one. Players can potentially mine 40 ore in a two-player game.
The Fast ice mining technology means that ice will be mined faster, but 20 is still the
maximum in a two-player game. This means that for the game resource balance, it is better to stimulate the duplication of ice rather than that of ore.

Figure 9.13 illustrates the mechanics of these extra types of stations.

BUiLdinG ecOnOmies

215

FIGURe 9.13

ChAptEr 9

new station types

desiGn challenGe
With the extra types of stations, you might want to create a longer playing experience to
let the player explore new strategies that these features offer. The purifier and refinery
already might lengthen the playing time until the last resource is mined from the table.
can you find out what number of initial ice and ore resources, placed at the beginning of
the game, works best?

desiGn challenGe
The purifier and the refinery are quite similar. The only differences are that they work for
different resources and have a small difference in energy cost. in games, it is generally
a good idea to diversify the functions of the game elements. right now, the risk is that
ice and ore will start to feel exactly the same. can you come up with alternative rules for
either one of the stations that are different but balanced?

216

Game mechanics: advanced Game desiGn

These rule changes make two important changes to the basic economic structure:
They remove the dynamic engine that was formed by gaining an action for every
two stations that you build. It is replaced by a new dynamic engine that operates
via transporters. The old system also produced a lot of feedback because players
had to build many way stations to get to remote resources and produced a lot of
static friction because they had to spend ore to build those stations. The new system
reduces both the feedback and the friction.

n

The role of energy has grown more important. Players can now use energy to
duplicate resources. This creates a converter engine, as shown in Figure 9.14. Energy
may be used to produce more ice (via purification), and ice may be used to create
more energy. From this figure it should become clear that building purifiers make
sense only when the player can convert ice into at least two energy tokens. Also,
these changes create a much higher demand for energy, and it might be a good idea
to increase its availability somehow.

n

FIGURe 9.14
The new converter
engine in Lunar

Colony

more Features, more upkeep
The downside of the suggested rule changes is that the game becomes slower and more
cumbersome to play. There is more information for the player to keep track of. Because
this game is only a prototype, you shouldn’t worry about this too much, however. if you
converted the prototype into a video game, the computer would be responsible for the
bookkeeping, and if you used it to develop a board game, the physical and graphical
design of the board would be used to help players keep track of the game.

Obstacles and events
One of the great features of Caesar III is the way that it uses obstacles and scripted
events to create different experiences for every mission. You can use them to improve
Lunar Colony as well. Here are some suggestions to create obstacles:
A very simple obstacle can be created by making parts of the playing surface
unavailable. Put anything that comes to hand (books, cups, small boxes) on the table
before setting up the game. Resources and stations can be placed only on the table

n

BUiLdinG ecOnOmies

217

itself, not on anything else. With enough obstructions, this could lead to completely
different play experiences.
Another simple way to create obstacles is to use a few blank sheets of paper to
indicate rough terrain. When setting up the game, the players must place all the
resources on the rough terrain, but stations on rough terrain cannot grow in size.
Or you might decide that stations on rough terrain cannot change into purifiers,
refineries, or transporters.
Stations themselves can also be used to create impediments. After all, in most
economy-building games, players have to deal with all sorts of limitations caused
by their own buildings. One example would be that no refinery or purifier can be
built too close to mines. They must be built at least the short length of a playing
card away from these stations.

n

Here are a few suggestions for events that you can add to Lunar Colony. Because it is
inconvenient to add scripted events to a board game prototype, a number of these
suggestions use random ways to create events. However, we designed them so that
any event would affect all players (although not always equally). This helps make
sure that luck doesn’t become too great a factor in the game.
We can create random events by having players throw a die at the end of their
turn. A roll of 5 means that the player can place three new ice tokens from the
unused tokens not on the table. He must place each token on a different ice lode.
A roll of 6 indicates that all players get the option to pay three energy tokens to
score an extra point at the end of the game. (You will need to write this down when
it occurs.)

n

Instead of using a die to generate random events, use homemade cards with
events written on them. At the end of his turn, a player draws a card to determine
the random event and then discards it. When the deck is exhausted, shuffle the
discard pile and use it again. Cards allow the designer far more control over the
distribution of the events. If, in a deck of 12 cards, there are two cards that will
add ice to the game, you are certain that event will happen twice every 12 turns.

n

You can also use cards to script a scenario. By placing the cards in a particular
order, you can control exactly how and when what event is going to happen. This
can be used to give players goals for the game. For example, if they know that after
10 turns they can earn extra points for selling ore, they could prepare for it. It could
even be used to create a solitaire version of the game, although in that case, you
would need a designer to set up the starting situation and determine the order of
the cards.

n

Cards can also be used to give all players one or more secret objectives during
the game. For example, they might score extra points if they end the game with
five energy tokens, get bonus points for building a size 4 station, and so on. Secret
objectives can spice up the game but work best if they include more mechanics that
support direct interaction between players.

n

ChAptEr 9

n

218

Game mechanics: advanced Game desiGn

desiGn challenGe
devise three different ways to add obstacles or events to Lunar Colony. Work out the rules
and playtest the gameplay for at least one of them.

desiGn challenGe
create mechanics and an interesting scenario for a single-player version of Lunar Colony.

Additional economic Strategies
In economy-building games it is always a good idea to provide multiple viable
economic strategies. We widened the economic options for Lunar Colony with the
addition of purifiers and refineries. In this last section, we will discuss one more
option that will also create more interaction between players: raiding.
Raiding is best implemented by using the attrition design pattern (see Appendix B),
but in a form in which the opposition’s resources are stolen rather than destroyed.
You must be careful that a new mechanism like this one doesn’t unbalance the
game. If raiding is too effective, it will become a dominant strategy: The players will
use raiding only, and the other mechanisms will become obsolete. If it is too weak,
nobody will use it, and there was no point in including it at all.
In general, two design approaches can help you create a balanced experience:
Make sure that the two strategies (in this case building versus raiding) are differentiated in the risks and rewards they might bring. We have already seen this in the
previous chapter when we discussed SimWar. In this case, it makes sense to at least
increase the risk involved in raiding.

n

Don’t try to balance two strategies, but create three strategies in a rock-paperscissors relationship. These relationships are more stable than a two-strategy balance,
because even if one strategy appears to be better most of the time, players can start
choosing the strategy that beats it more frequently. Rock-paper-scissors relationships
are less affected by slight imbalances between the strategies.

n

In the case of Lunar Colony, we opt for the first design approach. We will make raiding more risky. At the same time, we will make the raiding more effective for players
who are falling behind. This way, it creates an additional negative feedback loop
that will keep the game tight and fun.

BUiLdinG ecOnOmies

219

Players gain the following possible actions during a turn:
Build Raider. Pay one energy to build a raider in any station. Place the energy
token on top of the station to represent the raider.
Raid. Raiders can be used to steal resources from another player, but only if they
are in range. Raiders can target any enemy station within the length of the long side
of a playing card. When raiding, the active player rolls a die. If the number is lower
than or equal to the number of resources (ice and ore) that are currently stored in
the target player’s station, the raid is successful, and the acting player can take one
substance token from the target station and place it on the raider’s own station. The
player then rolls the die again. If the number rolled is lower than or equal to the number of resources (ice and ore) on his own station, the raider is destroyed. A raider can
be used only once per turn, but multiple raids can be launched from a single station
on successive turns.

n

desiGn challenGe
Find out whether the rules for raiders work and have the intended effect.

desiGn challenGe
create mechanics that allow players to defend against raids.

Summary
We examined games that, rather than providing the player with an economy,
permit her to build her own. These can be single-player games or multiplayer competitive ones. A key quality of economy-building games is that they offer the player
building blocks—often such things as buildings and roads—that let the player set up
economic relationships of her own design. We examined two such games in some
detail so that you could learn from their design: Caesar III, a single-player game, and
Lunar Colony, a multiplayer game of our own. We showed how, with some very simple building blocks, Lunar Colony creates a “land rush” for resources. We illustrated
how a designer could add some improvements for the game to make it richer and
more exciting, and we suggested ways to create a sense of progression in the game
using scripted events.
The next chapter delves further into the question of progression and shows how
game mechanics interact with level design and storytelling.

ChAptEr 9

n

220

Game mechanics: advanced Game desiGn

Exercises
1. Complete all design challenges in this chapter.
2. Create an automated model for a single-player version of Lunar Colony that can
be used to collect statistical data and use it to tweak the balance of the game.

3. Create a paper prototype for an economy-building game of your own. Build a
model for it in the Machinations Tool. Simulate the game in the tool, and play test
and refine the game with other people (if it’s a multiplayer game). Keep track of the
changes you make and why you made them.

ChAptEr 10
Integrating Level Design
and Mechanics
ChAptEr 10

In this chapter and the next, we shift our focus from purely emergent game mechanics
to mechanics as a tool for progression design. We look at the ways that game levels
organize their challenges into missions and how they interweave a story with the
player’s progress. Although people often think of level design as creating spaces or
using software level design tools, game mechanics play an equally important role in
defining how a level provides challenges to the player.
In this chapter, we investigate how to integrate level design with the design of game
mechanics. We look at different kinds of progress that take place in games and
address how levels structure play. We also discuss ways that you can use levels to
introduce game mechanics in such a way that players can get into the game easily.

From Toys to Playgrounds
A game’s mechanics should provide players with enjoyable gameplay, and most
games offer players a structured environment and an orderly progression of goals as
part of the experience. Creating the environment and the goals is part of the level
designer’s job. Level design also introduces the players to the game’s mechanics a
little at a time. In this chapter, we will focus on the role that levels play in structuring the gameplay experience. In the terminology of Kyle Gabbler (see the sidebar
“Make the Toy First” in Chapter 1, “Designing Game Mechanics”), thus far we have
been focusing on using mechanics to construct a toy. Now it is time to use that toy
to create a playground.

Structuring Play
We generally think of toys as enablers for free-form play, in which players can set
their own goals or play without any goals at all. Games come with a predefined goal
that specifies exactly under what conditions you beat the game or your opponent;
this is also called the game’s victory condition. Victory conditions can be very simple,
such as to destroy all enemy ships or collect a certain number of points. Some goals
are unachievable in practice: No matter how many aliens you destroy in Space Invaders,
the game continues to throw fresh waves at you until you lose your last life and
the game is over. In this case, the real goal of the game is not to defeat all the alien

221

222

Game mechanics: advanced Game desiGn

invaders but to survive and score as many points as you can before the game is over.
The high-score table that Space Invaders displays after each session supports this goal
and serves as a reward if you do well enough to enter your own initials.

learninG From real play spaces
The word playground is not just a convenient metaphor. as a game designer, you can
learn a lot by paying attention to various real-world spaces intended for play. For
example, theme parks are laid out cleverly to immerse their visitors in a fantasy world
yet still prevent them from getting lost. (This is the function of the castle in the middle of
disneyland; its height makes it visible from almost anywhere in the park and helps visitors orient themselves.) miniature golf courses have imaginative designs, too, increasing
in difficulty over their 18 holes. The courses start out easy enough but soon introduce
challenges such as bouncing off corners, navigating slopes, or going through tunnels.
some miniature golf courses add unique and wildly imaginative features. designing
miniature golf holes is a good exercise for anyone who wants to be a game designer.

Games of emergence typically establish simple goals such as collecting the most
points or defeating enemy units. In these kinds of games it takes skill, strategy, and
experience to play the game’s mechanisms and get the game into the state that the
victory condition is met. This works well for short games in which the mechanics
produce emergent gameplay but are not too complex. This way, players can develop
their game-playing skills and strategies over multiple short sessions. For games of
emergence, the exact definition of the goal can make a big difference (see the “Goals
in Machinations Diagrams” sidebar).

playinG Vs. GaminG: paidia Vs. ludus
The French scholar roger caillois, writing in his book Man, Play, and Games (1958), was
among the first to make a distinction between goal-oriented gameplay and free-form
play (as well as other forms). he used Latin terms for the names of his different categories of play. caillois states that games can be classified on a continuum from paidia,
where the focus is on unstructured playful activities, to ludus, where the focus is on
structured goal-oriented behavior. You can think of these two poles as playing and
gaming, respectively. Paidia is often associated with the way children play, while ludus
is often associated with more adultlike games or sports. Traditionally, games are found
on the ludus end of the scale, but certain games, for example role-playing games, offer
many opportunities for more free, paidia-like play at the same time. Ludus, or goaloriented gaming, is not necessarily better than paidia. it is a major design challenge to
offer both forms of play in one game and produce a harmonious result.

inTeGraT inG LeveL desiGn and mechanics

223

Goals in machinations diaGrams

In games of progression, goals also tend to be simple: find the treasure, rescue
Princess Peach (again), or defeat the evil wizard. However, in progression games,
achieving the victory condition requires the player to achieve many subgoals first.
Players progress from goal to goal until they can try to complete the final goal.
Compared with games of emergence, performing the action necessary to win the
game might not be all that difficult, but there are many more things the player must
do before she can even attempt that final action.
As we explained in Chapter 2, “Emergence and Progression,” emergence and progression are not mutually exclusive categories. Many games have elements of both.
The player’s experience benefits from game mechanics structures that create emergent gameplay, but very long games also need progression features to create a sense
of purpose for the player and variety in the gameplay.

Structuring Progress
Players can get a sense of progress in a game in a variety of ways. In the next few
sections, we explore different kinds of progress.

PrOGress ThrOUGh cOmPLeTinG TasKs
As designers, we can define progress in a game in terms of the number of tasks the
player has completed. This assumes that the game has a victory condition and that
it is something a player can actually achieve. This type of progress is often represented as a percentage: “You have completed 75% of the game.” Many games also
offer optional tasks that players don’t have to perform to win the game. In those
cases, the percentage of progress can be relative to the total number of tasks available, but the victory condition is set at less than 100% or is defined in terms of
specific tasks rather than numbers. For example, Grand Theft Auto III measures
progress in terms of many optional stunts and challenges, and the game lets you
continue to work on them even after you have nominally achieved victory. Many
classic adventure games such as the Kings Quest or Leisure Suit Larry series measure

ChAptEr 10

machinations diagrams use end condition elements to simulate goals in games. how
you define these goals can have a dramatic effect on the gameplay. For example, the
target number of energy points needed to win the harvester game determines the ideal
number of harvesters to build. (We introduced the harvester game in the section “Use
randomness to counter dominant strategies” in chapter 6, “common mechanics.”) if you
were to change the goal of the harvester game from a target number of energy points to
a target number of harvesters instead, it would create a different dynamic in which all
the players try to build harvesters as fast as possible (which doesn’t necessarily constitute better gameplay).

224

Game mechanics: advanced Game desiGn

progress in terms of a number of points earned by performing particular actions.
Again, most of these games could be finished without scoring all the points, and
players would replay them with a goal of completing the game with all possible points.
In games in which progress comes through performing tasks, you must offer players
enough variety to keep them engaged; you can’t simply string together a sequence
of identical tasks. You must also pace them correctly and create a suitable difficulty
curve to keep the player both interested and challenged.

the aesthetics oF shiFtinG perspectiVes
most people find sudden shifts in views or perspectives a pleasant and aesthetic experience. You might recognize the feeling from hiking through mountains. as you make your
way up through a forested hillside, your view is quite limited. Trees prevent you from
seeing far, and you are probably focused on a rocky trail. When you get closer to the
top, the landscape suddenly opens up. Trees are replaced by open meadows, and all of
a sudden you can see for miles around. For many, this sudden shift is one of the rewards
for going hiking in the first place. Well-paced changes in gameplay and environment can
have a similar result in games. it is one of the reasons it is always a good idea to have
different styles of landscapes or backgrounds in different sections of your game.

PrOGress as disTance TO TarGeT
In games of emergence, progress is more difficult to measure in terms of numbers of
completed tasks, because the tasks in such games are seldom discrete subgoals on
the way to the main goal. Yet, because these games often have a victory condition
that is stated in numeric terms, we can measure completion on that basis rather
than in terms of tasks. For example, in Caesar III (see the discussion in Chapter 9,
“Building Economies”), the goal of a certain level might be to build a city’s population up to a certain size. No specific sequence of actions leads to that target, but we
can still tell players how close they are to the goal. However, in these cases, the completion percentage doesn’t always guarantee that the player will achieve the victory
condition in a fixed amount of time. A player might have built a city that hosts 90%
of the target population, but if she also ran out of building space or has no access to
the food supplies needed to grow the city any further, she might still be a long way
from obtaining the remaining 10%.
A crucial difference between this type of progress toward goals through emergent
gameplay and more classical progress through completing tasks is that the player
can experience setbacks. In the Caesar III example, players might lose citizens and
buildings to invading barbarians, thus increasing the distance between their current
achievements and the target. By contrast, once a task is finished in an adventure
game, it can never be undone; the player never loses the benefit of achievements
already obtained.

inTeGraT inG LeveL desiGn and mechanics

225

PrOGress as characTer GrOWTh
A third way you can measure progress is through the avatar character’s own growth
in strength or abilities. Role-playing games typically use this type of progress, especially table-top role-playing games and massively multiplayer online role-playing
games (MMORPGs) that lack a goal that ends the game. Progress in these games is
measured in numeric character levels, which are obtained by collecting numeric
experience points. This type of progress tends to be open-ended: there may be no
limit to the level a character can achieve. It also has the potential to offer branching growth paths, if players have to choose between different ways to advance their
characters, especially when these options are mutually exclusive. A good example of
this type of development is found in Deus Ex. In this game, players can find augmentation canisters that increase a character’s abilities. Each canister offers a choice
among several cybernetic enhancements. Every choice is offered only once, and the
players have to decide between options that support different playing styles.
As with all types of progress, character development is used to structure gameplay.
For example, a player character must have a particular score for a strength ability
before being able to progress to certain areas. However, because the game designers don’t have direct control over how the player chooses to develop a character,
the game may need to support many different approaches to get to the same point
in the game. In some cases, the game offers different possible endings based on the
way the player character developed.

PrOGress as PLaYer GrOWTh
You can measure the player’s progress through the game in yet another way:
through the player’s own growth in skill. Compared with role-playing games, the
avatar characters in action-adventures such as The Legend of Zelda, Super Mario Bros.,
or Metroid Prime don’t progress much. They unlock new abilities and gain more life
points over the course of play but possess nothing like the fine granularity offered
by the character attributes in role-playing games. In action-adventure games, the
game trains the player to use his avatar’s abilities through increasingly difficult and
complex challenges.

ChAptEr 10

Another difference is that progress toward completing tasks typically follows a
predesigned trajectory that takes no account of the player’s level of skill. (Puzzlebased adventure games normally have no difficulty settings the player can adjust.)
Progress in emergent systems adapts to the player’s performance naturally—or it
can if you set up your mechanics correctly. For example, you can use the escalating
challenge and escalating complexity patterns (see Chapter 7, “Design Patterns,” and
Appendix B) to adapt quickly to a player’s level of skill. In an emergent game, variation in the gameplay has to come from different phases that the game goes through
as a natural part of its mechanics (see the section “The Shape of a Game of Chess” in
Chapter 4, “Internal Economy”). You can use the slow cycle pattern (Chapter 7 and
Appendix B) to cause gameplay phases to emerge.

226

Game mechanics: advanced Game desiGn

In many action-adventure games, abilities unlock new areas for the player to
explore, but often it is the player’s level of skill that determines whether he is able
to reach a certain location in the game world. Use the environment to measure
your player’s ability. Children do this all time in the real world, trying to walk on
low walls, jump over fences, or set themselves challenges such as not stepping on
cracks in the pavement. Many games use this learning instinct to great effect. When
players see a collectable coin in an odd location in a platform game, most will
immediately assume the designer intended it to be reachable and will try to find
out how to use their avatar’s abilities and their own game-playing skills to get there.
You’ll find that this instinctive and playful approach to the environment is a useful
design tool for creating compelling game worlds.

Focusing on Different Structures in Your Mechanics
Large games structure their gameplay into multiple distinct levels because their
mechanics are simply to complex to throw at the player at once, especially in the
early stages when the player doesn’t know the game well. By creating different levels or areas in the game that focus on different mechanisms, the game breaks down
its complex machinery into easier-to-manage segments. At the same time, it creates
more variety in the gameplay and can require the player to explore different strategies for playing a particular game.
In some games, each level focuses on a different aspect of the game mechanics. This
requires a mechanics core that is large enough to include multiple structures that
generate their own gameplay—enough gameplay to carry a level. Early levels in the
game highlight different subsets of the mechanics, while later levels might include
all the mechanics. Figure 10.1 illustrates this. It shows how different subsets of the
mechanics from the basic Lunar Colony game economy (Chapter 9) can be used to
create different levels. Because the core set of mechanisms of Lunar Colony is not
very large, each of these different versions will probably feel like a new introduction
to the game’s mechanics.
StarCraft II uses this technique to great effect. As with most real-time strategy games,
the economy of StarCraft II is extensive and includes resource harvesting, base building, and technology researching to create an effective strike force. The first level
doesn’t involve any building. It simply lets you learn to manage your combat units
and focuses on movement and combat. The second level introduces the base and
resource-harvesting mechanics, but only a handful of buildings are available at this
time. Only after completing particular levels do more buildings and unit upgrade
options become available. After the first three levels, players get to choose which
level they would like to do next, allowing them to pursue specific goals.

inTeGraT inG LeveL desiGn and mechanics

227

FIGURe 10.1
different subsets of the
core mechanics create different levels for

ChAptEr 10

Lunar Colony.

A big difference between the original StarCraft and StarCraft II is that many missions
