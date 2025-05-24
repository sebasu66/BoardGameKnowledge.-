Warcraft, some things like the technique for beating a given boss or where to buy a
certain crafting recipe seem much like hidden information to be uncovered, and other
things such as the best order in which to cast one’s spells seem like gameplay skills to
be learned, but really there’s no absolute distinction.
In general, puzzlelike hidden information does not tend to make for very repeatable
gameplay. You typically don’t want to do the same crossword puzzle twice or play
Myst again and again; once you know the secret, it’s time to move on. There are a few
exceptions where the hidden information is regenerated each time you play and
thus you can rediscover it: Roguelike games (items and maps) and Mastermind are
examples.
Randomness
One doesn’t normally think of randomness as hidden information, but it can often
be useful to take this viewpoint. If private information is something one player knows
and another doesn’t, the outcome of a die roll is something no player knows: information hidden from everyone.
Recall that we divided sources of randomness into three groups: explicit random
elements (e.g., dice or cards), von Neumann games (e.g., rock-paper-scissors), and
human ignorance (e.g., guessing between two apparently equal lines of play in
chess). Each of these can yield hidden information. Even visible randomizers like
dice generate hidden information in the sense that no players know what the die
roll will be before it is made. And other randomizers, like cards, typically are not
revealed to all. Thus cards or Mario Kart power-ups can be thought of as adding
hidden information in two ways: once because of their unpredictability before they
are drawn or run over, and again afterward because one person knows what they are
and the others do not.
Any time two players make a choice at the same time, as in rock-paper-scissors, and
the game has some mechanism for comparing them, the outcome is rather like the
roll of a die. Thus Von Neumann games yield hidden information of the “unknown
29. It’s a moot point whether these examples are “really” games: common usage would say the
crossword puzzle is not, but the other two are. Yet it’s not clear there’s anything in the gameplay
itself that distinguishes a crossword puzzle from Myst in terms of either one being a game.

164

Chapter 5

future” sort, much as a die roll does. That “die roll” is itself coming from private
information: the intention of each player, known only to himself or herself, as to what
Von Neumann choice he or she will make.
The situation involving choices made out of ignorance is similar, if one imagines
them as being made in effect by some sort of randomizer in the brain.
In general, when people speak of “hidden information” they are thinking of private
information. But any way of producing information that is not known to the players
is in some sense hidden, and there is some value to discussing all such game features
as a group.
Randomness and Hidden Information
Random elements, randomness, and hidden information are related to each other in
a number of ways.
As mentioned above, implementing hidden information in a game typically
requires putting some sort of random element into the game. This may be an explicit
random element, as in the case of the draw of a card. It can also be the kind of
random element that secret simultaneous choices give, as in the secret choices that
players in an RTS make (such as which units to build). A common example of the
first type is the hidden draw of a victory point chit found in many European boardgames (as discussed in section 6.5). Examples of the second type are rarer in the
boardgame genre, but they do exist—for example, Stratego. In sports, explicit randomizers are rare (other than the occasional coin flip to start the game), but simultaneous
decisions happen all the time—prominent examples are penalty kicks in soccer30 or
play-calling in football. Another interesting example of secret simultaneous choices
occurs in tournaments where a player can bring a strategic “package” of some sort to
each match: an army in a miniatures game, a deck in a trading card game, or a race
in an RTS.
RTS games have several further interesting examples of von Neumann–style hidden
information built into them. There’s very little in the way of significant explicit
random elements in most RTS games (they commonly have random damage, but that
doesn’t affect the outcomes of most battles; instead it serves to wash out breakpoints
that might otherwise exist along upgrade paths31). But a large amount of hidden
information arises from player choice. That hidden information may arise directly
30. Goalies may need to guess which direction the kicker will aim, with the kicker guessing
simultaneously which direction the goalie will leave open.
31. For example, if units always did the exact same damage, then a small upgrade in unit A’s
damage or unit B’s hit points might mean a large jump: unit A can now kill unit B in two hits
instead of three, or four hits instead of three. Keeping track of all these breakpoints (for all
upgrades on all unit pairs) would be a large memory burden.

Indeterminacy

165

during building, as players choose to create units, upgrade them, or follow entire tech
trees, with their opponents not necessarily knowing. Fog-of-war means the position
of a player’s army may not be known to his opponent, which also yields hidden
information and a Von Neumann game of “where is the army.” The choice to set up
a base is a decision only the player who makes it knows (until his opponent discovers
it), and it also leads to further hidden information: that part of the map is revealed
to the player who set up the base there, but not to his opponent. Of course, good
players do everything they can to learn as much of this hidden information as possible
through scouting, much as good card players try to deduce as much as possible about
their opponents’ hands.
Effects of Hidden Information
Hidden information can do a number of good things for a game:
•
•
•
•
•
•

Provide (a perhaps more acceptable form of) randomness
Control calculation (by diminishing returns to calculation)
Give a sense of discovery or pacing (as the hidden information is revealed)
Provide surprise
Provide an excuse for losing (“How was I to know he had the jack?”), valid or not
Provide gameplay in
The deduction of the hidden information from clues
Planning out lines that take into account various values hidden information might
have
A psychological game of bluffing and insight
䊊

