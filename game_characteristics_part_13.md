have a terrible destructive fight that leaves them both much worse off. Two doves will
share food and each gain a little. A hawk that meets a dove will frighten it off and
gain the whole meal for itself. (This game can also be thought of as the teenage driver’s
game of “chicken” with Hawk as Drive Straight and Dove as Swerve; it sometimes goes
by that name in the literature.)
Hawks and Doves is quite similar to Battle of the Sexes with its two Nash equilibria.
The focus here, though, is on the desire to be the Hawk: each bird would like to be
the Hawk if only it could be sure the other bird would be the Dove. But both birds
being the Hawk is a disaster, whereas both birds being the Dove is fine.
It’s hard to make much sense of this until you start thinking of populations. In a
population of Doves, a single Hawk will do very well (and presumably will start reproducing more and more, leading to more Hawks). In a population of Hawks (constantly
fighting and hurting each other) a single Dove will do very well. With some work,
one can compute what the end percentage of Hawks and Doves should be (i.e., the
percentage at which a new Dove or a new Hawk entering the population has no special
advantage over its opposite number). The Hawks and Doves game is a foundational
example for the application of game theory to evolutionary biology.

252

Chapter 8

This same population-based thinking can be applicable in real-world games, particularly those like Magic: The Gathering where people show up with a preset strategy—
in the case of Magic, their deck. Specific decks have various degrees of advantage over
specific other decks, which one can think of as a large game-theoretic payoff matrix
(your payoff in this case being your chance of winning against a specific deck type, a
chance that you naturally would like to be as high as possible). Then the numbers of
various deck types at Magic tournaments evolve in essentially the same way as the
numbers of Hawks and Doves in a population of birds, but with the difference that a
clever player can hope to predict imbalances in the population beforehand, and show
up with a deck to take advantage of those imbalances.4
V. Back to Rock-Paper-Scissors: Mixed Strategies and the Existence of Equilibria
We’ve been looking at Nash equilibria in various games, and we claimed at the start
that the big idea in the theory was to look for the equilibria in whatever game we
were trying to analyze. But it’s possible to have a game with no equilibria in it. In fact,
we already know such an example: rock-paper-scissors.
In rock-paper-scissors, no matter what strategy I pick, there is a strategy you can pick
that will beat it, and vice versa. So by definition a Nash equilibrium is impossible.
But is there a rock-paper-scissors strategy, in the more general sense of “a method
of play,” that would prevent one’s opponent from gaining an advantage? Certainly:
one could roll a die and then choose one’s strategy via 1–2: Rock, 3–4: Paper, 5–6:
Scissors. If I choose this overall strategy, I can even announce it to you beforehand
and (so long as I don’t reveal my die roll to you beforehand) there’s nothing you can
do to take advantage of it.
So let’s define a mixed strategy as a set of probabilities (totaling 1, i.e., totaling 100
percent), showing how likely you are to play each strategy given in the game’s grid
(which we’ll call pure strategies if we need to distinguish them from mixed strategies).
So our “unbeatable” rock-paper-scissors strategy is 1/3 Rock, 1/3 Paper, and 1/3
Scissors.
Probably the most basic result of game theory is the following:
Theorem:

Every game has a Nash equilibrium once you allow mixed strategies.

A few caveats about this Nash equilibrium:
(a) It may not be unique.
(b) It may not be the “best outcome” in terms of payoff.
4. However, if the field is at equilibrium, then it won’t matter what deck you bring (see caveat
(e) below on Nash equilibria—you can think of the field as a whole as playing an equilibrium
strategy). But given the complexity of the game, the field will never be at perfect equilibrium.

Appendixes

253

(c) It may be hard to find for more complex games.
(d) Any dominated pure strategies won’t show up in the mix—that is, they’ll have
probability zero.
(e) If you play the Nash equilibrium strategy, it turns out that although your opponent
won’t be able to “beat” you (get a better result against you), you won’t be able to
“beat” them either (i.e., no matter what, you’ll both get the expected result). Untangling what this really means takes more time than we have here, but you can get a
feel of it from the rock-paper-scissors example: play the die-rolling strategy, and on
average you’ll never do worse than 50/50, but you’ll never do better either, even
against a terrible opponent who always plays rock.
Note we already knew (a) from the Battle of the Sexes, and (b) from the Prisoner’s
Dilemma.
Despite its limitations, the existence of Nash equilibria is still a powerful and
perhaps somewhat surprising result: it means there is a kind of stability in even the
most complex games.
VI. Concluding Remarks
This survey of game theory has been a very brief one (see the references below for
further information). Many of the limitations of the theory as we’ve presented it can
be relaxed with some more work. Among the things people look at are
More than two players
Allowing players to take turns
• Looking at what happens under repeat play (this really changes the best strategies
for games like the Prisoner’s Dilemma)
• Allowing hidden information
• The differences between theory and experiment (i.e., how do real people actually
play these games if you give them the opportunity?)
•
•

If one’s main interest is actual games people play (e.g., chess or Starcraft), what
relevance does game theory have? In terms of the detailed techniques of game theory,
the answer is usually “not very much.” But the point of view of game theory can be
instructive when looking at subgames within a larger “real” game. Also, when doing
balance work, one is often mentally deleting dominated strategies (such as equipping
the trash items in World of Warcraft), and what’s left can be thought of as a large and
complex version of rock-paper-scissors: more than three strategy options, of course,
but with each option beating some other options and being itself beaten in turn by
yet other options.
If you understand this point of view—perhaps instinctively, or perhaps with the
help of some mental tools like game theory to help you along—you can guide your

