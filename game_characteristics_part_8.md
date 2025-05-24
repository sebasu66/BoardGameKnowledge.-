look for random elements. In games with dice or cards, it’s quite possible for a beginner to beat an expert. In games with no overt random elements, such as chess or go,
it’s almost impossible.
Not quite impossible, though. If one assumes that even against Kasparov there is
some line of play that will defeat him (after all, he does sometimes lose), then the
odds of stumbling into that line are around 3050 (assuming about thirty choices per
move, with a game lasting around fifty moves). But to win the New York State lottery,
you need to pick six numbers, each 1–59, so that’s about 606. So your odds of winning
5. The interested reader might look at Bewersdorff’s Luck, Logic, and White Lies, chap. 8, for a
gentle introduction, and at Knuth’s Art of Computer Programming, vol. 2, section 3.5, “What Is a
Random Sequence?”, for a much more intense treatment.
6. This remark may seem counterintuitive to some readers. After all, many sports outcomes in
practice may seem to be determined by luck. But any given matchup (be it a tennis match or a
chess match) between equally skilled players will, by definition, be close to 50/50—that is, its
outcome will seem determined by luck. And sports matchups very often involve relatively closely
matched players (indeed, the matchups need to be close due to the lack of luck in sports). To
see that sports are more like chess than backgammon in terms of luck, just ask yourself how
likely a player who learned to play tennis last week is to beat a pro. In chess and tennis, it’s
essentially impossible. In backgammon, it wouldn’t even be surprising.

142

Chapter 5

n times in a row are 606n, which is roughly equal to 3050 when n = 7. In other words,
your odds of beating Kasparov (assuming only that you know enough to make legal
moves; if you know a bit about chess it goes way up) are about the same as your odds
of winning the New York State lottery seven times in a row. It’s interesting to note
that most people would describe the first as “impossible” and the second merely as
“very unlikely.”7
We tend intuitively to think of a game (say in chess) between two beginners as
being “more random” than a game between two experts. If both matchups are even,
then the chances are 50/50, so how can we make sense of this intuition? One way to
think of it is to imagine swooping down early in the game and altering the board
somewhat, say by removing a pawn. The two beginners will probably still be around
50/50, say 55/45 in favor of the player whose opponent lost a pawn. But the game
between the two experts will become significantly more predictable; perhaps it will
now be 70/30 in favor of the expert who is now up a pawn.
In general, games thought of as “hardcore” or “serious” (ones where the typical
player devotes a great deal of time and energy to playing the game and to improving
his skills) tend to have less luck than games thought of as “casual.” Typically this is
because the lack of luck in the game means that the only way to win is by devoting
a great deal of effort to the game, which tends to drive out anyone who doesn’t want
to put in that amount of effort. The causation can run the other way, though: if the
game is being designed (or redesigned) to suit hardcore players, luck will often be
removed from it. More on this below.
Sources of Luck
Randomness arises from a number of sources. The most obvious are overt random
elements—game features that cause the game to move from one state to another in
an unpredictable (to the players) way.8 Dice and cards are random elements that very
clearly add uncertainty to the outcome. In sports, weather, lucky bounces, and similar
effects provide randomness. In computer games, random number generation in prin7. In fact, your odds of beating Kasparov are probably quite a bit higher than what’s computed
here, because with even a little chess knowledge you are playing much better than randomly.
For example, if you had an Elo rating of 1200 (a bright beginner), then given Kasparov’s roughly
2800 rating, Elo predicts your chances as 1 in 10((2800–1200)/400), or 1 in 104. A computation like this
is surely pushing beyond the boundaries of the Elo system’s reliability, and we don’t mean to
present it as authoritative, but it does suggest that 1 in 3050 is a gross underestimate.
8. One might argue that any game, even chess, has random elements in the sense that what
other players will do (and perhaps even what you yourself will do!) is unpredictable to you. But
when we say a game has random elements we mean something beyond this—some more overt
randomizer such as cards or dice. For the more general concept of uncertainty of outcome, we
use the term randomness.

Indeterminacy

143

