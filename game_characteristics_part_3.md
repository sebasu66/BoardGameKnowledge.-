one’s improvement in heuristics.
Heuristics at Different Skill Levels
Like most game characteristics, the heuristics of a game will be perceived differently
by players of different levels of skill. In go, the heuristics are very unclear to a beginning player: they cannot tell who is winning, and they are often at a loss for what to
do. In fact, beginners often have difficulty telling if the game is over or not!27 Chess
has excellent heuristics for absolute beginners (checkmate the other player’s king, or
failing that take his better pieces) and for advanced beginners (make advantageous
trades according to the point value system, develop your pieces, control the center).
But intermediate players may reach a state where they feel they are simply avoiding
moves that are obviously bad, waiting for their opponent to err—the intermediatelevel heuristics for chess are not as friendly. Indeed, chess is sometimes described as
the game where the winner is the person who makes the second-to-last mistake. Intermediate go players have a much easier time finding profitable moves, since many
moves will increase one’s score at least somewhat.28
In some games, there are heuristics of sufficient quality that, once known, players
can play perfectly (the game is “solved”). Tic-tac-toe is one such game (although arguably this is more a matter of reading out the game tree than heuristics per se). A better
example is Nim. Note that for Nim, there are not many good heuristics for levels of
skill below the complete solution. Thus Nim isn’t really a very fun game—it has an
excellent one-time metagame for the mathematically inclined (figure out how to solve
27. Technically, a game of go is over when both players pass. However, this should only occur
when neither player can make a move that would affect the score, and beginners cannot tell
when the game has reached such a state.
28. Part of what’s going on here is that in some games, one finds situations where it seems that
no move at all is better than any of the choices one can make—what in chess is called “Zugzwang” (the chess term is in fact drawn more narrowly, but the underlying idea is close enough
that the term is worth stealing for this more general concept). In chess, it’s quite common to
find situations where most moves worsen one’s position. In go, it’s more common that most
moves improve one’s position, at least a little. Zugzwang in this broad sense—of game positions
where bad (“bad” in the sense of “worse than doing nothing”) moves abound, and good moves
are rare—is quite common in games. (For a digital example, think of the paralysis a beginning
FPS player can feel moving out of a spawn point—surely, she thinks, the best choice is not to
stay at the spawn point, but when all other choices lead to death, what is she to do?) Zugzwang
tends to make for unsatisfying beginner heuristics.

34

Chapter 1

Nim), but it is hard to play an interesting game of Nim before you figure out the solution, and impossible to play an interesting game once both players know it. In particular, it is basically impossible to know anything at all about the state of a multipile
Nim game until you have entirely solved Nim.
As an aside, note that the possibility of a game having heuristics so powerful that
the game is “solved” does not depend on the game being deterministic. One could
construct a game “rando-Nim” where two players played Nim, and then a die was
rolled to see who won (say 1–4 the winner of the Nim game, 5–6 the loser). Once the
players understand Nim heuristics, this becomes a purely random game, but its strategy and its heuristics are the same as those of Nim.
What Makes for Good Heuristics?
There are a number of different axes on which one can measure the quality of a game’s
heuristics.29 Ideally:
Heuristics exist at all levels, from beginner to advanced. Players should be able to
improve at the game by acquiring increasingly sophisticated heuristics.
• Some heuristics should be easy for players to discover on their own; others need to
be more difficult (if they are all easy, eventually they will all be discovered and the
game will be exhausted) and will typically be learned from other players.
• The set of heuristics should be powerful enough to cover most situations (so that
the player is never without guidance) but not so powerful as to completely cover more
than a few situations (lest those situations, or worse yet all situations and thus the
game itself, be “solved”).30
• The heuristics are “satisfying” in the sense that the player feels she is exercising
judgment using rules of thumb, rather than executing a computer program. The Nim
heuristic or a memorized chess opening is not satisfying in this sense; “develop your
pieces” or “bluff occasionally, so that other players will call you when you do have
the best hand” is. One common way for a heuristic to be unsatisfying is for it to be
completely deterministic, eliminating judgment; another is for it to involve a great
deal of calculation (see the discussion in section 6.5 on reward/effort ratio).
•

29. Again, this is heuristic quality in the sense of contributing to a good game, one that players
will enjoy, not heuristic quality in the sense a player might mean it (how much the heuristic
helps the person who uses it to win). Solvable games like tic-tac-toe or Nim have terrible heuristics
in the first sense despite, or rather because of, having excellent heuristics in the second sense.
30. In chess, many endgame positions are “solved” and certain opening positions are to some
extent solved. Thus perfect or near-perfect heuristics of limited scope need not be fatal. Those
parts of the game are simply played through relatively quickly, and to some extent are removed
from active consideration. In other words, they become busywork.

Basics

35