254

Chapter 8

game’s development. If you think of the game’s strategic choices as a large rock-paperscissors structure, it’s important that all the strategies you want to remain viable (i.e.,
used at least occasionally by good players) neither dominate nor are dominated by
the other viable strategies. If, on the other hand, you can delete dominated strategies
one by one, and are then left with only one choice for each player, your game has
suffered complete strategic collapse—a grim fate indeed.
References
Arranged roughly in increasing order of difficulty.
Game Theory: A Very Short Introduction, by Ken Binmore. The “Very Short Introduction” series is
quite good in general, and this intro to game theory is particularly nice. Lots of good examples,
very readable.
Game Theory and Economic Modelling, by David M. Kreps. Another fairly accessible text. Don’t let
the Economic Modelling in the title scare you; it’s not a heavily mathematical text, and it’s fairly
user-friendly. It’s more a general text than an economics-specific one. A little more academically
oriented than Binmore, but not by that much.
Luck, Logic, and White Lies: The Mathematics of Games, Part III, by Jörg Bewersdorff. An excellent
survey that applies three different kinds of math to games: basic probability theory, combinatorial game theory, and Von Neumann game theory.
Evolution and the Theory of Games, by John Maynard Smith. Game theory is also used in biology
to explain how the behavior of animals can evolve (the Hawk-Dove game is an example). This
is the classic book by one of the founders of the field. Not too much math—very much focused
on evolutionary biology.
The New Palgrave Game Theory, edited by John Eatwell, Murray Milgate, and Peter Newman. A
collection of essays about game theory by and for economists (the New Palgrave is a series of
books for economists on various econ-related subjects). The essays vary widely in accessibility—
some friendly survey articles, some pretty hardcore stuff. The fact that the articles are all independent makes it useful for finding short bits on specific topics that interest you. A good place
to get a survey of how game theory is used in economics.
Game Theory for Applied Economists, by Robert Gibbons. A good intermediate-level survey of game
theory. A nice place to find careful and precise statements of definitions and theorems (if you’re
the type to find such things helpful) but definitely requires some ability to read math.
Game Theory, by Drew Fudenberg and Jean Tirole. The standard reference in the field. A serious
graduate-level text.
Theory of Games and Economic Behavior, by John von Neumann and Oskar Morgenstern. The book
that started it all back in 1944, and still in print (in fact, a commemorative edition was published
in 2004). Not an easy read, in part due to its density and in part due to the fact that notation
has changed since the 1940s, but still a classic.

Appendixes

B.

255

Combinatorial Game Theory

I. Introduction
Dating back only to the 1970s, combinatorial game theory is more recent than Von
Neumann game theory. Combinatorial game theory was invented primarily by John
Conway (also known for the 0-player game of Life). It’s still an active, albeit small,
field of mathematical research. No real-world applications of the theory have been
found (other than applications to games themselves), so not many people outside of
mathematics know much about it. It’s approachable enough, though, that recreational
mathematicians (who are often the sort of people who like games anyway) have some
interest in it.
It’s best suited for two-player games where players alternate moves, until finally
one of the players wins and the other loses. The games need to have no overt luck
(no dice or cards or other randomizers) and no hidden information. Games like chess,
checkers, and go fit into this category.
Chess and checkers, although the right sort of games, turn out not to be the best
ones to analyze using combinatorial game theory. There is, however, some good work
using the theory on go.5 Other games that the theory works well on include Fox &
Geese, Nim, and Dots & Boxes, plus a great number of more obscure games such as
Hackenbush, Chomp, Kayles, and Sprouts, the kinds of abstract strategy games that
recreational mathematicians like to invent and play. As in von Neumann game theory,
many of the games studied are made up for purposes of the theory; however, the
made-up games in combinatorial game theory feel much more like games one might
actually play as opposed to the pure thought experiments one sees in the von Neumann
theory (imagine actually playing Hackenbush as described below versus playing the
Hawk-Dove game described above).
The big idea of the theory is that game positions or states can be analyzed in a way
that lets you think of a game state as a kind of generalized number. The Conway game
theory is a type of math for these generalized numbers (sometimes called “surreal
numbers,” a term invented by Donald Knuth, who also wrote a book by that title on
the theory). If you can decompose the board position into pieces, evaluate the (surreal)
numerical value of the pieces, and know how to do (surreal) addition, you can win
games that would utterly baffle people who don’t know the theory.6
5. It’s possible to construct (admittedly somewhat unnatural) go positions that even a professional go player can’t solve, but that can be solved with the aid of the theory. See Berlekamp
and Wolfe, Mathematical Go.
6. This approach is why games like go or Dots & Boxes, where the board sometimes breaks down
into different independent areas, are more suited to the theory than games like chess, where one
piece often affects another piece all the way across the board.

256

Chapter 8