ciple provides uncertainty of outcome, but in practice there are a very large number
of numbers generated and the differences often tend to wash out—think, for example,
of random damage in an RTS.9
Many games, even those with no other overt random elements, have random elements in the setup. For example, in chess or football one might decide randomly who
goes first. In some multiplayer games, the exact choice of seating is important, and it
may be randomly determined. Also, the identity of one’s opponent may be thought
of as a random setup choice: in a tournament, there are often random pairings, and
poker is a different game if, for example, a table of experts happens randomly to have
one very poor player as well.
Another source of randomness comes from the randomness of von Neumann
games: players making simultaneous choices and then resolving the outcome.10 Rockpaper-scissors unit matchups and fog-of-war11 in an RTS are examples. Note that
although there are no overt random elements involved, these kinds of simultaneous
choices do add uncertainty to the outcome (turn-based rock-paper-scissors, in comparison, has very little uncertainty), so they constitute randomness in our sense of the
word. It is worth mentioning that, in practice, these choices can be made sequentially
as long as the choices aren’t revealed right away—for example, choices of which unit
to build in an RTS (where certain units counter others) tend to work this way.
One last source of randomness arises from human nature itself. Even games like
chess and go that have no overt random elements and no simultaneous choices still
involve human nature, and humans are notoriously unpredictable. Sometimes chance
will arise from one player being more “on” than another that day—perhaps she had
her morning cup of coffee and her opponent did not. Or perhaps a chess player will
choose an opening that, unbeknownst to him, is a particular weak point of an otherwise strong opponent.
Often a human player’s “game-playing algorithm” can be thought of as looking at
different choices, discarding the ones that are noticeably inferior in any way, and then
choosing more or less randomly among the remaining (apparently equally good)
choices. This approach is especially common in games that seem “hard,” in the sense
that there are multiple equally plausible choices, such as chess or “guess the digit of
pi.” Often, as in chess, there is some underlying combinatorial complexity to the game
that makes it difficult to analyze completely. But in fact these various choices may
not all be equally good, and thus luck enters in.
9. See the discussion in section 5.3 on hidden information.
10. See appendix A for more on Von Neumann games and the mathematical theory behind
them.
11. One can think of fog-of-war as a Von Neumann game based on the choice of the first player
to explore a given section of the map, and the second player to explore another section.

144

Chapter 5

Summary: Some Sources of Randomness
Overt random elements
Dice
Cards
Random number generators
Weather
Physics (e.g., ball bounces)
Setup (e.g., choice of opponent, or who goes first)
Von Neumann (simultaneous choices)
Rock-paper-scissors
Fog of war
Movement in an FPS
Units built in an RTS
Human nature (often make random choices out of ignorance)
Guessing from apparently equal options (e.g., in chess)
Pure guesses (e.g., guessing digits of pi)
Beginners playing instead of experts
Politics

Political choices in multiplayer games are highly complex, but in general can be
thought of as falling into this third category.
Costs and Benefits of Randomness
Players, especially more serious or expert players, will often object to random elements
in a game. Some sources of objection, and some negatives to luck that players may
not consciously notice, include:
Skilled players may want to be more often rewarded for their skill—that is, want to
win more often compared to unskilled players.
• Players may wish to feel they are masters of their own fate, perhaps best expressed
by the chess player who, after playing his first game of backgammon, said he was
never playing the game again, because it was a game “where you can not only make
the right move and lose, but lose because of it!” Of course, any game with random
elements has this property. At an extreme, randomness can make players feel their
choices don’t matter.
• People like predictability.
• Random elements can add complexity:
•

Indeterminacy

145

Random elements are additional game features and complex simply for that reason.
Probability is naturally hard for people to understand; we’re not wired to think
probabilistically.12
Luck can make it harder to climb the heuristics tree:
Heuristics involving probability tend to be more complicated.
It’s harder to learn any of the heuristics (even those not directly involving
probability)—if you make a move and lose, was it a bad move, or did you just get
unlucky?
䊊

䊊

•

䊊

䊊

One additional comment on the first item on the list: although players often want
to be rewarded for their skill with a higher victory percentage, in fact skilled players
don’t necessarily win more in games with less luck. Although in a given matchup, the
more skilled player has a better chance of winning the less luck there is in the game,
in practice players tend to play with others at about their own skill level, resulting
in a roughly 50/50 win chance even for skilled players. Moreover, in games with very
little luck, the less skilled players are often driven out (one sees this in online FPS
and RTS games, for example), and the skilled players are left playing each other. Of
course, if you have a fixed pool of opponents, it is to your advantage to gain skill
more quickly than others in your pool, and the less luck the game has, the more
rewarding it will be for you. For online games, though, that fixed pool typically does
not exist.13
But adding more luck to a game has many benefits as well. These benefits tend to
be much appreciated subconsciously (many games that have stood the test of time
have a great deal of luck in them), but not always consciously, so that deliberately
designed games do not always take full advantage of the good things luck has to offer.
Given the less obvious nature of the benefits, we will examine them in some detail.
Some of the benefits of luck are
•
•
•
•
•
•

Increased range of competition
Ego crutch: something to blame losses on
Increased variety of gameplay
Catch-up mechanism
Control of calculation
Additional psychological interest to outcomes

12. See, for example, Kahneman, Slovic, and Tversky, Judgment under Uncertainty, chap. 1 and
throughout.
13. Note that a solid automatic matchmaking system makes the problem of not being rewarded
for skill worse: everyone is being matched with players of equivalent skill, and thus each player’s
chance of winning is pushed toward 50/50. On balance, it is still an extremely good thing to
have, though; it creates better matches (both players have a chance to win) and without it the
bottom tends to drop out entirely in high-skill, low-luck games.

146

Chapter 5

