Characteristics of Games

Characteristics of Games

George Skaff Elias, Richard Garfield, and K. Robert Gutschera

foreword by Eric Zimmerman

drawings by Peter Whitley

The MIT Press
Cambridge, Massachusetts
London, England

© 2012 Massachusetts Institute of Technology
All rights reserved. No part of this book may be reproduced in any form by any electronic or
mechanical means (including photocopying, recording, or information storage and retrieval)
without permission in writing from the publisher.
For information about special quantity discounts, please email special_sales@mitpress.mit.edu
This book was set in Stone Sans and Stone Serif by Toppan Best-set Premedia Limited. Printed
and bound in the United States of America.
Library of Congress Cataloging-in-Publication Data
Elias, George Skaff.
Characteristics of games / George Skaff Elias, Richard Garfield, and K. Robert Gutschera ;
foreword by Eric Zimmerman ; drawings by Peter Whitley.
p. cm.
Includes bibliographical references and index.
ISBN 978-0-262-01713-8 (hardcover : alk. paper)
1. Games—Design and construction. 2. Games—Rules. 3. Game theory. I. Garfield, Richard.
II. Gutschera, Karl Robert, 1964– III. Title.
GV1230.E38 2012
793—dc23
2011031296
10

9

8

7

6

5 4

3

2 1

To Sadie, Ike, and Lucy, to Terry and Schuyler, and to Karl and Deborah Gutschera
And to the memory of Martin Gardner

Contents

Foreword ix
Preface xiii
Acknowledgments

Introduction
1

Basics

xvii

1

11

1.1 Characteristic: Length of Playtime

11

1.2 Characteristic: Number of Players

21

1.3 Characteristic: Heuristics

2

Multiplayer Games

29

37

2.1 Characteristic: Player Elimination
2.2 Characteristic: Interactivity

3

2.3

Characteristic: Politics

2.4

Characteristic: Kingmaking

2.5

Characteristic: Teamwork

Infrastructure

38

44

48
56
61

71

3.1 Characteristic: Rules

71

3.2

Characteristic: Standards

76

3.3

Characteristic: Outcomes

82

3.4

Characteristic: Ending Conditions

86

3.5 Characteristic: Positional Asymmetry
3.6 Characteristic: Sensory Feedback

4

Games as Systems

92

96

101

4.1 Characteristic: Abstract Subgames and Essential Games
4.2 Characteristic: Snowball and Catch-Up

101

106

4.3 Characteristic: Complexity Tree Growth and Game Arc
4.4 Characteristic: Game Balance and Strategic Collapse

120
129

viii

5

Contents

Indeterminacy

137

5.1 Characteristic: Randomness

6

5.2

Characteristic: Luck and Skill

5.3

Characteristic: Hidden Information

Player Effort

150

167

6.2

Characteristic: Rewards

6.3

Characteristic: Downtime

6.4

Characteristic: Busywork

6.5

Characteristic: Reward/Effort Ratio

Superstructure

174
178
183

203

7.2

Characteristic: Conceit/Motif

7.3

Characteristic: Spectation

212

7.4

Characteristic: Game Customization

220

7.5 Characteristic: Misbehavior

231

7.6

238

Characteristic: Play Lifetime

Appendixes

189

203

7.1 Characteristic: Metagame

8

161

167

6.1 Characteristic: Costs

7

137

226

245

Appendix A: Von Neumann Game Theory

245

Appendix B: Combinatorial Game Theory

255

Appendix C: List of Games
Bibliography
Index
305

301

271

Foreword

When Richard, Robert, and Skaff approached me about writing the foreword for their
book and I cracked the first pages of the manuscript, I must admit I was taken by
surprise. The book they had written goes against the grain.
Unlike the spate of publications about games hitting shelves over the last few years,
Characteristics of Games is not brimming with promises about how games are going to
change the world. This book is not going to tell you how games are going to revolutionize education, business, society, or other aspects of Life as We Know It.
There is nothing wrong with those kinds of books. But they often miss the trees
for the forest. In promising a grand purpose and glorious future for games, they generally neglect to look closely at games themselves.
Characteristics of Games is different. It is a meticulous book about the design of
games by some of the legendary craftsmen of the form. It is an investigation into the
details of games—the nuts-and-bolts minutiae of how games actually work.
As book readers go, I swing both ways. I can enjoy riding high on the hype about
games—because, truth be told, I do believe that games represent the most vital and
vibrant form of culture today, and that they have the power to transform our society
in ways we can scarcely imagine.
But getting there isn’t going to happen by reading books about how great they are.
It is going to happen through the rigorous work of brilliant designers and theoreticians, slowly unlocking the great secrets of games. The book you hold in your hands
charts just this kind of journey; Characteristics of Games may say less, but do more.
Games have a very long history—from their roots in the play of higher mammals,
to ancient sports and games of millennia past, up through today’s complex boardgames and videogames. Although we find ourselves in a time when games seem newly
relevant, the truth is that games are nothing new. As a wellspring of pleasure, games
are a cultural universal: our species, it seems, has always liked to play them.
But despite their seductive appeal, the nerdy little secret of games is that they are
intensely mathematical. Games as a form of culture have a unique relationship to

