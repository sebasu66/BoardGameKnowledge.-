to know for the game to take place, but the player may not need to know them (of
course, expert players often will know them).
Examples of first-order rules are how the pieces move in chess, that you score a
point in soccer by kicking the ball into the opposing net, or that you die in Diablo II
if your health goes to zero. Examples of second-order rules are the precise punishments
for various rule violations in a chess tournament, the finer details of the offside rules
in soccer, or how precisely different items that increase your attack speed in Diablo II
stack. Classic boardgames and card games tend to have relatively few second-order
rules, especially if formal tournament play is not considered (for example, Othello
arguably has no second-order rules). This is almost a requirement for such games,
given that they are so often not formally adjudicated. Sports tend to have more, with
referees responsible for knowing them. Computer games have enormous numbers of
second-order rules, adjudicated by the computer. Very often no one human being
knows all the second-order rules for a computer game; only the code itself is completely authoritative.2
One way to see the difference between first-order rules and second-order rules is to
imagine you are teaching someone how to play. In very few games would you want
to teach someone all the rules initially. Typically you only want to teach them the
first-order rules. And players often learn some basic heuristics before they learn secondorder rules—for example, a beginning chess player might know the point values of
the pieces but not be quite clear on en passant capture.
Some first-order rules for very complex games are slightly less important than most.
In some games there are rules players have to know that come up rarely enough that
in practice players are content merely to have access to them. Examples include parts
of the rules in Starfleet Battles or the text on all the trading cards in Magic. Even the
options in RoboRally form part of this rules space. While the player does not have to
know them to begin play, they will come up and once they do, knowledge of them
is required to proceed. Thus the burden on the player is somewhere in between most
first- and second-order rules.
2. In the case of a bug, one could argue whether the “real” rule was the one actually implemented
by the code, or the one intended by the designer.

Infrastructure

75

Rules as a Barrier to Play
In general, rules are a bad thing in the sense that one would like to achieve the same
gameplay results with fewer rules rather than more. Of course, this is not always possible. Too many first-order rules is especially bad: since every player needs to know
them to start playing, they provide a real barrier to entry. Second-order rules are not
as bad, although they are still pretty bad in games where you expect the players to
adjudicate.
Expert players, including game designers, tend to misjudge how ordinary players
interact with rules, and in particular with the learning of rules for a new game. Seeing
new paper games being blind-tested3 (rulebook and components handed to players
who know nothing of the game and attempt to learn it from them) is a very sobering
experience. Players typically do not want to read rulebooks, and very few people are
good at learning how to play from written rules longer than a page. Most players learn
from other people. This puts classic games, where there is a pool of people who already
know the game, at a big advantage over newer ones. Computer games also have a
huge edge here: because the computer adjudicates the rules, players can begin play
knowing very little, and learn as they go. In particular, for most computer games little
or no time must be spent reading or otherwise preparing to play before actual play
begins.
Even for computer games, though, complex rules can be a barrier to learning or
enjoying play. Computer adjudication (especially of second-order rules) takes a lot of
the burden off the player, but a beginner can still feel lost if he does not understand
what he needs to do to progress. And an expert player can become frustrated if it is
impossible to figure out the details of the system in her efforts to play better (i.e., a
lack of clarity in the second-order rules can make it hard for the expert player to keep
climbing the heuristic tree). In single-player games, clarity of rules is especially important in those rules that apply to the players; sometimes a little more obscurity can be
accepted in rules applying only to nonplayer parts of the system (for example, in an
RPG a player will demand a more detailed understanding of how to build her own
character, but may be willing to accept a more rudimentary understanding of how a
typical AI monster is built, and may hardly care at all about rules restricting the kinds
of level layouts that are possible).
3. The phrase “focus group” is also used, but this covers a wide variety of methods, and is most
typically used to refer to a discussion group led by a moderator. In a blind test, nobody is in the
room but the players themselves. The term blind test is perhaps unfortunate, because it’s easily
confused with the single-blind and double-blind methods of scientific testing, but it seems to be
the most commonly used term for this type of rule testing in the paper game world. Beta testing
for computer games is in some ways analogous, but it doesn’t test the clarity of the written rules
(which are of limited relevance for computer games in any case).

76

Chapter 3

One danger to watch out for when designing or modifying a game is the impulse
to fix things (problems in the other characteristics) by adding rules. Sometimes adding
rules is unavoidable, but in general it’s better to look for other fixes. Repeated little
extra bits of rules, each added to fix a different problem, can add up to a quite messy
game. Again, adding first-order rules is worse than adding second-order ones, and the
more players (rather than referees or computers) must adjudicate, the worse adding
rules becomes.
Counterintuitively, making a rule against some behavior and giving it an in-game
penalty can in some sense legalize it. A delay of game call in football or kicking in
basketball are activities against the rules, and yet commonly used in play. The rules
in actuality are not “don’t do x” but rather “when you do x, y happens.” This distinction is important and has implications when designing rule systems. For example, the
introduction of a rule that forces a move after a certain amount of time has passed
could be intended to speed up a game. Instead, however, the rule might lead to players
using all of that allowed clock time, thus actually increasing the average time it takes
to play a game. The normal agential pressure that would be exerted in speeding up
casual play can be short-circuited by a poorly thought out rule intended to have the
same effect.
Exercise 3.1:

Name some second-order rules in backgammon.

Exercise 3.2:

Name some second-order rules in baseball.

Exercise 3.3: Does the average computer game have more or fewer first-order rules
than the average noncomputer game? Why?
Exercise 3.4: How often do the rules change in computer games? How often do they
change in sports? Compare this to how often they change in boardgames or card
games. Why the differences?
3.2

Characteristic: Standards

Learning new rules is difficult. Learning new heuristics is difficult as well. Games can
get around this by following standards: commonly accepted patterns that many players
are already familiar with.
Some examples include putting a ball into some sort of net to score points, using
the standard fifty-two-card deck in countless card games, having each player take turns
moving a single piece in a boardgame, or using the keys W, A, S, and D to move around
in a first-person shooter. Standards can be low-level details, like the WASD keys, or
high-level ideas—the very idea of a first-person shooter is a standard, just as the turnbased boardgame is.

Infrastructure

77

Figure 3.2

Innovation Considered Harmful
People often decry the use of standards and claim they represent a lack of innovation,
especially when discussing computer games. The large software companies receive a
great deal of criticism on this score. Oddly enough, in paper gaming standards are
better respected—consider, for example, the European boardgames that are by and
large well received4 yet have very strong standards.
But in the end games are for people to enjoy, and most people enjoy games with
which they have a certain comfort level. Innovation is sometimes appreciated, but
convenience always is. So innovation is best saved for areas where it really pulls its
weight—where the innovation improves the game experience in some way. If an
innovation is no better than what it replaces, it can fail to be accepted for two reasons:
first because it is new and thus harder to learn, and second because being new it is
easy for the designer to get the details wrong so that the new feature may well be
unpolished. And when successful games do have innovative elements, they usually
have just one or two; more than that and the game may be too overwhelming for
most people. (On the flipside, there is an audience that deliberately seeks out innovation for its own sake, but this audience is relatively small.)
4. Well received, that is, by the type of elite player who tends to be making the “where’s the
originality?” criticism. We’re not speaking in this case of mass popularity but rather of critical
reception.

78

Chapter 3

Consider Blizzard Entertainment. They are almost universally viewed as one of the
highest-quality producers of computer games in the industry. But their games are not
unusually innovative: Diablo was preceded by other top-down action RPGs, Warcraft
was preceded by Dune II, and World of Warcraft was preceded by Everquest, Ultima
Online, and various MUDs. Blizzard’s greatness comes from understanding what makes
a game enjoyable for its players and from a willingness to put in the level of polish
to achieve that end. Their games stand out because they are better, not because they
are more innovative.
All this is not to say that standards must be respected at all costs. Rather, deciding
how and when to use standards is an important part of the game designer’s art. But
the point is to consider standards as a good thing, to be deviated from when there is
a real gain from doing so, rather than as a bad thing forced on unfortunate designers
by an ignorant public or a cowardly publisher.
When innovation really does add a lot to a game, to the point where it overcomes
any audience resistance to nonstandard games, the payoff can be big. Often the largest
payoff comes not to the first game to exhibit the innovation, but to later ones: Warcraft
rather than Dune II, the Pokémon trading card game rather than Magic: The Gathering,
World of Warcraft rather than Everquest. Given the difficulty of perfecting the innovative elements on the very first try, this is unsurprising.
Bundles of Standards
Standards often come in groups or bundles, usually in accordance with the game’s
genre. Genre is itself a large and complex topic, and not one we want to tackle here.
Instead, we take a naive working view of genre: everyone who plays games is comfortable with the idea that they fall into groups of similar games, such as “trick-taking
card games” or “first-person shooters.” These groupings can be at a very high level—
for example, “boardgames,” “sports,” or “arcade games”—or at a more detailed level,
such as “card games in the whist family” or “real-time strategy games.” Games in
such a grouping, at whatever level, will tend to have certain features in common,
and these common features are standards for those familiar with the group. A few
examples:5
Track boardgames with dice: Senet, The Game of Goose, Monopoly, Parcheesi, The
Game of Life.
Standards: Track with squares, piece(s) to represent the player, progression on a
track according to the throw of dice (or other randomizers).
Note this genre dates back at least 5,000 years (Senet), albeit with throwsticks or
knucklebones instead of dice.
5. This is of course just a sampling—nothing like an exhaustive list, either in terms of genres
covered or in terms of standards listed for the genres, is intended.

Infrastructure

79

