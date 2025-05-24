With discrete rules, it is possible to look ahead, to plan moves, and to create and
execute complex strategies. Although this isn’t always easy, it is possible, and many
players enjoy doing it. Players interact with discrete mechanics on a mental, strategic level. Once players grasp the physics of a game, they can intuitively predict
movements and results, but with less certainty. Skill and dexterity become a more
important aspect of the interaction. This difference is crucial for gameplay and can
be seen in a comparison between Angry Birds and World of Goo, two games that mix
physical mechanics with strategic gameplay.
In Angry Birds, players shoot birds from a catapult at defensive structures protecting
pigs (Figure 1.2). The catapult is operated with a touch device, and because the
physical simulation is so precise, a small difference in launch speed or angle can have
a completely different effect on the structural damage the player causes. Catapulting
the birds is mostly a matter of physical skill. The strategy in Angry Birds involves
those aspects of the game that are governed by discrete rules. Players have to plan
to attack the pigs’ defenses most effectively using the number and types of birds
available in the level. This requires identifying weak spots and formulating a plan
of attack, but the execution itself is based on hand-eye coordination, and the effects
can never be foreseen in great detail.

FIGURe 1.2
Angry Birds

desiGninG Game mechanics

ChAptEr 1

Compare the mix of strategy and skill in Angry Birds with a similar mix in World of
Goo (Figure 1.3). In World of Goo, players build constructions from a limited supply
of goo balls. The game includes a detailed physical simulation that controls the
player-built constructions. Physical phenomena such as gravity, momentum, and
center of mass play an important role in the mechanics of the game. Indeed, players
can form an intuitive understanding of these notions from playing World of Goo. But
more importantly, players learn how to manage their most important (and discrete)
resource, goo balls, and use them to build successful constructions. The difference
between Angry Birds and World of Goo becomes very clear when you consider the
respective effects of both games’ continuous, pixel-precise physics. In Angry Birds,
the difference of a single pixel can translate into a critical hit or complete miss.
World of Goo is more forgiving. In that game, releasing a goo ball a little more to the
left or right usually does not matter, because the resulting construction is the same,
and spring forces push the ball into the same place. The game even shows what
connections will be made before the player releases a ball (as shown in Figure 1.3).
You can see that the gameplay is more strategic in World of Goo than it is in Angry
Birds. World of Goo depends more on its discrete mechanics than on its continuous
mechanics to create the player’s experience.

11

FIGURe 1.3
World of Goo

12

Game mechanics: advanced Game desiGn

Innovating with Discrete Mechanics

N OT E The mechanistic perspective on
gameplay used in
this book is a narrow
one and focuses on
mechanics over many
other aspects of games.
it is what you might
call a mechanistic perspective on games and
gameplay. however, we
do not want to argue
that this is the only
perspective on games
or that it is the best
one. in many games,
art, story, sound, and
music, among other
features, contribute just
as much to the player’s
experience as gameplay
does. sometimes they
contribute even more.
But we wrote this book
to explore the relationship between game
mechanics and gameplay, and that is what
we concentrate on.

Discrete mechanics offer more opportunities for innovation than many of the current
forms of continuous mechanics do. As games and genres change, designers’ definitions
of physical mechanics are all evolving into a handful of directions that correspond
closely with game genres. Most of the time there is little point in completely changing the physics of a first-person shooter. In fact, as games increasingly use physics
engine middleware to handle these mechanics, there is less room to innovate in
that area. On the other hand, all designers want to offer unique content, and many
first-person shooters do include a unique system of power-ups, or an economy of
items to collect and consume, to make their gameplay different from their competitor’s. There is more room for creativity and innovation in the mechanics that
govern these economies than in the physics of the game. This book concentrates on
discrete mechanics.
Looking back at four decades of computer game history, it’s clear that game physics
have evolved much faster than any other type of mechanics in games. Physics are
comparatively easy to design because of the clarity of Newton’s laws and the increasing computing power to simulate them. The laws of economics are far more complex
and difficult to work with. In this book, we hope to give you a solid theoretical
framework for nonphysical, discrete mechanics to make it easier.

Mechanics and the Game Design Process
There are almost as many different ways to design a game as there are game companies. In Fundamentals of Game Design, Ernest Adams advocates an approach
called player-centric game design, which concentrates on the players’ roles and the
gameplay that they will experience. Adams defines gameplay as consisting of the
challenges the game imposes on the player and the actions the game permits the
player to perform. The mechanics create the gameplay. When Mario jumps across
a canyon, the level design may define the shape of the canyon, but it is the game’s
laws of physics—its physical mechanics—that determine how far he jumps, how
gravity behaves, and whether he succeeds or fails.
Because the mechanics generate the gameplay, we encourage you to start designing
the mechanics as soon as you know what gameplay you want to offer. The development process outlined in this section is player-centric game design with an extra
emphasis on creating complex, but balanced, game mechanics.