x

Foreword

math—to systems, structures, and numbers. And so it’s no surprise that Characteristics
of Games, as a detailed study of the form, is intensely analytical.
The question is, can systems be dramatic? Can math be breathtaking? Can numbers
move your soul? If you study, or play, or make games with any kind of depth—whether
your game is poker, basketball, Scrabble, Tetris, or Halo—you already know the answer.
So let this be a warning: playing a game may be an exercise in pleasure, but this
book is not easy reading. It is difficult fun, stuffed with hard-won insights that are
not laid out on a silver platter for easy consumption. But if you take the time, this
book will open your eyes to the beauty of games.
The authors command a formidable expertise in the way games work, and a charming fearlessness for taking on what seem like fools’ errands. They tackle the minefield
of measuring the amount of skill and luck in a game: how would you compare, for
example, chess versus poker versus roulette—not just in general terms but in specific
numerical ratings? Or another: charting the density of choices in a game over time,
to understand how climax and denouement take shape in the system of a boardgame,
or a real-time strategy game, or an MMO. And they actually make graphs.
Analytical? Certainly. But don’t let their logical style fool you. There is a passion
beating beneath these chapters. Its relentless rigor is its strength, breaking through
the numerical surfaces of games to the universes of pleasure swimming underneath.
You may still be asking yourself about the relevance of a book like Characteristics
of Games. It may have insight, but is it useful beyond communities of expert players,
hardcore fans, critics, scholars, or game designers?
To answer, let me take another example: a fundamental phenomenon of games
that the authors call the catch-up. It represents a deep paradox of play: to stay engaged,
game players need to feel that the possibility exists for them to win, even up until the
very end of a game (would you really keep on playing if you knew you were going to
lose?). But at the same time players can’t feel that only the end of the game matters—
they need to sense that their actions have meaning from the very start, that all of
their choices accumulate in a way that brings them logically and steadily to a knowable conclusion.
Does this impossible idea—that a game must keep hope alive for a reversal of
fortune, even while reassuring players that everything they do has a place in a fixed
progression—have relevance outside of game design? Absolutely. This little drama of
free will and fate plays out in every game, but it also rears its head in questions of
economics and the psychology of choice, in designing behaviors across massive online
social networks, and in classic philosophical problems of ethics and responsibility—
such as motivating voters to participate in a democracy. Every game is a context for
reflection, a laboratory for thinking about thinking.
So, yes, games are relevant to life outside the game—nearly infinitely so. But games
shouldn’t be thought of as valuable because they are relevant to other fields of

Foreword

xi

research. Above and beyond any definable utility, games are valuable because they are
a fundamental form of human expression. Like making music or telling stories, playing
games is an activity that connects us more deeply to who we are.
So believe the hype about games, but understand that realizing their potential
means setting aside grand visions and glittering surfaces. Instead, just play—spectate,
participate, analyze, modify, design. This book is here to help you do just that: play
more deeply.
And it’s damn hard to argue against putting more play into the world.
Eric Zimmerman

Preface

This book is meant for anyone interested in games: designers, reviewers, critics,
and players. We hope that anyone who looks at games and wonders how to
make them better, or wants to understand more clearly how they work, will get
something out of it. Our own background is that of game players and game
designers rather than academicians or reviewers, and that is the approach we take
here. It is not a “how-to” book on game design, though, but a way of looking critically at games and talking intelligently about them. In short, one can think of
Characteristics of Games as a framework for game analysis from the point of view of
a game designer.
From our point of view, games include boardgames, card games, sports, computer
games, and many other kinds of games—we mean to be inclusive. We think these
different genres of games have many things to teach each other. For example,
card games provide many good examples of the power of standards, sports are
strong at supporting spectation as well as direct participation, and boardgames
have wrestled extensively with the issues arising from multiple independent
players.
A word of warning, though: some topics that might seem central to someone whose
main interest is in computer games, say, or in sports, might receive a less thorough
treatment than they would in a book entirely about that subject. For example, singleplayer games are central to computer gaming, but are rather a special case when viewed
from the vantage point of gaming as a whole—we discuss them, but not nearly in the
depth a book about computer gaming would.1 We hope the gain from our broader
point of view makes up for this inevitable loss of detail.
Given our intended scope, we choose examples from a great many different genres
as we discuss various issues. We try to pick well-known games within these genres
1. Similar remarks apply regarding the briefness of our treatment of story in games and of griefing, both of which are especially prominent in computer games.

xiv

Preface