䊊

䊊

Note that this list of advantages is much like the list for randomness. Given the
close relationship between hidden information and randomness, this similarity is
hardly surprising.
The negatives of hidden information are also very similar to those of randomness,
but perhaps a few points are worth mentioning separately. Although hidden information can, as mentioned above, help control calculation, it may sometimes increase
busywork or calculation, either due to memorization of occasionally revealed data or
due to the necessity of reading out various alternate lines of play based on possible
values of the hidden facts (“if the king of spades is on the left, I’ll play this way, but
if it’s on the right I need to play that way”). Hidden information can be harmful to
spectation—the question of what hidden information to let the spectators see is often
hard to solve. And certainly games like chess or go, with completely public information and no overt random elements or simultaneous choices, have a kind of purity to
them that is appealing to many players despite the difficulties inherent in such a style
of play.

166

Chapter 5

Exercise 5.14: In bridge, one player (the dummy) “plays” with an open hand. How
does this elimination of hidden information affect the skill in the game? In other
words, would bridge have more or less skill without the dummy rule, and why?
Exercise 5.15: If all players in bridge played with open hands, how would it affect
the skill in the game?
Exercise 5.16: If all players in poker played with open hands, how would it affect
the skill in the game?
Exercise 5.17:

Give examples in baseball of hidden information.

Exercise 5.18:

Give examples in football of hidden information.

6 Player Effort

Games can be rewarding for players, but they also require effort. Those efforts impose
a cost on players that they may or may not be willing to pay. We open with a general
look at costs, and then go into more depth on two: the cost of downtime (time not
spent playing) and of busywork (rote activities in the game that aren’t perceived as
fun). Lastly, we look at the rewards players get—first what kinds of rewards a given
game might offer, and then how rewards (particularly the reward of winning) scale
with effort.
6.1

Characteristic: Costs

If there’s a game you want to play, you might be dissuaded if the cost of playing it is
too high. By cost, we mean not just monetary costs, but every possible obstruction to
your playing the game, including how long it takes to play, how difficult the game is
to learn, injuries you might incur playing, how much physical space is needed to play,
and so on. So for example Starcraft might cost $30 for the box, but you also have to
buy and maintain a computer (and a net connection if you want to play online), you’ll
need to spend some time to learn the build tree, you’ll have to put up with annoying
people if you play online, and so forth.
Costs will vary not only in how high they are but also in how necessary it is that
you pay them:
Required: a ball and at least one bat for baseball
Effectively required: a certain amount of stamina to play basketball (the amount will
depend on the group you are playing with)
Helpful: a fast Internet connection to play Quake
Optional: a really nice graphics card for the latest MMO
The largest costs are usually either time and effort, or money and materials. Time
and effort include not only the time it takes to play the game, but the time it takes
to learn it, and any time that needs to be spent practicing or preparing. Practice and

168

Chapter 6

Figure 6.1
©iStockphoto.com/daniel sainthorant

preparation costs tend to be more agential than in-game costs: one playgroup may
spend slightly more or less time than another in playing the game, but preparation
time will differ vastly. NBA games do not take that much longer than the average
pickup basketball game, but the preparation time needed is hugely different. A certain
amount of preparation is often forced on the player by the game system: you need to
come with a well-equipped level 80 character to go on certain World of Warcraft raids,
and you need to come with your own deck to play Magic.
In terms of money and materials, there may be relatively little required, as in tag,
where one only needs a place to play, or twenty questions, where one needs nothing
at all. More often one needs some basic equipment, as in most sports games. For paper
games, all the equipment and rules typically come in a box, and if you’ve bought that
box you’re all set.1 Electronic games typically need the “game itself” (software in a
box, or downloaded over the Internet) and some sort of platform: a PC, a console such
as the Xbox or Wii, or a handheld device like a GameBoy or Nintendo DS.
1. Except for a place to play and an opponent, which one might think of as material requirements, and some time.

Player Effort

169

The platform costs can be amortized over many games, but definitely present a
barrier to entry. For consoles, there are a number of tricky issues for the platform
maker. Is it best to make as little money as possible on the console, and make it back
on the games (“give away the razor, sell the blades”)? How much should other people
be allowed to enter the game market (more means more market power for your
console, but perhaps fewer sales for your own games)? If you do let others enter, how
much freedom should you give them (for example, limit the games they can make to
protect your IP and marketing message, or let them create whatever they think is
profitable and take a cut)? How should you market the console compared to the
games?
The cost of a PC is particularly hard to analyze, because the PC typically has other
uses, and might be thought of as “free” (you have one anyway), except for the fact
that a PC used for PC gaming2 needs additional hardware, such as a high-end video
card and perhaps some specialized controllers. The success of web games is due not
just to their broader appeal as games, but also to the fact that (like the much-played
Minesweeper and FreeCell) no additional hardware is needed to play them.
One way to think of the money cost of games is in terms of the business models
behind them. In other words, if there are people making money selling the game, how
are they doing it, and how does it look to the consumers? Some possibilities:
It’s all but impossible to make money off of the game (e.g., tag).
Equipment sales (Go Fish, baseball).
• The equipment is the game, “game in a box” (chess, Settlers of Catan).
• Rental (equipment, as in skiing, or a place to play, as in golf).
• “Pay to play”: arguably a variation on rental, but may be perceived differently
(gambling, World of Warcraft).
• Object model: a version of equipment sales. The game requires many (possibly
consumable) objects to play (auto racing, Magic, many Asian online games).
•
•