The numbers involved include the usual numbers we all know and love (or hate,
as the case may be). But they also include numerous oddities, including many types
of infinite numbers, and even stranger beasts such as
* star
↑ up
+2 tiny-two
Very roughly, the number you associate with a game position is the number of moves
that you’re ahead, but that can be a bit puzzling for a position with value 3/4 (what
does it mean to be 3/4 of a move ahead?) and even more confusing for a position
with value * or ↑.
We’ll begin by describing a game many of our readers may not know, called Hackenbush,7 that will help make some sense of the link between games and numbers.
Once you understand Hackenbush, you will see why it makes sense to assign values
of 3 or –2 or 0 (or even 1/2) to game positions. Then we’ll redo what we did for Hackenbush from a more general point of view. In particular, we’ll define game in the
general sense of combinatorial game theory, and explain what it means to add two
games together. Lastly, we’ll talk a bit about another simple game, called Domineering,
where some of the stranger numbers like * and ↑ will make their appearance.
II. Hackenbush
In this game, there are two players, Black and White (later we will call these players
Left and Right). A game state is a series of black and white lines (called “edges”) each
connected to the ground or to other edges.

Figure 8.1
A typical Hackenbush position

On her turn, a player must remove an edge of her color, and any edges that lose
their connection to the ground fall down and disappear. If a player has no edges left
to remove (e.g., if it’s Black’s turn but only white edges are left), then that player loses.
7. Strictly speaking, we will be showing a variant called Blue-Red Hackenbush or Black-White
Hackenbush; there are other variants as well.

Appendixes

257

For instance, in the above position, if it’s White’s turn, he might take the rightmost
white edge (killing the black edge above it). Then Black would be forced to take the
only remaining black edge. Then White would take any edge he liked. Now it’s Black’s
turn and she has no edges to take, so she loses.
Now that we have this game, let’s try to understand it better by analyzing some
very simple positions.
Our first trick will be to think of positions as games in their own right: this makes
sense because for any position, we can play a game starting from that position. So from
now on we’ll be referring to positions as games, and we’ll try to figure out, for each
such “game,” who will win. Of course, that may depend on who gets to play first. (We’ll
assume each player plays perfectly, i.e., always makes the best possible move.)

Figure 8.2

In this game (no edges of either color available), if it’s Black’s turn to move, she’ll
have no move and thus she will lose. But the same thing will happen to White if he
must move first. So in this game, whoever moves first loses.
We call this game, naturally enough, 0.

Figure 8.3

In this game, Black wins going first (she takes her edge, and then it’s White’s turn
to move in the game 0). But if White goes first, he still loses. So this game is a win
for Black no matter who goes first.
We name this game 1, and we think of it as a 1-move advantage for Black (more
on that below).

Figure 8.4

258

Chapter 8

This game is a win for White, no matter who goes first. We call it –1.

Figure 8.5

This game is even better for Black than the game 1. It will, we trust, surprise no
one that we are going to call it 2. However, it’s not clear yet if all these names mean
very much.

Figure 8.6

Here is a game that looks like 1 and –1 standing next to each other. Let’s interpret
“standing next to each other” as + (we’ll expand on this idea of adding two games
together as we go . . . it’s the core of combinatorial game theory, appearing here in a
very simple form). Well, what should 1 + (–1) be? Surely it should be 0!
Well, how does this game work? If Black goes first, she takes her edge, then White
takes his edge, and then Black loses. If White goes first, he takes his edge, then Black
takes hers, and White loses. So whoever goes first loses, just like the game 0!
The big trick: we will declare any game (not just the special game with no options
at all) where the first player always loses to be equal to 0. So even though this game
looks different from the game with no options at all, we will still call it 0.

Figure 8.7

Appendixes

259

Here’s 2 + (–2). Try playing it Black first, and then playing it White first (each player
is playing smart, so she or he will of course chop off their upper edge rather than their
lower edge), to see that the first player always loses. So 2 + (–2) = 0, just as we’d hope.

Figure 8.8

This one’s a bit strange. It’s not hard to see that Black wins no matter who goes
first (try it!). So far we’ve been assigning positive numbers to Black-favorable positions,
and negative numbers to White-favorable ones, so this game should be a positive
number. Let’s call it x for now. Note this game is worse for Black than the game 1
(there’s a white edge in it, which can only help White). So presumably 0 < x < 1.
Well, maybe x = 1/2? What could that possibly mean?
It turns out we already have the tools to answer this question. If x = 1/2, then surely
x + x + (–1) = 0. And that’s something we can explicitly check.

Figure 8.9

Here we have x + x + (–1). If this game is 0, we can feel we are on the right track
assigning the value 1/2 to x.
So we should check to see that the first player always loses. If Black goes first, she
takes one of her edges. Then White should take the edge he has on top of the remaining black stalk. Then Black takes her remaining edge, White takes his last edge, and
Black loses.
If White goes first, he takes a white edge on one of the black stalks. Black takes her
other stalk (killing a white edge). Then an edge for White, an edge for Black, and
White loses! So whoever goes first does indeed lose, this game is indeed 0, and so we
are happy to say x = 1/2.

260

Chapter 8

Figure 8.10

Similarly, this is –1/2 (try checking it by showing (–1/2) + (–1/2) + 1 = 0).

Figure 8.11

You might want to try showing this is 1 1/2.

Figure 8.12

And this, it turns out, is 1/4 (try it!). (You might think this would be 1/3, but if you
check, you’ll find y + y + y + (–1), where y is this game, is a win for White no matter
who goes first! That means the game must be less than 1/3, which might lead you to
try 1/4. And if you check, you will find y + y + y + y + (–1) does indeed equal 0.)
Exercise 8.1:

Check the various statements above regarding –1/2, 1 1/2, and 1/4.

Appendixes

261