whenever possible, so as to lighten the burden on the reader. Also, in appendix C we
have a list of games referred to in the text, with brief descriptions of each. The reader
with a broad experience of games, and a broad view of what gaming is, will be more
likely to find our book congenial reading.
Other than presupposing an interest in games, and at least some familiarity with
them, this book has no formal prerequisites. There are occasional mathematical digressions for which a familiarity with high school algebra would be helpful, but these can
by and large be skipped with no loss of continuity. In particular, this book is by no
means a book about mathematical game theory, although we do give brief surveys of
its two main branches (with references for the interested reader) in the first two
appendixes.
The different chapters are largely independent, and readers are encouraged to read
start to finish or as their interests take them. It is perhaps worth beginning with
chapter 1 (“Basics”) because some terminology is introduced there that’s used throughout the book. Determined readers can ignore this advice, though, and look up any
unfamiliar terms as they go.
This book is based on a course, also titled Characteristics of Games, taught by the
authors at the University of Washington from 2006 to 2009.
About the Exercises
Exercises are included throughout the book. Depending on the class’s background,
some exercises may need modifying, most commonly by replacing a game in the
exercise that the students don’t know with a game that they do. Some exercises may
require a little research for students lacking certain bits of background information
(e.g., the three-act narrative structure is mentioned in one exercise), but in most cases
simple web searches should suffice to fill any holes. For some simpler games mentioned frequently in the exercises (such as werewolf and Survivor), it may be useful to
have the students play (or watch) the game during class or as an assignment. Gaining
familiarity with other games (e.g., bridge or go) will take more effort, but it can be
well worth it for the serious student of games. In general, though, we have avoided
exercises that require familiarity with specific complex games, especially ones many
students may not play.
A few exercises (especially those in chapter 5, “Indeterminacy”) require some mathematical skills, but nothing beyond some algebra and some basic probability. Instructors may assign these exercises to students with the appropriate background; in a
longer course it may even be practical to teach some of the relevant mathematics—all
of which will in any case be useful to anyone serious about games. In a course where
further mathematical analysis of games is desired, the references in appendixes A and

Preface

xv

B may prove helpful (we particularly recommend Bewersdorff’s excellent survey of the
mathematics of games).
Many of the exercises make good in-class discussion topics as well, and instructors
are encouraged to spend some class time in this manner. And, of course, the exercises
here should be supplemented by larger projects, such as designing a complete game
(paper games are sometimes more suitable than electronic ones for this purpose),
giving detailed critiques of existing games, and so on.

Acknowledgments

The authors would like to thank Julie Villegas and especially Wanda Gregory at the
University of Washington for helping us start the course on which this book is based.
Thanks also to our teaching assistant Jonathon Loucks, and to all of our students for
serving as willing, and even enthusiastic, guinea pigs.
Timothy Chow and David Reiley gave many helpful comments, as did the three
anonymous reviewers. We would also like to thank Hilary Ross and Adam Dixon at
Wizards of the Coast for their help.
Many thanks to the gang at the Pit, who, while not directly involved in the book,
formed the best working environment a game designer could hope to inhabit.
The third author would like to thank Bill Rose, Jason Robar, and David Brevik for
being generous with time for the course and the book, and Eleanor Rieffel for advice
and support with the wild world of academic publishing. Thanks also to the Chit-Chat
Café and the Honey Bear Bakery. And last of all, but also first of all, thanks to Sandy,
Scotte, Jan, Sean, Eric, Judy, Sarah, Daryl, Dan, and all the rest of the original gaming
group.

Introduction

Figure I.1
©iStockphoto.com/Baris Simsek

Figure I.2
©iStockphoto.com/Pamela Moore

Figure I.3
©iStockphoto.com/Jess Wiberg