Beginner heuristics, also called “zero-level heuristics,” are particularly important.
Players who first learn the game need to have some idea of what they are trying to
do and how they might go about it. Even heuristics that look quite ineffective from
an advanced player’s point of view may serve, since beginners can use them against
other beginners and hope over time to improve their heuristics. But with no good
zero-level heuristics, the game may be so unenjoyable the beginner simply gives up.
Games with good zero-level heuristics include Uno (even out your suits) or even bridge
(win a trick with the lowest card you can, bid what you can make31). Games with bad
zero-level heuristics include go and some European boardgames, where there are often
a plethora of options with no one obviously better than any other (“silk costs more,
but gives me more victory points, compared to wheat . . . which should I pick?”). In
general, any game with a large number of options, carefully balanced to preserve
gameplay variety for advanced players, runs the risk of damaging its zero-level heuristics. This risk is one reason one might want bad cards in a trading card game or bad
items in an RPG: they provide zero-level heuristics, choices that even beginning
players can make and improve their game.
If a game does have weak beginner heuristics, more advanced players can often
help beginners get started by giving them some heuristics that are not too difficult to
apply but that would be difficult or impossible for the beginners to discover on their
own. Chess openings are an example of this kind of transmission at a somewhat more
advanced level. At a more basic level, the relative values of the pieces in chess provide
a simple and powerful heuristic for beginners. Too many of these transmitted heuristics, however, can create a burden on the memory.
Heuristics and the Player Base
As players gain skill at a game, the heuristics can change. Tic-tac-toe has decent heuristics if the player base is small children, but the heuristics are not good for the adult
player base. Games like chess or go evolve over time as players learn more and develop
better heuristics.32
An interesting extreme example of heuristic dependence on the player base and
development of heuristics over time is Dots and Boxes. Commonly played by schoolchildren, Dots and Boxes has slightly weak zero-level heuristics—for example, “move
31. An example of a heuristic that is terrible for intermediate and advanced players, but that
might help a group of beginners get started (even a single more advanced player in the playgroup
would probably prevent such a heuristic from taking hold, though). Note we are not claiming
bridge is an easy game to learn (the rules are quite messy, and beginners are often taught difficult
advanced heuristics like bidding systems from the start), merely that if a group of beginners all
knew the rules, there would be some simple low-level heuristics they could use to play.
32. See the discussion “Skill Is Agential” in section 5.2.

36

Chapter 1

randomly except don’t complete the third side of a box.” But it has some good, reasonably easy to discover, intermediate-level heuristics that apply to its endgame (in
particular, the trick of not taking the last two boxes in a long chain, thereby forcing
your opponent to begin a new chain). The beginning stages of the game seem impossible to analyze—that is, there are no obvious positional heuristics, and play tends to
proceed essentially at random. However, relatively recently, advanced techniques in
theoretical mathematics (namely combinatorial game theory) have allowed one to
play the earlier stages in a productive way.33 In other words, Dots and Boxes now has
very interesting and powerful heuristics for a certain small player base, namely combinatorial game theorists. Schoolchildren, presumably, have chosen to continue as
before.
Exercise 1.8: What are some first-order heuristics in werewolf? What gives werewolf
so many basic heuristics?
Exercise 1.9: What are some heuristics that Risk and RTS games share? Name some
other games that share these heuristics.
Exercise 1.10:

What are some heuristics that bridge and hearts share?

Exercise 1.11: Name some games (besides go) with poor first-order heuristics. Why
are they so poor?
33. See the references in appendix B, and in particular Berlekamp’s The Dots and Boxes Game;
Berlekamp, Conway, and Guy’s Winning Ways for Your Mathematical Plays, vol. 2; and Albert,
Nowakowski, and Wolfe’s Lessons in Play.

2 Multiplayer Games

When a game has multiple players, many phenomena arise that are absent in twoplayer games. We discuss a number of them in this section. Most of them are, properly
speaking, phenomena of multisided games: when a game has three or more sides, one
side can be eliminated but the remaining sides continue to play, or perhaps two sides
collude against the third (an example of politics), or perhaps the losing side picks
which of the two frontrunners actually wins (kingmaking). It’s easiest, though, to
think of these phenomena in games where there is just one player per side, and hence
we normally speak (somewhat imprecisely) simply of “multiplayer” games.
Multiplayer games can allow a widely varying amount of interaction among
the players. This amount of interaction will lead to critical differences in many aspects
of play.
Some multiplayer (multisided) games can be categorized as races. Races are generally games built up from one-player games. Other games are best categorized as brawls,
which are at their core irreducibly two-player games with extra players added.1 Many
of the multiplayer characteristics of a game will come out of this distinction. In particular, races tend to have logical elimination (defined below) and low amounts of
interactivity, politics, and kingmaking; brawls tend to have high amounts of interactivity, politics, and kingmaking.
There are of course games that fall in between these two extremes. Typically they
can vary between these two styles of play inside the rules, and agentially differ in how
the gameplay is expressed. Purposefully constructed games can attempt to cut this line
down the middle; RoboRally is one example. Some of the interest in playing such a
game is seeing just how the play develops from session to session.
Although many multiplayer phenomena can be seen most clearly in games where
there is one player per side (and three or more sides), there are, of course, many
important games that do have multiple players on a single side. The most basic case
1. Our categorization here is similar to James Ernest’s distinction between “racing games” and
“fighting games” (Salen and Zimmerman, Rules of Play, 594).