There’s a lot more to say about Hackenbush, but we’ll stop here. Let’s summarize
the main ideas of our analysis, and then we’ll use those ideas to develop a general
theory that applies to any two-player game of the appropriate type (players take turns,
someone eventually wins, no randomizers, no hidden information).
Games = positions. We think about a position in a game as a game in itself (start
playing from that position).
• Look from both points of view. Think about who wins the game when one player
goes first, and then when the other player goes first.
• The 0 game.
Call all games where the first player always loses 0.
• Adding games.
If a game/position is made up of two unlinked games/positions,
think of the big game as a sum of the two little games. Use this idea (sometimes with
help from the 0 game idea) to assign the right numerical values to unknown games.
•

III. The Theory
A game G is denoted by {A, B, C, . . . | P, Q, R, . . .} where A, B, C, . . . and P, Q, R,
. . . are games. All games are built up in this way. (Think of this as like set notation,
but there are left elements of G and right elements of G, and we want to keep them
distinct in our heads.)
The game is played by Left (formerly known as Black) picking one of the games A,
B, C, . . . if it’s her turn, or Right (formerly known as White) picking one of the games
P, Q, R, . . . if it’s his turn. We call the games A, B, C, . . . the left options of the game
G, and P, Q, R, . . . the right options. Play continues with the players taking turns—for
example, if Left picks B, then Right picks one of the right options of B (not of G), and
so on. A player who has no options loses.
If all games are built from other games, how do we get started? How is it that there
are any games at all?
The answer is that we “build up from nothing”—that is, we start with the game
{ | }, which we will call 0. This is the game where neither player has any options (so
it’s true, in a formal mathematical sense, that all of its nonexistent options are games,
as required by the definition, i.e., 0 is a game by our definition). So whoever moves
first in this game loses.
Then we define some more games from that:
1={0|}
This is the game where Left can move to 0, but Right has no options. Note that this
game is a win for Left, no matter who moves first.
2 = { 1, 0 | }
–1 = { | 0 }
1/2 = { 0 | 1 }

262

Chapter 8

Quick detour: Let’s compare this with some of our Hackenbush games. We claim it’s
the same thing, just with different notation.

The game with no options for Left (Black) or Right (White). So it’s the game
0 = { | }.

Left can move to 0, but White has no options at all. Thus this game is 1 = { 0 | }.

Similarly this is –1 = { | 0 }.

Left can move to 1 or to 0, but White has nothing. So it’s 2 = { 1, 0 | }.

Appendixes

263

Left can move to 0, and White can move to 1. Thus it’s 1/2 = { 0 | 1 }.
Back to the more general case. If we have some game G, and we assume both players
play perfectly, then there are only four possibilities:
1.
2.
3.
4.

L always wins (whoever goes first).
R always wins (whoever goes first).
Whoever goes first always loses.
Whoever goes first always wins.

We will say G > 0 in the first case, G < 0 in the second case, and G = 0 in the third
case. We haven’t encountered the fourth case before, but let’s label it G || 0 and say
“G is fuzzy” or “G is confused with 0.” (Fuzzy games never come up in Hackenbush,
which is why we haven’t seen them before.)
Here’s an example of a fuzzy game:
G={0|0}
(Convince yourself that whoever goes first wins this game!) This game is called *
(“star”) and it comes up a lot. (If you know the game Nim, you can think of * as a
Nim game where there is a single pile with just one stone in it.)
Addition: If G, H are games, we define G + H to be the game where players can move
in either G or H on their turn (and they lose if they have no moves anywhere).
Negatives: We define –G to be the game with the roles of Left and Right reversed
(just like switching Black and White in Hackenbush).8
Equality: We say G = H if G + (–H) = 0.
Note that two pretty different looking games can be “equal” in this world. You
might want to try checking that { 1 | } is equal to { 1, 0 | }, for example (the game
we’ve been calling 2).
If you are trying to do all this with mathematical rectitude, there are a bunch of
facts to prove, like
G+0=G
If G > 0 and H > 0, then G + H > 0
G+H=H+G
G – G=0
8. Note that you have to switch the roles of Left and Right “all the way down,” not just at the
very top level. More formally, if G = {A, B, C, . . . | P, Q, R, . . .} then –G = {–P, –Q, –R, . . . | –A,
–B, –C, . . .}. If this seems weird, try it out on a few simple Hackenbush positions, or just ignore
it for now.

264

Chapter 8

One might try to define multiplication of games as well (multiplication turns out
to be rather tricky, although proving the above addition facts isn’t too bad). We won’t
delve into multiplication, or go through all the formal proofs, since that would take
us too far afield (see the references below for more details). We’ll give the outline of
the last one, though, because it’s short and appealing, and it actually shows a good
strategy in some games (e.g., two-pile Nim).9
Theorem: G – G = 0.
Proof (sketch). By definition, G – G = 0 means G + (–G) = 0. So we have to show G
+ (–G) is a win for whoever goes second. Suppose R goes first. Then, because –G is just
G with the roles of L and R reversed, L can make the exact same move R made in the
other game (if R goes in G, L goes in –G and vice versa). Now it’s Right’s move again.
L can continue to mirror Right’s moves until R finally runs out of moves, and then L
wins! But R can do the exact same thing to L if she moves first. So whoever goes first
loses.
So in Hackenbush, our games are all nice things like 2 and –3 and 1/2, but we’ve
seen there are games like * that are weirder. We can sort out the actual numbers from
the nonnumbers as follows.
We say a game G is a number if G = {X1, X2, X3, . . . | Y1, Y2, Y3, . . .} where all the
Xi and Yj are numbers, and Xi < Yj for every i and j. In other words, G is a number if
it’s built out of things that you already know are numbers, and each left option is less
than each right option.
Remembering that vacuous statements are automatically true (the same trick that
made 0 = { | } a game), we find
0 = { | } is a number
2 = { 1, 0 | } is a number (all the left options are less than all none of the right
options)
– 1 = { | 0 } is a number
1/2 = { 0 | 1 } is a number
If the “vacuous statements are true” bit feels awkward, one can just think of it as a
special rule that G is a number if it has no Left options and all the Right options are
numbers (or vice versa), and that 0 is a number by fiat.
There are some weird numbers too. One interesting one is
ω = { 1, 2, 3, 4, . . . | }
9. Also see note 32 in chapter 2.