Range of Competition
If a game has very little luck, it’s much harder to find a good matchup. You won’t
have much fun playing chess against Kasparov unless you yourself are an extremely
good chess player—indeed, the range of chess players with whom you can have a
reasonable game (in the sense that both people have a decent chance to win) is quite
narrow. But you could play backgammon or cribbage against a wide range of people.
Even if they were a lot better than you, you would win at least some of the time.
Note that increased range of competition is an advantage in several ways. If you
bump into a random person and play with them (whether informally, or at a tournament), you’re more likely to have a good game. Perhaps more important, if you want
to play with a specific person you already know (a friend or spouse, perhaps) you are
both more likely to have a good experience.
Increased range of competition is extremely important for games requiring physical
presence, because of the more limited choice of opponents—you can play cards with
your spouse, but you will probably have to go to the club to find a chess opponent.
Again, this is not because there is less skill in cards, but because there is less luck
in chess. With a very large pool of potential opponents and a good matching system
(a large tournament or online14), the need for a large range of competition in a game
is less pressing. But it is still a valuable asset for a game—people may want to play
in other environments, such as with a group of friends, and no matching system
is perfect.
Ego Crutch
It is a natural human tendency to take credit for our wins and blame the fates for our
losses. In a game with overt random elements, it is easier to do that. In chess, you can
hardly say you lost to Kasparov due to bad luck. In backgammon, you can say you
would have beaten the world champion, if you just hadn’t made that terrible roll at
the end (conveniently forgetting all the terrible rolls he made, or the terrific rolls you
made, earlier in the game).
Also, players with a more casual attitude can feel easier about experimenting with
different playstyles or tactics. After all, it’s not as if they’re expected to win every time.
Variety of Gameplay
Luck causes odd situations to come up during the course of the game, situations that
might not occur in a game where the gameplay state is due to the conscious choices
14. Online matching isn’t always great, but the best systems are pretty good, and the potential
is clearly there. The old-school system of “list of games, pick one to join” is a disaster in terms
of getting a reasonable game (where it works, it is typically because the less skilled part of the
community has simply been cut out, leaving players of similar skills), but it is thankfully becoming less and less common.

Indeterminacy

147

of the players with little intervention from random elements. Dealing with these odd
gameplay states (typically by applying more general heuristics) is often more interesting than becoming ever more expert at a very narrow set of gameplay states (typically
by memorizing patterns that have been worked out in advance). Fischer Random
Chess (Chess 960)15 is just one example of using randomness to solve this problem of
stagnation in play.
Luck also increases the number of situations where a good player may have to
struggle to come from behind, or a bad player may need to play steadily to have the
best chance of maintaining a likely win. Play in these situations tends to be different
from normal play in interesting ways. One sees this, for example, in bridge, where
one takes risks to make an unlikely contract or plays conservatively to bring home an
easy contract.16
And of course anything that increases the variety of gameplay tends to increase the
replayability of the game. So additional randomness increases replayability. A classic
example is the replayability of NetHack and Diablo due to their randomized dungeons
and items.
Catch-Up
As discussed in section 4.2, random elements can provide a kind of catch-up feature,
without some of the disadvantages other catch-up features can have.
Control of Calculation
Games with more randomness often (although not always) have less pressure for
players to perform difficult calculations, such as the detailed reading out of moves in
chess or go. We discuss this further in section 5.3 on hidden information and section
6.5 on reward/effort ratio.
Add Interest to Outcomes
Random elements often galvanize player interest. Players become excited to see how
the event will turn out. A typical example is the focus all players at a D&D table have
on an important roll to hit in a difficult battle. Late in a Monopoly game, there is a
15. A chess variant invented by Bobby Fischer, where the starting positions of the pieces are
chosen randomly.
16. Playing aggressively when behind or conservatively when ahead is a general phenomenon—
it happens all the time in chess and go, for example. Randomness simply means it can happen
more often, and (in an uneven matchup) it can happen to the player one would not expect it
to happen to. One can think of this advantage of randomness as a special case of the range-ofcompetition advantage—randomness allows an uneven matchup to have the same variety an
even matchup would have.

148

Chapter 5

great deal of interest in a player’s roll, as the other players look to see if he will land
on their property and pay them a great deal of money.
Player Acceptance of Randomness
Since the benefits of randomness are less clear than the costs, players may not be that
accepting of it. This is especially true of highly enfranchised players, say in a game
that is a sequel or more generally a game that is in an established genre. There is
certainly a place for the low-luck game (although historically it has tended to be a
small niche, at least in the case of boardgames and card games17—the intensity of
chess does not appeal to everyone). But for designers who want to take advantage of
what randomness has to offer, it’s worth looking at what tends to make it more or
less palatable.
The most important factor in acceptance of randomness is the nature of the player
base. More expert players tend to dislike random elements because they make them
lose; less expert players tend to like them because they help them win. Of course, over
time a game will tend to attract a player base that fits it, so a game like chess or Quake
will have a high proportion of very serious players (the more casual ones having been
driven out by their high rate of losing), and games with more randomness (like poker
or Parcheesi) will have more casual players. If you make a new game in an existing
genre, it is very hard to overcome players’ expectations. If you add randomness to
such a game, players who already like the genre will usually not be pleased (they are
experts who want to demonstrate their skill as much as possible, and they are an
audience already selected for not liking luck). The new players you might want to
acquire are unlikely even to try the game (they have already made up their minds that
this genre is not for them). All this goes double for a sequel to an existing game.
There is some evidence that individual games and game genres evolve so as to
reduce luck, perhaps due to the pressure of their more serious players. The existence
of the dummy in bridge (a feature not found in whist, from which bridge evolved),
for example, serves to reduce luck. Even chess once had dice.18 If casual players,
however, prefer games with more luck, it may be that expert players are pushing games
to evolve in a direction that makes fewer people want to play them, somewhat like
the proverbial peacock’s tail.19
17. At present, computer games have tended on balance to be more low-luck, like sports, rather
than high-luck, like most boardgames and card games. It’s interesting to speculate if that’s
because computer games really do have more in common with sports (so that being low-luck is
perhaps “natural” for them), or if it’s because computer games are deliberately designed, and
designers, being generally expert players, tend to prefer games with low luck.
18. Parlett, A History of Card Games, 13.
19. More generally, see the discussion of “grognard capture” in the section “Excessively Increasing Costs” in chapter 6.