38

Chapter 2

is the two-sided team game, like soccer or bridge. In these games, issues of teamwork
arise—what roles do the different team members play? How do they communicate
with one another? And, as a special case, sometimes there is only a single side, and
all the players are on it, winning or losing together. These are the cooperative games,
such as Hacky Sack or (sometimes) World of Warcraft. They are, quite simply, the team
analog of single-player games, just as two-sided team games are the team analog of
two-player games.
It’s worth spending a bit more time discussing races and brawls before examining
the multiplayer characteristics themselves.
Races are built2 by gluing together a number of copies of a one-player game, one
for each player. Each player is pursuing her own victory condition. A footrace, Scrabble,
and golf are all races. Although there are multiple players, one can imagine the race
taking place with just one player (perhaps with some rules tweaks).
Brawls are built by taking a two-player game that is not built up from one-player
games and adding more players—think, for example, of adding more players to chess.
Risk and free-for-all Starcraft are examples of brawls. There are few if any examples
from classic games and sports, for reasons we will discuss below. Unlike a race, it is
hard even to imagine reducing a brawl to one player.
The winner of a race is typically determined by some sort of scaled performance: a
point score, time, or distance. Often players cannot affect each others’ progress much.
The winner of a brawl is typically determined by some variant of “last-person standing”: the players knock each other out of contention. Players definitely can affect each
other’s progress, and indeed much of the gameplay centers around just that.
Many games do not fit this distinction well, in particular poker and many other
card games. Gameplay will tend to follow not this categorization of construction, but
rather other underlying characteristics such as amount and type of interactivity, type
of elimination, and amount of politics. Our focus will be on these basic characteristics
rather than general form.
2.1

Characteristic: Player Elimination

In a game, players can be eliminated: they’re out of the game, but the game continues.
Players can be eliminated strictly, in the sense that they are entirely out of the game,
or logically, in that they have no chance of winning although they continue to play
(in a sports season where the object is to make the playoffs, this is usually referred to
as “mathematical elimination”). Being out of a game is generally less fun than being
in it (or one would not play); being in a game but having no chance to win is often
2. “Built” in the sense of how their gameplay is logically constructed; no claims about the games’
historical origins are intended.

Multiplayer Games

39

Figure 2.1
©iStockphoto.com/Sergejs Razvodovskis

even less fun than that. So how a game handles player elimination can make a big
difference to the enjoyability of the game.
One can also speak of effective or perceived elimination: where a player has a chance
to win that is extremely low, but not quite zero, so that she is effectively eliminated,
or she thinks of herself as all but eliminated. Such a measure is highly subjective, of
course—different players in the same game, or the same player at different times, may
perceive the same game state in different ways. The nature of the game itself matters
a great deal as well—a player in a lottery might see himself as very much in the
running with a less than 1 percent chance to win, whereas that same player might
feel effectively eliminated in a chess game where he had the same chance. Players who
perceive themselves to be eliminated may be unhappy to continue the game, and they
may resign if the game rules (either written rules or social conventions) permit.
One-Sided Games
The situation here is basically equivalent to that of two-sided games (below). Note
that computer players are generally quite bad at conceding appropriately, though.
In some computer games (e.g., Civilization) the distance between logical elimination
and strict elimination of one’s computer opponent can be dismayingly great. In
one-sided games where the human player perceives himself as eliminated, there is

40

Chapter 2

essentially no social pressure against resigning. The effective elimination problem is
in some sense halved.
Two-Sided Games
The analysis of player elimination is quite different depending on the number of sides.
In a two-sided game, strict elimination poses no special problems: the game is over,
and someone has won. A new game can now be started if the players wish to continue
playing.
One exception occurs with two-sided team games, where it’s possible to be out of
the game (perhaps because of injury in a sport, or the elimination of all your units in
an RTS) while your team plays on. As in any case of strict elimination, the eliminated
player is converted into a spectator, but in this case he is a more interested spectator,
since his team is still in the game.
Logical elimination can be an issue with two-sided games, but there is an easy
solution: the eliminated (i.e., losing) player can concede. If the losing player does not
concede, the game is now pointless for both players, at least from the point of view
of winning. So why would the losing player not concede? There are at least three
possible reasons.
First, the losing player may not understand that he has lost. He might feel that he
is merely behind but still with a chance to win. This is most likely to occur in games
with a great deal of skill where the less skilled player is behind. (It can also occur in
games with hidden information, where the losing player doesn’t see the information
that would let him understand he is losing.) His positional heuristics may simply be
inadequate. This will be somewhat frustrating to the more skilled player, but the less
skilled player feels he is playing a real game, so it’s not especially frustrating to him
(other than the frustration he’ll feel for losing).3
Second, the losing player may simply be stubborn or feel that it’s “right” to “finish
the game.” In fact, in some playgroups, this may be the preferred or expected behavior.
On some level, the feeling that a hopeless game should be played to completion (or
more generally, how hopeless a game has to be before conceding makes sense) is just
a social convention. If both players share the same understanding, it’s not often a
problem; if players have differing views (especially common online), frustration can
ensue. It is interesting that some classic games that often have an especially long
period of effective elimination have developed extensive cultures of resignation. Chess
provides the best example of this. The game has solved this problem agentially over
3. One particularly nice way to reward the better player for that player’s superior positional
heuristics is the doubling cube in backgammon (a remarkable device from a number of perspectives). A winning player can offer a double, and if the losing player makes the wrong decision
on accepting it, the winning player will be rewarded. Use of the cube does require, however, that
the players play for money, or at least for points.