Appendixes

265

and its friend
–ω = { | –1, –2, –3, –4, . . .}
So ω is the game where Left picks any whole number she wants (and Right has no
options). In Hackenbush terms, ω is the game.

Figure 8.13
An infinite tower of moves for Black

A very popular game among young children is the game
ω–ω
If Left goes first, she will pick a number from ω. Then Right will pick a larger-sized
number from –ω, and the sum of those two will be less than 0—that is, a win for
Right. Similarly Left will win if Right picks first, so ω – ω = 0 (a second-player win).
This game is more commonly known as “my dad makes more money than yours.”
You can think of ω as “infinity,” but normally it’s hard to make sense of concepts
like “infinity plus one” or “infinity minus three.” However, ω + 1 and ω – 3 make
perfect sense in this theory.10
10. Being able to talk sensibly about ω + 1 and so on predates combinatorial game theory,
though. It goes back to the late nineteenth century and Georg Cantor’s theory of transfinite
ordinals.

266

Chapter 8

Note that * = { 0 | 0 } is not a number according to our definition. And a good thing
too, because * > 0, * < 0, and * = 0 are all false, and we’d want one of those three things
to be true for any respectable number! (Which in fact is true, and it’s another of the
things one would prove when developing this theory carefully.)
Before leaving the world of theory and looking at another specific game, we’ll quote
a result that really shows off the power of the theory. It does require you to know
about Nim, which fortunately is easy to describe. Nim is a two-player game played
with piles of pebbles or other objects. On your turn, you can take any number of
pebbles from any one of the piles. If there are no pebbles left for you to take, you lose.
(You might try playing a few games . . . it’s not too hard to figure out the strategy if
the starting position has one or two piles, but it’s quite hard to figure out how to play
if there are three or more piles.)
Call a game G impartial if L and R have the same options at every step. So Nim is
impartial (anyone is allowed to take any pebble they want), but Hackenbush isn’t
because Black can only take black edges.
Lastly, let’s write *n for the very simple game that’s a Nim heap of n pebbles (note
*n is a first-player win, i.e., *n || 0, i.e., *n is fuzzy). The games *1 = *, *2, *3, . . . are
sometimes called “nimbers” (note that they are not numbers in the sense that we
defined them above, but they are still games).
Exercise 8.2:

How do you write *n in the { | } notation?

Theorem (Sprague-Grundy): If G is any impartial game, G = *n for some integer n.
This is quite remarkable. If you see any game, no matter how complex, that’s impartial,
then you know it’s really a pile of pebbles in disguise. (In particular, any collection of
pebble piles is equal to a single pebble pile of some size, although not in the way you
might think, e.g., it turns out *3 + * 2 = *1, not *5!)
Exercise 8.3:
1. Show *n + *n = 0, i.e., –(*n) = *n.
2. Verify *3 + *2 = *1. (Hint: Using (a), it’s enough to show *3 + *2 + *1 is a secondplayer win.)
3. (Hard) Figure out how to add *m and *n for any two whole numbers m and n. (Hint:
Try writing out the addition table for small values of m and n, say 1–10 or 1–20. Look
for patterns involving powers of 2.)
IV. Domineering
Hackenbush was a nice game to start with because it was simple, and because the
values of the positions turned out to be numbers we are already knew. Domineering

Appendixes

267

is a nice game to look at now because it’s still simple, but lots of nonnumerical values
arise very naturally.
We won’t try to do anything like a complete analysis of Domineering. Instead, we’ll
just show a few positions and what values arise from them.
The game is played with dominoes on a grid (say a chessboard). Players take turns
placing dominoes so that they cover two squares. Left places her dominoes vertically,
and Right places his dominoes horizontally. As usual, if someone is unable to move,
that player loses.

Figure 8.14
A 6 x ×6 Domineering game in midstream

Once a few moves have been played, the Domineering game breaks up naturally
into a sum of games (the various still-empty regions that are left on the board). So we
can hope to understand Domineering better by evaluating the various shapes that
empty regions might have and understanding how to add them (if shapes correspond
to numbers, of course, it will be very easy to add them).
This is a pretty big project, but let’s do just a little to see how it would go.

Figure 8.15

Here’s a single empty square. Nobody can place a domino here—that is, nobody
can move here—so this is the game 0 = { | }.

268

Chapter 8

Figure 8.16

Left can place a domino here (after which nobody can move), and Right can’t move
at all. So this game is 1 = { 0 | }.

Figure 8.17

Either player can move to 0 from this position. So this is * = { 0 | 0 }.

Figure 8.18