Relatively little scholarly work has been written about games compared with the
amount produced on other cultural phenomena of similar size such as films.
Historically most of the material on games, such as Huizinga’s Homo Ludens or
Caillois’s Man, Play, and Games, has focused on the place of games in society, and thus
on historical, sociological, and cultural issues. Less attention has been paid to the
games themselves, as games: what it is like to play them, what features differentiate
one game from another, or what features make one game a more or less enjoyable
experience for its players. Other books, such as Bell’s Board and Table Games from Many
Civilizations, Murray’s A History of Board-Games Other Than Chess, or Parlett’s various
books on boardgames and card games, are primarily catalogs of game rules or historical
treatments—excellent references, but without much analysis of games as a whole.
Later academic work, such as that of Avedon and Sutton-Smith in the 1960s and 1970s,
continued to focus largely on historical and cultural issues.
Today most of the published material on games comes from the computer gaming
industry, in the form of books with titles like Secrets of Game Programming in C++. These
books tend to focus on practical advice relevant to computer gaming, concerning
issues such as programming or project management (important exceptions include

2

Introduction

Crawford’s various books and Schell’s The Art of Game Design, which focus on the
process of game design itself), rather than the more general approach we hope to
pursue. There are also a growing number of academic titles, often collections of essays,
such as Cassell and Jenkins’s From Barbie to Mortal Kombat or Wolf and Perron’s The
Video Game Theory Reader. These books tend to have a somewhat different approach
from ours, though, with more sociological and cultural issues and less gameplayspecific analysis; they also tend to focus on computer games. One notable exception
is Salen and Zimmerman’s Rules of Play, which has a great deal of gameplay discussion
and devotes considerable space to boardgames and card games.
Our intention is to focus more on issues intrinsic to the games themselves, the
kinds of topics that game players or game designers often discuss but rarely write
down.1 Again, to take film as an example, when students come to the university to
study film, they arrive having a rough familiarity with a large number of basic narrative concepts: character, plot, theme, irony, foreshadowing, and a host of others.2
Every subject has its own collection of basic concepts, but those belonging to games
have been largely neglected until recently, and much past study of games has attempted
to adopt the concepts belonging more properly to other disciplines. There is, of course,
a place for the interdisciplinary approach, but it’s no substitute for developing the
basic concepts peculiar to the discipline under discussion. That development for games
is now beginning, and our hope is to assist in the process with this book. We hope it
will help lead to a better understanding of games as games, and pave the way for more
advanced work to follow.
Since so little has been done (at least in any structured way), this work will necessarily take a fairly high-level view. Many of the topics we cover could be books of their
own. We hope to provide an overall framework and some basic discussion of a number
of topics, but we do not by any means have the last word in any of these areas. To
use the film analogy again, this is not an advanced work of film criticism; rather, it’s
an attempt to explain in a basic way character, plot, foreshadowing, and similar concepts. Although we can’t hope to cover everything in as much depth as we’d like, we
have attempted to include all the topics we see as most important.
General Approach
Although we are attempting to develop a vocabulary for games, we are not interested
in defining terms per se, but rather in choosing some topics for discussion and beginning the discussion on those topics. Our approach is not primarily academic—all three
1. Some discussion can be found on the Internet, though—see, for example http://www.sirlin
.net, http://www.boardgamegeek.com, or http://www.costik.com/weblog/.
2. These particular concepts are of limited use when studying games; see section 7.2 on conceit
and motif.

Introduction

3

of us are game designers first and academicians second, and that is the approach we
are taking. What we are writing here is very much a continuation of the kinds of
discussions we as game designers have had with each other and with other designers
and thoughtful players of games.
In general, we tend to be descriptive rather than prescriptive—we are trying to start
a conversation about games, not write a how-to guide (although we believe a better
understanding of games should lead to better games, so we hope this book will prove
useful to game designers in that sense). Games are a big field, and different people
like different kinds of games, which is a fine thing. Still, though, we have our own
preferences and biases, and when we feel one approach is better than another we’ll
say so. Usually, though, we prefer to talk about how this or that game feature makes
a game more suitable for this or that audience.
Characteristics
Our discussion is centered around the concept of the characteristics of games: general
groups of features that give a high-level description of the sort of game it is. These are
the sorts of features another player might ask a friend about (or that the back of the
box might mention, if it’s a boardgame)3 before agreeing to play a game: How many
players does it take? How long does it take to play? Is there a lot of luck in the game?
Typically answers to questions like these are a lot more useful than a description of
the rules of the game.
There are some questions along these lines that are harder to phrase, and that only
fairly advanced players are likely to ask (although many players will notice them when
things go amiss): How possible is it for a losing player to catch up? Do you spend a
lot of time waiting for your turn to come? Are there a lot of difficult or boring calculations you’re forced to make if you want to be at all competitive? What information
in the game is hidden from the players? Is there danger of a player who is out of
contention determining, on a whim, which other player will win the game?
Sometimes answers to these questions appear in disguise. For example, if someone
asks “what kind of game is it?” and is told “it’s a card game,” she is getting, in one
fell swoop, a host of information about how long the game is likely to last, how much
luck there may be, and various other game characteristics. (And indeed, if the game
turned out to be played with small thin pieces of cardboard but otherwise had nothing
in common with any card game, the questioner would surely feel misled.)
We’re primarily interested in “player-centric” questions like these, rather than in
issues of sociology, history, or aesthetics—although such issues come up in our discussions, and we address them to some extent.
3. Oddly enough, computer games tend to be much worse at giving this kind of basic information to potential customers.

4

Introduction

Our list of characteristics is not meant to be final or definitive. Not all characteristics
will be relevant to all games, and we don’t claim the list is exhaustive. Some characteristics could perhaps be split into two, or different ones combined—the characteristics are in no way “official” but simply our way of structuring a discussion about
games.
Exercise I.1: In about fifty words, describe a game to a friend of yours in an attempt
to convince your friend to play.
Computer Games and Deliberate Design
For us, computer games are just one more kind of game. As a genre, computer games
have their own issues and problems, but so do boardgames, or card games, or sports.
As stated above, we’re happy to draw on all these genres for topics for discussion and
for specific examples.
However, computer games are different from other game genres in one very important way: they are almost all deliberately designed. There are card games and boardgames that have been designed by specific people, but always against a backdrop of
well-known “classic” games that have evolved over time.
One can think of the distinction between designed games and evolved games as
parallel to that between modern novels, with specific authors, and ancient oral poetry
or folktales. Perhaps an even better parallel is the distinction between modern architecture and traditional architecture: as Christopher Alexander discusses in Notes on the
Synthesis of Form,4 even very intelligent people can have trouble designing complex
systems as good as ones that have evolved gradually over time.
Our feeling is that these classic games and sports, which have evolved through an
unselfconscious process, are an especially good source of examples for the modern-day
deliberate game designer. Many problems that crop up repeatedly in deliberately
designed games have been “evolved out” of classic games. Indeed, for many characteristics one can go to modern games for examples of problems, and classic games for
examples of solutions—not because ancient people were geniuses, but because the
classic games that survive today have undergone a long process of evolution and of
weeding out.
On Definitions, of “Game” and Other Things
It is common to begin a treatise on games with a definition of games. Our feeling is
that such an approach is of limited use.
4. See especially chapters 4 and 5.