Multiplayer Games

41

time, and clear deviations from accepted resignation standards in competitive play
can be the source of scandal.
Third, the losing player may understand that it is annoying to the winning player
to be forced to continue playing, and deliberately draw out the game to frustrate her.
This is less common in games among friends (in part because friends presumably are
less likely to want to annoy each other, and in part because anyone who gets in the
habit of playing this way will find whatever friends he has remaining are unlikely to
want to play games with him). It is more common in tournaments. It is even more
common online, where inhibitions against antisocial behavior are few, and where
losing players can even hope to get a win by concession from their frustrated opponent.
In RTS games, it can take the particular form of “hide the farm”: a defeated player will
build a small building in an out-of-the-way place in the hope that it will take the
winning player a long time to find it (see the discussion of griefing in section 7.5).
In environments where losing players are likely to draw out games, it’s usually best
if the game mechanics allow a winning player quickly and easily to turn a logically
eliminated player into a strictly eliminated one. Automatically revealing hidden buildings of an RTS player who has no army and no economy is one example of such a
mechanic.
Multiplayer Games
When one player is strictly eliminated, the others typically keep playing. On the one
hand, this can be seen as a bad thing: the eliminated player is no longer able to have
the fun of playing the game. If the game takes a long time for the remaining players
to finish, the eliminated player may well decide to go do something else and thus not
be available to join the next game, leading the session to break up.
On the other hand, the alternative is often for that player to be logically eliminated,
which can be worse. Race games, such as Scrabble, are particularly prone to this—the
simplicity of the race game positional heuristic makes it easy to see that you have no
chance. Playing a game when you have no chance to win is frustrating. And if you
are strictly eliminated, at least you can go to the bathroom, get a snack, or simply
relax for a few moments. The length of time until the next game starts is probably
the largest factor in how annoying players will find it to be knocked out of a game
(beyond, of course, the annoyance of losing). In poker, people sit out hands all the
time and it’s no big deal because the next hand starts quickly. In Monopoly or (multiplayer LAN) Starcraft, players may sit out for quite a while.4
In party games, where people are more focused on being together socially and relatively less focused on the game itself (and who is winning it, and by how much),
4. In online Starcraft play, as opposed to LAN play, a player can immediately find a new game,
and the cost of elimination goes way down.

42

Chapter 2

strictly eliminating a player is especially costly. So avoiding strict player elimination
in party games is especially important, particularly if long wait times are involved,
and logical elimination, while still bad, is perhaps not quite as bad as it would be in
a more competitive game. Monopoly used to live in the party game space but has to
some extent been supplanted by games like Pictionary and Trivial Pursuit; long wait
times for eliminated players may be part of the reason.
Although being strictly eliminated is often preferable to being forced to play while
logically eliminated, far better is not to be eliminated at all. Many games are designed
to allow players, even ones who are clearly behind, still to have some chance to win.
Trivial Pursuit, for example, although it is a race game, has no upper limit to how far
one can progress in a single turn. Thus any player has a chance of taking the lead at
any point.5
One variant that is occasionally used is to eliminate the winners: in card games
where the object is to eliminate one’s hand, such as Old Maid, people stop playing
once they have won, and the potential losers continue to play. In a footrace, players
drop out of the race beginning with the winner. The same considerations (e.g., keeping
wait times short for those sitting out) still apply, but the annoyance of elimination is
considerably lessened psychologically by the reward of winning. Ending the game
with the elimination of a single loser is another possibility; see section 3.3 for further
discussion.
Overall, though, a game tends to be faced with three basic options, each of which
carries its own risks:
1. Strictly eliminate players.
2. Logically or effectively eliminate players.
3. Give everyone a chance to win until the very end.
The first option, common in brawls, risks making the eliminated players unhappy.
The second, common in many games, risks making them unhappy (once they realize
their state) and leaves them in the game where they may disrupt play for others. The
third is tricky to do, and may lead to a game where only the very last portion of the
game is relevant.
Playing for Points
Some games, bridge for example, track points in each subgame, so that a player cares
how much he loses by. That means there is no logical elimination (or, if you prefer,
that logical elimination’s pernicious side effects are avoided), because it is always valu5. This design feature can backfire. The authors know of one family, extremely good at trivia,
that bought a copy of Trivial Pursuit, sat down to play, and had the first team on its first turn go
all the way to the end and win. They decided the game was pointless and never played again.