Outlining the Game Design Process
Roughly speaking, the process of designing a game goes through three stages: the
concept stage, the elaboration stage, and the tuning stage. These stages are discussed
next, but you can find more details about these stages in Fundamentals of Game Design.

desiGninG Game mechanics

13

During the concept stage, the design team will decide on the game’s general idea, the
target audience, and the player’s role. The results of this phase will be documented
in a vision document or a game treatment. Once you have made these key decisions,
you should not change them throughout the remainder of the design process.
In the concept stage, you might create a very quick, experimental version of the game’s
basic mechanics just to see if it produces fun gameplay, if you are not certain what
kind of game you want to make. These proof-of-concept prototypes can also help you
pitch your design vision to the rest of the team or to a funding agency, or playtest
key assumptions. However, you should assume that you will throw this work away
and do it again from scratch in the elaboration stage. This will enable you to work
faster in the concept stage, without worrying if you create something buggy. You
should not start to design the real, final mechanics until this stage is over, because
your plans may change and it would be wasted effort.

eLaBOraTiOn sTaGe
During the elaboration stage—which usually begins once the project has been
funded—the development of the game goes into full swing. During this phase, you
will create game mechanics and levels, draft the story, create art assets, and so on.
It is vital that during this phase the development team works in short, iterative
cycles. Each cycle will produce some playable product or prototype that must be
tested and evaluated before the design can move on. Do not expect to get everything
right the first time. You will have to redesign many features during this stage. It’s a
good idea to get players representative of the audience from outside your team to
playtest parts of your game during this stage, too. When a prototype is playtested
only by members of the development team, you will not get a good idea of how real
players will eventually play and approach the game. Your development team may
fall outside the game’s target audience, and they generally know the game too well
to be good test subjects.

TUninG sTaGe
The tuning stage starts with a feature freeze. At this point, you will decide as a team
that you are happy with the game’s feature set and you are not going to add any
more features. Instead, you focus on polishing what you have. Enforcing a feature
freeze can be difficult: You are still working on the game, and you will invariably
come up with some new clever ideas you did not think of during earlier stages.
However, at this late stage of development, even small changes can have devastating unseen effects on the game and add significantly to the debugging and tuning
process—so don’t do it! If anything, the tuning stage is a subtractive process: You
should take out anything that does not work, or has little value for the game, and
focus the design on the things that do work to make it really shine. In addition,

ChAptEr 1

cOncePT sTaGe

14

Game mechanics: advanced Game desiGn

when planning a game project, it is easy to underestimate how much work tuning
actually is. In our experience, polishing and tuning can take anywhere between onethird and half of the entire development time.

documentinG desiGns
Game design documents are used to record designs as games are being built. every
game company has its own standard for these documents, and every game company uses
them in a different way. Typically, a game design document starts with a brief description of the game’s concept, target audience, core mechanics, and intended art style.
many companies keep the design document up-to-date. every mechanism that is added
and level that gets designed will be added to the document. For this reason, design
documents are often called living documents: They grow as the game grows.
documenting the design process is important for many reasons: Writing down goals
and vision will help you keep on track during later stages of development. Writing down
your design decisions during development will prevent you from having to reconsider
past decisions over and over again. Finally, when working in a team, it is very useful to
have one document that specifies the collective goal. This reduces the chances that the
team effort diverges and that you waste too much energy on features that end up being
incompatible.
For now, we suggest that you do get into the habit of documenting your design by
whatever method works best for you. You’ll find a longer discussion and some useful
templates for design documents in Fundamentals of Game Design.

Designing Mechanics early On
Game mechanics are not easy to create. We advise that you start working on your
game’s mechanics early in the elaboration phase. There are two reasons for this:
Gameplay emerges from game mechanics. It is difficult, if not impossible, to tell
whether your gameplay will be fun simply by looking at the rules. The only way to
find out whether your mechanics work is by playing them or, even better, by having
somebody else play them for you. To make this possible, you may need to create a
number of prototypes. We will go into this in more detail in later chapters.

n

The game mechanics that we focus on in this book are complex systems; gameplay relies on a delicate balance within this system. Once you have mechanics that
work, it is easy to destroy that balance by adding new features late in the development process or by making changes to existing mechanisms.

n

Once you have the core mechanics working and you are sure they are balanced and
fun, you can start working on levels and art assets to go with them.

desiGninG Game mechanics

15

Game designer Kyle Gabler gave a video keynote for the first Global Game Jam in 2009.
in his talk, he gave seven useful tips to help develop a game in a short time span. These
tips are so useful that we suggest they apply to most game development projects, no
matter how much time there is.
One tip, which is very relevant for our discussion here, is make the toy first. Gabler suggests that before you spend any time on creating assets and content, you have to make
sure that your mechanics work. This means you should start by building a prototype or
proof of concept for those mechanics. The mechanics should be fun to play around with,
even without nice art, clear goals, or clever level design. in other words, you need to
design a toy that is fun to interact with in its own right and build the game from there.
Obviously, we agree, and we suggest that you follow Gabler’s advice.
You can find Gabler’s full (and witty) keynote online: www.youtube.com/
watch?v=aW6vgW8wc6c.