Left can move to 1, and Right can move to –1, so this is the game { 1 | –1 }. This
is a game we haven’t met before. Let’s call it ±1. It’s very good to grab this position
quickly, because if you do it gives you yet another move, and if your opponent grabs
it, it gives him another move. Such positions are called “hot,” and there’s a whole
“temperature theory” within combinatorial game theory that tells you about hot positions, how to evaluate them, how to play in them, and so on.

Figure 8.19

Appendixes

269

Left can move to either 0 or –1. Of course, 0 is better—why give Right a free move?
Since we are assuming everyone plays perfectly, we should just say Left moves to 0.
Meanwhile Right can move only to 1. That makes this game { 0 | 1 }, which is our old
friend 1/2.

Figure 8.20

Left can move to –1, and Right can move to *. So this is { –1 | * }, which looks
confusing at first, until we realize that it’s just a game where whoever moves first loses
(Left moves to –1, Right takes the –1, and then Left has no move, or Right moves
to *, Left takes the *, and then Right loses). So this game is in fact just 0!

Figure 8.21

Here Left can move to 1/2, *, or –1/2, and 1/2 is clearly Left’s best move. Meanwhile
Right can move to either 1 or 2, and 1 is the best choice. So this is the game { 1/2 |
1 }, which you can show (using Hackenbush pictures, or doing the same trick but with
Domineering pictures if you prefer) is 3/4.

270

Chapter 8

Figure 8.22

Here Left can move to 0 or * (0 is better for Left), and Right can move only to *.
So this is the game { 0 | * }. This is a game we haven’t seen before; it’s called ↑ (pronounced “up”). No matter who goes first, this game is a win for Left, so ↑ > 0. But ↑
is smaller than any positive number. In other words, ↑ + ↑ + ↑ + . . . + ↑ + (–1) < 0 (the
game is a win for Right) no matter how many ups you add. So our system has infinitesimals built right in, and they aren’t even that complicated (we’ve made one out of
0 and *, two very simple games).
Exercise 8.4: Show ↑ + ↑ + ↑ + . . . + ↑ + (–1) < 0 for any number of ups. (Hint: If you’re
having trouble, try playing the game with just two or three ups first.)
V. Concluding Remarks
This survey has only scratched the surface of combinatorial game theory. It’s a big
field, and still fairly young, so it’s still growing at a good rate.
The theory only helps you analyze certain types of games, so its usefulness is somewhat limited (but then, if you are looking for direct usefulness, games might be the
wrong place to be looking!). But it’s a very beautiful theory that combines games and
numbers in an elegant way. And it certainly stretches your brain in the way abstract
math does.
It’s perhaps ironic that although the von Neumann theory doesn’t actually let you
analyze any real-life games, it can be useful in thinking about more complex games
(e.g., in looking at the abstract rock-paper-scissors relationships in an RTS), whereas
Conway’s theory actually lets you do a good bit of serious analysis on real games like
go, but isn’t terribly useful for thinking about complex games outside of its tightly
defined domain of applicability.
References
Again arranged roughly in increasing order of difficulty—very roughly indeed this time, because
the books vary so much in tone. Some may find the chattiness and casual approach of Winning

Appendixes

271

Ways to be the most accessible; other readers may find the more structured approach of Lessons
in Play more to their taste.
Winning Ways for Your Mathematical Plays (4 vols.), by Elwyn R. Berlekamp, John H. Conway, and
Richard K. Guy. Introduces the theory using lots and lots of example games. If you are wondering
how the theory might apply to some particular game you like, this is the place to look.
The Dots & Boxes Game: Sophisticated Child’s Play, by Elwyn Berlekamp. In-depth application of
the theory to the classic childhood game of dots & boxes. Read this book and be an unstoppable
dots & boxes force!
Surreal Numbers, by Donald E. Knuth. An odd but fun little book about two people stranded on
a desert island who decide to pass the time by constructing the surreal number system. Good if
you are a Knuth fan, or like the Socratic style of presentation.
Luck, Logic, and White Lies: The Mathematics of Games, Part II, by Jörg Bewersdorff. Part II of
Bewersdorff’s three-part survey of the math of games (mentioned in the previous appendix) is
on combinatorial game theory; it also covers some other topics like computer chess.
Lessons in Play: An Introduction to Combinatorial Game Theory, by Michael H. Albert, Richard J.
Nowakowski, and David Wolfe. A textbook (complete with exercises and answers in the back) at
an undergraduate level. Good for those who found the casual approach of Winning Ways more
confusing than friendly.
On Numbers and Games, by John H. Conway. A more formal treatment of the subject. Good for
those who want precise definitions, statements and proofs of theorems, and a generally mathematical approach. More abstract and more advanced than Lessons in Play.
Mathematical Go: Chilling Gets the Last Point, by Elwyn Berlekamp and David Wolfe. A fairly
involved application of the theory to a very complicated game. Good if you want to see the
theory applied in a big way to a hard problem.
Games of No Chance, More Games of No Chance, and Games of No Chance 3, edited by Richard J.
Nowakowski. Separate collections of papers on combinatorial game theory. Good if you want to
see a broad scope of applications of the theory and if you want to get an idea of the state of
(relatively) current research. Most areas of math are so dense and complex that it’s basically
impossible for a layperson to get to current research, but combinatorial game theory is young
enough that it’s almost approachable for a smart and hard-working amateur.

C.

List of Games