If the game is owned (in the legal sense) by the seller, he can hope to charge a
premium for it; if it is in the public domain, the seller will face competition from
other people selling the same game. The market for Settlers of Catan is very different
from the market for chess sets (of course, if the seller owns the game, he has gamedesign costs to recover that the chess-set manufacturer does not).
Many games follow multiple business models, sometimes with the same company
involved in each case, sometimes with different companies. If there are two different
costs to play, a player might need to pay them both (rent time on the golf course and
2. “A PC used for PC gaming” sounds redundant, but in fact “PC gaming” has come to mean,
not any game played on a PC, but one specifically written for its hardware, as opposed to browserbased web games.

170

Chapter 6

buy clubs), in which case overall costs tend to be high, or she might have an option
(buy a game or rent it), in which case the costs will probably be lower for her.
The possible combinations are endless: Nintendo sells both game consoles and
games for the console. Other people may rent either of those things to players. Nvidia
sells you a high-end video card you can use in many different games, and other people
sell you the individual games. Golf-course owners rent course time, and different
people manufacture golf clubs. Blizzard sells you a box containing the game World of
Warcraft, and then charges you each month to play.
Trading Costs
Often players can exchange one cost for another. The risk of getting injured in football
is a cost, but you can pay money for pads. If you don’t want to buy skis, you can rent
them. Carrying your clubs around, and walking, are costs to playing golf, but there
are caddies and golf carts. Particularly interesting are situations where you can trade
time for money, since many people have more of one than of the other. Letting both
money-rich, time-poor and time-rich, money-poor people play your game can expand
your audience a great deal. For example, in Magic, you can buy some cards, and then
do a lot of trading to improve your collection, or you can spend less time trading by
just buying a lot of cards. In World of Warcraft, you can play a great deal to get all the
gold you need, or you can save time by purchasing gold from Chinese gold farmers.3
Skills Players Need
One cost players must bear is that of developing (or possessing already) certain skills
or abilities. Of course, developing one’s skills can be part of the enjoyment of a game,
but for the moment we’ll be thinking of it as a cost.
Most games fall into three broad categories in terms of the skills players need:
•
•
•

No physical skills needed: chess, bridge
Only eye-hand coordination: many computer games, like RTS, FPS, darts, pool
Broad physical skills needed: basketball, soccer

Games in each category may require more or less mental skill: go versus slots on
the nonphysical end, Starcraft versus target shooting in the eye-hand category, or
football versus sprinting on the physical end.
In general, physical skills are needed for sports, but not for card games or boardgames (with a few exceptions like Spit). Computer games are sometimes purely mental
(e.g., Civilization) or sometimes involve eye-hand coordination (e.g., Starcraft), usually
because they take place in real time. When discussing a game in a category that may
3. Although purchasing gold is frowned on (but commonplace) in World of Warcraft and most
Western online games, Asian games such as Maple Story often have it built right into the system.

Player Effort

171

or may not require eye-hand coordination and quick reflexes to play, we say the game
has “twitch” or is a “twitch game” if it is at least in part reflex-based: so Starcraft or
Quake is a twitch game, whereas Civilization or Minesweeper is not.4
Non-twitch skills include skills like reading out moves, memorizing openings,
political skills (fast-paced games often lack time for politics), and so on. Non-twitch
games are often rich in conscious game heuristics (control the center, don’t draw to
an inside straight). As games get faster, more of the heuristics need to be unconscious
and automatic, although they are often trained consciously and then executed
automatically.
Twitch skills in computer games include aiming, splitting your attention, timing
attacks, or simply performing many actions in a short amount of time. This last is
often referred to as “apm” (actions, i.e. clicks, per minute) in the RTS community and
is especially powerful in certain kinds of games: in an FPS, shooting fast is limited by
ammo, but in an RTS being able to perform 200 actions in a time period where an
average player can only perform 10 is an overwhelming advantage.5 Player tolerance
of games that demand these kinds of skills varies widely: some players want no time
pressure at all, some are willing to accept a certain amount of aiming or quick thinking but no more, and only a few are willing or able to play a game at a level that
demands a hundred or more productive clicks every minute.
Of course, there are a huge number of different skills in sports and other highly
physical games: catching, throwing, running, and so on.
In addition to skills per se, there are also attributes that players may need that are
not amenable to training and thus are not generally thought of as skills: height in
basketball is the classic example. But the line between what is trainable and what is
not is by no means hard and fast: although anyone can hope to increase his Starcraft
apm, it is certainly imaginable that 200 apm is simply out of reach for many people.
And while anyone can increase her muscle mass with exercise (or steroids), there are
limits that only some people can reach. And who is to say whether a given person
has, even in theory, the ability to memorize as many chess openings as Karpov? The
more a particular attribute seems unreachable, of course, the more players who feel
they do not have it will be discouraged from playing the games that demand it—short
4. An intermediate case is a normally nontwitch game like Civilization or chess played with a
timer: some speed is required, but typically more speed of thought rather than reflexes and
coordination. In general we think of these games as nontwitch, but obviously the faster the timer
runs the closer the game becomes to a twitch game, and in some sense Starcraft is Civilization
with millisecond turns (thus Starcraft has made a tradeoff by reducing downtime but increasing
the skills needed to play). The dividing line is somewhere around the point where the turn length
equals the physical time needed to make whatever moves are allowed in a turn.
5. An apm of 10 might be fairly quick for a beginner, and top players do indeed reach 200.