Multiplayer Games

43

able for a player to eke out a few more points even if he is fated to lose that particular
subgame. Without the pressures of logical elimination to drive it, strict elimination
becomes unnecessary in such games as well,6 so elimination in general is pretty much
a nonissue.
Games played for money are particularly good examples of how a point system can
prevent the problems of logical elimination. Money can be thought of as a pointtracking mechanism that matters even after the game is over, so that no matter how
far behind you are, you still care about playing as well as you can. In poker, even if
you have no chance at having the most chips at the end of the night, you still care
about how you do in those last few hands.
Informally, players who are losing in games with logical elimination may play in
an analogous fashion, playing to do as well as possible according to some simple
positional heuristic, usually score or distance along a track. For example, in Scrabble
a player who may have no chance of getting the most points, and thus winning the
game, will probably be playing to get as many points as possible anyway. (Of course,
it’s hard to play this way in games without simple positional heuristics.) This way of
playing allows players who are losing still to find some meaning in their choices and
in their play of the game, and thus presumably to find some enjoyment despite being
logically eliminated. Sometimes this behavior will be called “playing for points” (if
the game has points) or “playing for second” (or third, etc.).
In a game that allows for this sort of play, it is often an unspoken social convention
that players should play this way if they are logically eliminated. If a player who has
no chance to win forgoes this style of play and instead chooses to focus on affecting
the play of other players in an attempt to determine which other player will win the
game, the group will not be pleased. Such play is called “kingmaking” and is discussed
below.
Online Play
The logic of player elimination shifts somewhat with online play.
Some things get worse: many kinds of behavior that are fairly rare in face-to-face
gaming become more common online. For two-player games, the additional problems
are enough to take player elimination from a relative nonissue in paper gaming to a
moderately serious one in computer gaming. “Hide the farm” and other failures to
concede are the most obvious examples.
Some things get better: strict elimination can generally be solved by having the
eliminated player immediately begin a new game. This solution comes with its own
set of problems, though: repeat play with the same group of people becomes more
6. Bridge has it nevertheless, but the duration is short and it serves largely as an opportunity for
one essentially random person (the dummy) to get drinks for the table.

44

Chapter 2

difficult, and players who are only losing by a bit may just quit to try again, leading
to some unsatisfying games. Players that perceive themselves as eliminated generally
have a much stronger recourse during online play than in physical play. They can
either join a new game instantly or begin griefing the other players by remaining as
long as possible. In many ways the effectively eliminated player has gained power at
the expense of others. This can be an especially large problem if a player’s perception
of his chances differ greatly from his teammates. He may leave a game still being
contested, often dooming his side prematurely. Direct social pressure virtually eliminates this possibility in offline play. The anonymous nature of most online play
provides challenges for designers struggling to use social structures to solve problems
of effective elimination in the same way the chess community does.
Still, although the frequency of the various problems may be different, many of
the fundamental issues are the same. And for some forms of online play, such as a
group of friends wishing to play several games in a row, the situation can look very
similar to face-to-face play.
Exercise 2.1: Describe the strict and logical elimination in werewolf. Describe the
effective elimination.
Exercise 2.2: Describe the strict and logical elimination in Survivor. Describe the effective elimination.
Exercise 2.3: How much logical elimination is there in chess? Discuss the effective
elimination in chess. How does it vary based on player skill?
Exercise 2.4: How much logical elimination is there in soccer? How much effective
elimination? Why is resignation a common part of chess, but not soccer?
2.2

Characteristic: Interactivity

Games vary widely in their interactivity: the ability of players to influence the progress
of players other than themselves.7 A boxing match, or a game of chess, is highly
interactive. A footrace is almost entirely noninteractive. Note that we do not use the
term interactivity the way it is used in computer gaming, meaning something like the
reciprocal action of the player and the game system on each other (see chapter 6 of
Salen and Zimmerman’s Rules of Play for extensive discussion).
7. Note that even to discuss interactivity presupposes at least some basic level of positional
heuristics. You can’t know if you are changing the progress of other players if there’s no way to
tell how other players are doing. As an example, imagine a game where each player rolls a die
in secret, and then all dice are revealed, with the highest untied die roll winning. If just before
dice are revealed players may force other players to reroll, is the game interactive or not? The
question is moot.

Multiplayer Games

45

Figure 2.2
©iStockphoto.com/Brane Bozic