Introduction

5

Words (and the concepts they represent) as people actually use them do not possess
necessary and sufficient conditions that define their boundaries.5 There are no precise
definitions of complex concepts like “game,” no definitions that will include all things
that people accept as games and exclude all things that people reject. Instead, as
Wittgenstein pointed out, a category like “game” includes a great many different
things that have a family resemblance rather than exact boundaries:
There is the tendency to look for something in common to all the entities which we commonly
subsume under a general term. We are inclined to think that there must be something in common
to all games, say, and that this common property is the justification for applying the general
term “game” to the various games; whereas games form a family the members of which have
family likenesses. Some of them have the same nose, others the same eyebrows and others again
the same way of walking; and these likenesses overlap.6

Some members of the family of games can be thought of as “especially good
examples of games,” like chess or hearts. Some other games are still clearly games, but
less central: perhaps Settlers of Catan or the word game ghost. Other things are so
marginal that one doesn’t often use the word game to describe them: a footrace or a
crossword puzzle. Yet people typically refer to, say, Mario Kart or Bejeweled as games.
Are they so different? Perhaps people call them games just because they’re on a computer. But you can do a crossword puzzle on a computer—does it then become a game?
5. For a survey of this line of thinking about conceptual and linguistic categories, see George
Lakoff’s Women, Fire, and Dangerous Things, especially chap. 2, “From Wittgenstein to Rosch.”
6. The Blue Book, 17. Another related passage, from Philosophical Investigations, is worth quoting
at length:
66. Consider for example the proceedings that we call “games.” I mean board-games, card-games, ball-games,
Olympic games, and so on. What is common to them all?—Don’t say: “There must be something common,
or they would not be called ‘games’”—but look and see whether there is anything common on all.—For if you
look at them you will not see something that is common to all, but similarities, relationships, and a whole
series of them at that. To repeat: don’t think, but look!—Look for example at board-games, with their multifarious relationships. Now pass to card-games; here your find many correspondences with the first group, but
many common features drop out, and others appear. When we pass next to ball-games, much that is common
is retained, but much is lost.—Are they all “amusing”? Compare chess with noughts and crosses. Or is there
always winning and losing, or competition between players? Think of patience. In ball-games there is winning
and losing; but when a child throws his ball at the wall and catches it again, this feature has disappeared.
Look at the parts played by skill and luck; and at the difference between skill in chess and skill in tennis. Think
now of games like ring-a-ring-a-roses; here is the element of amusement, but how many other characteristic
features have disappeared! And we can go through the many, many other groups of games in the same way;
can see how similarities crop up and disappear.
And the result of this examination is: we see a complicated network of similarities overlapping and crisscrossing: sometimes overall similarities, sometimes similarities of detail.
67. I can think of no better expression to characterize these similarities than “family resemblances”; for the
various resemblances between members of a family: build, features, color of eyes, gait, temperament, etc., etc.
overlap and criss-cross in the same way.—And I shall say: “games” form a family.

6

Introduction

Even a good definition of game, like Salen and Zimmerman’s carefully constructed
“A game is a system in which players engage in an artificial conflict, defined by rules,
that results in a quantifiable outcome,” necessarily suffers from these difficulties of
definition. As Salen and Zimmerman themselves point out, things like crossword
puzzles, which people generally do not call “games,” do meet the definition, and
things like Dungeons & Dragons, which people do call a “game,” arguably do not. Or
consider the stock market—is it a game under this definition? Perhaps one should take
artificial to mean, among other things, that the game is being done “for fun” in some
sense, not as part of a serious purpose such as making a living. This approach would
exclude the stock market, at least for most people. But then is professional baseball
not a game, while amateur baseball is? None of these are faults with this particular
definition so much as they are limits to the definitional enterprise.
Asking “Is X a game?” (or worse yet, “Is X really a game?”) is not a useful question
when done with the idea that there is a “right answer” one must find, although it can
be useful as a mental exercise. Searching for a definition that exactly separates games
from nongames is, for our purposes at least, not helpful, and finding such a definition
is ultimately not possible. The subject matter of our book is games in the common
sense of the word, and we take our examples largely from boardgames, card games,
computer games, and sports (both sports that tend to have the word game attached
to them and sports that do not), but we will take examples from other activities when
it seems enlightening to do so, without worrying too much about whether they are
“really” games. In particular, we utterly reject the point of view that some games are
worse than others because they are “not really games”: games can be better or worse
than others for all kinds of reasons, but adherence to some definition of what is a
“real game” is not one of them.
In other words, for us a “game” is whatever is labeled a game in common parlance.
Our subject matter is these games and whatever other activities are close enough to
them to be fruitfully joined to them in discussion. We exclude the games without
formal rules that very small children play (e.g., “playing house” or swinging);7 we
include most sports, even those such as footraces where the label “game” is not generally used, and we include activities like crossword puzzles that we find not fundamentally different from, say, card solitaire or Minesweeper. These inclusions and exclusions
are not meant to be a formal definition of game, but merely a description of the subject
matter we discuss.8
Our skeptical point of view on definitions carries over into other discussions of
category as well. In general, we are not greatly concerned with questions of the type
7. See Caillois’s Man, Play, and Games, 168, for a discussion of games with and without rules.
8. What Wittgenstein calls an “ostensive definition” (see, e.g., Philosophical Investigations, chaps.
27–30): pointing to the thing you mean as a way of defining it.