Indeterminacy

149

Game designers in particular tend to be fairly serious players, so they are often
inclined to remove luck from games rather than to add it. It is important for designers to be conscious of this tendency so that they can add luck when the situation
calls for it. Computer games in particular tend to suffer from this tendency to shortchange randomness. Boardgames and card games usually fare better here, whether
because of a greater appreciation of the advantages of randomness or simply because
the traditional mechanics of the genre include random elements (rolling dice, shuffling cards).
When a new genre is created, or when an existing genre is ported to a new platform,
the audience is more fluid, and adding randomness can be more acceptable. On
balance there are probably more players who enjoy games with random elements than
who enjoy games without them, so it is certainly worth considering whether extra
randomness is appropriate.
Player expectations and the conventions of the genre are the main factors that
influence player acceptance of randomness. But there are some other factors as well.
Players who dislike overt random elements like dice and cards will often accept von
Neumann–style randomness. Indeed, many will not even perceive it as random, since
it stems entirely from choices that they or their opponent have made.20
When a game does have overt random elements, it is often best if they are frontloaded. Players may enjoy being dealt a hand and then figuring out how to play it
more than they enjoy arranging a complex attack and then rolling the dice to see if
their plan succeeded or failed.21 If it gets to the point where the entire game feels
predetermined fairly early on, though (e.g., if the outcome of an RTS match is determined by the initial choice of races), it will be too much for most players unless the
game is very short.
All this said, many players are quite happy to have luck in their games. Although
it may be appreciated more by casual players, it brings expert players many benefits
as well, particularly in terms of a larger pool of opponents and increased variety of
play. The main cost they must accept is that they will sometimes lose to players worse
than themselves. They may still win just as often overall, simply because they will
20. And indeed although there is much randomness in, say, rock-paper-scissors, there is also
some potential to predict one’s opponent. Furthermore, many games with Von Neumann randomness offer ways to get around it, such as scouting in an RTS.
21. Random damage in an RTS might seem to be an acceptable mechanic that violates this rule,
but keep in mind that the randomness in this case is very slight. The outcome of most RTS battles
is at least 99 percent determined by the preparation and in-battle management of the players,
as opposed to random number generation during the battle. A better example might be a paper
RPG battle, where a great deal can hinge on the roll of the dice, but again there are many die
rolls, and if one plan fails it is expected that the players will come up with a new one—the failure
rarely represents a permanent defeat.

150

Chapter 5

more often encounter players worse than themselves—players who would not even
play them if the game had very little luck.
Team Fortress 2 is an interesting case of applying luck to a game. After reading an
article22 covering much of the material above, the development team decided to add
some wild critical hits to the game and see how it went. Their goal was to broaden
the appeal beyond niche players. After a couple weeks they had glowing reviews from
the playtesters, who couldn’t put their fingers on why the game seemed so much more
fun. At that point the developers became committed to having luck injected into play
through critical hits. Once the extent of the critical hit system was understood,
however, the hardcore players had many complaints. Two years after the product’s
release, the development team still considers the addition of critical hits a success.23
Exercise 5.1: Pick a low-luck game. What sources of luck does it still have? How can
you tell it is nevertheless a low-luck game?
Exercise 5.2: Choose a high-luck game. What sources of luck does it have? How can
you tell it is a high-luck game?
Exercise 5.3: Estimate the chances of achieving perfect play in checkers by moving
randomly.
Exercise 5.4:
randomly.

Estimate the chances of achieving perfect play in tic-tac-toe by moving

Exercise 5.5: Think of a game you like to play. What is its biggest source of luck?
Would you remove or reduce that source of luck if you could? How?
Exercise 5.6: In general, card games tend to have a lot of luck. Boardgames may have
very large or very small amounts of luck. Sports and computer games tend to have
relatively little. Why?
5.2

Characteristic: Luck and Skill