Getting It Right
As mentioned, to get game mechanics right, you must build them. The methods
and theory described in this book will help you understand how mechanics work,
and they will include new, efficient tools to create early prototypes, but they can
never be a substitute for the real thing. You must build prototypes and iterate as
much as you can to create games with balanced, novel mechanics.

Prototyping Techniques
A prototype is a preliminary, usually incomplete, model of a product or process
created to test its usability before building the real thing. Because prototypes don’t
have to be as polished as the final product, they are (usually) quicker and cheaper
to construct and modify. Game designers create prototypes of games to test their
mechanics and gameplay. Some of the more common prototyping techniques that
game designers use are software prototypes, paper prototypes, and physical prototypes.

A Few Terms
Over the years, software developers have devised a number of terms to describe different types of prototypes. A high-fidelity prototype resembles the intended product
closely in many ways. In some cases, a high-fidelity prototype ends up being refined
into the final product. A high-fidelity prototype is relatively time-consuming to build.

ChAptEr 1

make the toy First

16

Game mechanics: advanced Game desiGn

In contrast, a low-fidelity prototype is quicker to build and does not need to resemble
the end product as closely. A low-fidelity prototype typically uses a different technology from that used in the end product. You might use a 2D Flash game to
prototype a 3D console game, or you could even use PowerPoint to create an interactive storyboard for a game. Developers build low-fidelity prototypes to test ideas
quickly, and these prototypes tend to be focused on one particular aspect of the game.
Developers also create a vertical slice of the intended product with their prototype.
The term comes from a visual representation of a software project, as shown in
Figure 1.4. A vertical slice is a prototype that includes all the elements (code, art,
audio, and anything else) required to implement one or a small number of features
of a game. Vertical slices are useful for testing the moment-by-moment gameplay
of a game and to give people an impression of your game while not showing the
complete product. A horizontal slice is a prototype that includes all the parts of some
aspect of the game but none of the others. For example, a horizontal slice might
include a complete user interface but no functioning mechanics.

FIGURe 1.4
vertical and horizontal slices
of a game project

Software Prototyping
If you want to get a sense of how your video game will feel to your players, the best
way is to create a software prototype that approximates your designs, as quickly
as possible. To speed the prototyping process, it sometimes is a good idea to use

desiGninG Game mechanics

17

The advantage of using software prototypes is that you can get a good indication
of the gameplay of your game, even if the art is only temporary and the features
might be buggy or incomplete. However, the disadvantage is that creating software
prototypes takes longer than creating the other kinds. Depending on the available
options and the skills of your development team, it might take almost as long as
making the real game. Still, it is a good idea to build software prototypes, even if
you end up throwing away all the art and code that was produced for them. Having
an early software prototype will help keep the project on course. Programmers will
know what type of game elements are needed, level designers will have an idea of
the direction the design takes, and game designers will have an environment to play
around in and test ideas. Software prototypes function almost as design documents:
The development team can refer to the prototype when building the real thing. The
prototype can illustrate some aspects of a game, such as interactive features, better
than a description in words can.
One critical factor of a successful software prototype is easy customization of the
game within the prototype. When a game’s gravity is vital for the gameplay of your
3D platformer, make sure designers can change the setting easily during play in
order to get a feel for what works best. If you have a factory producing resources for
a real-time strategy game, make sure you can change the production rate easily in
order to find the right balance quickly. Don’t waste time creating a fancy user interface for this; store key initial values in a text file that the program reads when it
starts up. This way, the designers can play with the values simply by editing the file
and rerunning the program. Or even better, include a simple, off-the-shelf console
in your game that allows you to make changes while playing the game. This will
speed up your development-test cycle even more.

Paper Prototyping
Because software prototypes are relatively slow and expensive to create, more and
more game studios are using paper prototyping techniques. A paper prototype is a
noncomputerized, tabletop game that resembles your game. Some game mechanics
are media-independent. If your game does not rely too heavily on precise timing,
physics, or other computation-intensive mechanics, you should be able to create a
board game from your video game concept. If your game does rely heavily on computation-intensive mechanics, it can still be worth your time and effort to create a
paper prototype for those aspects of the game that don’t. Remember, a prototype
typically zooms in on a particular aspect of the game, and you just might want to
zoom in on the internal economy of a game that otherwise derives most of its gameplay from its extended physics simulation. It’s important to know what aspect you
want to explore before you start designing a paper prototype.

ChAptEr 1