Introduction

7

“Is X in category A or category B?” When we give definitions of concepts, it’s in order
to be able to discuss them, and we accept that there will be borderline cases, cases
that may or may not fall inside the definition. Such borderline cases are often interesting to discuss, but deciding on which side of the border they fall is moot. So, for
example, the question “Is Risk a political game?” is not really the right question—the
correct question (for which the aforementioned is often a shorthand) is more along
the lines of “How political is Risk?” or “What can you say about politics in Risk?”
If one were to explore the meaning of the word game, a better approach than trying
to find necessary and sufficient conditions might be to list various properties that
push an activity in the direction of being gamelike—in other words, to find some of
the family resemblances. For example, many games involve making tactical decisions
(chess, football, and gin do; Candyland or a footrace do not). Many games are played
on a board (chess and Candyland are; gin, football, and a footrace are not). Typically
people refer to football, chess, and Candyland as games, but not a footrace—arguably
because the former do have “enough” of the family properties of games, but a footrace
does not. Even with this approach, though, one shouldn’t expect an exact procedure
for determining what is and isn’t a “game.” In any case, this enterprise may well teach
one more about linguistics than about games, and it is not something we will undertake here.9
If game is a difficult term to come to grips with, art is even tougher. The classic
question of “Are games art?” is not one we intend to address. For us, it seems to be
more a question about words (and particularly about the meaning of the word art)
than a question about games. We are doubtful whether the question can be answered
even in principle. In any case, it is a question very different from the ones that will
concern us here.
Formal Definitions: Orthogame and Agential
Although trying to find exact boundaries for existing English categories is not useful,
occasionally defining new words is useful. If there’s no good word for something
already, sometimes one must make something up. We have no objection to definitions
in this sense (this is defining in the sense that mathematicians do it: declaring what
a word means for purposes of a subsequent discussion, rather than trying to find the
“true definition” of some preexisting word).
In general, we prefer to use existing terms where possible, but there are a few terms
that we haven’t found available.
9. For readers interested in the various attempts to define the term game, there is an excellent
survey of a number of different definitions that have been offered over the years in Salen and
Zimmerman’s Rules of Play, 71–83.

8

Introduction

The first is orthogame,10 which we define as a game for two or more players, with
rules that result in a ranking or weighting of the players, and done for entertainment.
Explicit winners or losers, scores, or time to completion all count as rankings or
weightings—the point is there is something explicit to tell you how well you’ve
performed.
This definition is meant to exclude games like Dungeons & Dragons or World of
Warcraft, where there is not an explicit win condition, and players may have many
different goals.11 Also excluded, due to the “done for entertainment” clause, are professional military simulations and other “serious games.”12 In general, our focus is on
orthogames, but we will occasionally discuss nonorthogames as well (games that
violate the ranking/weighting condition frequently, games that violate the entertainment condition rarely).
Many characteristics of a game depend on its audience as much as on the game
itself. A game might be played quickly or slowly, as a two-player game or as a multiplayer game, casually or seriously, all depending on the pool of players. We’ll say a
characteristic is systemic if it depends mainly on the game as a system (e.g., on the
rules) and agential if it depends primarily on the player base. (We derive the latter term
from the use one sees occasionally of the term agent to mean a player in a game; one
can think of agential as a more euphonic version of “player-ential.”) Although our
default set of players is “all the players in the world,” we’ll sometimes discuss a specific
subset, such as “players in Africa” or “middle-aged women with disposable incomes
of over $50,000 a year.” Often we’ll compare two different subsets, like hardcore
players versus casual players, or wealthy players versus poorer ones.
One can think of a game’s characteristics as depending on the combination of the
game itself and the people who play it. Since player populations are changing all the
time, the game’s characteristics can change without any systemic feature of the game
changing.
The terms agential and systemic are very much relative: hardly any property is
purely one or the other. For example, there are certainly systemic reasons that a game
of chess takes longer to play than a game of tic-tac-toe, but there are agential consid10. Ortho- from the Greek word meaning “straight” or “correct,” the idea being that orthogames
are the most “normal” or “usual” kind of game.
11. Although RPGs and MMOs have plenty of numbers in them, no one number is completely
authoritative in the sense that you “win the game” if you have the highest score in that number.
One player might be glad to have reached a certain level, another player might be happy to have
a large amount of gold, and yet another player might care most about the items she has and
how powerful they are.
12. Although some issues we discuss in this book will be relevant to simulations and “serious
games,” our focus is on games played for fun. We don’t generally concern ourselves with features
that might be needed to increase the educational value or simulational accuracy of a game.