172

Chapter 6

people may choose not to play basketball, or slow people not to play Starcraft, even
if the game otherwise seems appealing. The unattainability of certain skills may seem
to players very similar to out-of-reach monetary costs, such as those required to participate in yacht racing or polo.
If a game has different roles available to players, the skills required may vary quite
a bit by role: a football linesman has different skills from a running back, and a World
of Warcraft rogue has different skills from a priest. If there are leadership roles available, the differences can become even more pronounced: a quarterback or a World of
Warcraft raid leader needs a number of specialized skills. One can think of coaches or
managers as “playing” a game as well (and indeed some sports-themed computer
games and card games have the participant take on that role rather than that of a
player in the game itself), again with a very different set of skills needed.
Besides the skills needed to play the game, there are often quite different skills
needed in the metagame: discipline in training, building of social networks among
other players, “gaming” the tournament system for greater rewards, finding the right
instructors, and so on.
It is worth looking twice when the skills needed to play a game vary widely. If the
variance is too great, it can cut down the potential player pool dramatically. Sometimes
this is deliberate—for example, chessboxing.6 Mostly, though, it is probably inadvertent—think, for instance, of the players who like strategy games generally but gravitate
toward turn-based ones because they feel RTS games are out of reach. Other potentially
“incompatible” skills might be character building and grinding in MMOs, or logical
thinking and rote memorization in chess. Of course, what is incompatible with one
group may be perfectly acceptable, even enjoyable, to another.
Excessively Increasing Costs
It will usually take a while to acquire skill, so one important cost to a game is how
much time and effort it takes to become good enough at it that you can find a reasonable game. This cost is highly agential: if you are surrounded by very casual chess
players, you can quickly get up to speed and have some fun. But if everyone you know
is rated 1800+, you have a lot of work to do before you will be able to enjoy
yourself.7
Over time, in the absence of other forces, players who are not good at a (low-luck)
game will tend to leave if they are constantly playing with good players—losing all
the time is no fun. But as more low-level players drop out, the game can get harder
and harder for new players to enter: the amount of effort to become an okay player
6. Exactly what it sounds like. See, for example, http://site.wcbo.org.
7. Once again, games with lots of luck shine here. Their barriers to entry are lower because a
modest amount of effort on your part will allow you to play and win at least a few games.

Player Effort

173

of the game goes up. Or, to put it another way, small amounts of effort on the part
of new players aren’t rewarded—only the very large amount of effort required to bring
them up to the level of the pack gives noticeable rewards. So more of the new players
who do enter may drop out. And as bad players drop out, players who once were near
the middle of the pack may find themselves near the bottom, losing much more often
than they had been, and they may drop out too. At its worst, the game-playing audience may become a smaller and smaller group of ever more skilled players.
If a game is one that is deliberately designed, and part of a larger genre, further
iterations of the game will typically be made to appeal to this more elite audience.
The game design shifts in this way partly because that is the audience that is available,
and not appealing to them makes the new version highly likely to fail, and partly
because the game designers themselves are likely to be members of the elite and will
tend to design for themselves. But this new game filled with features for the elite is
likely to be even harder for a newcomer.
This two-pronged narrowing of the audience—more casual or less skilled players
dropping out as they lose, and new game designs appealing to a narrower and narrower group of elite players—has been termed “grognard capture” by the game designer
Greg Costikyan8 (the term grognard is a term for old-school wargamers, from a French
word meaning “veteran soldier” or, literally, “grumbler”). One sees it in many game
genres, such as RTS games; the push for ever-larger feature lists as seen on box copy
(“Now with 437 different units!”) and the nature of online play (players of all different
skill levels in the same pool9) make computer games especially vulnerable. Another
notable example is the fighting game, where entry into the genre for a new player is
extremely difficult.
Costs can spiral out of control in other ways as well: raiding in an MMO requires
enormous time costs, more so in the time costs of building a character suitable to go
on the raid than the costs of the raid itself. The cost in time or money to build a suitable Magic deck has gone up greatly compared to the original vision, where it was
imagined that most people would have only a modest number of cards and nobody
would have them all. Magic in particular made a concerted and expensive effort to
cap these costs in order to keep the game accessible to newcomers. While costing more
than originally intended, the cap placed on player expenditures was a drastic reduction from what it had become shortly after its launch.
When costs spiral, once people understand these costs they may choose not to play
at all, even though they would have been perfectly happy to play at a more modest
cost level.
8. http://www.costik.com/weblog/2003/08/grognard-capture.html.
9. Good matchmaking solves this. Unfortunately, few online computer games have good matchmaking, although the situation is improving.