open-source game engines or game development environments such as GameMaker
or Unity, even if your target platform will be something completely different.

T I P many of the
prototypes for Spore
are published online:
www.spore.com/comm/
prototypes. We suggest
you download a few
and play them for yourself. These prototypes
will give you an unique
insight in the development process for a
triple-a title by a professional game studio.

18

Game mechanics: advanced Game desiGn

Paper prototyping is not trivial. Designing good board games is an art in itself, at
least as difficult as designing a good video game. It helps if you are familiar with a
wide variety of board games yourself. There are many more board game mechanics
than “role a die and move that many spaces.”

a Good paper prototypinG kit
corvus elrod, a professional game designer, recommends keeping the following items
together to use as a prototyping kit:
• Two near-identical decks of cards with different colored backs.
• A small notebook (not too big or it becomes distracting). Good pencils or pens, obviously.
• Tokens of some sort—poker chips, Go stones, or similar.
• Several dice; it doesn’t really matter how many sides they have, and you don’t need
a large number. if you design your mechanics using percentages, then two ten-sided
dice are useful for generating random numbers from 1 to 100 (elrod 2011).
To this we might also add the following:
• A pad of sticky notes
• A batch of blank cards, 3x5 or similar
We also recommend you add some card sleeves to your paper prototyping kit. card
sleeves are plastic sleeves that players sometimes use to protect cards for trading card
games such as Magic: The Gathering. They can be purchased from any specialist game
store. You can simply slide a marked piece of paper into the sleeve to create a playing
card that is easy to shuffle and handle. an additional benefit is that you can easily slide
in revisions on top of old cards. That way, the design history of your cards is preserved.
With these items, you have a way of generating random numbers, some tokens you can
use to represent the numbers (in a poker game, poker chips stand for money), some
blank materials for designating all sorts of things, possibly including a game board, and
a notebook to write down your ideas in. That’s really all you need to get started.

Paper prototyping has two important advantages: It is fast, and a paper prototype
is inherently customizable. Paper prototypes are quick to make because they do
not need to be programmed. When creating a paper prototype, you should not
waste time on creating nice art for cards or boards; instead, you should spend your
time drafting rules and testing them. With some skill and experience, you can put
together a decent paper prototype for any game in a matter of hours. That leaves
you a lot of time to start playtesting and balancing the mechanics.
With a paper prototype, it is easy to change the rules. You can even do this on
the fly. If during play you notice something does not work as intended, change it

desiGninG Game mechanics

19

immediately. This way, you can almost create the game as you play. Iteration cycles
do not get shorter than this.

ChAptEr 1

Paper prototyping has two disadvantages: It is more difficult to involve test players, and not all mechanics translate to board games easily. If you are going to test a
paper prototype with new players, you will need to explain the rules to them yourself—it’s not worth the time to write them down, because you’ll be changing them
all the time. In addition, test players, especially if they have little testing or board
game experience, might find it difficult to see how your paper prototype is related to
a video game.
More problematic is that not all mechanics translate to paper prototypes easily. As
we mentioned, mechanics that deal with a game’s physics are difficult to translate.
Continuous mechanics, which are computationally intensive, really need to be
implemented on a computer. This is something to take into account when creating
a paper prototype: It is best used to test discrete mechanics. Paper prototyping is
more suited to designing mechanics that govern a game’s economy or progression.

Physical Prototyping
Prototyping is not restricted to creating software or paper games; simply drafting
rules and playing the game out in real life can be just as effective. This is especially
true when a game has many continuous, physical mechanics. Running around an
office building armed with laser-tag guns can give you a fairly good idea of what a
first-person shooter game might feel like. Most of the time, this requires even less
preparation than paper prototyping. As with paper prototyping, physical prototyping is fast and adaptable. Some game designers mix physical and paper prototyping
techniques to great effect. However, again as with paper prototyping, physical prototyping is not easy: Getting it right requires some skill and expertise from both
designers and players.

Prototype Focus
Apart from choosing the appropriate medium for your prototype, another critical
aspect of effective prototyping is finding the right focus. Before you start building
a prototype, you must ask yourself what you intend to learn from the exercise. If
you are trying to find out something about the balance of the economy, you will
need a different prototype from one intended to test a new user interface. Look
at the prototypes of Spore (www.spore.com/comm/prototypes). Each was created for a
specific reason.
Choosing a single focus should help you create prototypes faster. If you are focusing
on one aspect, you do not have to prototype the entire game. A tight focus should
also help you get the right feedback from test players: They will be less distracted by
features (or bugs) that are unrelated to the issue you are studying.

T I P To appreciate the
opportunities offered
by physical prototyping,
it can be a good idea
to join (or observe) a
live-action role-play
(LarP) session. LarPers
employ a wide variety
of techniques to deal
with physical combat
safely and have come
up with ways to include
things that are not part
of our physical reality,
such as magic spells.
Because LarP takes
place in a specific location, you will have to
find a LarP community
near you. The website
http://larp.meetup.com
lists a few.

