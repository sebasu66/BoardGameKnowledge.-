TABLETOP

ANALOG GAME DESIGN

Copyright © by

Greg Costikyan
Drew Davidson et al.
&
ETC Press
2011
ISBN: 978-1-257-87060-8
Library of Congress Control Number: 2011933529
TEXT: The text of this work is licensed under a Creative Commons
Attribution-NonCommercial-NonDerivative 2.5 License
(http://creativecommons.org/licenses/by-nc-nd/2.5/)

IMAGES: All images appearing in this work are used and reproduced
with the permission of the respective copyright owners,
and are not released into the Creative Commons.
The respective owners reserve all rights.

Design & composition by Ethan Gladding and Maya Irvine

CONTENTS

INTRODUCTION

13

DESIGNING TABLETOP GAMES

15

The Three Player Problem .....................................................................................................................17
Lewis Pulsipher
Simulation Game Design
James F Dunnigan

27

Randomness, Player Choice, and Player Experience
John Kaufeld

33

Dice as Dramaturge
Chris Klug

39

Designing for Publishing
JT Smith

49

Simply Knizia
Kevin Jacklin

55

Filtering Feedback
Ira Fay

61

15 games in 15 years
Stone Librande

69

GAME ANALYSES
Settlers of Catan
Ian Schreiber

91
93

Conquest
David Parlett

101

Fair Isn’t Funny: The Design of Cosmic Encounter
Peter Olotka

105

The Greatest Gift
Ray Mazza

111

Pandemic
John Sharp

129

Design Lessons from Poker
Richard Garfield

137

Ra
Brian Magerko

141

Train
Simon Ferrari

146

Twilight Struggle
Pat Harrigan and Noah Wardrip-Fruin

158

THE STUDY OF TABLETOP GAMES

169

Understanding Strategic Boardgames as Computational-Thinking Training Machines
Matthew Berland

171

Boardgame Aesthetics
Greg Costikyan

179

Improv
Brenda Bakker Harger

187

AUTHORS

199

TABLETOP
ANALOG GAME DESIGN

12

Tabletop: Analog Game Design

Introduction

INTRODUCTION

Much has been written about the videogame revolution, which is often portrayed as springing spontaneously from the forehead of Nolan Bushnell, like Athena from the brow of Zeus.
In a scant thirty some-odd years, we’ve grown from nothing to one of the world’s largest
entertainment forms, grossing tens of billions annually, with games being the mainstay of
entertainment and acculturation for most of the planet’s youth.
Works that discuss the evolution of the game industry from an historical perspective
generally talk about the connection between the pre-digital arcade and the earliest digital
games; I’ve even heard some claim that “without the arcade, videogames would not exist.”
This is, of course, bosh. Early creators such as Crawford, Garriott, Bunten, and the Brothers Gollop were not inspired by coin-drop amusements, but by tabletop games, either of the
board or roleplaying variety. Without the arcade, we might have fewer twitch games and
more that require cerebration, but that is another story.
Indeed, you can draw a direct line of descent from, say, Tactics II to Call of Duty, or from
Dungeons & Dragons to World of Warcraft – or, for that matter, from games like Rail Baron to
Farmville. If, as I do, you accept that digital and non-digital games are not different in essential nature, you must conclude that our history extends far longer than thirty years; as
Stewart Cullin documented in a series of landmark works for the Smithsonian at the turn of
the century, every Neolithic culture that survived into the modern era has its own games,
and one can presume that this was true millennia ago as well. Even if you prefer to draw a
line between what David Parlett (in the Oxford History of Board Games) calls “folk games,” and
games intentionally designed by identifiable creators, our history can be said to begin with
Don Casimir Freschott’s Map Game, published in 1680 in Venice; or perhaps with Cribbage,
designed by the poet Sir John Suckling in the early 17th century; or with A Journey Through

13

14

Tabletop: Analog Game Design

Europe, the first English-language boardgame ascribable to a creator, designed by John Jefferys and published in Britain in 1759. The last is perhaps the most important of the three,
since it is followed in subsequent decades by dozens of other original games, the first time
what we can reasonably call a “game industry” appeared, an evolution that led directly to
the 19th century efflorescence of boardgame publishing.
And far from being crippled by the advent of digital games, tabletop games have flourished in the same era – with ups and downs, to be sure, as waves of innovation have washed
over them: the rise and decline of wargames, roleplaying games, and trading-card games
followed, today, by increasing interest in Eurostyle boardgames.
As many game studies programs have discovered, tabletop games are particularly useful in the study of game design, because their systems are exposed to the player, not hidden
in code. It is easy to misunderstand the essential nature of a digital game, if you focus on
graphics or narrative without appreciating the way in which system shapes the experience,
a fundamental failing of the narratological school. Tabletop games may have an intimate
connection to narrative (as with roleplaying games), and certainly the nature of their graphics and components has an impact on the feeling of play; yet the system of rules they use to
shape the experience are explicit and immediately graspable. Digital games can be far more
complicated, in terms of the algorithms they use and the number of elements in play than
tabletop games, but they are controlled, in the final analysis, by algorithms that, like those of
tabletop games, create gameplay loops, provide positive or negative reinforcement, and pose
challenges to players they must work to overcome.
In other words, whether your interest is in tabletop games themselves, in game design as
a discipline, or in the historical evolution of the form, tabletop games are worthy of study.
In this volume, we have asked people of diverse backgrounds – tabletop game designers,
digital game designers, and game studies academics – to write about tabletop games. Some
have chosen to write about their design process, others about games they admire, others
about the culture of tabletop games and their fans. The results are various and individual,
but all cast some light on what is a multivarious and fascinating set of game styles.
This volume is not a definitive study of the field, nor of the design of tabletop games, nor
of their history; it is not intended to be. Rather, we trust that readers will find in these pages,
interesting and different views on the pleasures to be gained from tabletop games; and perhaps, in reading, will discover a renewed interest in playing and designing them.
Greg Costikyan

DESIGNING TABLETOP GAMES

16

Tabletop: Analog Game Design

Designing Tabletop Games

THE THREE-PLAYER PROBLEM
Lewis Pulsipher

In quantum or classical mechanics, there’s a well-known class of problems that has traditionally proven very difficult to solve, complex problems that model the motion of three particles
or objects such as the sun, earth, and moon: the “three-body problem.”
In games, the equivalent of this is the “three player problem.” There are actually two
problems. In a three-player conflict game without a definite end, the two players who are
behind will usually beat on the one who is ahead, resulting in a perpetual stalemate. This
can be avoided by placing a time limit on the game. However, as soon as you add a definite
end to the game, such as a number of turns or a number of points, the situation changes drastically. Perpetual stalemate is no longer possible. But it is frequently possible for one player
(call him “A”), if he believes he will lose and cannot catch up in the remaining duration of the
game, to determine which other player wins. That is, late in the game the losing player exerts all his efforts against another player “B,” which tends to let the third player “C” win. R.
Wayne Schmittberger (long-time editor of Games magazine) called this the “petty diplomacy
problem” in his book New Rules for Classic Games. “Petty” here is derived from “pettiness,” I
believe, implying that the player who thinks he’ll lose often chooses for petty reasons which
of the others to take with him to defeat.
This is not usually a problem in games where players can do little to affect other players,
such as most race games. If a player can hardly affect the other players (as though each were
playing alone), then the “petty diplomacy problem” goes away. Many “Euro”-style board
and card games (which are often for three or four players) have been called “multiplayer
solitaire,” a popular style partly because it avoids the “petty diplomacy” problem.

17

18

Tabletop: Analog Game Design

But it can be a big problem in wargames and other conflict games. And this is why we
rarely see such games that are “naturally” good for three players. Generally most conflict
games are best for two, or four to five. When there are four or more players, a single player
has less influence on the outcome, mitigating the effects of “I’m going to lose so I’ll make sure
you don’t win.”
I’ve discovered a number of ways to retain a strong competitive aspect in a game yet
make it work well for three players. The example games I’ll describe are non-electronic but
these solutions apply just as well to videogames. I’m going to follow the examples with a
discussion of problems that occur in any game with more than two separate interests, all of
which can be applied to the three player problem.
The general description of the two solutions is:
1. The victory condition must be one that can be attained in a single move/turn, and that
can change over time, yet players can usually (but not always) anticipate that it might
occur. This enables two players to “gang up” on the third to stop him. If they succeed, the game returns to an equilibrium until one player once again threatens to win.
Even without a time limit, the game will eventually end.
2. Have a situation where changes in the state of affairs are quite small, so that no single
move can make a very large difference in the state of things, in who is ahead and who
behind and what the margin is. Only late in the game will a player be able to recognize that he’s not going to win. By that time, he usually cannot make enough difference in the short run that remains, to throw the game to another.
Actual examples will make this clearer.
Law & Chaos
In my prototype titled Law & Chaos (in the publishing queue with Mayfair Games, and
likely to have the name changed), I serendipitously discovered how the first method can
work.
The game is played on a simple hexagonal board (61 hexagons) with one kind of piece.
The game is an example of one that arises from components, as I wanted to devise a way to
use in a game the colored glass beads or “stones” so common in flower-arrangements nowadays. (In the end, I had to abandon those pieces because they weigh too much, as publishers
usually pay for shipping to distributors!)
Unadorned hexes and one kind of piece don’t offer much room for variety, and I settled
on using cards to provide that variety. There are three types of cards:
• Victory conditions. These specify patterns a player can form to win the game, such as
a row of six stones
• Capture methods. These specify patterns that let a player capture opposing stones
• Action cards. These enable the player to take/cause a specified action (such as preventing the replacement of a victory condition card)
Each player has cards in hand, and there are cards on the table that apply to players selectively. Each turn a player either places a piece on the board (which could also result in
one or more captures) or plays a card. The key for our discussion is that anyone can win at
any time by having the right victory card in combination with the corresponding pattern on
the board. The card needs to be face up on the table already, or it must be played from the
player’s hand; in the latter case the other players have one round to try to break up the pattern. (There are more details than this, especially about player interaction, that will await
the game’s publication.)

Designing Tabletop Games

Players soon learn the possible victory patterns (which are also illustrated on a separate
sheet), and can either see that another player has the right victory card on the table for a pattern he can soon form, or can anticipate that it is in the player’s hand, as that player builds
patterns.
When the other players see this, they tend to gang up on the “leader” to thwart his plan.
If they succeed, then they play once again in a kind of equilibrium. If one player is far behind (it’s possible to have no pieces on the board), the others will usually concentrate on one
another, which gives the third a chance to catch up. But sometimes the other players will fail
to see that the “leader” is threatening, or will be unable to stop him or her.
In the end, it is that rarity, a game that is not only good but outstanding for three players,
and best played with three, though it can be played by two or four.
The “sudden victory that can often be forecasted and prevented” characteristic is the
key. Unlike many wargames, some information must be uncertain or hidden, or players
will always know who is threatening to win. It is also important that the victory conditions
themselves can change over time.
Any kind of foreseeable/definite time limit helps “petty diplomacy” rear its ugly head.
Using a criterion of victory by reaching a set point total, very common in boardgames these
days, is unsuitable because the end is fairly predictable. On the other hand, a margin victory
criterion– for example “have 20 points more than the next highest player”--means no one
knows for sure when the game will end, because the players behind can catch up and the
margin can get smaller as well as larger. When the player who is furthest behind can still
hope to catch up, he’s not likely to give up and “suicide” against another player. If a set total
of points determines when the game ends, then at some point the player furthest behind will
realize he doesn’t have time to catch up, allowing “petty diplomacy” to kick in.
So this kind of game needs an open end, probably with some mechanism that prevents
the game from going on forever but does not arbitrarily end it. In Law & Chaos I added that
mechanism when playtest games among expert players stretched to more than two hours,
much longer than the average. The mechanism comes into play at a certain point, by increasing the number of ways players can win.
The game doesn’t work as well with two or four players. With two, when a player “gets it
going,” there’s a steamroll effect that’s hard to stop. With four, it’s too easy for three to gang
up to stop one, and that led to a variation of the game, recommended for four players, that
limits what a player can do to stop someone else because they do not have a hand of cards.
A military version of this kind of game
How might this apply to a military game rather than an abstract one? Occasionally we
see three-way, rather than two-way, historical struggles for supremacy. The one that first
comes to mind for me is Athens, Sparta, and Persia in the fifth century BC. Athens and Sparta joined together to defeat the great Persian invasion of 480 BC. Then Athens’ sea empire
became dominant for a while, and Sparta abandoned the alliance against Persia. By the end
of the Peloponnesian War, Persia controlled Greek Ionia, and gave subsidies to Sparta, enabling the Spartans to build fleets to defeat Athens. In the fourth century it was Sparta’s turn
to be pulled back, this time by Thebes in conjunction with Athens. Finally, the Macedonians
conquered Greece, and soon after conquered Persia with the help of the traditional Greeks.
In other words, one power or another threatened to become completely dominant, but
was defeated by the other two, until yet another more-or-less Greek power defeated them all.

19

20

Tabletop: Analog Game Design

How can this be represented in a game? The key will be a card for each round of play that
will indicate a victory condition for one of the nations (or perhaps all three). If the condition
is attained, the game will end right there. The order of play will change from round to round
to help give nations a chance to thwart the one closest to a win, and some mechanism that
abandons the move-all-units-in-your-turn tradition might be desirable as well. There’s also
a possibility for a point game here, with the card specifying the points that can be earned
by achieving certain objectives, and if any nation reaches a given point margin over the next
highest, it wins. In essence, in many if not all rounds we want at least one nation to have a
chance to win while the others must thwart that nation, possibly ignoring their long-term
interests in favor of defeating the temporary leader.
Because there have been at least two Peloponnesian War games published in the past few
years, I have not tried to develop this game.
Other Historical Wargames
Now what about the second version of a natural three player conflict game? I call this
the “equilibrium” method. I have a prototype Britannia-like game called “Frankia: the birth
of France and Germany,” that includes three scenarios, 406-814 AD, 843-1215, and 1215-1492.
As in my game Britannia, each player controls several nations in the course of the game, and
victory is determined by points. The first two scenarios are for four players, as with almost
all Britannia-like games, but the last one is for three. I decided to try this because the situation in this scenario is so different from the typical Britannia-like game. The typical situation
sees major raids and invasions from external sources, and a considerable turnover of nations
and locations–which is the situation in the first two scenarios. In 1215-1492 in this part of the
world, the nascent nation-states of modern Europe could already by discerned, there were
no external invasions or raids at all, and in part thanks to geography, borders did not shift a
great deal over time.
I was fortunate insofar as I had changed two of the fundamental systems of Britannia for
Frankia, the combat system and the economic system. The three player scenario would not
work as well with the combat system used in Britannia, in which casualties can be quite high.
(Roll a die for each army in a battle; a 5 or 6 kills an opposing army.) Frankia uses a cardbased, diceless combat system that does not eliminate more than one army in a fight, and
often none at all. Sometimes, in fact, the battle ends with both participants jointly occupying
the area they’ve contested.
The economic system depends on the number of armies a nation already possesses, so
that Powers tend to reach an equilibrium until they can conquer more territory. Your economy must pay to maintain existing units before you can get new units. In contrast, in Britannia, the number of new units you receive depends only on the economic value of the areas
you hold, regardless of how many units you already have. Armies are also a representation
of population, so you can build up armies until you reach your population maximum. In
Frankia, the cavalry and infantry armies are more specialized, not representing the population as a whole.
Finally, the number of units is relatively low, in part because the stacking limit, the number that can be in a given area, is lower than in Britannia. In particular, there is no unlimitedsize stack. When you cannot concentrate large forces, it is harder to make a sweeping invasion.
The result is that this scenario is even less a “conquest game” than normal Britannia.
Much of the time in Britannia, you protect what you have rather than attack, until your next
big invasion comes into play. In Frankia, you don’t have the forces to launch a big invasion,

Designing Tabletop Games

nor can you kill the enemy fast enough to overwhelm them. It is a case of nibbling a little
here, a little there, trying to be on top of an equilibrium. And that is what we need to help us
avoid the “petty diplomacy problem.”
Another situation that lends itself to this kind of game is eighteenth century Europe.
This was an era of “the laws of war,” a reaction against the excesses of the Thirty Years War.
Professional, not mercenary, armies relied on long supply lines guarded by highly efficient
earthwork fortifications. The “civilized rules of warfare” prohibited living off the land (the
commonplace in the Thirty Years). The aims of warfare were usually limited to wearing out
the opponent while gaining bits of land (and fortresses) here and there. It is another case of
“nibbling”, though in the game ahistorical events can occur, just as in other games with this
long chronological scope.
My prototype (tentative title, Struggle for Hegemony in Europe, 1689-1789) also sees each
player controlling several of twenty-two nations–there are no uncontrolled neutrals. The
game is for three to five players. The dice-based combat system once again rarely results in
casualties, with much of warfare revolving around sieges and the occasional assault on forts.
The lines of forts tend to prevent sweeping invasions. A submission rule allows small nations to become subordinate to an attacker (at a cost) rather than be wiped out. The economic
system once again considers the number of armies and fleets you already have, and there
are maximum numbers of units as well reflecting the general difficulty of maintaining large
armies and fleets.
As “sweep of history” games, both of these have a definite number of turns, but that is tolerable for an “equilibrium” game. More changes occur in nation positions in this game than
in the real world–the purpose is to have a good game–but it is largely a situation in equilibrium, which we need to avoid “petty diplomacy”. The scoring system also contributes to this.
Prussia, for example, doesn’t score any points for areas in France, or deep in Austria, or in
Russia or the Ottoman Empire. The Prussians may (rarely) invade France in order to reduce
the French score, but gain no points from it themselves. If they’re pursuing their self-interest
as indicated by their scoring areas, they are unlikely to stray far from home. The English
might, in some games, conquer Spain with Portuguese help, but they won’t gain points for
every area in Spain, any more than the French would.
The right situation, then, combined with appropriate combat, economic, and scoring systems, allows these two wargames to be played by three players while avoiding the petty
diplomacy problem. It is still possible for two players to decide to try to wipe out the third,
but when they choose to do that early in the game, the victim has the opportunity to throw
his forces against one of his two tormentors with sufficient effect to throw the game to the
third. The threat of doing so actually tends to help restore the situation to something close
to equilibrium. Late in the game, with all that has passed before, the simple two-against-one
is much less likely to occur, and will be less effective.
Of course, another possible way to avoid the three player problem is a wargame in which
almost all information, including information about who is winning, is hidden from the
players. If you don’t know you’re losing, or who’s winning, the petty diplomacy problem
goes away. Then we have a kind of race, or something that wouldn’t be much of a game, in
most cases.

21

22

Tabletop: Analog Game Design

Another Abstract
I’m going to go back to abstract games for a moment to describe another solution. What
makes this game work for three players is that it isn’t really a conflict game, it’s a positional
game. That is, while player interaction is high, you cannot throw or exert force against another player, though you may be able to temporarily eliminate one of his pieces. You can
block a player from scoring, but this may help the third player more than it helps you.
The game is played on a four by four square grid with stackable pieces (tentative title,
which is likely to be changed when a theme is attached, is Four by Four). To score you must
get four in a row or four in a square–a little like Tic-Tac-Toe/Noughts and Crosses--and the scoring pieces are then removed. There are stack size limits depending on the number of players.
Some of the pieces have special powers, such as the “Top” piece that another player cannot place a piece on top of, and the “Order” piece which freezes the order of pieces in a stack.
The pieces alone might not be very interesting, but each player also has a hand of cards. The
sequence of play is that all play one card simultaneously, then play two rounds of placing
pieces on the board. The cards have “initiative numbers” that determine order of execution
both for the current card round and for the following placement rounds, so there is no question of consistent advantage for playing first the way there is with Chess and many other
games. The cards allow various manipulations of the pieces, such as moving the bottom
piece in a stack to the top or allowing you to move a piece (not necessarily one of yours).
Each time a player achieves the scoring condition he gets a point, and play goes to three
points, or fewer if players agree. Sometimes when one set of scoring pieces is removed, another score is revealed, and it is also removed. It is not unusual for one player to be behind,
but come back to win the game. As the game progresses, a player must often choose whether
to prevent a score by another, or to work toward a score for himself. Late in the game you
know who’s threatening to win, because you can see the score. The time of ending of the
game is uncertain, but there is a mechanism to end it rather than go on indefinitely (when a
player has no more pieces to play). The game can also be played by two or four, with rather
different tactics in each case.
In some ways the three-player problem can be seen as a subset of problems that occur in
many games involving more than two sides. I’ll discuss some of those next.
Problems with Multi-sided Games
Boardgamers call any game with more than two players “multiplayer”, but this term is
used in the videogame world for “more than one player;” and in videogames, a “multiplayer”
game often has just two teams, as in Team Fortress. So I use the term “multi-sided,”meaning
more than two separate interests regardless of the number of human players.
Certain kinds of problems crop up in three player games just as they do in multi-sided
games for more than three. These potential problems exist to a lesser or greater degree in
most multi-sided games, but in the extreme become obstacles to enjoyment. These are:
• Turtling
• Leader bashing
• Sandbagging
• Kingmaking

Designing Tabletop Games

Turtling
A player sits on the sidelines, avoiding conflict, while other players fight a debilitating
war; then the turtle steps in and wins the game because the others are too weak to stop him.
In videogames this is often called “camping”, although “campers” often choose the tactic
because they can occupy a very good defensive position and kill many opponents without
dying often. In boardgames, the player may avoid combat altogether.
How is turtling avoided? The clearest method is with a zero-sum game, such as Diplomacy. You can only gain units by taking supply centers from another player: the general
definition would be, a player can only gain something that another player loses.
Most games are not zero-sum. However, if a player stands to gain more by attacking
than by turtling, the turtle tends to fall behind. This requires that there be a positive rather
than negative economy, that is, that a player can acquire additional force/capability over
time through the game economy. This is what makes turtling somewhat dangerous in Risk,
because the players controlling more areas gain more new units. Nonetheless, the entire system of gaining new armies through cards exists, in part, to encourage players to attack rather
than turtle (if you don’t successfully attack in a turn, you don’t get another card).
In many tactical battle games, there is no economy (or, to put it another way, there’s a
negative economy, as both sides gradually lose units). If there are only two sides, this is
not a problem. If there are more than two, it becomes a big problem. Three player Chess,
for example, is likely to be an exercise in turtling. Even if a player is awarded control of all
remaining opposing pieces when he checkmates a king, this may not be enough incentive to
attack rather than turtle.
Turtling can happen in a two-sided game. For example, in Chess a player may try to create
a very strong defensive position and wait for his aggressive (or computer) opponent to make
a mistake, then attack.
It is very common for beginning designers of multi-sided conflict games to allow, even
encourage, turtling, because there is not a positive economy.
Another way to discourage turtling may be extreme uncertainty about the overall situation. The turtle needs to know when other sides have been debilitated to the point that
he can attack and probably win. If he doesn’t have enough information to know when that
occurs, he may decide he needs to go forward rather than turtle. But this is not a desirable
solution, especially in a boardgame. It is more practical (and more often used) in card games,
where the cards provide a simple, natural means of hiding information.
Finally, victory conditions can discourage turtling. In a game where points are scored
periodically throughout the game, a player who turtles may not be able to score well. This
will certainly be true if those point awards involve holding certain locations, or destroying
numbers of opposing units. Even if the victory conditions only apply at the end of the game,
as in Axis & Allies (where the objective is to hold enemy capitals, with no predetermined
time/turn limit), the turtle is less likely to hold these areas at game end. Yes, if everyone
else wears themselves out without achieving the victory criterion, the turtle may be able to
sweep the board and then achieve the victory. In A&A, because there’s a positive economy
as well, and because there are only two sides, turtling doesn’t happen.
Leader Bashing
Leader Bashing is simply the tendency to attack whoever is ahead. This is a necessary
component of multi-sided conflict games, though generally absent from race games. It becomes a problem when the typical thing to do is to attack whoever is in the lead, regardless
of one’s own position.

23

24

Tabletop: Analog Game Design

In my game Britannia and other Britannia-like games, there are two elements to discourage leader-bashing. First, players score at different junctures of the game, so it’s difficult to
actually know who is ahead at a given time. For example, the Romans score a lot early on,
because they conquer much of Britain. The (yellow) Romans can have more than a hundred
points in turn five, more than any other color, but yellow would be well behind overall because the average Roman score is about 125. (The average score for each of the four colors
at game end is around 217.) Experienced players understand whether the yellow color is
doing better or worse than average, but even then, this must be seen in relation to the scores
of the other three colors. As the game goes on through sixteen turns and seventeen nations,
discerning who is ahead becomes more complicated. In other words, there can be honest differences of opinion as to who is actually ahead, and you’ll often hear players over a Britannia
board each explaining (sometimes disingenuously) why they are behind and someone else
is ahead.
Further, the latest version of Britannia includes scoring markers. If players agree not to
track the scores on a scoresheet, the scoring markers provide further uncertainty about who
is ahead. In a game like the Hasbro version of History of the World this kind of uncertainty is
absolutely necessary to avoid rampant leader-bashing.
Second, in a four player game, if you expend your efforts trying to “stop the leader” at
the cost of your own score, then the other two players benefit. In Britannia each nation has
historical scoring objectives that sometimes conflict with other nations, but not necessarily
the one that you want to “bash” right now. This doesn’t work as well in a three player game,
because only one other player benefits, not two, but it certainly helps in Frankia and Struggle
(described above) which use a simpler version of the Britannia scoring system.
Sandbagging
Sandbagging is the reverse side of leader-bashing. Sandbagging is pretending to be
worse off than you are, to somehow disguise how well you’re doing. In some games in
which leader-bashing is easy, that is, each player is able to exert some influence and exert it
against any other player regardless of positioning on the board, then it makes sense to try to
be slightly behind the leader near the end of the game. In a game such as Vinci this is a common strategy. Either you need to be fairly far ahead when the end of game approaches, or
you need to be in second or third place in order to win when others bash the leader(s). (How
this works depends on the players, of course: some refuse to attack the leader, concentrating
only on how best to maximize their own score.)
The easier it is for other players to see the reality of the game situation, the harder it is to
sandbag.
Kingmaking
Kingmaking is the more general term for “petty diplomacy problem”. If it is too easy
for one player to affect another sufficiently to cause him to lose, regardless of the number of
players, the game suffers for it. Obviously, as there are more separate interests, each player
can have less effect on the game as a whole, and kingmaking becomes less problematic.
Of course, in games allowing negotiation, a player with a weaker position can try to
persuade a stronger player to leave him alone because “if you attack me I’ll throw my entire
force against you and you won’t win.” If players can significantly hinder one another, this
kind of negotiation strategy cannot be avoided.

Designing Tabletop Games

Further, in some games a player can influence any other, while in other games there are
circumstances of geography or even of turn order that reduce the effect some players can
have on certain others. For example, in Diplomacy (World War I), the English player can try
to influence others to attack Turkey, but he cannot affect Turkey with his units until late in
the game, because the nations are on opposite corners of the board.
As with the specific case of the petty diplomacy problem, if players don’t know that
they’re losing, they’re less likely to try kingmaking.
Insofar as uncertainty tends to mitigate the petty diplomacy/kingmaking problem, the
problem is less likely to occur in card games than in board games. Cards naturally hide
information, whereas boards naturally reveal information. In this respect, videogames are
often more like card games, naturally hiding information from the players.
In summary, here are some ways to deal with the three-player problem:
• A race or “multi-sided solitaire”; players cannot do enough to hinder/harm another to
make a significant difference in the end portion of the game
• Sudden victory that can frequently be forecasted and prevented, with changing victory conditions
• “Equilibrium”, no side can drastically alter the situation in a single turn
• A game that is almost entirely positional
• Extreme uncertainty about who is winning and losing

Britannia references:
Wikipedia: http://en.wikipedia.org/wiki/Britannia_%28board_game%29
Boardgamegeek: http://boardgamegeek.com/boardgame/240/britannia
Publisher’s Site: http://new.fantasyflightgames.com/edge_minisite.asp?eidm=42&enmi=Britannia

25

26

Tabletop: Analog Game Design

Designing Tabletop Games

SIMULATION GAME DESIGN
James F Dunnigan

My specialty is historical simulations. I designed over a hundred (that got published), and
ran Simulations Publications, Inc (SPI), a company that published over 400 of these games
while I was there (1969-80). Most of these were wargames. Peace games don’t sell as well,
which says something about us all. We’d rather fight. Kill for peace and all that.
Wargames have been around for thousands of years, with Chess being the most obvious
example. Chess, as we know it, is still a pretty accurate simulation of ancient battles. Over the
centuries, there have been many variants on the Chess idea, and in the last two centuries, the
idea of adapting the Chess concept to contemporary military operations, took hold. Over the
last century, more and more of these “wargames” have been published as entertainments
for those interested in such things. Military professionals took the same basic concepts and
developed more complex “Chess variants” for planning and training. These were very successful, and are still used in a limited way.
I entered the business in the late 1960s, with the belief that the games could be a bit more
accurate, and informative, without becoming a lot more complex. It turned out that there
were many others out there with the same idea, but I got the ball rolling with some new ideas
on how to go about quickly turning history, or current events, into a playable game. The
main reason for this was curiosity. I, and many others, wanted to do more than read about
history, we wanted to see a convincing model of how historical events worked, and have
the ability to explore “what ifs” in a believable fashion. Most importantly, we were creating
historical games that convincingly allowed the players to make the same historical decisions,
and get the same results. But, most importantly, you could make other decisions, and see an
accurate alternative result.

27

28

Tabletop: Analog Game Design

My basic premise was, and still is, that any situation can be turned into a useful model/
game/simulation. Naturally, I developed a tool set to accomplish this. Here are the tools,
along with some examples. The following discussion assumes that you are seeking to create
some kind of conflict simulation (the term we coined to describe these kinds of games).
But remember, these guidelines can be used to create games on anything. And I mean
anything. I first realized this in the 1960s. Late in that decade, Tom Shaw, the guy who was
running game publisher Avalon Hill, had doubts about this. He challenged me. I told him to
name any situation, and I would deliver a publishable (entertaining and easy to learn) game
within a month or two. He responded with, “do a game about getting lost in the woods.”
I did, he did, and Outdoor Survival became a best seller. I’ve taken up that challenge many
times since, often in casual conversations, and always came up with a solution. So be confident as you proceed. For more examples (visual and otherwise), surf over to: http://www.
hyw.com/Books/WargamesHandbook/Contents.htm. But the basic tools are as follows:
The Tool Of Understanding
It’s easy enough to do a game on a subject you are interested in, if you are the only one
who is going to use it. But if others are involved, especially a client, the situation can become
difficult. Know what the user/customer wants. It’s difficult enough knowing what you want
to do when you are doing a model for yourself. It’s easy to start building a model with a
vague idea of what you want, and then sharpen your focus as you proceed. It’s impossible to
complete an adequate model unless you have developed a precise idea of what you want it
to do. If the user is someone else, you have to help them figure out what they want it to do.
This is not easy, and is often avoided because of the difficulty. Don’t avoid it, be difficult if
you have to. In the long run, this is the easy way out. To define the needs of the project, apply this checklist. It will get you started in defining the model users need. If you can’t define
your project adequately, you’ll waste a lot of time and effort. You probably won’t complete
your project, either. The last thing you want to hear from the user is, “that’s what I asked for,
but it’s not what I want.”
1. Determine the Process to be modeled. Many different aspects of your model must be
defined before you can proceed. Scale (Strategic, Operational, Tactical), Environment
(Land, Air, Naval, Combined), Intensity (Low, Medium, High), Basic Aspects (Movement, Combat, Order of Battle), Special Aspects (C3I, Logistics, Doctrine & Tactics,
Fog of War--Is the situation highly dependent on one, or both, sides being in the dark
about what is going on? If so, you will have to model this aspect of the situation.)
2. What do you want it to do? There are several different tasks you can direct your modeling towards. These can include training, research, analysis, etc. For example: You
may want to test a hypothesis. This can be historical, contemporary, or future. It can
be about weapons, tactics, organization, or whatever. Be rigorous in defining your
hypothesis. A model/wargame will eat you alive if you are sloppy. Perhaps you want
to better define a process. You may want to break down an existing system into only
its essential parts. A wargame building exercise is excellent for this.
3. How do you want the game to go about its work. Do you want to use a map (most
common with wargames), or cards, or a computer interface? The customer, or user,
might not even be sure which form of game would work best. You have to figure this
out before you proceed.

Designing Tabletop Games

The Rule of Plagiarism
Start with an existing model. For example, to create a wargame for contemporary ground
combat operations, you can wander off to your local game or software store and see what
the commercial designers are up to. There are also companies that deal in out-of-print games
that may be of use. If there are any gamers in your area, buy them a beer and pump them
shamelessly for leads. There’s also a lot of previous work in the non-commercial sector waiting to be plundered. No sense reinventing the wheel, especially since that approach is sure
to lead to exceeding your budget and missing deadlines. Don’t endanger your career. Plagiarize. There’s no copyright on ideas and most of the ones you need have already been thought
of and thought out by more experienced designers. I know, I often steal from myself (as well
as others, that’s why I’m an expert).
The Rule of Self Knowledge
Be sure you know what you know. Pick a subject you have a keen interest in, or have
gained a perceptive knowledge of. This will eliminate a lot of time-consuming research. You
wouldn’t be doing this if you weren’t an expert in something.
The Rule of Digging
Compile information. Once you have agreed upon what you want to do, you must gather
information. Here is a sample checklist.
• Area of Operations- Where, in time and geography, is the conflict to take place?
• Scale- What is to be represented on the map, a few square miles or a continent?
• Significant Terrain- For the Terrain Effects Chart, this is a winnowing process, in
which you reduce all the terrain information you have gathered into a usable format.
• Order of Battle- Units involved, their movement capability, combat capability, and
other characteristics.
• Victory Conditions- This is a critical element, and often slighted or overlooked. What
were the goals of the combatants?
• Combat Results- Attrition rates in combat, with adjustments for other factors as needed and likely distribution of results for use with non-deterministic (unpredictability
of combat) procedures.
• Sequence of Play- The sequence that appears to work best in most situations is: 1-Planning and preparation operations, 2-Movement, 3-Combat, 4-Post operations checks
(victory, morale, command control, etc.).
The Rule of Taking a Chance.
This is all about the “Integration Phase.” The Big Moment, when you create the prototype. This is where you assemble the first working version of the game. The Prototype is
usually quick and dirty. Just get it working, quickly. Once that is done, you can make many
minor changes to get it to work (produce a certain result using a certain sequence of moves).
Whether the game is manual or computerized, you should have probability tables that can
be easily changed to adjust the game’s outcomes in a controllable fashion.
Finally, a note on “Pre-Dawn Madness & The Bleeding Edge of Technology.” There is a bit
of magic involved while creating the prototype. The model must be exercised, errors noted
and modifications made, and the process repeated. Strange things will happen and you will
often find yourself spending more hours working on this phase than you realize. This is

29

30

Tabletop: Analog Game Design

the Pre-Dawn Madness most programmers are familiar with. Don’t expect to understand
everything that’s going on in the prototype. If it works, leave it be and move on. Don’t be any
more inventive than you have to be. Beware the Bleeding Edge of Technology. Stay with the
simple and don’t get cute.
The Truth Rule
This is all about testing and user acceptance. First there is Alpha Testing, where first you
and then some typical users must be able to reproduce the Historical Event, or the defined
hypothetical event. If the game can’t do this in the hands of others (the people who created
the game sometimes unconsciously make the game work by, well, cheating), you have to tinker with it until it does. That’s the truth, and you cannot ignore it. Once you have done this,
you can proceed to Blind (or Beta) Testing, where the game is handed to typical users without you hovering over them (“blind” to you). These people may break the game, but mainly,
this crew will point out the many errors you made in writing the instructions and laying out
the components. All games, and especially commercial products, should have a degree of addiction to them. As commercial game developers like to say, while developing such a game,
“is it crack (cocaine) yet?” Lastly, there is ongoing testing after installation/publication. No
model is ever truly finished.
And now, there is the bad news. These types of simulations/games appeal to a small number of people. While Chess is played by about twelve percent of the U.S. population, that’s ten
to twenty times the number of people who are interested in these simulation type games.
I know this because I ran surveys and other forms of market research for over a decade, in
an attempt to discover how big the market actually was. Turns out that while there are forty
million chess players in the United States, less than one percent of Americans are willing
(deep interest in history/current affairs), or able (knowledge of math and operations research
concepts, consciously or subconsciously) to handle these kinds of games. In the 1970s, we
came to call wargaming, “the hobby of the over-educated.” The manual games further restricted the number of users, because these games are more time consuming to learn and
play. Computerized versions of these games appeal to a wider audience, but still a niche audience -- An audience of under a million people. While complexity frightens the many, it appeals to the few. Thus wargames are often lumped into all things geekish. Guilty as charged.
People who are into playing or designing wargames do not think like the rest of us. Actually, this applies to most people in the sciences, or anyone who uses the scientific method
(testing hypotheses until you get a proof in the form of a reproducible result). Wargamers
look at wars, and most other things, in a more analytical fashion, taking into account historical precedents and antecedents. When I started designing games on contemporary (wars not
yet fought) situations in the 1970s, I discovered again the old adage, “the past is prolog to the
future”, still applies. But the basic rules of historical simulations still applied. Or, as we put it
back then, “If you can’t predict the past, you can’t predict the future.”
But take heart. This stuff really works. If you have the analytic and math skills, you don’t
have to be a military history buff to make this work. These techniques really can be applied
to anything. Over the years, I have been approached with many requests for advice on how
to apply these tools. Most had nothing to do with warfare. For example, I once had a fellow
from the New York City Health Department come in asking for help in training inspectors, stationed at the ports and international airports, to screen people for rare diseases (like
AIDS, this being the 1970s). I came up with a card based system, where the inspectors could
be presented with a wide array of “people with suspicious diseases” and exhibiting an even

Designing Tabletop Games

wider array of symptoms. Sort of a play on flash cards, but with some branching and game
play. The NY Police Department wanted help in building training simulations for commanders who had to cope with public disorder. Turned out the NYPD had a lot of details on past
disturbances. So we discussed, “if you can predict the past, you can predict the future.” That,
plus the fact that the police department has a disproportionate number of wargamers in their
ranks. Then there was the guy from the U.S. Forestry Service (walking into my office wearing cowboy boots and a ten gallon hat). That was more like war, and the forestry service, like
the cops, had lots of good data to mine, from past wild fires. I think that’s what they ended
up calling the game, Wildfire, which eventually evolved into the current computerized, and
very accurate, version. Then a group of academics at a Mexico City university wanted help
in simulating rural agriculture, and the impact of some new ideas on productivity, and local politics. Some of these guys were already into wargames, and they immediately grasped
the concept of modeling media and political factors. More recently, a NATO country wanted
help in building a crisis simulation for senior political and military leaders. In this case,
politics and media reaction played a major role in their most likely crises. The two guys who
were my main contacts (they had gone to graduate school in the U.S.) were wargamers, and
immediately understood what I needed when I asked for a media “Order of Battle” for their
country. Within weeks, I received an elaborate spreadsheet, containing all the major national
media (and that of some neighboring nations), along with the critical characteristics of each