People often speak of luck and skill as if they were opposites of each other. And indeed
in the case of individual events they can be: one can speak of some success, such as
catching a ball, as being due either to luck or else to skill (although it is more often
due to some combination). But when looking at a game as a whole, the two concepts
are independent (or, as a mathematician might say, orthogonal): a game can have a
large or small amount of skill, and it can have a large or small amount of luck. Knowing
the amount of luck there is in a game tells you nothing about the amount of skill, and
knowing the amount of skill in a game tells you nothing about the amount of luck.
22. Garfield, “Getting Lucky.”
23. Chris Green, Valve Software, personal communication.

Indeterminacy

Figure 5.2
©iStockphoto.com/iofoto

151

152

Chapter 5

Table 5.1
Game

Amount of luck

Amount of skill

Poker
Chess
Tic-tac-toe
Slots

High
Low
Low
High

High
High
Low
Low

For example, poker and chess both have a lot of skill, even though poker has much
more luck than chess. Tic-tac-toe and slot machines both have very little skill, even
though the former has essentially no luck and the latter is essentially all luck.
For another example, consider “die-rolling chess”: Two people play a game of
chess (replaying draws). Then a die is rolled; 1–2 means the first player wins, 3–4
means the second player wins, and 5–6 means the winner of the chess game wins.
This game has all the skill of regular chess—every book written about regular chess
still applies to die-rolling chess—but it certainly has more luck. In fact, this game
would likely have the same world champion as regular chess—after all, he would still
have a higher win percentage against everyone than the second best player would.
However, because of the noise in the system, more matches would need to be played
before the rank order of chess players coalesced to (roughly) the same ordering as in
regular chess. What, then, is the relationship between luck and skill? The short
answer is that luck decreases, not skill, but the returns to skill. In this section we
explore that relationship.
Returns to Skill
If there’s a lot of luck in a game, then the best player may not always win. The more
a skilled player can win at a game, the higher returns to skill we say that game has.
So returns to skill is naturally enough a function of both skill itself and luck.
Unlike skill alone or luck alone, there is a relatively simple way to measure returns
to skill: the “skill chain.” Consider the set of all people who play the game (in particular, these are all people who can play correctly according to the rules). Choose one of
them, and then choose another one who beats that one 60 percent (say) of the time.
Then choose another player who beats that person 60 percent of the time, and so on,
until you’ve reached the best players in the world. Go in the opposite direction as
well, finding a person that your original player defeats 60 percent of the time, and so
on. Now you have a long chain of players, each beating the next. What does the
length of that chain measure?
At first glance it measures skill. Certainly the players higher up on the chain are
better than those lower down. But think again of die-rolling chess: if you beat me 60
percent of the time at regular chess, then at die-rolling chess you only beat me 53

Indeterminacy

153

Better
A
A beats B
60% of the time.
B
B beats C
60% of the time.
C
C beats D
60% of the time.
D
D beats E
60% of the time.
Worse

E

Figure 5.3
The skill chain

percent of the time, even though there is the same amount of skill in each game. In
fact, what the length of the skill chain is measuring is return to skill: how much a
player can hope to leverage whatever skills she may have in order to achieve victory.
Exercise 5.7: Check that winning 60 percent of the time at regular chess means
winning 53 percent of the time at die-rolling chess.
The skill chain may be short because there is not much to the game: tic-tac-toe
has no luck, but it would be hard to find a dozen adults, each of whom had a 60
percent chance of beating the next. Or the chain might be short because of luck: a
two-player card game might have a lot of skill, but the luck of the deal could mean
that even a very skillful player didn’t win 60 percent of the time against an average
opponent.
A game like chess, with a lot of skill and very little luck, will have a long skill chain.
And indeed given a good set of match results (one that covers a large number of games
from players at all skill levels), one can actually compute the skill chain. The Elo player
rating system is precisely a measurement of any player’s chance of beating any other.
(This system is used in many games, but most famously in chess—see Elo’s The Rating
of Chess Players Past and Present for more details. Chess currently utilizes a modified
version of the system.) Given a set of Elo ratings, the chance for one player to beat
another is directly based on the difference in ratings. More precisely, if D is the

154

Chapter 5

difference in ratings between two players, Elo tells us that the chance for the stronger
player to win is
1/(1 + 10(–D/400)).
Setting that equal to 0.6 and solving for D, we find the players are roughly 70
Elo points apart.24 In chess, nobody keeps Elo ratings for the worst players (a bright
beginner is considered to have an Elo of roughly 1000), but if we guess that the scale
goes down to about 700, and up to about 2800, we find the skill chain has length
around 30.
In die-rolling chess, for comparison, one needs to win 80 percent of the time at
regular chess (a difference of about 240 Elo points) to win 60 percent of the time at
die-rolling chess. So the skill chain for die-rolling chess has length about 10. The
amount of skill hasn’t changed, but the rewards you get (in terms of winning) in return
for your skill have gone down, because of the addition of luck to the game. And the
skill chain’s length decrease from 30 to 10 reflects this.
It is possible to partially correct the Elo ratings for the randomness of die-rolling
chess. One can see this intuitively by realizing that the current world champion would
still be the world champion even under die-rolling chess or that player A will still be
better than player B despite adding the die roll if he was better before. If the Elo system
were modified so that the number of points awarded to the winner (and subtracted
from the loser) was based not on their true Elo ratings (which gives their actual chances
to win), but on a modified one where the point difference was equivalent to their
chances to win without the die roll (a simple calculation for every ratings differential),
then you would recover the full rating scale from before. This works for the simple
die-rolling chess because the effect of the overt randomness on win percentage is so
transparent. In a way it is differentiating “skill chain” from “winning percentage
chain” or more precisely “skill chain with die roll” from “skill chain without die roll.”
This gives a clear example of the fact that there is no cure-all rating system, and
systems can be tailored to specific games. This tailoring is quite common in the world
of professional sports. Analogously to the comments on standards, crafting new types
of ratings can be a burden for players to understand, and the costs and benefits must
be weighed individually.
Exercise 5.8:
a. Compute that 240 Elo points difference gives an 80 percent win chance at regular
chess.
b. Compute that winning 80 percent of the time at regular chess means winning 60
percent of the time at die-rolling chess.
24. See section 8.43 of Arpad E. Elo, The Rating of Chess Players Past and Present, 1978, which has
recently (2008) been reprinted by Ishi Press International.