20

Game mechanics: advanced Game desiGn

A prototype’s focus affects the choice of prototype technique. If you are trying to
design a balanced economy of power-ups in a physical platform game, a paper
prototype can work even though physics are hard to reproduce as a board game.
However, if you are trying control schemes with a new input device, you will need a
high-fidelity, software prototype that is close to the real game.
The following aspects of game design are typical focuses for prototyping, loosely
ordered from early to later prototypes:
Tech demos. It is always a good idea to make sure you or the team of programmers can actually deal with the technology involved. For a tech demo, you should
try to tackle the most difficult and most novel aspect of the game technology and
prove to yourself, and ideally a publisher too, that you can build the game. Tech
demos should be built early to prevent surprises during later stages of development.
While building a tech demo, keep an eye out for interesting gameplay opportunities. Especially when you are working with novel technology, quickly building
something simple can lead to deeper insights later.

n

Game economy. A game’s economy revolves around a number of vital resources.
You can prototype a game economy with low-fidelity, paper prototyping techniques;
this is best done early during the design process. The following are typical playtest
questions: Is the game balanced? Is there a dominant strategy that wins all the time?
Do the players have interesting choices? Can they sufficiently forsee the consequences
of their choices? Getting the right players for a game economy playtest is important. You and your team are good test subjects, although you will be handicapped
because you have an idea of how the game is intended to be played. In general, the
ideal test player for this type of prototype is an experienced power gamer who can
quickly grasp the mechanics and has experience in finding and using exploits. Make
sure you ask them to try to break the game. If it can be broken, you should know.

n

Interface and control scheme. To find out whether players can control your
game, you must have a software prototype of your game. The prototype does not
need to have much content or complete levels; rather, it is a playground where players can try most of the game’s elements and interactions. These are typical playtest
questions: Can players perform the actions you offer them correctly? Are there other
actions they want or need? Are you giving them the information they need to make
correct decisions? Is the control scheme intuitive? Do the players have the information they need to play? Do they notice they are taking damage or that a vital game
state has changed?

n

desiGninG Game mechanics

Tutorials. To build a good tutorial, the game must be in its later stage of development. After all, nobody wants to waste time and resources to build a tutorial for
game mechanics that still might change. When testing a tutorial, it is important
your test players have not seen your game before. In many ways, developing a game
is like a long and detailed tutorial: Developers spend many hours tweaking mechanics, and during this time, they play a lot. It is easy to forget how skilled you have
become at your own game. Therefore, you cannot trust your own judgment of the
game’s initial difficulty and learning curve. You really need new players for that, and
while they play, do not interfere with their learning process. The most important
question for a tutorial prototype is this: Do my players understand the game and
how it should be played?

21

reFerence Games: Free prototypes
sometimes the most efficient way to prototype your game is to look at existing games
and use them as a model for your project. This way, you can take advantage of a lot of
work done by others. This is especially true of user interface design, controls, and basic
physics, in which players want consistency from game to game. There’s no point in
changing the traditional Wasd control scheme for first-person Pc games to esdF instead,
just for the sake of innovation.
Obviously, you should not steal designs, but there is no harm in learning from others or
avoiding mistakes they made. When picking reference games for your project, pay attention to the project scope. if you have only a couple of months to develop your game, don’t
pick a reference game that was created by a large professional team over a period of
years. Try to choose reference games that are similar in size and quality to the game you
plan to make, unless you are using the reference only to study a particular detail in the
game interface or mechanics.

Summary
Game mechanics are the precisely specified rules of a game, including not only
the entities and processes at the heart of the game but also the data necessary to
execute those processes. Mechanics may be categorized as continuous or discrete.
Continuous mechanics are usually implemented in real time, with many floatingpoint calculations every second, and are most often used to implement physics in a
game. Discrete mechanics may or may not operate in real time, and they use integer
values to implement a game’s internal economy. It is imperative to begin designing
game mechanics early, so you can create prototypes to playtest.

ChAptEr 1

n

22

Game mechanics: advanced Game desiGn

Particular structures exist in game mechanics that contribute strongly to emergent
gameplay. In the following two chapters, we will explore this structural perspective
on game mechanics in more detail, and we will use that perspective to create a practical method and design tool to help design game mechanics.

Exercises
1. Practice your prototype skills. Translate an existing video game to a paper
prototype.

2. Find a relevant reference game for a game that you want to build. Explain what
aspect of the reference game is useful in illustrating the kind of game you have
in mind.

3. Find examples of discrete mechanisms and continuous mechanisms in a published game for each of the five types of game mechanism described in this chapter
(physics, internal economy, progression, tactical maneuvering, and social interaction). Don’t use any of the examples given in this chapter.