Alternating-move two-player boardgames: chess, checkers, go, reversi/Othello.
Standards: Two more or less identical sides of different colors, square grid board,
players take turns moving or placing a single piece, no randomizers, some method
for capturing opponents’ pieces.6
Some of the standards here, such as taking turns, are so ingrained that they
might seem required to someone who is not a student of games. Indeed, it seems
that the standard of taking turns was “broken” fairly late, and for a purpose involving the simulation of reality rather than reasons of pure gameplay: the wargame,
invented in the eighteenth century to train officers in the Prussian army. The
wargame is now a genre of its own, with its own conventions (move all of your
army when it’s your turn, hex-based map, roll dice and look up the results on a
chart, etc.).
Sports races: 100-yard dash, marathon, horse racing, regatta.
Standards: Multiple simultaneous participants, starting line, finish line, starting
signal, measured time to finish.
An interesting example of standards being broken for a specific purpose comes
from the bicycle time trial. In bike racing, drafting (following closely behind another
racer to reduce drag) is such a large factor that simultaneous races are often teambased, with teammates helping each other out, and individual races are often “time
trials”: each rider starting at a separate time and riding against the clock rather than
directly against the other players. The cost of breaking the standard is necessary if
you want the race to measure individual performance.
Team sports with a ball: Football, basketball, soccer, rugby.
Standards: Two sides, team victory rather than individual, point-based scoring, goal
or scoring line, concept of possession of the ball, allowable methods for moving
the ball.
Baseball and similar games are probably best thought of as part of a different (but
related) genre.
Real-time strategy games: Dune II, Warcraft: Orcs & Humans, Command & Conquer, Age
of Empires.
Standards: Real-time play, rough simulation of cities/bases and armies (building
both units and buildings in-game), tech trees, multiple unit types (both economic
and military), multiple building types, rock-paper-scissors relationships among the
unit types, group-selecting units by drawing a mouse box around them, a pulledback overhead view.
6. Note that some of the listed games violate some of the standards—for example, in go or reversi
the pieces are placed rather than moved, and in reversi the pieces (but not how each player uses
them) are identical for each side. This violation of some standards by some members of a category
is the norm (see Lakoff’s Women, Fire, and Dangerous Things).

80

Chapter 3

All these standards existed in Dune II, and they have continued throughout the
life of the genre. Although the standards arguably arose as part of Dune II’s attempt
to simulate a specific intellectual property, they stayed because they fulfilled other
needs, such as pacing and complexity control. A “standard” from Dune II that did
not survive for long (although it can be found in the first Warcraft) was the building
of squares as a foundation for the player’s base: logical from a simulationist point
of view in a world where you are building on sand, but a gameplay annoyance. The
standard of mining resources with peons to build military units works well in matching a Frank Herbert setting rather than any independent simulative principle. Its
general utility in controlling the pace of the game and providing a multifaceted set
of heuristics (namely the interplay between the economy and military) has made it
a standard difficult to replace despite the jarring nature of its simulative qualities
for most settings. This exemplifies the power and utility of standards—other pacing
mechanisms that fit a particular property better may well be easy to find, but they
must be weighed against the fact that following the standard allows players to enjoy
the total experience more by shortening their learning curves. Notably the learning
curve for designers attempting to balance complex games such as this is also
shortened.
Shooter games: Doom, Quake, Half-Life, Tomb Raider.
Standards: First-person (or over-the-shoulder third-person) view, WASD maneuver
keys (if on a PC platform), spacebar to jump, health and ammo bars, different
weapons, possibility of being hit from behind,7 importance of dodging and aiming,
respawning after death.
Occasionally a shooter will try to make a game more immersive by eliminating
UI standards such as health and ammo bars (e.g., Peter Jackson’s King Kong). This can
prove frustrating for players who were expecting such elements.
Card games (fifty-two-card deck): bridge, cribbage, poker, solitaire, hearts.
Standards: The standard fifty-two-card deck itself, shuffling, dealing, hands of cards,
the discard pile. There are many subgenres within this genre, from trick-taking games
(with standards such as bidding, tricks, trumps, and following suit) to poker to solitaire, these latter two really being families of games rather than individual games.
Early decks of cards varied widely, but over time they settled on a number of
standard varieties in use today (besides the fifty-two-card deck used internationally,
many countries have their own versions, with roughly the same structure but
varying numbers of cards).8 However, there has been one interesting drift away from
previous standards: the low card in older games often becomes the high card in
7. That is, a full 360-degree environment as opposed to the shooting on rails common in earlier
games (where your enemies were always in front of you).
8. David Parlett, A History of Card Games, chap. 3.

Infrastructure

81