Indeterminacy

155

Skill Is Agential
Implicit in this point of view is the idea that skill is agential. Skill is something that
a community of players has more or less of. It is not something inherent in abstract
properties of the game itself (although it is certainly influenced by those properties),
like the number of options at each stage or overall size of the abstract game tree. For
example, there may be a great deal that could be brought to bear in “guess the digit
of pi” (facts about pi and the various infinite series one uses to compute it, perhaps),
but the skill chain for (unaided) human players is length 1: nobody can beat anyone
else 60 percent of the time.
Two related thought experiments may further illuminate the agential nature of skill
and the skill tree. Imagine that, on the planet of geniuses, the very brilliant beings
there see the entire game tree of chess. Perhaps they show chess to very young children
(as we do tic-tac-toe), but at least for adults, there’s not much to the game: they play
perfectly, knowing the game is a win for white, perhaps, and their skill chain has
length 1. Meanwhile, on the planet of morons, the very stupid beings there play tictac-toe as their favorite game. They have great tic-tac-toe tournaments and write books
of tic-tac-toe strategy. Their skill chain for tic-tac-toe is quite long—certainly their
tic-tac-toe amateurs, even the very good ones, have little hope of beating a true tictac-toe professional!
These two hypothetical planets should not be taken too seriously, especially the
second—it is not clear there is enough going on in tic-tac-toe to support that many
distinct levels of skill, even among very stupid beings. But for games like Nim where
the strategy is not immediately obvious, but the game can in fact be “solved,” a given
community of players can essentially make a transition from the planet of morons to
the planet of geniuses as they learn the game’s strategy. With the recent solving of
the game of checkers, our own planet has undergone a similar transition, at least if
one allows artificially assisted play.
In general, increasing knowledge within a community can either increase or
decrease the skill chain. If more is learned, but only by a subset of the community,
that gives more different available skill levels. Something like this has arguably happened to chess and go over time.25 One also sees expansion of the skill chain when a
new RTS, for example, is released, and the players start to separate as they learn the
game. Early on, a middling player can be matched up against a random player and
have a decent chance of winning; later on, as skills start to diverge, random pairings
are more likely to lead to very one-sided games. Although the overall skill chain has
25. There is some evidence of this in famous go games such as that of Yara no Satanoshi versus
Honinbo Dochi (or more to the point, Satanoshi versus one of Honinbo’s students), where a top
player from a distant province came to the capital only to discover that go had evolved far past
what he knew (Ohira, Appreciating Famous Games, Game 2).

156

Chapter 5

increased, it’s questionable whether the skill chain of the active players has increased,
or whether so much of the bottom of the skill chain has dropped out that the length
has stayed the same or even shrunk.
Occasionally, however, increasing knowledge can collapse the skill chain. This
certainly happens when a game like tic-tac-toe or Nim is “solved.” In principle, it can
also happen in nonsolved games if some powerful and relatively easy-to-learn set of
heuristics spreads throughout the community. It could well be that greater knowledge
of chess openings or the relative value of pieces had a contracting effect on the skill
chain (but it’s also certainly arguable, especially in the former case, that the net effect
was expansive).
Measuring Luck
Luck, unfortunately, is less easy to measure than applicable skill (measuring pure skill
directly seems hardest of all). One approach is to look at how often the worst player
beats the best player: the more often that happens, the greater the luck in the game.
Given that the very ends of the skill chain are problematic, and especially the lower
end (how low can you go before you don’t want to count someone at all?), it might
be best to compare, say, the 25th percentile and 75th percentile players. However, this
is an agential measurement. If hardly anyone plays the game, the 25th and 75th percentile players might be quite close in skill, and thus be fairly evenly matched, giving
a low measure of luck; as player skills increase, the skills spread, and the luck measured
in this way goes down. Another problem is that for actual data sets, there may not be
a lot of good data for players spread that far apart. And if the amount of luck in the
game is low, one may be trying to distinguish between various extremely low win
rates where statistical noise may drown out the signal (how many games of chess
would one need to look at to get a good read on how often a weak player could defeat
Kasparov?). Perhaps a better approach is to look at chains of three players, say A, B,
and C, each beating the other 60 percent of the time, and ask how often A beats C;
the more luck there is in the game, the better chance C should have.
Roughly speaking,26 though, we know that
Applicable skill = skill – luck.
Given that one can numerically measure applicable skill (with the skill chain) and
luck (perhaps with some measure of bad players beating good ones, although it’s not
clear which measure would be best), one could hope to compute the actual amount
26. Very roughly. In particular, we’re not saying you can really find numbers and add or subtract
to get the other numbers; it might just as well be division, square roots, or some other more
complex function. More precisely, applicable skill is a function of both skill and luck, and tends
to increase as skill increases, and decrease as luck increases.