ChAptEr 2
Emergence and
progression
ChAptEr 2

In the previous chapter, we introduced five types of game mechanics: physics, internal economy, progression, tactical maneuvering, and social interaction. Of these
categories, the mechanics of progression create what in game studies are called
games of progression. The other four types of mechanics correspond fairly well to
another category, games of emergence. For ease of reference, we will call the other
four types of mechanics mechanics of emergence in this chapter.
The two categories of games of emergence and games of progression are considered
important, alternative ways of creating gameplay. In this chapter, we explore this
important distinction in more detail and provide examples of each category. We also
explore the structural differences in the mechanics that generate emergence and
progression and the problems and opportunities they create when a designer tries
to integrate emergence and progression in a single game.

The History of Emergence and Progression
The categories of emergence and progression were originally introduced by game
scholar Jesper Juul in his paper “The Open and the Closed: Games of Emergence and
Games of Progression” (2002). Put simply, games of emergence are those games that
have relatively simple rules but much variation. We use the term emergence because
the game’s challenges and its flow of events are not planned in advance but emerge
during play. Emergence is produced by the many possible combinations of rules
in board games, card games, strategy games, and some action games. According
to Juul, “Emergence is the primordial game structure” (p. 324); that is, the earliest
games were games of emergence, and in creating a new game, many people begin
with emergent designs.
Games of this type can be in many different configurations, or states, during play.
All possible arrangements of the playing pieces in chess constitute different game
states, because the displacement of a single pawn by even one square can make a
critical difference. The number of possible combinations of pieces on a chess board
is huge, yet the rules easily fit on a single page. Something similar can be said of the
placements of residential zones in the simulation game SimCity or the placement of
units in the strategy game StarCraft.

23

24

Game mechanics: advanced Game desiGn

emerGence and proGression outside Video Games
in Juul’s categorization, all board games are games of emergence. Games that start with
randomized elements, such as cards or dominoes, also qualify. such games typically
have a small number of pieces and little or no predesigned data. The text on Monopoly’s
chance and community chest cards are examples of predesigned data, but they require
less than 1KB to store.

T I P don’t confuse
the term games of
progression with other
ideas about progression in games, such as
leveling up, difficulty
curves, skill trees, and
so on. We use Juul’s
definition of the term:
a game of progression
is one that offers predesigned challenges,
each of which often has
exactly one solution, in
a fixed (or only slightly
variable) sequence.

a game of progression requires a large amount of data, prepared in advance by the
designer, that the player can access at arbitrary points (called random access). This is
inconvenient for board games but easy for video games now that they can store many
gigabytes of data. Progression is the newer structure, starting with the text-adventure
games from the 1970s. however, progression is not limited to games running on computers.
Pen-and-paper role-playing games like Dungeons & Dragons offer published scenarios,
and these scenarios also constitute games of progression, as do the books in the choose
Your Own adventure book series. Books are another medium that can handle a large
amount of data and offer easy random access.

In contrast, games of progression offer many predesigned challenges that the
designer has ordered sequentially, usually through sophisticated level design.
Progression relies on a tightly controlled sequence of events. A game designer dictates the challenges that a player encounters by designing levels in such a way that
the player must encounter these events in a particular sequence. According to Juul,
any game that has a walkthrough is a game of progression. In its most extreme
form, the player is “railroaded” through a game, going from one challenge to the
next or failing in the attempt. In a game of progression, the number of game states
is relatively small, and the designer has total control over what is put in the game.
This makes games of progression well suited to games that tell stories.

Comparing Emergence and Progression
In his original article, Juul expresses a preference for games that include emergence:
“On a theoretical level, emergence is the more interesting structure” (2002, p. 328).
He regards emergence as an approach that allows designers to create games in which
the freedom of the player is balanced with the control of the designer. In a game of
emergence, designers do not specify every event in detail before the game is published, though the rules may make certain events very likely. In practice, however,
a game with an emergent structure often still follows fairly regular patterns. Juul
discusses the gun fights that almost always erupt in a game of Counter-Strike (p. 327).
Another example can be found in Risk, in which the players’ territories are initially
scattered all over the map, but over the course of play their ownership changes, and
the players generally end up controlling one or a few areas of neighboring territories.

emerGence and PrOGressiOn

25

data and process intensity