Introduction

9

erations in the length of playtime as well—some playgroups consistently finish games
of chess very quickly, other groups will regularly take hours. The fact that horse racing
has a lot of rich people involved in it is an agential property, but there are systemic
reasons supporting it (you need a horse to play, and poor people in the West may find
it hard to keep horses).13
So claims such as “this characteristic is agential” should be read as “this characteristic has a lot of agential properties, which we’ll now discuss.” The point is not to
classify all characteristics as either agential or systemic, but rather, for each characteristic, to look at its agential and systemic properties. Characteristics are more or less
agential or systemic, not all one or all the other. In particular, beware of the frame of
mind where everything seems systemic (“after all, everything stems ultimately from
the properties of the game system, right?”) or everything seems agential (“it all
depends on how people choose to react to it, after all”). While there’s some theoretical
truth to each of these points of view, neither is much use for analyzing games and
drawing distinctions between them.
Minor Conventions in the Text
We sometimes use “he” and sometimes “she” when referring to people (typically
players of games). Often we use both as a way of differentiating two different players.
Nothing is meant by any particular gender assignment beyond the fact that “he” and
“she” are not the same person.
Our statements (if they are correct at all) are more often generally true as opposed
to being true without exceptions. In a field as large and varied as gaming, there will
be exceptions to almost every rule. We may point out some of these exceptions if they
seem interesting or enlightening, but often we leave it to the reader to discover them.
It is very tedious always to repeat phrases such as “generally,” “for the most part,” and
“with very few exceptions,” so while we will resort to them occasionally for emphasis,
the absence of such phrases should not be taken to mean that we are claiming a statement holds in every single case.
We follow the American English convention in using soccer for European football
and football for the rugbylike game played primarily in the United States and Canada.
When we discuss specific game examples, it is usually the case that the analysis
applies to other games of that genre (e.g., we may use Starcraft as a stand-in for RTS
games generally, or hearts as a stand-in for trick-taking card games). We do this because
concrete examples are easier and more enjoyable to follow than very abstract statements about categories. In most cases, a moment’s thought should make it clear how
13. In some parts of the Third World, many people have horses, and sports involving horses
there are not the exclusive province of the wealthy.

10

Introduction

much the remarks about that game extend to others—when it is problematic, we will
try to call it out.
Of course, when we criticize a game on some narrow grounds, that doesn’t mean
we think it is a bad game. (In general, we choose games we like as examples.) In any
case, we are not intending to rate or evaluate games as good or bad—we are interested
in using the examples to illustrate the general principle. Also, a game can be lacking
in an area without it being the case that “fixing” that lack would improve it—for
example, chess has weak “atoms” (satisfying chunks of play shorter than a full game),
but trying to introduce stronger atoms to chess would not necessarily improve the
game. In other words, certain weaknesses may need to be accepted to get other
strengths.
In general, we take the point of view that players are trying to win, and that part
of the designer’s task is to make the game enjoyable under the stresses of players’
attempts to win. So when we speak of heuristics, balance, strategic collapse, politics,
and so on, the background assumption is that most often, players will want to win
and will engage in behaviors that help them do so. This is not to deny that players
have many other motivations as well (killing time, socializing, aesthetic enjoyment
of the game materials, and countless others). But even players who are playing to
satisfy other motivations usually still try to win, and games shouldn’t provide a bad
experience when they do. Also, note for some games, especially orthogames, such as
chess, “winning” is fairly clearly defined, and for others it’s vaguer, or there are multiple different ideas of winning in the heads of different players, or even in the head
of the same player (examples include paper RPGs, MMOs, and sandbox games like
SimCity).

1 Basics

We begin our survey of game characteristics with three so basic that they influence
all the others. The first two, length of playtime and number of players, are familiar to
everyone. Anyone, when asking a friend about a game, might well ask how long it
takes to play and how many players it requires. Most boardgames give this information on the back of the box. But even though this information is basic and seemingly
simple, there is actually quite a bit of complexity hidden here, and we try to unpack
some of it.
Our third basic characteristic, heuristics, may seem more esoteric. But by “heuristics” we simply mean the rules of thumb by which players play games (“develop
your pieces” in chess or “never draw to an inside straight” in poker). When players
discuss among themselves a game they know, it is these heuristics that they talk
about. Given our goal of analyzing games from the point of view of thoughtful
players, it’s only natural that game heuristics should be a basic characteristic
for us.
1.1