newer ones. So the ace, once the lowest card, is now the highest card in most games,
and there are a number of games of more recent vintage (e.g., Dai Hin Min or poker
with deuces wild) where the two is high.
In the last hundred years or so, card games with dedicated decks (Pit, Rook, Uno) have
arisen. Sometimes these games had gameplay that really required a new deck, but
often they were minor variants of games that can be played with a standard fifty-twocard deck. The trend toward these nonstandard decks is probably due to some combination of technology (it’s much easier to print a unique deck of cards today) and
financial/legal reasons (if a company makes a unique deck, it has ownership rights
and can charge a premium for its game; it is essentially impossible to profit selling
just the rules for a game to be played with a fifty-two-card deck).
Computer role-playing games: Final Fantasy, Fallout, Knights of the Old Republic,
Baldur’s Gate.
Standards: Player-controlled party of one to eight adventurers, character stats, levels
and experience points, hit points, weapons/armor/equipment, paper doll interface.
Many of these standards are inherited from paper role-playing games (particularly
Dungeons & Dragons). For massively multiplayer online RPGs, additional standards
come into play, such as spawning monsters, respawning after death, and grinding
to level.
Occasionally standards will cross from one genre to another, such as the standard of
hit points. Also, sometimes interesting game features can come from pulling standards
of one genre into a different genre, such as the adoption of turn-based strategy gaming
standards into the real-time strategy game Rise of Nations. And of course occasionally
a game is so successful that its features become standards, either in that game’s existing genre or (occasionally) in an entirely new genre that game spawns.
Bundles of standards such as these provide a very powerful tool for learning. If you
fire up an unknown computer game and you see a 3-D world with two hands close
up holding a gun, your hand will naturally move to the WASD keys, and you’ll know
what to do. Or consider poker: a whole family of games called poker exist, all sharing
some basic properties such as betting, a pot, and a certain ranking of hands. If you
know how to play one of them, you can quickly learn another. Standards apply not
only at the level of rules, but also at the level of heuristics: knowing something about
how to play one game in the family will usually mean you have some heuristics you
can apply to other games in that family as well (don’t stand still for too long in an
FPS; bluff occasionally when playing poker).
Individual games can sometimes be (deliberately) designed to have the variety that
an entire (evolved) genre has. Consider scenarios in hex-based wargames, or different
formats like draft or sealed in the card game Magic, or various PvP battlegrounds and
arenas in World of Warcraft. Although normally viewed as variants of a given game,

82

Chapter 3

they can just as profitably be viewed as different games sharing a set of standards.
Given that these games require a large amount of mastery of detail on the part of the
user, it’s very reasonable to try to leverage that mastery into a number of different
play experiences.
Exercise 3.5: Think of three genres of games, and for each of them give example
games and standards. Make sure at least one of your genres is high-level (e.g., “winter
sports”) and one is low-level (e.g., “electronic tactical RPGs”).
Exercise 3.6: Pick one genre and try to give all the standards for it. (You are unlikely
to succeed, but try to be as complete as you can!)
Exercise 3.7:

What are some standards that cross multiple genres of computer games?

Exercise 3.8: What are some standards common to all of the following professional
sports: football, baseball, basketball, soccer, and hockey? What are some standards
common to all of these except baseball?
3.3

Characteristic: Outcomes

For most games—in particular, those we term orthogames—the game ends at some
point and winners or losers are declared. The first examples one tends to think of are
games like chess or football: two sides, and at the end of the game one of them is
declared the winner and the other the loser, or perhaps a draw is declared. But there
are a number of other possible game outcomes, especially when there are more than
two players. After a short discussion of games without explicit defined outcomes, we’ll
discuss the basic kinds of game outcomes and their influence on the flow of the game.
Finally, we close with a brief discussion of draws.
Nonorthogames
Some games—ones that are not orthogames—have no formally defined winners and
losers. Typically players of such games define their own victory criteria, some of which

Figure 3.3

Infrastructure

83

might look much like an orthogame’s victory criteria and others of which do not. For
example, in an MMO a player might decide to focus on gaining levels, defeating
certain monsters, gaining skill in a trade, defeating opponents in PvP, griefing, accumulating gold, or accumulating equipment. Alternatively, she might decide to focus
on role-playing, accumulating many friends, gaining political power in a guild, getting
a certain visual look to her character, or helping new players. Most often, a player will
focus on some combination of these goals.
With a physical or paper multiplayer game, the choice of goals will typically come
not just from the one player, but from his community: a group of friends will decide
to play in a certain fashion, perhaps playing Hacky Sack to keep the bag in play for as
long as possible, or perhaps trying for spectacular stunts. In online games, a player
may decide individually on a set of goals, and then pick a community based on that,
joining a PvP guild if she is interested in those goals, or a raiding guild if that matches
her personal victory condition better. Of course, the reverse can happen as well, but
the relative abundance of different community choices online means players are probably relatively more likely to fit a community to a gamestyle preference instead of vice
versa.
In single-player games, such as sandbox games (The Sims, Roller Coaster Tycoon),
victory conditions tend to be purely individual, and sometimes highly idiosyncratic.
In all of these cases, there is no formal sorting of players into winners and losers,
but rather varying levels of satisfaction for players depending on to what extent they
achieved whatever goals they chose or had set before them.
Types of Outcomes
There are a variety of possible outcomes to an orthogame:
Unique winner or team of winners (chess, football)
Unique loser, with everyone else considered a winner (Old Maid, Skitgubbe, drawing
straws)
• Subset of winners—that is, alliances are allowed to form, and anyone in the winning
alliance is declared a winner (Cosmic Encounter, the Dune boardgame, qualifying races)
• Rankings: place, with first being best, but for example third still better than fifth
• Scaled performance: the game assigns players a score in some way
points, usually with more points being better (poker, many European
boardgames)
time, with accomplishing some task in a shorter amount of time being better (very
rarely more time is better, e.g., a dance marathon)
• In any of the above cases, draws may or may not be allowed.
•
•