174

Chapter 6

Controlling Spiraling Costs
The basic way to prevent players from leaving a game as the costs spin out of control
is to have good player matching. If players are matched against players who want to
pay about the same amount that they do (in time, money, or some combination of
the two), they are more likely to have good games and more likely to perceive the
game as fair.
People sometimes think of player matching as a new thing, but it’s really very old.
Players choosing to play with their friends (who are more likely to want to invest
about the same amount), regional microclimates (where an informal consensus about
how much to invest can build up), different levels of leagues in sports, and beginner
tournaments in chess are all examples of matching systems of one kind or another.
With electronic games, many of the traditional matching methods break down to
some degree, due to anonymity. In a vast undifferentiated sea of players, it’s hard for
microclimates to form. Friend lists help; so do matching systems based on explicit
ratings systems such as Elo. Guilds and guild migration can be thought of as a kind
of online matching solution. However, the fluid nature of identity on the net leads
to phenomena like smurfing (where an experienced player creates a new, low-rated,
account in order to be matched against other low-rated players and thus win more
often), and the problem of player matching is by no means completely solved.
Online or offline, although matching (broadly construed) is the main solution,
other things help as well. Having more luck in the game is extremely useful, because
the beginner can reach a point where enjoyable games are possible much more quickly
and with much less effort. Explicit training, be it coaching on a sports team or a tutorial for a computer game, can also help beginners get up to speed.
Exercise 6.1: Purely from a monetary cost perspective, would you expect single
people or people in families to spend more time playing PC games (consider how the
costs are spread out)? Why? How does this difference compare to the difference you
might see in other kinds of games, such as sports or boardgames?
Exercise 6.2: Purely from a cost perspective (both monetary and otherwise), would
you expect younger people to play more basketball or more golf? What about older
people? What costs change absolutely and relatively for people as they age?
Exercise 6.3: Describe from a cost perspective (monetary and otherwise) what type
of demographic differences you would expect to see in the player populations of an
MMO and of online poker.
6.2

Characteristic: Rewards

Offsetting the costs of playing a game are the rewards. Often the rewards stem simply
from the enjoyment of playing the game itself, but many rewards go beyond pure
in-game enjoyment and connect with various factors outside of the game.

Player Effort

Figure 6.2
©iStockphoto.com/Catherine Key

175

176

Chapter 6

In-game rewards can include
Pleasure from winning
Satisfaction from playing well
• Enjoyment of mental or physical challenge
• Aesthetic enjoyment of the game experience (computer graphics, well-crafted game
pieces, etc.)
• Excitement or adrenaline rush (more common in sports and first-person shooters,
less common in boardgames)
• Escapism
• Enjoyment of social interactions during the game
•
•

Note that we do not include fun as an item in the above list, because the term is too
broad to be useful as a specific reward category. For us, the term fun is simply a casual
synonym for enjoyment or in-game reward. If a game is said to be “fun,” the question
to ask is “in what way?”—that is, what rewards is the game offering?10
Much of the pleasure of games comes from out-of-game analogs to these various
in-game pleasures. For example, many playgroups keep track of who won (and
how often, and how spectacularly) over time. Most often, the tracking is done
informally, simply by remembering notable events and occasionally telling stories
about them. Sometimes it’s done more formally, with written records being kept.
Computer games, and arcade games especially, typically record high scores. Getting
on the high score board, or better yet getting the highest score, is a special sort of
achievement.
Although players have always talked about special accomplishments in their games
(spectacular catches, winning from behind, winning several games in a row), and often
tracked them explicitly (think of baseball stats), computer games recently have
extended and automated achievement tracking with systems like Xbox Live Arcade’s
Achievements or the City of Heroes badge system.
Parallel to the satisfaction of playing well is the pleasure of seeing improvement in
your skills over the long term—that is, in climbing the heuristic tree. This pleasure
ties in with that of winning, since as your skills improve, you either win more often,
or at the very least you win against opponents you could not defeat before. It also
connects with the enjoyment of challenge, since you can tackle tougher challenges as
your skills improve.
If you play soccer, you may be enjoying the challenge of doing so. One part of
that challenge is exercise. But even if you do not enjoy exercise, you might still enjoy
10. For other breakdowns, see Marc LeBlanc’s list of eight kinds of fun at http://
algorithmancy.8kindsoffun.com/, or the discussion of typologies of pleasure in Salen and
Zimmerman’s Rules of Play, 334–346.