This section introduces interactivity, and sections 2.3 and 2.4 on politics and kingmaking pursue the subject in more detail.
Races, Brawls, and Interactivity
In some games, each player is trying to achieve a result, and players can’t influence
each other (or can’t do so very much). If a winner is declared in a race game, it will
be based on some sort of score (often the score is time, i.e., whoever achieves a certain
result first is the winner, but it may be some other score, as in golf). Classic sports
races are the most common example, but many track boardgames, such as Candy Land
or Parcheesi, are to some degree races. Any solitaire game with a score can be played
as a race, with each person playing separately and the scores compared at the end;
this is a common play pattern for arcade games. Such play patterns can serve as the
basis for more interactive variants, as in the case of the card game Spit.
Even in games where players can’t directly influence each other, they often can
react to each other’s progress by altering their strategy. A longer race, like a marathon

46

Chapter 2

or (in our sense of “race”) a golf tournament, is more likely to give opportunities for
such a reaction. The reaction may simply be one of trying harder (physically or intellectually). On a more strategic level, the reaction usually takes the form of a pressyour-luck strategy: when ahead, be conservative; when behind, risk falling even
further behind in an effort to win. Examples of nonsports games that are essentially
races and that have a strong press-your-luck element include Yahtzee and Can’t Stop.
Note that a game can be more or less of a race, just as an activity can be more or
less of a game (and indeed this point of view applies to all our definitions). A sprint
is very much a race, since players hardly interact at all. A marathon or a game of
Yahtzee is essentially a race, but perhaps a less pure one since players can press their
luck when behind.
Backgammon is somewhat like a race, in that both players are heading toward their
own personal win condition. And after a certain point many backgammon games
become a true race, with the opposing pieces having passed each other and no longer
able to interact. But backgammon is somewhat like a brawl, in that the level of interaction is fairly high and players can capture each other’s pieces. It is hard to think of
chess as a race at all. Note that in backgammon one can imagine playing solitaire with
no enemy pieces on the board, attempting to win as quickly as possible, something
difficult even to imagine with chess.
Sometimes players are trying to interfere with one another directly, as in a brawl,
and strong player interaction is built right into the system. Just as various game features can be added to increase interaction in a race (think for example of the shells
in Mario Kart), limits can be added to a brawl to control its level of interaction. But
in the absence of such limits, brawls will exhibit certain common features that we
discuss in sections 2.3 and 2.4 on politics and kingmaking. And in the absence of
added interactivity, races will not exhibit these features. So while the race or brawl
core of a game may push it in a certain direction, ultimately it is the level and kind
of interactivity that is telling.
Targeted Interactions
It is useful to break down the interaction between players not only by amount, but
also by the degree of control over the interaction a player has. If a player has an
opportunity to interact with another player, and that first player may choose which
player to interact with, we refer to the interaction as targeted. A common example in
a game with customized cards is a card that allows the user to choose another player
and do something bad to him (typically take one of his assets, i.e., take one of his
chips—see below). This distinction is obviously meaningless in two-player games, but
it becomes very important in multisided ones, as we will soon see.
Note that despite the terminology, targeted interaction often is not negative to the
player being targeted. The ability to trade with other players gives a positive game

Multiplayer Games

47

state change to the two trading. Scrabble provides another example, where playing
long words and stretching the board might give an advantage to the current player
and the one immediately following. In a three-player Scrabble game, depending on
player skill and the board state, by deciding how defensively to play, one is effectively
targeting one of the other players.
Interactivity and the Number of Players
The right way to think about interactivity depends very much on the number of
players, or more precisely on the number of sides. Interactivity is at its most complex
and most problematic in games with more than two sides, and, after a brief discussion
of the simpler cases, that case is the one we will focus on, both in this section and
the related sections to follow.
For true one-player games, there’s nothing to discuss—no other players means no
one to interact with.8 For “one and a half” player games, discussions of interactivity
run along the lines of such discussions for two-player games, with the imagined or
computer opponent taking the place of the human one in the two-player case. A
computer’s behavior, of course, will often be different from a human’s: computers are
not good at conceding appropriately, but are otherwise unlikely to engage in griefing.
The underlying level of gameplay interactivity will be about the same.
In two-sided games (of which two-player games are of course a special case), interactivity is relatively unproblematic, at least in principle. By and large, it’s good for the
players to be able to influence each other, because it makes the game more interesting.
If the players can’t influence each other at all, they might as well play solitaire against
a set score, so why go to the trouble of finding an opponent for such a game? And
indeed, two player races are rare.9 The vast majority of two-sided games are highly
interactive—chess, soccer, fencing, a one-on-one Starcraft match, and Mortal Kombat,
to name just a few.
In multisided games, as we will see, the situation is quite different.
Exercise 2.5:
interaction.

Describe the degree of interactivity and targeting in werewolf player

Exercise 2.6:
interaction.

Describe the degree of interactivity and targeting in Survivor player

8. This points out again the difference between our definition of interactivity and the definition
used in computer game studies. In the computer game sense of “interactivity,” there is a great
deal to say about single-player games; indeed they are arguably the model case for interactivity
discussions. Again, we point the interested reader to Salen and Zimmerman’s Rules of Play and
the references contained therein.
9. This argument raises the question of why there are races at all, which will be discussed below.