In his later book Half-Real, Juul is more nuanced in his discussion of emergence and
progression (2005). Most modern video games are hybrids; they include some features of both. Grand Theft Auto: San Andreas provides a vast open world but also has
a mission structure that introduces new elements and unlocks this world piece by
piece. In the story-driven first-person shooter game Deus Ex, the storyline dictates
where the player needs to go next, but players have many different strategies and
tactics available to deal with the problems they encounter on the way. It is possible to write a walkthrough for Deus Ex, which would make it a game of progression
according to Juul’s classification, but there are many possible walkthroughs for Deus
Ex—just as, at least in theory, it is possible to create a walkthrough for a particular
map in SimCity, instructing the player to build certain zones or infrastructure at a
particular time in order to build an effective city. It would be hard to follow such a
walkthrough, but creating one is possible.
Emergence is not better than progression. They are simply different. Pure games of
emergence and pure games of progression represent two extremes on a bipolar scale.
Many casual games, such as Bejeweled, are pure games of emergence. Pure games
of progression are fairly rare. The most typical examples are adventure games such
as The Longest Journey, but they are no longer the dominant genre they once were.
Other games include elements of both, often by exhibiting emergent behavior
within a given level but offering their levels in a strict sequence from which the
player cannot depart (progressive behavior). Today, action-adventure games such
as Half-Life and the Legend of Zelda series are much more common than traditional
adventure games: Action-adventures include some form of emergent action as part
of the gameplay. Among large games, hybrid forms are the most popular.

ChAptEr 2

The game designer chris crawford’s notions of process intensity and data intensity apply
to progression and emergence in games. computers differ from most other gaming media
because computers are good at processing numbers. computers also allow fast access
to random locations within a large database, an ability put to good use within games
of progression. But it is the ability to create new content on the fly and handle complex
simulations where computers really shine. Like no other medium before, computers have
the capacity to surprise players and designers with clever simulations and emergent
gameplay. crawford believes games should capitalize on this ability of the computer:
Games should be process-intensive, rather than data-intensive. he says that video games
should be games of emergence rather than games of progression.

26

Game mechanics: advanced Game desiGn

Games of Emergence
The use of the term emergence in games, which predates Juul’s categories, originates
from the use of the term in complexity theory. There it refers to behavior of a system
that cannot be derived (directly) from its constituent parts. At the same time, Juul
cautions us not to confuse emergent behavior with games that display behavior the
designer simply did not foresee (2002). In games, as in any complex system, the
whole is more than the sum of its parts. Go and chess are famous for generating
enormous depth of play with relatively simple elements and rules. Something similar
can be said of relatively simple computer games such as Tetris, Boulder Dash, or World
of Goo. These games consist of relatively simple parts, yet the number of strategies
and approaches that they allow is enormous. No two play-throughs will feel the
same. The emergent quality of the gameplay comes not from the complexity of
individual parts but from the complexity that is the result of the many interactions
among the parts.

Simple Parts in Complex Systems
The science of complexity studies all manner of complex systems in real life. While
the active agents or active elements in these complex systems can be quite sophisticated in themselves, they are typically simulated with simple models. For example,
to study the flow of pedestrians in different environments, great results have been
achieved by simulating pedestrians with only a few behavioral rules and goals (Ball,
2004, pp. 131–147). In this book, we take a similar approach to games. Although
it is possible to create emergent games with a few complex elements, we are more
interested in the mechanics of game systems that work with simple parts but still
create emergent gameplay. The advantage of our approach is that, in the end, these
games are efficient to build, even if they are initially more difficult to understand.

probability space
in the previous chapter, we mentioned that games are often regarded as state machines:
hypothetical machines that progress from one state to another based on their current
state and the input provided by players. in games, the number of states can grow very
fast, and yet not every state is possible. not every random placement of pieces on a chess
board represents a game state that can be reached through actual play. For example, it
is not possible to have pawns in your color on the row closest to you in a real game or
to have both your bishops on a square of the same color. When the number of possible
states is very large, game scholars refer to them collectively as a probability space. The
probability space represents all the possible states that can be reached from the current
state. The probability space can be described as having a wide or a deep shape. When
the shape of the space is wide, there are many different states that can be reached from
the current state: Usually this means that players have many options. if the shape is
deep, there are many different states that can be reached after many subsequent choices.

emerGence and PrOGressiOn

27

C. E. Shannon, in his early paper “Programming a Computer for Playing Chess,”
estimated that there are more possible game states in games like chess and Go than
there are atoms on earth (1950). The rules of the game determine the number of
possible states, but it is not necessarily true that more rules will lead to more possible states. In addition, when a game can create a large number of possible states
without using many rules, the game will be more accessible to players.

When we speak of the path players take through the possible states of a game—its
probability space—we sometimes describe this path as a trajectory. The possible game
states and play trajectories through a game are emergent properties of the game
rule system. Games that allow many different, interesting trajectories arguably have
more gameplay than games that generate fewer trajectories or less interesting ones.
However, determining the type and quality of the gameplay is hard, if not impossible, by simply looking at the rules. Comparing the rules of tic-tac-toe and Connect
Four serves as a good illustration of these difficulties. The rules for tic-tac-toe are
as follows:

1. The game is played on a three-by-three grid.
2. The players take turns to occupy a square.
3. A square can be occupied only once.
4. The first player to occupy three squares in a row (orthogonally or diagonally) wins.
The rules for Connect Four are as follows (with the differences emphasized):