Player Effort

177

the fitness it causes. So parallel to the physical or mental challenge within a game is
the larger physical or mental fitness that may result. Physical games are widely
acknowledged to provide physical fitness; mental games are more often viewed as
“wastes of time,” but they surely provide mental fitness.11 Some games are specifically
designed to be “educational” and provide a specific knowledge base, but many noneducational games have such knowledge benefits as well (e.g., Civilization or SimCity),
and all games that involve effort to achieve victory are exercising the mind or body
to some extent.
The social benefits to gaming may be fairly modest during the game—everyone’s
too busy playing—but can be quite large before and after the game. The bonds that
form around a high school football team, or a Dungeons & Dragons group, can be
very strong, and they may even last a lifetime. A further reward is the status one
can get from the group, be it from winning in general or from knowledge or skill
in some specific subtask (see also section 7.1). These status rewards for players may
extend beyond the playgroup, especially if the game is frequently played before
spectators.
Tangible Rewards
Sometimes there are tangible rewards for winning—the most obvious of these is
money. In a society where money matters, a victory that is rewarded by money may
seem more real, more valuable, than one that is not, even on a purely psychological
or status level. And the money itself is certainly a reward. Many games have tournaments with cash prizes. Some games, such as poker, are built on top of money in
such a way that it’s hard to play them satisfactorily without money. Others, like
backgammon, improve with money (mainly because the doubling cube is then of
more use, and the doubling cube adds a great deal to the game). With some games
that can be played for money, playing for points works quite well also—bridge is
one example. This phenomenon is in large part agential, in that bridge players accept
that points are important, and play to some extent as if the points were backed
by money even when they are not. Poker players and backgammon players do this
less often.
Money is so powerful as a reward that some games that use it can be popular even
though they would be completely uninteresting without it. It’s hard to imagine
playing slots, for example, if no money were involved.
Strictly speaking, while money is certainly a reward for professional baseball players,
say, it is probably better to say that the dream of money, or the opportunity to fantasize about money, is the actual reward for gambling games. Most people who gamble
do not do so in the expectation that they really will have more money afterward (and
11. See, for example, Johnson’s Everything Bad Is Good for You.

178

Chapter 6

of those who do, most of them are wrong). And perhaps even more important than
the fantasies of money are a certain status gain for playing—a kind of conspicuous
consumption—and above all the thrill of risk.12
Besides money, certain games offer other tangible rewards. In the case of Magic, the
cards are a reward, and while they can be purchased they can also be won as tournament prizes. In-game “material rewards” such as virtual loot, virtual currency, or even
experience points are an interesting borderline case. They can be thought of simply
as part of the game’s mechanics, or as a kind of achievement, but it is also natural to
think of them as a reward. Certainly the players think of them that way. The fact that
they give in-game power distinguishes them from other achievements such as having
slain a particular monster without assistance, or passing a level by popping only red
and blue balloons.
Exercise 6.4: What are some rewards in bridge? Monopoly? Party games? What correlation might you expect with high downtime and rewards?
Exercise 6.5: What are some rewards in Myst? Other puzzlelike games? What correlation might you expect with these games’ rewards and replayability?
Exercise 6.6:
costs?

What are some rewards in playing high school football? What are the

Exercise 6.7:
costs?

What are some rewards in playing high school chess? What are the

6.3

Characteristic: Downtime

Downtime is time during a game when a player is not actively playing (she may or
may not be considering strategies, but she is not making any moves, or even about
to do so13). It is often seen by players as a detriment—usually they would rather be
playing than waiting around—but it can sometimes be a benefit, as when it provides
scope for socializing. Also, no downtime at all can sometimes be a detriment, as we’ll
discuss below.
The most typical example of downtime is waiting for your turn to come, perhaps
in a boardgame or card game, or perhaps in a sports game where some players sit out
12. Compare putting $10 on the roulette wheel with, say, seeing a scary movie for $10. In each
case you get a thrill (and in the case of roulette you even have a chance of getting your $10
back). If seeing the movie makes sense, then betting the $10 on roulette can make sense, even
for someone who understands that in the long run they are not going to come out ahead
monetarily.
13. In particular, we don’t consider it downtime when you’re thinking about what move to make
while it is your turn.

Player Effort

179

Figure 6.3
©iStockphoto.com/Tom Nguyen