Indeterminacy

157

of skill in the game (i.e., the amount of brainpower—or physical prowess—the players
are bringing to the game) from the other two measures. Then one could hope to
answer reasonably questions such as “Is there as much skill in poker as there is in
chess?” that have been the topic of much debate. However, it’s not obvious how best
to proceed.
Skill and Longer Game Sessions
When one wishes to know which of two players is more skillful, one typically has
them play a series of games rather than a single game. That’s because if the better
player has, say, a 60 percent chance to win a single game, there is still a 40 percent
chance that the inferior player will win and be judged the victor. But the chance that
the inferior player wins two out of three games is less, and for three out of five still
less.
Exercise 5.9: If the better player has a 60 percent chance to win one game, how likely
is she to win best two out of three? Best three out of five?
Exercise 5.10: How many games must be played to ensure the better player has at
least a 90 percent chance to win?
But if we are thinking of games in terms of how much skill is required to play
them, there is nothing magic about a single game. Why compare one game rather
than best two out of three? Going in the other direction, for games like basketball
or tennis, one could compare atoms—possessions or games in a tennis match—just
as well as full games. And for games like poker, it’s very unclear what the right
measure is. A single atom (hand)? A session (evening of play)? How long a session?
Ultimately, then, the real measure is skill per unit of time. If one wishes to compare
the skill of two different games, one should first pick a unit of time long enough to
allow some measurable amount of play in each of the games (i.e., for which one can
measure some number of wins and losses in that time period, and declare the winner
of the time period to be the player with the majority of the wins). For example, if
one game takes three minutes and the other takes five, one could choose fifteen
minutes as the time period and look at best out of five for the first game and best
out of three for the second. Then one can compute the skill tree length, chance of
a bad player beating a good one, and any other related information, all based on
that time period.
Another way to say all this is to note that one can make a skill chain to be as long
as one likes simply by allowing players to play for long periods of time (thereby making
two players who would otherwise have a 51 percent difference in skill instead have a
60 percent difference). So to keep things meaningful one has to disallow that, or
correct for it by using a standard amount of time for a particular match.

158

Chapter 5

Gaining Skill over Time
Players often wish to improve their skill at a game over time. One might think of this
roughly as how many hours of study or practice it takes for a player to gain 100 Elo
points. Of course, the more luck in the game, the less the return to skill, so the harder
it will be to gain those Elo points. Other factors enter the picture as well: if the game
is utterly incomprehensible, like “guess the digit of pi,” it will be hard to gain skill.27
In addition to systemic factors like luck and comprehensibility, there are agential
factors. If the player community is weak (maybe the game has just been released), the
Elo points per hour of studying will tend to be very good. Good tools, such as strong
players to play with, teachers to study under, strategy books, or libraries of famous
games, can all increase one’s rate of skill growth. We’ll have more to say about the
returns players get for their efforts in section 6.1 on costs and section 6.5 on reward/
effort ratio.
Returns to Skill: Luck vs. Politics
The astute reader may have noticed that, although we have described luck as causing
a decrease in return to skill, we have made much the same claim about politics (see
section 2.3). How are politics and luck similar and how are they different?
Partly it is the other effects of luck and of politics. For example, luck tends to
increase play variety, whereas politics decreases it. As another example, the psychological negatives behind the “gang-up” behavior often found in political games might
strike many players as less appealing than the vicissitudes of fortune found in games
with luck. Just looking at the change in returns to skill itself, however, there is often
a significant difference between luck and politics: luck tends to gradually decrease
returns to skill, whereas politics more often reaches a point where it completely cuts
it off any return to skill. This is perhaps because the effects of politics sometimes
require advanced heuristics before the essential game is revealed. It would be far less
common to have a situation where luck would at some point give zero return to skill
without having this be immediately recognized. Recall our examples of die-rolling
chess (where your chess skill still helped, albeit less than in regular chess) and chiptaking chess (where your chess skill didn’t help you in the slightest).
In pictures, we have the curve in figure 5.4.
Your return to skill goes gradually down as more and more randomness is added
to the game (figure 5.4).
27. It has been argued that Othello suffers from this to some extent: the flipping nature of the
pieces makes it hard for humans to visualize (see Norvig’s excellent Paradigms of Artificial Intelligence Programming for a discussion and a short program that nevertheless plays Othello well).
And indeed computers are better than humans at Othello (although difficulty in human visualization is not the only reason; the relatively small size of the game tree means minimax, a strategy
computers excel at, works better as well).