1. The game is played on a seven-by-six grid.
2. The players take turns to occupy a square.
3. A square can be occupied only once.
4. Only the bottom most unoccupied square in a given column can be occupied.
5. The first player to occupy four squares in a row (orthogonally or diagonally) wins.
While there are only a few differences in the rules for these two games, the differences in gameplay are immense, much greater than the amount of mental effort
needed to understand the rules. In the commercially available version of Connect
Four, the most complicated rule (number 4) is enforced by gravity: A player’s token
will automatically fall to the lowest available space in the upright playing area (see
Figure 2.1). This relieves players from manually enforcing this rule and allows them
to focus on the rule’s effects instead. Despite the small difference in the complexity
of the rules, tic-tac-toe is suited only for small children, whereas Connect Four can
also be enjoyed by adults. The latter game allows many different strategies, and
it takes much longer to master the game. When two experienced players play the

ChAptEr 2

Gameplay and Game States

28

Game mechanics: advanced Game desiGn

game, it will be an exciting match, instead of a certain draw as is the case with
tic-tac-toe. It is hard to explain these differences just by looking at the differences
in the rules.

FIGURe 2.1
in Connect Four,
gravity makes sure
players can occupy
only the bottom most
unoccupied square
in each column.
(image by permission
of Wikimedia
commons contributor
Popperipopp under
a creative commons
3.0 license.)

example: Civilization
Sid Meier’s Civilization is a good example of a game of emergence. In Civilization,
you lead a civilization as it evolves over roughly six millennia. During the game,
you build cities, roads, farmlands, mines, and military units. You need to upgrade
your cities by building temples, barracks, courthouses, stock markets, and so on.
Cities produce money that you use to research new technology, to convert into
luxuries to keep the population happy, or to speed up the production of units and
upgrades. Civilization is a turn-based game set on a tile-based map, with each turn
representing a number of years of your civilization’s history. The choices you make
determine how fast your civilization will grow, how sophisticated its technology is,
and how powerful its military. Several other computer-controlled civilizations compete with you for space and resources on a finite map.
Civilization is a large game with many different game elements. However, the individual elements are surprisingly simple. The mechanics for city upgrades can easily
be expressed with a few simple rules. For example, a temple costs one gold per turn
and will reduce the number of unhappy citizens in a city by two. Units have simple

emerGence and PrOGressiOn

29

integer values representing the number of tiles they can move and their respective
offensive and defensive strengths. Some units have special capabilities. For example,
settlers can be used to build new cities, and artillery can be used to bombard enemy
units from a distance. Terrain modifies the capabilities of units. Mountains cost
extra movement points to cross but also double a unit’s defensive strength. Players
can build roads to negate the extra movement costs imposed by mountains.

inspecting Civilization reveals that most of its mechanics are discrete: The game is turnbased, the positions of units and locations of cities are restricted to tiles, and offensive
and defensive strength is represented with whole numbers. Because the mechanics are
discrete, they are easy to understand individually. You can, in principle, do all of the calculations to work out their effects in your head. still, the probability space of Civilization
is huge. Civilization is an excellent example of creating enormous variety with relatively
simple discrete mechanics that invite players to interact with the game on a strategic level.

A complete description of all the mechanics of Civilization easily fills a book, especially if all the details of all unit types and city upgrades are listed. The game comes
with its own encyclopedia to provide access to all these details. However, all these
elements are easy to understand. And more importantly, there are many relations
between the elements: Units are produced in cities, consuming vital resources that
could have been used toward other ends. After a unit is produced, you will often
have to pay gold for its upkeep every turn. Building roads also requires an investment in time and resources, but it allows you to deploy your forces more efficiently,
which reduces the need to keep a large military. You can also invest in researching
new technology to make sure your units are stronger than those of your opponent.
In short, everything in Civilization is connected to almost everything else. This
means that the choices you make will have many effects, sometimes unforeseen
ones. Building a strong military early on allows you to capture a larger part of the map
but will take a toll on other developments, which might set you back in the long
term. To add to the complexity, the choices made by the civilizations surrounding
yours will influence the effectiveness of your strategies.
There are many different strategies to play Civilization, and players often have to
switch between strategies as the game progresses. Early on, it is important to capture
territory so that your civilization can expand quickly. It also helps to develop technologies quickly so that you can identify and capture vital resources during this stage.
Once you encounter other civilizations, you can attack them or befriend them. In
the early stages of the game, it is easier to conquer other civilizations completely.
Later in the game this will be much harder, and other strategies work better. When
your civilization is wealthy and your neighbor is not, you can start a cultural offensive to persuade neighboring cities to join your realm. The game often progresses
through a number of distinct phases: early expansion, investing in your economy,

ChAptEr 2

the mechanics oF Civilization are discrete

30

Game mechanics: advanced Game desiGn