䊊

䊊

The above categories are not mutually exclusive. In particular, rankings very often
arise from scaled performance, as in a footrace or a boardgame played for points.

84

Chapter 3

Sometimes, though, one has rankings not based on score, with the ranking arising
perhaps from players being eliminated (the last person left in the game receiving first
place). Occasionally, too, points may not result in ranking: in a poker game, one typically doesn’t think of players coming in first, second, third, and so on, but each player
simply considers how much she is ahead or behind at the end of the session.
One normally thinks of the rules surrounding winning, losing, and game outcome
as systemic. But in fact they are often agential. For example, a multiplayer boardgame
may have a point track, with the winner being the person who scores the most points.
Some playgroups may treat the game as a “unique winner” game, caring only about
who the winner is and caring nothing for points or second place versus third place.
Other groups may choose to play for place, or play for points. So even though we
normally think of how you win a game as systemic (after all, it’s written right there
in the rules), it can be agential as well (the rules don’t tell you whether you should
play to maximize your points if you are too far behind to win). For an extreme
example, consider Starcraft: strictly speaking, the game is systemically based on scaled
performance (it gives you a point score), but nobody plays that way, and instead there
is all but universal agreement that only elimination matters.
Note that if the game has only two sides, there is almost always a unique winner.
Thus the different game outcome types are the most relevant in the context of multiplayer games. Scaled performance, however, is still relevant. In two-player games it
can provide a context for monetary stakes. In single-player games it gives a good way
to compare across different games.
Game Outcomes and Politics
Games will have different gameplay characteristics depending on what type of outcomes they can have—and since those outcomes are often agential, so too are the
resulting gameplay characteristics. Political characteristics are especially affected.
For a multiplayer game with a unique winner, the play can become different in
character toward the end because the players will take crazy chances and make desperate plays to win. The game can also become political, with picking on the leader and
kingmaking being an issue. If there is some natural way to determine position, players
will often play for that, even if the rules don’t support it. For example, in a game
where first and second place get the same points (e.g., a qualifying heat), people may
still vie for first. Some games have a condition where everyone loses (e.g., the card
game Nuclear War), which can be problematic—is it better for you to come in second,
or better for everyone to lose? If enough people in a playgroup feel the latter is better,
games may end with everyone losing almost all the time.
Games where the goal is to avoid losing can tend toward picking on the player that
is behind. As with all political problems, limiting the scope for targeted interaction
can limit the negatives. Also, some games based on another outcome type (rankings,

Infrastructure

85

say) can agentially become games with unique losers: the playgroup can agree to quit
as soon as someone is knocked out.
Games with a subset of winners may be very political as players jockey to be on
the winning side. As with unique loser games, games of other types can be turned
into games with subsets of winners by agreement of the players. For multiplayer
boardgames that take a long time to play and have player elimination, this transformation happens quite frequently, and in fact some playgroups may more often agree
to call a game over, with the players remaining as winners (perhaps ranked informally
according to some score), than play the game out to the bitter end.
Scaled performance occurs in a great many games, even ones that are according to
the rules in one of the other categories. Players, or player groups, may react in different ways, either focusing very much on first place (or highest point total), or focusing
on trying to place as high as possible (or score as many points as possible) even when
first is out of reach. Differing interpretations of the “right” way to play can sometimes
lead to strife (see sections 2.3 and 2.4); money or other rewards can help here, because
they make it clearer what value positions other than first place have. A poker player
in fifth place9 rarely worries about whether to sacrifice all his chips to help the secondplace player come in first. Scaled performance when accepted by the players can go a
long way toward mitigating unwanted effects of politics and kingmaking because very
often players in a “lost” position with only their ability to affect the leaders to consider
will have something more concrete to play for.
Draws
Sometimes the rules of a game specify no winner in certain circumstances, with chess
being perhaps the classic example. Draws are sometimes seen as undesirable—after all,
if players are playing an orthogame, they are expecting a winner, and if none is
declared the game may seem unsatisfying. Sometimes explicit mechanisms are added
to a game to prevent draws, such as penalty shootouts in soccer or noninteger komi
in go.10
Games that allow draws are often fairly low-luck games, perhaps because there
draws seem “fair”: if the different sides are evenly matched, perhaps the draw is the
best representation of the (minimal or nonexistent) difference in skill levels. In a game
with lots of luck, it seems more natural to allow luck to determine the winner if
necessary.
If a game allows players to play for a draw, players in danger of losing will of course
attempt to draw if they feel they cannot win. This sort of play occurs, for example, in
9. Even the phrase “fifth place” sounds odd when applied to a poker player.
10. In go, komi is a point bonus given to one of the players, typically 7 1/2 points given to white
to offset the advantage black has in moving first. The half point serves to prevent ties.