This appendix lists most of the games referenced in the text (we occasionally omit
games that receive extremely brief mentions). In most cases, a nodding familiarity
with the game will be enough to understand these references.
We often use specific games as stand-ins for others in their genre—for example,
we might give Starcraft as an example game to illustrate some point, but almost any

272

Chapter 8

other real-time strategy game could serve as an example as well. Context should make
our usage clear, and in doubtful cases we say something like “unlike other RTS games,
Starcraft . . .” Games we use especially often in this synecdochic fashion we mark
below by putting their genre after them. For these games we list similar games after
the entry; our hope is that a reader who has not played the game we mention has
played one of the others. Substituting one for the other in the reader’s mind should
do no harm.
Underlined games are ones that have an entry elsewhere in this appendix.
Our descriptions of the games are necessarily brief, and tend to focus on the features
relevant for our discussion in the main text. Many games have variant ways of playing
them, or are actually part of a series of closely related games; we do not mention such
details unless we have a particular need to make distinctions.
Discussion of a game in the main text, and the corresponding inclusion in this list,
should not be taken as a measure of the quality or the importance of the game. We
often reference lesser-known games to make some particular point. Many very important and well-known games are not included in this list.
Games are marked with one to four asterisks based on how often we use them as
examples. A game marked **** is one readers should be familiar with or they’ll miss
a lot of what we’re trying to say. Games marked * are only mentioned once or twice
and little harm will be done if readers don’t know them. This is not in any way a rating
of the quality of the game in question.
BOARDGAMES, CLASSIC
Backgammon**
A two-player race game in which players move their pieces in opposite directions
around a track according to the throw of a pair of dice. There is interaction between
the pieces in both capturing and blocking. The winner is the first player to remove
all his pieces from the board. When played as a gambling game, players may use the
doubling cube, a device that allows them to alter the stakes in a controlled way as the
game progresses (typically a player who feels he’s winning offers to double the stakes,
and the other player may either concede immediately for the original stakes or play
on for the doubled amount).
Checkers**
A two-player game with no overt random elements played on an 8 × 8 grid. Players
alternate, moving their pieces with the goal of capturing all the enemy pieces.
Chess****
A two-player game with no overt random elements. Players take turns moving a variety
of pieces with different movement and capture rules on an 8 ×8 grid. The game is won

Appendixes

273

by checkmating the opponent’s king: putting it in a position where it would be captured
with certainty on the next turn.
Not part of the game rules, but still familiar to most players, is a point-value system
for the pieces: 1 point for a pawn, 3 points for a knight, 5 points for a castle, and so
on. Players can get a rough idea of how far ahead or behind they are by comparing
the total point values of captured pieces on each side.
Chinese Checkers*
A race game for two to six players with no overt random elements. Players alternate
moving their pieces across a star-shaped board with 6 points and 121 holes, often by
leapfrogging enemy and friendly pieces. The goal is to be the first to move one’s pieces
across the board.
Chinese Chess (Xianqi)*
A Chinese two-player game in the same family as chess. Interesting features of Chinese
chess include a river and castle on the board, which restrict piece movement.
Chutes and Ladders, Snakes & Ladders*** (race game)
A children’s race game for two or more players in which a player’s single piece is moved
according to the roll of a die, with the goal being to reach the end of the track first.
There are many spaces that advance a piece further along the track (ladders), and many
spaces force a piece to fall back to a previous square (chutes or snakes).
Similar games: Candyland, Game of Goose, Game of Life, Parcheesi.
Fox & Geese (Fox and Hounds, Wolf and Sheep)*
A family of two-player games with no overt random elements, characterized by the
asymmetry between the two sides’ pieces and goals. The fox player has a single piece
and is attempting to capture or bypass the geese; the geese player has several pieces
and is attempting to immobilize the fox.
The (Royal) Game of Goose*
A race game for two or more players played on a spiral track with movement being
determined by a die roll and board spaces often having a reward or penalty. This game
is one of the first examples of the commercialization of proprietary boardgames.
Go (Wei-chi, Weiqi, Igo, Baduk)***
A two-player game with no overt random elements. Players alternate placing pieces
on the intersections of a 19 × 19 grid with the goal being to surround the most territory (vacant intersections). While not well known in the West, it is extremely popular
in East Asia, with a history stretching back over 2,000 years.

274

Chapter 8

Mancala*
A family of two-player games with no overt random elements, generally played in
Africa and the Middle East. The games are played on a board with a track of pits. The
pieces in these pits are moved by “sowing” them around the track, and the game is
generally won by capturing all the pieces on the opponent’s side.
Monster Chess*
A highly asymmetric variation of chess in which one player has far fewer pieces but
can make two moves each turn.
Parcheesi/Pachisi*
A race game for two to four players where moves are determined by dice. Players move
around a cross-shaped track and interact via capture and blocking.
Reversi/Othello*
A two-player game with no overt random elements. The pieces are white on one side
and black on the other and when captured are flipped to join the capturer’s team.
Players alternate placing pieces on the board, with the goal being to have the most
pieces at the end.
Senet*
Perhaps the oldest known boardgame, dating back to at least 3500 BC. It is presumed
to be a racing game, although all rules used today are educated guesses as to the actual
rules.
Shogi (Japanese chess)*
A Japanese two-player game in the same family as chess. One interesting feature of
shogi is its “drop” rule, where captured pieces can be placed on the board so as to join
the capturer’s side.
CARD GAMES, CLASSIC
Asshole/President/Dai Hin Min*
A family of games for four or more players, in which the goal is to get rid of your
hand. Each player can only play higher-ranked combinations of cards in the same
category as the previously played combination. The last player to play leads to the
next trick. These games often give significant advantages to particular seats and disadvantages to others, and players switch seats to more favorable ones if they do well
in a hand, leading to a “king of the hill” feel to the game.