for some part of the game. Playing dummy in bridge is another example. Downtime
is not necessarily imposed by strict lines in the rules saying you can do nothing: less
sharply defined examples include a soccer goalie waiting while the ball is at the far
end of the field, an RTS player waiting for an early building to be finished, or an MMO
player waiting for mana to recharge.
Downtime is often at its most problematic with multiplayer turn-based games (e.g.,
multiplayer boardgames), especially as the number of players increases. If there is not
a lot of interaction among the players, then the total downtime is enormous, as each
player waits for a succession of other players to take their turns before he can play
again. Even if there is player interaction, it is very often one-on-one, and all but those
two players experience downtime while the two of them interact. An extreme case
of this may be found in the boardgame Titan, where every so often two players
essentially stop the game and play a one-on-one miniwargame before normal play
continues.
When considering player tolerance of downtime, note that both the total percentage of downtime (i.e., how much time the player is playing versus not playing) and
the length of a stretch of downtime (i.e., what the longest stretch of time is that a
player must wait) matter. The two of course are related, but not absolutely—there are
games where one sits out a lot, but never for that long (poker), or where one spends
most of one’s time playing, but every so often sits out for a good chunk of time
(hockey).

180

Chapter 6

Exercise 6.8: Suppose a turn-based game has n players, and turns last t minutes. Also
suppose there is essentially nothing to do on an opponent’s turn. What percentage of
a player’s time in the game is downtime? How long is a given stretch of downtime?
Downtime turns players into spectators. This is not all bad—watching other players
play can be a fun part of the game, and the fact that you are participating in the game
yourself makes the fates of the other players particularly interesting to you. Of course,
if a game is very interesting to watch (see section 7.3, on spectation) the downtime
may be more bearable. However, in general downtime looks very different to players
and to (true) spectators. On the one hand, players are more likely to need a rest, or
to be willing to think about the game when they aren’t actively involved, and in that
sense are more likely to benefit from downtime. On the other hand, spectators are
less committed to the game, and may be happy simply to step away for a few moments
(e.g., getting a drink during a break in the action). And of course for sports on commercial television, there are economic incentives to have downtime in which the
networks can sell commercials. Also, downtime for just one player hardly matters to
spectators—they can simply watch another player. It is only downtime that affects
everyone, such as a time-out, that matters.
Downtime—Good and Bad
Since generally players want to be playing, designers should, and do, attempt to
minimize downtime. However, it should be recognized that too little downtime can
be bad also.
In some games, downtime varies with player skill, with weak players sitting out
more. Counterstrike and Defense of the Ancients both can have very high amounts of
downtime for weaker players.14 Such a situation is very punishing for beginners and
other weak players (not only is sitting out discouraging, but it also makes it harder to
improve one’s skill), and such games tend not to make good casual games.
Waiting a long time between turns is not so bad if you can plan your strategy during
that time. Some games with a lot of calculation, such as chess, almost require this
downtime in the sense that the game would take almost twice as long without it in
order to get the same quality of moves.15 Games without overt random elements are
more amenable to this kind of analysis: it is much easier to read out one’s moves if
those moves don’t rely on, say, the unknown roll of the dice at the start of one’s turn.
Some games with random elements, such as Scrabble, can still benefit in this way if
14. In a very different way, team sports have the same issue, with weaker players being forced
to sit on the bench.
15. Go players can use this downtime even more effectively than chess players can, because
different regions of the board are more independent. Thus a player can read out one portion of
the board while his opponent is (most likely) playing in another.

Player Effort

181

the random elements are placed at the end of one’s turn rather than the beginning
(drawing a new card or tile at the end of one’s turn rather than the start16), or if the
influence the random element will have on one’s turn is not too large. The utility of
this downtime can vary agentially with skill. Waiting for the other player in chess can
be painful to a weak player, but a highly skilled player may relish every extra second
he has to think about the board.
Turn-based multiplayer games with many players suffer in terms of a player’s ability
to use downtime, because the board state on one’s next turn may be very different
from what it is at the end of one’s current turn. In such games, one often starts
thinking about one’s turn only during the turn of the player immediately preceding,
rather than as soon as one’s own turn is over. (One way to think of this is that the
state heuristics of the game, as applied by me at the end of my turn, are damaged by
all the intervening players, forcing me to apply them later.) However, the more interested I am in what happens during other players’ turns, the less onerous the downtime. One particularly good example of this is Monopoly: the best thing that can
happen to me—namely someone landing on my property and paying me lots
of money—happens on my opponents’ turns. So I am excited to watch the turns of
other players.17
Downtime can also be useful for pacing. It allows the game to be less high-pressure
and lets players take a break. No downtime at all makes for an exhausting game.
Anyone who has played indoor soccer, where the ball never goes out of bounds, can
appreciate how much more exhausting it is than regular soccer, which is itself more
tiring than games like football where one sits out frequently, or baseball, where one
essentially sits out almost the entire game.
Computer games are both better and worse in terms of downtime. If the computer
game has fast AI opponents, the downtime problem is essentially solved even for
multiplayer (more precisely, one-player, multiple simulated opponent) turn-based
games: you take as much time as you want on your turn, playing as quickly or as
slowly as you like, and then the AIs all quickly complete their turns. But if such a
game is ported directly to true multiplayer form, it becomes all but unplayable: every16. This can have an unintended consequence, however: a player may get a bad draw, and then
spend considerable time feeling sad that her fate is sealed. Drawing at the end of the turn is more
likely to be a positive in games like Scrabble where any draw will have some use, and less likely
where, as in Magic, a draw tends toward “success” or “failure.”
17. Monopoly tends to come in for a lot of criticism among game designers. (A highly popular
game that the “experts” all hate should be a warning flag for the thoughtful designer—if the
game is so bad, why do so many people like it? Some answer beyond “people are stupid” is
required.) While the game certainly has plenty of flaws, this one innovation, of exciting downtime in a turn-based multiplayer game, is enormously powerful and still not as widely appreciated
as it should be.