Characteristic: Length of Playtime

It is easy for hardcore players (including most game reviewers and game designers) to
underestimate the importance of game length and the cost a long playtime imposes
on players, especially more casual ones. But game length is probably one of the most
important characteristics people use when deciding whether to play a game: picture
someone saying to a friend “want to come over and play a game?” The answer is very
likely to depend on how long that game takes to play. And if the game is going to be
played in some specific time slot—over lunch, say—the players will want to pick a
game that can be played comfortably in that amount of time.
Note that the amount of time a game takes to play is not just a property of the game
itself, but of the community that plays it—that is, length of play is agential. The African
game of mancala (actually a family of related games, such as kalah and oware) is played
with great rapidity in Africa, although Europeans and Americans who play it are liable

12

Chapter 1

Figure 1.1
©iStockphoto.com/Lev Mel

to do so at a slower speed.1 Chess in the West is often played relatively slowly, with
games that last over an hour not being uncommon, but Eastern versions of chess, no
less complex in terms of their rules, are generally played at the speed of casual checkers
in the West (perhaps because the game go has taken up the “serious” gaming niche in
the East that chess occupies in the West). The advent of the chess clock has meant that
chess has to some extent become two different games: “normal” chess, where the total
clock time is around two hours per player, and speed chess, where the total clock time
can be five minutes per player. These two games have (slightly) different rules, different
rating systems, and somewhat different player bases. This splitting of the audience is
merely a more formal version of a phenomenon common in many turn-based games:
casual players like to play quickly, more serious players prefer to spend more time on
their moves, and thus informal conventions arise within different play groups as to
how long a game is “supposed” to take to complete.
As the length of time to play a game changes, it can affect many other characteristics of the game: skill, randomness, costs and rewards for playing, how pleasing the
game is to watch, and so on.
Units of Gameplay Length
To discuss length of playtime in more detail, it is useful to break down units of play
into various pieces of (usually) increasing length:
1. Parlett, The Oxford History of Board Games, 217.

Basics

13

Atom The smallest complete unit of play, in the sense that the players feel they’ve
“really played” some of the game (e.g., two possessions in football, or one level in
Donkey Kong)
Game What is conventionally thought of as the length of the game—a “standard”
full round of play (most typically starting from a standard beginning state and ending
with the determination of a winner)
Session A single continuous period of play (e.g., an evening of play)
Campaign A series of games or sessions that are all linked in some way (the weekly
poker game at Randy’s place, a match, or an ongoing paper role-playing game)
Match A series of individual games commonly agreed on as the correct amount of
play in order to arrive at a satisfactory determination of the victor. For many games
this is merely “best two out of three” or similar grouping.
Depending on the game, some of these categories will make more or less sense. The
categories are also sometimes subjective (especially the atom).
For example, take poker. Here, the atom is probably a single hand. The game may
last until a player cashes out or gets knocked out. A session would be an evening of
play, and a campaign would be an ongoing game featuring the same players. For
tennis, an atom might be a couple of games or even a set, a game would be a standard
tennis match, and a session might be several matches in a row, or perhaps a tournament. A campaign might be a professional tennis season, or an ongoing series of games
between two friends who compare their progress. With Donkey Kong, an atom might
be a single level, a game would begin when you put in your token and end when you
ran out of lives, and a session would be the amount of time you spent in the arcade
playing Donkey Kong that day. There might be no campaign involved, but if you went
to the same arcade regularly, trying to improve your position on the high-score board,
then there would be. Note that the campaign ties in very much with the “metagame”;
see section 7.1 on that topic.
Typically the game is the most clearly defined unit of play, but there are exceptions
even to that. Poker was already mentioned; World of Warcraft is another example. Some
playgroups might play bridge hand after hand, without necessarily keeping game
score. If a game has separate stages, like bridge, a game probably needs to include each
of the stages to be considered a game: you could argue that bidding to a contract is
an atom, and playing the hand is an atom, but either one alone can hardly be a game.
You would need to bid and then play a contract at the very least to call it a game,
even informally. Of course, to have an official game of bridge you’ll need to play
several hands so as to reach the required point total.
Not all games have matches, but many do. The most common form is simply to
play a fixed number of games, with the winner of the majority being the winner of
the match (extra games that won’t affect the match outcome typically are not played,
so for example a best three out of five match will end as soon as one player wins three

14

Chapter 1

games). Often matches are used as a sort of “extended game”: if the game length is
short, playing best three out of five is a way to play a longer game. Playing more games
makes it more likely that the better player wins the overall match, and when determining the best player is an important goal, matches can become very long—championship chess and go matches, for example, can consist of many games played over
a period of weeks or even months.2
So a match can be shorter or longer than a session. Multiple matches may take
place inside a session, for example when playing a trading card game, or a match may
be longer than a session as in the playoffs in many sports. The length of a match often
varies with a particular subset of its player base. The interaction between players’ skill