Appendixes

275

Barbu*
A game for four players. Similar to hearts, but the scoring rules vary (in accordance
with a standard sequence) every deal—for example, in one round every trick taken
might lose points, and in another round only tricks with queens in them carry a
penalty.
Blackjack**
A gambling game for one or more players against a house. Each player is dealt as many
cards as they want, one at a time after an initial pair, with the goal of getting a sum
as close as possible to, but not exceeding, 21. Among gambling games played against
the house, blackjack is distinctive in the amount of skill (typically involving card
counting and probability calculation) that can be applied. Even more unusually, when
played optimally the game is generally in the player’s favor—the house relying on the
difficulty in playing optimally.
Bridge***
A trick-taking game for two teams of two. Players receive a hand of thirteen cards and
bid for the right to name trump based on the number of tricks they can take. One of
the distinctive features of bridge is the elaborate bidding systems that have been
created, and that are designed to communicate to the partner the nature of the hand
and obfuscate the ability of the opponents to bid effectively. Another interesting
feature of bridge is that the team that wins the bid plays with one open hand, known
as the “dummy,” reducing the amount of hidden information (especially for the
bidding team, which will know all the cards its partnership has).
Cribbage*
A game for two players. Players alternately deal six cards and each casts off two cards
and plays out the remaining four, scoring points for a variety of plays, which include
matching the previous play and bringing the total to 15 points. After the hand is
played it is scored on its own, and the dealer scores the discarded crib cards. The game
involves lots of scoring and so is traditionally played with a pegboard, which easily
keeps a running score for all the players.
Gin*
A game for two in which players alternately draw cards from the deck or from the
opponent’s discards in an attempt to make a hand that scores. There are many games
for a wide number of different players using the basic gin mechanics, including Mah
Jong and Phase 10.

276

Chapter 8

Go Fish*
A children’s game in which players attempt to get the most sets of four of the same
rank. On a turn a player can ask another player for their cards of a particular rank and
that player must give them those cards. Any sets of four can be immediately scored.
If a player fails to name a card that the chosen opponent has then her turn is over.
Hearts**
A game generally for three to five. All the cards are dealt out and played and captured
in tricks. Taking hearts and the queen of spades is bad for your score, but getting them
all is called shooting the moon, and is very good for your score, which allows for some
big comebacks at a risk.
Oh Hell*
A family of trick-taking games for two or more players, in which players receive a hand
and a random trump is selected. Each player must bid exactly how many tricks he
will take (in contrast to most trick-taking games, where making extra tricks is not
penalized). Often the number of cards dealt in each hand varies.
Old Maid*
A children’s game. The deck is stripped of three of the four queens, dealt out, and
players take turns drawing cards from their neighbor’s hands. Whenever a player has
a pair the cards are discarded. Since the queen has no mate, it will be in the game
until all other cards are discarded. At that point the player with the queen is the
loser.
Pinochle*
A game for two to four, which involves both melding (laying down certain combinations of cards from the hand) and trick taking. Each hand has three stages: bidding,
melding, and trick taking.
Poker****
Poker is a family of card games for two or more players. Poker involves players receiving cards and betting. The player with the best five-card hand (based on an established
hand ranking) wins the pot (all the money bet during the hand). Usually there are
several rounds of betting each hand, with players receiving additional cards between
rounds.
Often players have more than five cards and choose which of the five cards to use.
Some of the cards may be public (everyone can see them), and some may be communal
(all players can use them to make their final five-card hand). During a round of betting,

Appendixes

277

each player in turn will either call (pay the round’s current wager), raise (increase the
round’s current wager), or fold (drop out of the hand). Versions of poker include:
Stud Poker. Players have some hidden cards and some public cards. The hand has
several rounds of betting where players receive more cards.
Draw Poker. Players receive five cards, have a round of betting, and then can exchange
some of their cards for new cards, followed by a final round of betting.
Texas Hold ’Em. The currently most popular form of poker, in which players receive
only two secret cards and share five communal cards, which are progressively revealed
in rounds of betting.
Dealer’s Choice. Each round, the deal rotates, with the dealer choosing which poker
variant to play for that round.
Skitgubbe*
A game for three to five players. The object of the game is to avoid being the goat: the
last person to get rid of his cards. The game is played in stages. In the first stage players
accumulate a hand, and in the second they get rid of that hand. The two stages work
completely differently from one another.
Solitaire (Patience)**
A large family of single-player card games (or, more generally, any single-player card
game). The rules vary widely, as does the skill required to win: some variants are
completely mechanical, with no player choice at all, and others are quite complex.
Most solitaire games involve laying the cards out in some specified pattern (the
tableau) and then attempting to clear the laid-out cards according to various allowable
pattern-matching rules. Some popular variants include Canfield, Clock, FreeCell, Klondike, Pyramid, and Spider. The term solitaire is also sometimes used to refer to Klondike
in particular.
Spit*
A speed game for two. The cards are divided equally between the players and players
make a tableau of cards that can be played from onto a central pair of cards, a legal
play being up or down one rank with suit being irrelevant (this play is essentially a