86

Chapter 3

chess, tic-tac-toe, or Nuclear War. If a draw is too easy to get, the game may rarely
reach a satisfactory conclusion.
In some casual games, especially children’s games, draws can be desirable. The game
has been played and no one need lose. The draw outcome can be a powerful incentive
to play again, as long as there is some reasonable possibility of a nondraw in the future.
Exercise 3.9: Do NFL games have scaled performance as part of their outcome? Do
NFL seasons?
Exercise 3.10: Do campaign structures tend to enhance or detract from scaled performance in individual games? Why?
Exercise 3.11: What is the primary reason that games allow draws? Why do games
with less luck tend to find draws more acceptable?
Exercise 3.12: Often, the total prize purse in a tournament is fixed for cost reasons
and the payout to the winner is fixed for marketing reasons. If the primary goal for
distributing the rest of the money is to reduce kingmaking, what might the payouts
look like?
3.4

Characteristic: Ending Conditions

At some point, an orthogame will end and a winner (or group of winners, or unique
loser, etc.) will be declared. There are two basic ways this can happen:
Winning ends the game—for example, checkmating your opponent’s king means
you win, and the game ends at that point.
• An end condition occurs, then the winner is determined—for example, when the
Scrabble tiles run out, the game is over, and whoever has the highest score is the
winner.
•

In both cases, the phrase “victory condition” is commonly used to mean “what a
player needs to do to win.” In the first case, achieving the victory condition immediately ends the game; in the second case, an independent ending condition occurs (e.g.,
nine innings have passed in baseball), and the victory condition is to be in the proper
state (e.g., having the most points) at that moment. Games with an explicit end condition tend to have some sort of scaled performance as their victory condition; games
where winning ends the game may be based on scaled performance (e.g., first person
to 100 points wins) but may have some nonscaled victory condition (e.g., take all of
the opponent’s pieces).
Exercise 3.13: Give five examples each of games where winning ends the game and
where an end condition occurs. Do you believe the generalization that end conditions
tend to have scaled performance? Can you think of any exceptions?

Infrastructure

87

Figure 3.4

Sometimes the end condition occurs more or less independently of what the players
do, as when time runs out or a certain number of turns pass. Sometimes, though, the
players have some control over when the end condition happens. The dynamics
involved—with winning players attempting to hasten the game’s end and losing
players trying to delay it—can be intriguing or annoying depending on the details.
Some problem areas to watch out for include an ability of losers to delay the game’s
end ad nauseam, or annoying calculations that potential winners feel compelled to
make as they decide exactly when to end the game.
Points
Points—numerical scores assigned to each player, typically with highest being best
(although sometimes lowest is best, as in golf or hearts)—are extremely common in

88

Chapter 3

games.11 Even games that do not have points as an explicit part of the rules may
develop point systems of some type—really state heuristics—such as the point value
for pieces in chess (each piece is assigned a point value, and your total “score” is the
total value of pieces you have taken from your opponent).
It’s perhaps not surprising that even games without explicit scores may develop
them, since reducing one’s position to a single number is an extremely powerful
first-order heuristic. It tells you both whether you are winning or losing, and by how
much.
Exercise 3.14: Consider the games listed in appendix C. Of the ones you’re familiar
with, how many have formal point systems? How many have informal ones? How
many have no point systems at all? Discuss two or three of the borderline cases that
you find most interesting.
In single-player games, sometimes there is no way to “win,” but instead one plays
until one loses but tries to get as many points as possible before that happens (with
time spent until one loses being a common alternate player-chosen metric). Tetris, or
almost any arcade game, is an example of this style of play. Sometimes this lack of a
clear victory condition feels a little unsatisfying, and so an explicit win condition (e.g.,
defeat the big boss, or clear all the levels once) is put in at a certain point during the
game, and if one achieves it the game goes back to the beginning but with everything
much harder—for example, Donkey Kong or Diablo.
Complex games such as RPGs and especially MMOs often have a number of different point tracks (gold, experience points, faction reputation, craft skill, PvP points),
and the player can pick and choose which ones to go after. Even loot becomes a point
track system in World of Warcraft, given the raid loot tier system—having Tier 8 gear
instead of Tier 7 gear is a kind of advancement along a victory track.
Money and “Playing for Points”
Often points are spendable, either as in-game currency as in an MMO (not only gold,
but perhaps also honor, reputation, or experience points) or as real-world currency as
in gambling games. In this case, “playing for points” (playing to maximize one’s point
score, regardless of whether one is in a position to win the game or not) is very natural
and in fact may seem more natural than playing for place. After all, most people would
probably choose to be up $200 at the end of a night of poker with someone else at
the table who has more, rather than being up $100 even though everyone else at the
table has less. In fact, a game like poker is so connected with playing for points that
it is hard to think of it differently.
11. Many of the remarks here in fact apply to scaled performance generally—both points and
time—but are phrased in terms of points to avoid awkwardness.