182

Chapter 6

one is spending an enormous amount of time waiting for others to take their turns,
turns that tend to be very long in a game originally designed with a one-player focus.18
Computer game players tend to be less tolerant of downtime in general. Partly this
is the faster pace of the computer world, and partly it is due to being accustomed to
the lack of downtime in the single-player computer game experience. But perhaps the
greatest part is due to the computer as a gaming interface: there are far fewer social
cues, less of a sense of another human being doing something rather than doing
nothing, less to watch as the other person is taking her turn, less of a sense as to how
the other player’s turn is progressing (is she thinking hard, or did she just leave and
get a cup of coffee?). Indeed, often most of what the other person is doing is not even
visible.
The computer enables various solutions to the downtime problem, though: automatic clocks are easy to build in, simultaneous turns are possible, real-time play is
possible. Strategy games are an interesting case: early on, turn-based single-player
strategy games against AI opponents were the norm (e.g., Civilization). The downtime
situation was good. But when made multiplayer, the downtime was awful. The RTS
was a solution to the downtime issue:19 no downtime at all, just keep doing what you
want! But now you are playing indoor soccer, with no resting of any kind allowed.
And the twitch skills required, in terms of clicks per minute, were out of reach of the
vast majority of players. One’s skill at the game was influenced more by one’s ability
to click quickly and efficiently and less by thinking strategically, at least at all but the
very highest levels of play (and those high levels of play absolutely required outstanding clicking skills). The whole situation was rather disheartening if you were originally
interested in playing a strategy game—the promise of “Civilization without waiting
around” was never entirely met. An interesting new genre of games arose, but one
with an awkward tension between fast clicking and strategic thinking.
Lastly, one interesting and unusual approach to downtime can be seen in poker.
Poker has a lot of downtime, which is bad for the enjoyment of the game. One indication that poker’s downtime is probably more than is optimal can be seen from the
tendency of many people to play multiple games simultaneously in online poker (not
many people want to play simultaneous games of online chess). But poker’s downtime
provides part of the economic engine on which the game is based: most players at the
low and intermediate levels probably play too many hands. Poker’s approach to down18. One of the authors still has nightmares about a particularly stressful game of multiplayer
Masters of Orion II in which he played against a much more experienced (and thus much faster)
and very irate opponent.
19. Except in the early phases of the game, where one had to wait, for example, for resources
to be gathered and buildings to finish. These problems weren’t too hard to fix, though; see
section 6.4 on busywork.

Player Effort

183

Figure 6.4
©iStockphoto.com/Gustaf Brundin

time is very capitalistic—you can always simply pay to eliminate your downtime, by
staying in a hand you shouldn’t be in. Many weaker players will occasionally call
simply because they have sat out several times in a row, and they want to have the
experience of being in a hand to the end.
Exercise 6.9: How much downtime is there in chess? For advanced players? For
beginners?
Exercise 6.10: Why are turn-based multiplayer games dominant in the world of
boardgames and card games and virtually nonexistent online?
Exercise 6.11: How does player elimination affect downtime differently in online
games versus party games?
6.4

Characteristic: Busywork

Busywork in games consists of the rote activities that the player must perform, which
are not part of what they would consider the fun of the game. As such, it is in principle
an agential characteristic, since what one person considers rote or boring another
might enjoy. In practice, though, much busywork is fairly clear from a systemic point
of view. For example, setting up the board before the game begins (or between rounds
for more complex boardgames), shuffling and dealing out the cards, adding up scores,
or making change in Monopoly all count as busywork.

184

Chapter 6

Busywork is like downtime in that the player is not “really playing,” with the difference that the player is doing something mindless rather than doing nothing at all.
If downtime is a player doing nothing, busywork is a player doing nothing much.
One way of attempting to decide what’s busywork is to look at the decisions
involved: if there aren’t any, or if they are arbitrary from the players’ point of view,
that’s busywork. In other words, players are not using any heuristics to do busywork.
In games where physical skill is relevant to victory, players can’t be using any of that
either for a task to count as busywork—basically, busywork can’t be done well or badly,
at least not in the sense of it affecting one’s chances of victory.
Activities that may eventually seem like busywork are rarely considered so when
players are first learning a game. This is because exploration provides interest before
a game’s limitations are well understood. Standards can accelerate a player’s identification of activities as busywork for themselves. For example, in the first RPG you ever
played it was probably more exciting to walk around the town finding armorers and
apothecaries than in later ones where the constant walking between them can become
numbing.
Busywork does not always have to be bad: some players might enjoy the feel of