48

Chapter 2

Exercise 2.7: What is the degree of interactivity in (touring) bicycle racing? Why is
this form of race no longer an individual event (the Tour de France started as an
individual event)?
2.3

Characteristic: Politics

The Chip-Taking Game
Imagine a game, which we’ll call the “chip-taking game,” where each player starts
with a pile of ten chips. Players take turns going around the table. On her turn, a
player may take one chip from any player and discard it. The winner is the last person
with any chips left.
Most people would not enjoy playing this game for long. There is no real skill
involved, other than the skill of convincing other people not to take your chips. And
even if you possess that skill, once the other players notice you have it, they will
probably react by trying to eliminate you first.
Unfortunately, many multiplayer games reduce to the chip-taking game, in the
sense that most of their game features are irrelevant for determining the winner, who
is instead chosen ultimately in chip-taking fashion. All that’s necessary is that the
game be highly interactive, in the sense that players can affect the positions of other
players, and also that players can target whoever they affect.10 Players can simply
choose to hurt (“take chips from”) the leader using whatever means the game offers.
Even if the leader is highly skilled, he is unlikely to be able to withstand the onslaught
of all the other players. Once the leader is eliminated, or at least knocked back from
his leading position, the players can attack some new player.
As a simple albeit artificial example, suppose we modify the chip-taking game so
that on a player’s turn, she chooses another player and plays a game of chess against
him; if she wins he discards two chips, and if she loses he discards only one. This
game has all the complexity and skill of chess, but it doesn’t matter. Kasparov is no
more likely to win than anyone else at this game, and probably less; the other players
are likely to choose him consistently until he’s eliminated.
Targeted Interaction, Politics, and Voting Games
Our previous observation can be restated: a game with a high level of targeted interaction will tend to be a chip-taking game. Note that both interaction (in the sense that
10. Oddly enough, poker is not a “chip-taking game” in our sense, because you don’t choose
your victim. You can only take chips from people who choose to go up against you, a choice
based in large part on the randomness of the cards. So in a sense poker is similar to a tournament
with random pairings.

Multiplayer Games

Figure 2.3
©iStockphoto.com/Shane Stezelberger

49

50

Chapter 2

players can significantly affect other players’ game state) and targeting (players can
choose who they will affect) are necessary.11
When players can target other players in an arbitrary way that differentially affects
their game states, we refer to this as politics. The higher the degree of interaction
(ability to affect each other’s game state) and the higher the ability to target specific
players, the more political the game is. A game may have political mechanics inside
it without its general character dominated by politics.
Some less obvious examples of political mechanics in games include the trading in
Settlers of Catan or Monopoly. Here the players are not choosing someone to hurt, but
rather someone to help. The politics arising from trading in these games are mitigated
by the rules or by social convention and for most playgroups do not dominate the
rest of the game.
Another way to describe a game with a lot of politics is as a voting game: the players
are essentially electing a winner.12 As a concrete model, consider the game where in
every round, players literally vote for someone to be eliminated, until only two people
(who are the cowinners) are left.
Calling a game political, calling it a chip-taking game, or calling it a voting game
are all broadly similar. A game with few restrictions on the amount or targeting of
trading falls into this category as well. Political is the most general term; chip-taking
emphasizes the ability of players to damage the positions of other players by
targeting; voting emphasizes the fact that players are choosing a winner according
to their tastes rather than that the game process is choosing a winner based on
some combination of that winner’s skill and whatever luck may be inherent in
the game.
Note that virtually no classic boardgames, card games, or sports fall into these
categories; examples of highly political games are almost all from modern games.
Perhaps this is because politics tends to be “evolved out” of games, or perhaps people’s
taste in games is changing.
Also keep in mind that all these terms, and indeed this entire section, apply only
to games with three or more sides. You can’t choose among opponents if you only
have one opponent.
Exercise 2.8: Play “Truel” (tri-duel). In this game, three players take turns shooting
a target of their choice. One player has an 80 percent hit chance, one 60 percent, one
11. Even with interaction and targeting, a game may still avoid being a chip-taking game by
giving players reasons to target one player over another. More on this below.
12. Some games have explicit voting mechanics, in the sense that at certain points during the
game players actually vote on something as part of the game. It is not necessary for a game to
have a voting mechanic to be a voting game in our sense, although games with voting mechanics
may become voting games in our sense to a greater or lesser extent if care is not taken.

Multiplayer Games

51