Infrastructure

89

Although monetary systems are the most obvious examples of systems where
players will tend to “play for points,” they are not the only ones. For example, many
runners in a marathon (particularly those not among the top finishers) will care more
about their time than about how they place—coming in under four hours for the first
time will mean more to most people than placing 163rd rather than 167th.
“Playing for points” is extremely common. In games where the points have some
explicit value, such as poker where the points have the real-life value that money has,
playing for points is obviously natural. But even in games where the points have no
such value built in (Scrabble or hearts, say), players will often track them over time
(perhaps informally) in order to give them value. And even absent such a tracking
system, players may continue to play for points or for position in individual games.
Playing in such a way has a number of advantages: it reduces politics, and it gives
meaning to the game for players who are out of contention. You may not be able to
win the game—you may not even be able to move from fourth place to third—but
you can almost always try to eke out a few more points. Playing to do so is not entirely
satisfying (especially if the points have no intrinsic value), but it is still more appealing
to most people than playing randomly. One can think of this phenomenon as a way—
often player-adopted—of controlling the problems around player elimination and
politics. In other words, the more valuable points are, either explicitly or implicitly,
the less trouble the game is likely to have with player elimination, politics, kingmaking, and the whole complex of issues surrounding multiplayer play.
We’ll have more to say about money in section 6.2.
Dual-Track Point Systems
Sometimes the point track simply records who is winning. Sometimes, however, the
points also can be spent within the game to improve one’s position, as in Monopoly.
If the advantage to spending points to win is very great, it can lead to excessive snowballing; whoever is ahead spends points to get further ahead—that is, to get more
points. One approach to control this problem is to use two (or more) point tracks,
one for victory and one for power. This approach is especially common in European
boardgames, which often have money (representing in-game power) and victory
points (which are used solely for determining the winner). A similar dynamic appears
less explicitly in go, where there is a balance between power/influence (roughly,
outward-facing thickness, which is useful for scoring points in the future) and territory
(the actual victory condition of the game), although the parallel is inexact since power
is not easily converted into a point-based system. One can also think of an RTS in this
way, with a measure of one’s military strength representing victory points, and one’s
economic strength being the “money points” that influence victory only indirectly.
Separating money and victory points adds complication, of course, which is a
disadvantage. But it can have some good effects as well.

90

Chapter 3

It can give a kind of catch-up, since the player behind on victory points may have
more power points that she can use to close the gap. This is the flipside of the fact
that single-track point systems tend to cause snowballing.
• There are often interesting strategic choices (“guns or butter”) in terms of balancing
the two. Typically investing in victory points means going for a quick victory, and
investing in power points means giving up an early lead in the hope of winning in
the end.
• Games may seem closer; the person who loses will often be ahead in power points
and can say “I would have won in another turn or two.”
• Having the most power points (or the most of any one kind of power point in
complex games with multiple point tracks) is a kind of consolation prize or alternate
victory condition—“Yes, I lost, but look how much more wood I had than anyone
else!”
•

Victory Conditions
Games have countless victory conditions besides “amass the most points”: checkmate
the opponent’s king, get rid of all the cards in your hand, control the hill for three
consecutive turns. As mentioned above, such games tend to end on the achievement
of the victory condition as opposed to having a separate ending condition.12
For deliberately designed games, tweaking the victory conditions can be an important way to solve various problems that might come up in a game. For example, in a
game about battling armies, having the game continue until one army is destroyed
might lead to players hanging back and avoiding a fight. Having the victory condition
be control of a center area for a certain period of time can prevent that, while keeping
the basic feel of the game the same (i.e., the new victory condition encourages players
to have a large fight leading to the destruction of one army, the behavior that was
hoped for with the initial victory condition). Another example might be a Monopolylike game, originally designed to be played until all but one player is bankrupt. Such
a victory condition could cause player-elimination problems (players who go bankrupt
early have to sit out for a long time) or problems maintaining interest at the end of
the game (the winner is clear, but it takes a long time to actually end the game by
bankrupting everyone else). In such a case, changing the victory condition to amassing a certain amount of money might fix the problem, while leaving the basic gameplay
intact: players are still trying to amass the most wealth, just as before. Fixes of this
kind tend to come at a cost in increased complication, so there are always tradeoffs.
Some games have multiple victory conditions: in Magic you can run your opponent’s life down to zero or you can run his deck out of cards; in Age of Empires you
12. This is just a restatement of “games with ending conditions tend to have scaled
performance.”

Infrastructure

91