159

Return to skill

Indeterminacy

Randomness

Return to skill

Figure 5.4
Adding randomness to a game

Politics
Figure 5.5
Adding politics to a game

160

Chapter 5

With enough politics in the game, your skill (again, excepting political skill) doesn’t
help you at all. If you were to add enough luck to a game that return to skill got zeroed
out, it is likely there would be no interesting beginning part to the curve.
This difference is an important one: in the first case, the player always has at least
some incentive to improve and to learn more about the game. In the second, if the
level of politics is great enough, there are no rewards at all for the player’s further
study of the game.
It’s perhaps also worth mentioning that the simple fact of returns to skill declining
is not by itself terrible—it is actually all but inevitable, even in a game of “pure skill.”
Players will tend to learn the most productive heuristics first, and gradually add more
and more esoteric heuristics that yield ever smaller benefits, with the end result that
almost all games give smaller rewards, in terms of increased win chances, for the
thousandth hour of study than for the first hour. More on this in section 6.5.
Is Poker a Game of Skill?
People often argue whether a given game is a game of skill or a game of luck. If the
game in question is a gambling game (gambling in the sense that it is commonly
played for money, not in the sense that it has any particular amount of luck in it),
the argument is even more frequent, sometimes taking place in the courts. By way of
wrapping things up, let’s take a look at this common question in the case of poker.
The simple answer is that poker has both luck and skill in it. But it’s better to note
that the question has in it a subtle but incorrect assumption: that luck and skill are
somehow opposed. The fact that poker has a lot of luck in no way decreases its skill.
The fact that it has a lot of skill in no way decreases its luck. Poker has a great deal
of both luck and skill.
The luck in poker means that a highly skilled player may not defeat a less skilled
player in any given hand. But over the course of many hands, eventually the skilled
player will tend to win out. One could hope to measure the amount of luck by seeing
how often the less skilled player did manage to win. All these measurements are best
made on a per-hour basis, at least if one hopes to compare the skill and luck involved
in poker with that of another game. One might even dream of comparing the skill in
poker with the skill in chess, but that would require some way of “subtracting out”
the luck buried in the skill chain for poker—since the length of poker’s skill chain,
like that of any game’s, combines both luck and skill together in a single measurement
of applicable skill.
In any case, the rewards a skilled player can get for her skill are lessened by the luck
in poker, even though the skill itself is not.
Exercise 5.11: Assume that a round of head-to-head elimination poker between two
players lasts an average of twenty minutes. If Player A wins two-thirds of the time
versus Player B, how long would two players need to play (i.e., how long would a

Indeterminacy

161

match have to last) in order for Player A to have an Elo rating 300 points higher than
player B?
Exercise 5.12: Consider the following alternate version of die-rolling chess: each
player rolls a die, highest roller wins, and only the ties are settled with games of chess
(for simplicity, assume the chess games never result in a tie). What would the highest
Elo rating be in this form of die-rolling chess? What would the skill chain look like
compared to regular chess?
Exercise 5.13: If the luck in poker decreases the return to skill, why do skilled people
who wish to make money through gaming nevertheless play poker? Why don’t they
play some game that has less luck?
5.3

Characteristic: Hidden Information

Types of Hidden Information
Many games contain hidden information: things about the game state that are not
known to all players. (The contrasting term is public information: things that are known
to all players.) For our purposes, hidden information falls into at least three rough
(nonexclusive) categories:
1. Private information (e.g., a card I hold that you can’t see, or a portion of an RTS map
that is fogged out to you but not to me)
2. “Puzzlelike” hidden information (e.g., what damage type the boss is weak to)
3. Randomness (any of the sources of randomness as discussed above)
Because some of the above are not generally thought of as hidden information,
let’s briefly discuss each in turn.
Private Information
This is what most people commonly think of as hidden information. One player sees
it, another does not. Note that for the information to be private, it can’t be generated
in a completely obvious and deterministic fashion (or both players would know it),
so it is usually generated by some sort of random process. A card that I draw from a
deck and put into my hand without showing it to you is hidden information; so is a
Mario Kart power-up I drive over.28
“Puzzlelike” Hidden Information
Sometimes the game has information that the player does not know, and part (or
all) of the game is figuring out this hidden information, based on some mixture of
28. Unless we are both playing Mario Kart from the same screen, and you are particularly
attentive.

162

Figure 5.6
©iStockphoto.com/Alexander Garaev

Chapter 5

Indeterminacy

163

experimentation and clues provided by the game. The crossword puzzle is a model
example, but many one and a half player games like Super Mario Brothers have hidden
elements in them, and some single-player games, such as Myst, are almost entirely
made up of this kind of gameplay.29
Indeed, discovering how to play the game is such an essential part of any game
that the line between hidden information and simple knowledge of the game can
become quite blurry. When one thinks of all the knowledge it takes to play World of