40 percent.13 A player who is hit is out, and the winner is the last person left. Rotate
who gets the first shot in each game. Play thirty or so games. What are the results?
Are you surprised? What explains your results?
Strategies Found in Political Games
Political games and chip-taking games lead to certain common behaviors among
players, such as
Lying low so that players do not perceive you as a threat.
Waiting while other players fight it out and then mopping up the pieces.
• Cajoling, whining, or begging other players not to hurt you.
• Offering out-of-game benefits (“I’ll get you a Coke”) or making out-of-game threats
(“You’ll have to walk home!”) to influence other players’ behavior.
• Hurting the player who last hurt you (“revenge”).
• Threatening revenge in an effort to get another player to choose a different victim.
• Deliberately taking an action that harms another player but also hurts your own
chance of winning, due to anger or in order to establish credibility as a player who
will indeed avenge hurts (the latter may be thought of as a rational attempt to win
more often in repeat play).
• Taking turns hurting other players, or deciding randomly who to hurt, perhaps to
be “fair” or to reduce victims’ desire for revenge.
• Explaining to the victim why your choice was the rational one given the current
game state (for reasons similar to taking turns above).
• Arguing that a player’s choice of you as the victim is not optimal, and that their
chances of winning would be higher if they chose another victim.
• Arguing that some other player should “fall on the grenade”: make a sacrifice to
stop the leader from winning (or getting too far ahead).
• Deliberately passing up an opportunity to stop the leader from winning when your
turn comes, so that the last remaining player who has a chance to stop her is forced
to “fall on the grenade.”
• Kingmaking: near the end of the game, a player who has no chance to win determining which of the players still in contention actually wins (discussed in the next section).
•
•

We will sometimes refer to these sorts of behaviors as “political.”14 Note how generic
these effects are, in the sense that they occur independent of the game mechanics of
any particular game. If the game has targeted interaction, the above effects will occur.
13. If you can’t find a ten-sided die, use a six-sided die and reroll all 6s (so the first player hits
on 1–4, the second player hits on 1–3, and the third player hits on 1–2).
14. We make this somewhat inconsistent word choice partly because “the kinds of behaviors
that tend to arise from strong targeted interaction” is just too long, and partly because it accords
with the common usage of game players.

52

Chapter 2

If the game has enough targeted interaction, the above effects will dominate the game,
and in some sense all games with enough targeted interaction are the same game.15
One’s ability to win such a game will depend more on one’s skill with the above
behaviors than with any skills specific to that particular game’s mechanics.
Problems with Politics
If political games have a problem, it is not that political interaction is inherently
uninteresting—although there are some players who play games hoping to avoid that
sort of thing—but that it can overwrite the rest of the game. Skill at the game doesn’t
necessarily increase one’s chances of victory,16 and in fact it may decrease it as one
becomes more of a target for the other players.
If one considers games from the point of view of heuristics, the potential problems
of political games are highlighted. Normal positional heuristics become largely irrelevant: if at any point any player can be “picked on” and eliminated by group consensus, how can one know what one’s position in the game is? And if positional heuristics
are irrelevant (or, more precisely, if positional heuristics relating to the mechanics of
that particular game are replaced by general social heuristics involving predictions of
who is likely to do what to whom), then directional heuristics (again, of other than
the social kind) are likewise irrelevant.
Depending on the playgroup, climbing the heuristics tree in highly political games
can be very interesting. Without a good grasp of the basic positional heuristics (those
independent of politics), the effect of political interaction can be mitigated. Once a
set of players has developed a good set positional heuristics independent of the politics, the game can often be reduced to a simple voting one, but that process of understanding who is in the lead and how to stop them is often an interesting one.
Games with targeted interaction are more prone to arguments. In a game without
targeted interaction—a two-player game like chess, for example—there’s no need to
argue with someone that she is following the wrong strategy. If the other player is
hurting herself, then so much the better for your chances.17 But if someone is taking
15. The cynical (or realistic, depending on your point of view) may see some resemblance to life
in general.
16. Thoughtful readers will notice a paradox: How can skill not increase one’s chances of victory,
since being skillful at a game means by definition that one does things that make one more likely
to win it? A more precise way of stating the situation would be that skill at making game choices
that increase one’s progress toward the victory condition doesn’t actually increase one’s chances
of victory, and that the true skill in the game is thus the skill of convincing players to attack
players other than oneself, through means such as lying low until the last minute, looking harmless and friendly, threatening out-of-game consequences, whining, browbeating, and so on.
17. Of course, in a friendly game one might point out an error just to be helpful. And a very
nasty player might try to talk someone out of a winning move (which is why it often pays not
to listen to an opponent’s advice in very competitive situations).

Multiplayer Games

53

one of your chips in a game with targeted interaction, it is to your advantage to
convince him to take someone else’s chip. Perhaps there are good reasons for him to
take someone else’s chip, and you need only make him understand that—and how
frustrating if he does not! But if the game is very political, and his choice is essentially
arbitrary, there is still some pressure on you to convince him to make a different,
but still arbitrary, choice, a situation unlikely to lead to enjoyable or productive
conversation.
Players’ problems with politics can also be mitigated in situations where there is
some consensus that a particular move is forced due to its clearly being the best
option. For instance, consider a toy game where players on their turn can either add
two chips to their total or take one away from another player. The game ends when