can destroy your opponent’s civilization or you can build a wonder. The appeal of
multiple victory conditions lies in the added depth and replayability they give the
game; it’s almost as if there are different games in the same game framework, one for
each victory condition.13 There is a real complexity cost, however: a moderate one for
the players, who must learn each victory condition, and a large one for the game
designers, who must balance the different victory conditions. Ensuring that two different routes to victory are both viable tends to be even harder than ensuring that
two different game pieces, say, are both viable.
Asymmetric Victory Conditions
Sometimes the victory conditions of the opposing players are not the same. This is
common in simulation wargames, but appears in other games as well. It is commonly
associated with asymmetric sides, but does not have to be. Some games even have
victory conditions known only to individual sides, as in some modern Risk variants.
The asymmetry in victory conditions can be critical for simulations. For example, in
recreating military battles it might be important to have initial conditions that presuppose one side as the winner, but by declaring victory in the game to be based on the
losing (in the historical sense) side holding out for a certain number of turns, a relatively fair contest can be created out of an unfair one.
This is seen commonly in many sports with handicaps to score in order to make
games fair. A game of HORSE may have the better player start with an H-O and thus
his victory condition is to make five unrepeatable shots, while his opponent’s win
condition is only to make three unrepeatable shots.
A wide variety of changes in audience skill range, in styles of play, and in strategy
can be created by varying victory conditions asymmetrically, often with minimal cost
to the overall rule structure.
Exercise 3.15: Give an example of a game where sometimes winning ends the game,
and sometimes an end condition does.
Exercise 3.16: Give some examples of games played professionally and casually where
the type of end condition changes. Why is this the case?
13. A less appealing corner case occurs with victory conditions put in to cover holes in the rules,
with the expectation that they will rarely come up. In reversi/Othello, one normally wins by
having the most pieces of one’s own color when the final sixty-fourth piece is played. But under
rare circumstances one can flip all the pieces to one’s own color at an earlier stage of the game
and win that way. Such alternate victory conditions tend to come up too rarely to be relevant
to normal play, and are often included in the rules mainly for logical completeness. Another
example is the triple ko in go, which under traditional Japanese rules could lead to an automatic
draw.

92

Chapter 3

Exercise 3.17: Single-player computer games commonly have a variety of victory
conditions throughout their campaign. Why are varied victory conditions more
common in these types of games?
3.5

Characteristic: Positional Asymmetry

Almost all games have different starting states for the players. These range from something as simple as one player moving first in chess to something as grossly asymmetric
as one player being a level 40 rogue and another a level 43 priest in a World of Warcraft
duel. These asymmetries may come from the game itself (white starts first in chess),
from the environment (wind in football), or from the players. Asymmetries coming
from the players may involve different gameplay options each player has (what char-

Figure 3.5
©iStockphoto.com/Juan Escalante

Infrastructure

93

acter class that player chose to play) or relations between the players (the ordering of
various players around the poker table).14
The effects may become washed out over the course of the game, or they may stay
in play throughout. In general, effects that might be washed out (like moving first in
chess) are more likely to do so at lower player skill levels. Sometimes the asymmetries
hardly seem to matter: moving first in Monopoly does not appear to make much of a
difference.
To find a game without any asymmetries, one needs to have all players moving
simultaneously and choosing from the same option set. Such games are rare; rockpaper-scissors is one example, and bicycle time trials are another as long as riders don’t
know how well other riders have done. Many games, though, are fairly close to
symmetric—for example, in a marathon the initial positioning doesn’t matter much
given the length of the race.
Extreme Asymmetry
Positional asymmetry may be seen as “unfair,” but some games use it deliberately to
increase game variety and replayability. Games such as single-player RPGs are built
around complete asymmetry: the player role and the (AI) monster role are wildly different. Simulation wargames are asymmetric for reasons of historical accuracy. Some
games, like Cosmic Encounter, Counterstrike, Magic, Starcraft, or any MMRPG, allow
players to pick from among different positions, or assign them to one, with the intention that these different starting positions are reasonably balanced.15 There is arguably
a trend toward more positional asymmetry in computer games nowadays, as can be
seen in the increasing use of different character classes in first-person shooters like
Team Fortress compared with the symmetry of Doom or Quake.
Although classic games are rarely grossly asymmetric, there are a few exceptions
like Fox and Geese or monster chess (if one accepts the latter as “classic”).
Moderate Asymmetry
Games with more modest amounts of player asymmetry—roughly equal player roles,
but with a slight advantage such as moving first given to one player—usually try to
14. Strictly speaking, the fact that one chess player is better than her opponent is a kind of
asymmetry, but we do not mean to include this case when we speak of positional asymmetries.
For a slightly more formal definition, one can say there is a positional asymmetry when swapping the positions of two equally skilled players can change the likely outcome. Thus the presence
of a weaker third player (on my left, but your right, say) might introduce a positional asymmetry
between us, but we don’t consider the weakness of that player relative to you as a positional
asymmetry between you and that player (it is an asymmetry, of course, but it is not one based
on position).
15. Or, in the case of Magic, a subset of the starting positions (decks) are reasonably balanced.

94

Chapter 3

limit that asymmetry as much as possible, most often by rotating which player has
the advantage. Teams take turns kicking off at the start of each half in football, the
deal rotates in most card games, chess matches involve multiple games with players
alternating black and white, and the go player who has white receives 7 1/2 points
