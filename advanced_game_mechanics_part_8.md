three of them in his article:
Intention. Players should be able to make an implementable plan of their own
creation in response to the current situation in the game world and their understanding of the gameplay options.

n

Perceivable Consequence. Game worlds need to react clearly to player actions;
the consequences of a player’s action should be clear.

n

Story. Games might have a narrative thread, whether designer-driven or playerdriven, that binds events together and drives the player toward completion of
the game.

n

Between 1999 and 2002 the Gamasutra website hosted a forum where people could
discuss and expand the framework. The term design tool was quickly replaced by
design lexicon indicating that the formal abstract design tools seem to be more successful as an analytical tool than a design tool. Bernd Kreimeier reported that “at
least 25 terms were submitted by almost as many contributors” (2003). As a project
the formal abstract design tools have been abandoned; however, Church’s article is
often credited as one of the earliest attempts to deal with the lack of a vocabulary
for game design, even though his framework never caught on.

desiGn Vocabularies online
You can find a few design vocabularies online. although some of these seem to be abandoned, they are still a useful resource for game designers:
•
The 400 Project. Initiated by designers Hal Barwood and Noah Falstein, the 400
Project sets out to find and describe 400 rules of game design that should lead to better
games. The project website lists 112 rules so far, but the last one was added in 2006. see
www.theinspiracy.com/400_project.htm.
•
The Game Ontology Project. This project attempts to order snippets of game design
wisdom into one large ontology. it is primarily an analytical tool; it aims at understanding games rather than building them. nevertheless, it contains valuable design lore. see
www.gameontology.com.
•
The Game Innovation Database. This project focuses on tracking innovations in
game design to their original sources. it is slightly different from typical design vocabularies as it creates a historical perspective on common game design structures. see
www.gameinnovation.org.

desiGn PaT Terns

151

Design Patterns in Games
The attempts to set up a design pattern language, as opposed to a design vocabulary, have been fewer. Bernd Kreimeier suggested a design pattern framework in his
Gamasutra article “The Case for Game Design Patterns” (2002), but he never actually built one. In their book Game Design Patterns (2005), Staffan Björk and Jussi
Holopainen describe hundreds of patterns, and you can find many more patterns on
the accompanying website. However, Björk and Holopainen choose the following
definition as their starting point for their pattern language: “Game design patterns
are semiformal interdependent descriptions of commonly reoccurring parts of the
design of a game that concern gameplay” (p. 34). In other words, their approach is
much more like a design vocabulary than it is like a pattern language. They do not
formulate a clear theoretical vision on what quality in games is or where it might
come from. Their book is a valuable collection of design knowledge, but it does not
really tell you how to use that knowledge effectively to build better games.

Machinations Design Pattern language
In the previous chapters, we discussed quality in games from the perspective of a
game’s internal economy. Our discussion focused on how certain structural features
of the game economy (such as feedback loops) create emergent gameplay. It should
not come as a surprise that the relation between the structure of a game’s internal
economy and its emergent gameplay is the focal point of the pattern language we
present in this chapter. In addition, as Machinations diagrams proved to be very
useful in describing the structure of a game’s internal economy, it makes sense to
use Machinations diagrams to express these patterns.

Pattern Descriptions
In Appendix B you will find complete descriptions of all the design patterns used in
this book. You will notice that these descriptions follow a strict format. If you are
familiar with software design patterns, you might recognize the format; we took it
from the descriptions used in Design Patterns by the Gang of Four.

ChAptEr 7

Any effort to identify design patterns in games should begin with a clear theoretical
vision on what makes a game objectively good—where its intrinsic quality comes
from. Based on that vision, it should identify common problems and offer generic
solutions to those problems, just as Alexander did for architecture. In that way,
design patterns really become a useful tool for game design, not just game analysis.
That is how we approach the game design patterns in this book.

152

Game mechanics: advanced Game desiGn

Each description includes the following items:
Name. Every pattern has a descriptive name. Sometimes a few alternative names
are listed under Also Known As.

n

n

Intent. This is a short statement that describes what the pattern does.

Motivation. The motivation describes the use of the pattern more elaborately
and suggests a few use-case scenarios.

n

Applicability. The section describes in what situations the pattern is best used;
it describes the problems the pattern might solve.

n

Structure. This is a graphical representation of the pattern using Machinations
diagrams.

n

Participants. This describes and names the elements, mechanisms, and compound structures that are identifiable parts of the pattern. These names are used
throughout the pattern’s description.

n

Collaborations. Identifies the most important structural relationships between
the pattern’s participants.

n

Consequences. This section describes what you might expect if you apply this
pattern to your design, including potential trade-offs and possible risks.

n

N OT E To make the
diagrams illustrating
the patterns as generic
as possible, we have
avoided precise numbers. many resource
connections are simply
labeled with n, and
many state connections
are labeled with + or -.
To run these diagrams
in the machinations
Tool, you would have
to supply additional
details.

Implementation. For most patterns there are many different ways to implement them. This section describes a few alternative ways of implementing a pattern,
including the effects of randomness on it.

n

Examples. This section lists at least two examples of the pattern in published
games.

n

Related Patterns. Most patterns are related to another one. Some patterns act
against each other, while others complement each other. These and other relationships are described here.

n

In the next few sections, we’ll introduce the design patterns that we have collected.
The patterns described here include a diagram and are organized into categories.
This is only a brief synopsis, however. You can find full descriptions of each pattern,
along with examples of games that use it, in Appendix B.

desiGn PaT Terns

153

Category: engines
Engines generate resources that may be required by other mechanics in the game.

sTaTic enGine
A static engine produces a steady flow of resources over time for players to consume
or to collect while playing the game.
Use a static engine when you want to limit players’ actions without complicating
the design. A static engine forces players to think how they are going to spend their
resources without much need for long-term planning.

A source produces an adjustable flow of resources. Players can invest resources to
improve the flow. Use a dynamic engine when:
You want to introduce a trade-off between long-term investment and short-term
gains. This pattern gives the player more control over the production rate than a
static engine does.

n

ChAptEr 7

dYnamic enGine

154

Game mechanics: advanced Game desiGn

cOnverTer enGine
Two converters set up in a loop create a surplus of resources that can be used elsewhere in the game. Use a converter engine when:
You want to create a more complex mechanism to provide the player with more
resources than a static or dynamic engine provides. (Our example converter engine
contains two interactive elements while the dynamic engine contains only one.) It
increases the difficulty of the game because the strength and the required investment of the feedback loop are more difficult to assess.

n

N OT E remember
that the profile of a
feedback loop is the
collection of its characteristics such as effect,
investment, speed,
and so on, that we
described in Table 6.1.

You need multiple options and mechanics to tune the profile of the feedback loop
that drives the engine and thereby the stream of resources that flows into the game.

n

enGine BUiLdinG
With this pattern, a significant portion of gameplay is dedicated to building up and
tuning an engine to create a steady flow of resources. Use engine building when:
n

You want to create a game that has a strong focus on building and construction.

n

You want to create a game that focuses on long-term strategy and planning.

desiGn PaT Terns

155

Category: Friction
Friction patterns drain resources out of an economy, reduce its productivity, or both.
You can use them to represent loss or inefficiency.

sTaTic FricTiOn
A drain automatically consumes resources produced by the player. Use static friction
when:
You want to create a mechanism that counters production but that can eventually be overcome by the players.

n

You want to exaggerate the long-term benefits from investing in upgrades for a
dynamic engine.

dYnamic FricTiOn
A drain automatically consumes resources produced by the player; the consumption rate is affected by the state of other elements in the game. Use dynamic friction
when:
n

You want to balance games where resources are produced too fast.

You want to create a mechanism that counters production and automatically
scales with players’ progress or power.

n

You want to reduce the effectiveness of long-term strategies created by a dynamic
engine in favor of short-term strategies.

n

ChAptEr 7

n

156

Game mechanics: advanced Game desiGn

sTOPPinG mechanism
This pattern reduces the effectiveness of a mechanism every time it is activated. Use
a stopping mechanism when:
T I P in formal economics, a stopping
mechanism is also
known as a law of
diminishing returns.
For example, beyond
a certain point, adding fertilizer to a field
reduces, rather than
increases, crop yields
because it is toxic in
large quantities.

n

You want to prevent players from abusing particular actions.

n

You want to counter dominant strategies.

n

You want to reduce the effectiveness of a positive feedback mechanism.

aTTriTiOn
Players actively steal or destroy resources of other players that they need for other
actions in the game. Use attrition when:
n

You want to allow direct and strategic interaction between multiple players.

You want to introduce feedback into a system whose nature is determined by the
strategic preferences and/or whims of the players.

n

desiGn PaT Terns

157

Category: escalation
Escalation patterns put pressure on the player to deal with growing challenges.

escaLaTinG chaLLenGe
Progress toward a goal increases the difficulty of further progression. Use escalating
challenge when:
You want to create a fast-paced game based on player skill (usually physical skill)
in which the game gets harder as the player advances; his ability to complete tasks is
inhibited as he goes.

n

You want to create emergent mechanics that (partially) replace predesigned level
progression.

escaLaTinG cOmPLexiTY
Players act against growing complexity, trying to keep the game under control until
positive feedback grows too strong and the accumulated complexity makes them
lose. Use escalating complexity when:
n

You aim for a high-pressure, skill-based game.

You want to create emergent mechanics that (partially) replace predesigned level
progression.

n

ChAptEr 7

n

158

Game mechanics: advanced Game desiGn

arms race
Players can invest resources to improve their offensive and defensive capabili-ties
against other players. Use arms race when:
n

You want to create more strategic options for a game that uses the attrition pattern.

n

You want to lengthen the playing time of your game.

Miscellaneous Patterns
The remaining patterns in our library don’t fall into any other category, so we have
collected them here.

PLaYinG sTYLe reinFOrcemenT
By applying slow, positive, constructive feedback on player actions, the game gradually adapts to the player’s preferred playing style. Use playing style reinforcement when:
You want players to make a long-term investment in the game that spans multiple sessions.

n

You want to reward players for building, planning ahead, and developing personal strategies.

n

n

You want players to grow into a specific role or strategy.

desiGn PaT Terns

159

mULTiPLe FeedBacK
A single gameplay mechanism feeds into multiple feedback mechanisms, each with
a different profile. Use multiple feedback when:
n

You want to increase a game’s difficulty.

n

You want to reward the player’s ability to read the current game state.

This pattern allows trade between players to introduce multiplayer dynamics and
negative, constructive feedback. Use trade when:
n

You want to introduce multiplayer dynamics to the game.

n

You want to introduce negative, constructive feedback.

You want to introduce a social mechanic that encourages players to interact with
one another via commerce (as opposed to combat).

n

ChAptEr 7

Trade

160

Game mechanics: advanced Game desiGn

WOrKer PLacemenT
The player controls a limited resource she must commit to activate or improve different mechanisms in the game. Use worker placement when:
n

You want to introduce constant micromanagement as a player task.

n

You want to encourage players to adapt to changing circumstances.

n

You want to introduce timing as a crucial factor in successful strategies.

n

You want to create a subtle mechanism for indirect conflict.

sLOW cYcLe
This is a mechanism that cycles through different states slowly, creating periodic
changes to the game’s mechanics. Use a slow cycle when:
n

You want to create more variation by introducing periodic phases to the game.

n

You want to counteract the dominance of a particular strategy.

You want to force players to periodically adapt strategies to shifting
circumstances.

n

You want to require a longer period of learning before achieving mastery of the
game. (Players experience slow cycles less frequently, so have fewer opportunities to
learn from them.)

n

desiGn PaT Terns

161

You want to introduce subtle, indirect strategic interaction by allowing players to
influence the cycle’s period or amplitude.

n

Games rarely implement just one design pattern. Most of the time, you’ll find that a
game combines a few of these patterns in a clever construction. For example, Tetris
combines escalating complexity (the game gets more difficult as the tetrominoes
build up and more and more holes—unfilled spaces—appear at the bottom) and
escalating challenge (the tetrominoes start falling more quickly as the player clears
more lines). As you can tell from their descriptions, many patterns in the library
complement each other, but you’ll find that even more unlikely combinations of
patterns can have some interesting consequences.
Certain patterns combine so well that they drive entire game genres. For example,
the core of most real-time strategy games is formed by a combination of a dynamic
engine with attrition. The players build up their base with a dynamic engine for
production to fuel a war of attrition. Larger real-time strategy games complement
this combination with an arms race pattern or (less commonly) an engine-building
pattern to provide more strategic options and create longer gameplay. Most role-playing games combine playing-style-reinforcement (character building) with escalating
challenge (harder challenges as the player progresses).
The descriptions of the patterns in Appendix B include many suggestions on how
patterns might be combined, but we encourage you to explore and experiment with
different combinations yourself.

elaboration and Nesting Patterns
Reading through the pattern descriptions in this chapter and in Appendix B, you
might have noticed that some of the patterns seem similar. For example, a dynamic
engine allows the player to make changes to the production rate of a resource, while
the engine building pattern does something very similar, except that it doesn’t

ChAptEr 7

Combining Design Patterns

162

Game mechanics: advanced Game desiGn

dictate a particular implementation. You can think of the dynamic engine pattern
as a special instance of the engine building pattern. If you include a dynamic engine
in your game, you have implicitly included some form of engine building. Attrition
and dynamic friction exhibit the same relationship: Attrition is a more specialized case of dynamic friction. Creating attrition is simply a special case of applying
dynamic friction symmetrically.
From the perspective of design pattern theory, this type of relationship between
patterns is called elaboration. One pattern (for example, attrition) is a more elaborate implementation of another pattern (for example, dynamic friction). Within
the engine patterns, the worker placement pattern elaborates the engine building
pattern, while the engine building elaborates the dynamic engine, and the dynamic
engine elaborates the static engine.
Elaboration can be an important tool to design games. For example, if a game is too
simple, replacing one pattern in the game with a pattern that elaborates the original pattern will make the game more complex. At the same time, when a game is
too complex, replacing a complex pattern with a simpler pattern that the original
elaborates will make the simpler. Ultimately, all engine patterns elaborate an ordinary source node, and all friction patterns elaborate an ordinary drain node. In your
game, you should be able to replace any source with an engine, and vice versa. The
pattern descriptions in Appendix B list what patterns elaborate other patterns and
by which patterns it is elaborated under the related patterns section.
To illustrate how elaboration might be used as a design tool, consider the Harvester
game. As was mentioned in the beginning of this chapter, it implements a dynamic
engine pattern. There are a few possible elaborations. For example, we might
elaborate the entire pattern to the engine building pattern or even to the worker
placement pattern (Figure 7.3).
Another option would be to elaborate elements within the dynamic engine. As
we already mentioned, we could elaborate any source to an engine pattern. As the
Harvester game contains a source, we could replace that source with a converter
engine pattern (Figure 7.4). In turn, because the converter elements themselves
actually consist of a combination of a drain triggering a source, we could replace
any of them with an engine or a friction pattern.

desiGn PaT Terns

163

FIGURe 7.3

FIGURe 7.4
another elaboration of
the harvester game

ChAptEr 7

elaborations of the
harvester game

164

Game mechanics: advanced Game desiGn

reVersinG elaboration: simpliFication
You can use elaboration to make games more complex, but you can also do the reverse.
By replacing elaborate patterns with simpler ones, you can remove complexity from a
design. You can also use simplification to create diagrams that are more abstract than
the game that they describe yet that still retain some of the game’s dynamic behavior. We
used this simplification technique for several diagrams in this book, notably the Pac-Man
examples in chapter 5 and the Risk examples in chapter 6. For example, in the diagrams
for Risk, we modeled the opposition from other players as dynamic friction (see Figure
6.27). a multiplayer diagram for the same game would use the attrition pattern for the
same mechanism. By replacing attrition with dynamic friction, we removed the other
players from the diagram entirely and focused more on the internal economy from the
perspective of a single player.

Elaboration does not apply only to design patterns; it applies to almost any element
in a Machinations diagram. For example, Figure 7.5 displays a number of ways to
elaborate a converter. Any game mechanism can be an elaboration of a converter as
long as it displays more or less the same functionality: consume one resource to produce another. The elaborated converters cannot be called design patterns, because
they don’t present a generic solution to a common problem. However, building up a
repertoire of such structures (while being aware of what they originally came from)
will allow you to experiment with game mechanics with great ease.

FIGURe 7.5
different elaborations
for a converter element

desiGn PaT Terns

165

elaboration and desiGn Focus
elaboration and its reverse, simplification, can be great tools to match the mechanics of
your game to its design focus: your intended gameplay. if your game is primarily about
combat, you might create elaborate mechanisms for that part of the game and use simpler mechanisms for parts of the game that the player will spend less time on (and care
less about). if you notice that the mechanisms controlling secondary gameplay (construction or inventory management, for example) are too elaborate, try replacing them with
simpler patterns or even single elements. sometimes it is better to replace a complex
production mechanism with a simple source that has a random flow rate. By choosing to
elaborate the mechanisms that generate the most important gameplay and simplify the
other aspects, you can focus your design on what matters most to your player.

The patterns in this book are the result of many studies of existing games and also
of using Machination diagrams to help design games. However, we do not mean to
suggest that the pattern language as presented here is complete. Although the patterns we have described already capture many important aspects of a wide variety of
games, we expect that in the near future we will add more patterns to this collection. In fact, we encourage you to keep an eye out for more interesting patterns that
emerge from your own designs or from your analysis of other people’s games.
When encountering a new pattern, it is important to try to describe it in generic
terms. You might have found a new pattern in a science-fiction game about intergalactic trade, but that doesn’t mean the pattern and its participants should take
their names from that game. When describing new patterns, stick to the description
format and general terms described in the earlier section “Pattern Descriptions.”
Identify and name the most important participants; try to think of a number of different ways to implement the pattern, but most importantly identify the common
design problems your pattern solves.

ChAptEr 7

extending the Pattern language

166

Game mechanics: advanced Game desiGn

tWo criticisms oF Formal methods
The machinations diagrams and the pattern language formalize the practice of game design to a certain extent; they are tools that we hope will enhance and complement your
existing skills. however, not everyone in the game industry sees value in such methods.
Game designer raph Koster gave a lecture at the Game developers’ conference called
“a Grammar of Gameplay: Game atoms—can Games Be diagrammed?” (2005), in which
he discussed game mechanics at some length and proposed a method for diagramming
them. Later he noted that the audience reaction was quite mixed (sheffield 2007). From
our own discussions on game design methodology with various people in the game
industry, we have noticed a similar split. some designers dislike the premise of design
methodology and argue that they are academic toys with little relevance for real, applied
game design. Others recognize the value of these tools and are happy to experiment with
them to improve their designs.
another common argument against game design tools and methodology is that they can
never capture the creative essence that is the heart of successful game design. according
to this view, no formal method can replace the creative genius of the individual designer (Guttenberg 2006). supporters of this argument fear that the tools will ultimately
limit designers because they tend to view game design only through the lens of formal
methods.
design tools can be Worth the investment
We cannot deny that the current vocabularies and frameworks for formal methods have a
poor track record within the game industry. There are a number of them in existence, but
many were designed by academics with little hands-on game design experience. Often
it takes a considerable investment to learn their tools, while the return value of using
them is not particularly high. This is especially true of tools designed primarily to analyze
games. Formal game analysis is done more often in universities than in industry.
The criticism is valid, but it does not mean that there is no point in trying to create game
design methodologies. it simply suggests that we should adopt criteria for evaluating them:
They should help designers to devise, understand, and modify their designs, not just to
analyze other people’s games. We hope that by now, you see that the design patterns and
the machinations language are not simply tools for analysis; they can actually help you
improve your mechanics and offer the opportunity of experimenting with your designs
at an early stage during development. chapter 9, “Building economies,” features an extensive case study. in that chapter, we’ll show you how to use these tools to design game
mechanics in a way that goes beyond the typical brainstorming techniques. (We do encourage you to use the brainstorming opportunities that design patterns offer, however.)
continues on next page

desiGn PaT Terns

tWo criticisms oF Formal methods

167

continued

any design tool requires some investment to master, but we feel that learning
machinations will pay back this investment. Your design will be better because the tools
offer you an efficient way to test your mechanics quickly.

The image of the artist as a creative genius extemporaneously devising brilliant works
with raw talent is a romantic vision that rarely fits reality. To create art, artists must learn
the techniques of the trade and work hard. This has always been the case for all forms of
art, and there is no reason to assume that games are any different. The artist’s tools and
techniques are many. They range from the practical to the theoretical. Painters learn how
to use a brush with different types of paint and learn about the mathematical principles
of perspective and the psychological principles of cognition. The invention of geometric perspective—a seemingly scientific rather than aesthetic innovation—revolutionized
renaissance painting. The development of abstract art throughout the nineteenth and
early twentieth century has been a gradual and deliberate intellectual process. none of
these changes would have happened if painters treated intuition and individual skill as
their only source of progress.
We feel that skeptics of design methodologies are missing the point. Formal design
methods are created to support the creative genius, not to replace it. no matter how
good a method or tool is, it can never replace the vision of the designer, nor can it
replace the hard work involved in designing a game. at best it can ease the burden and
refine a designer’s techniques. The best methods do not restrict a designer’s vision.
rather, they enhance it, enabling the designer to work faster and create better results.
machinations diagrams also facilitate teamwork and collaboration. instead of arguing
about how their proposed mechanics will behave once the code is written, a design team
can diagram and simulate them before a line of code is written.

ChAptEr 7

design tools support creativity
The second argument, that no formal design method can replace the instinctive creative
genius of the individual designer, is more problematic. People who subscribe to this
opinion dismiss the whole idea of design methodology. however, this opinion is often
informed by a rather naive conception of art. art is, and always has been, the combination of creative talent, practiced technique, and hard work—a lot of hard work. There is
no point in denying that one artist has more talent than another, but pure talent rarely
makes up for the other two aspects entirely. especially within an industry where much
money rides on the success of each project, investors simply cannot afford to gamble on
creative talent to deliver all the time.

168

Game mechanics: advanced Game desiGn

leveraging Patterns for Design
A pattern language is a tool designed to help you. It does not enforce a particular
way to design games. Patterns are guidelines you can use to explore your designs,
not rules instructing you what you must do to make a good game. Nevertheless, we
advise you to stick to the patterns initially. Implementing these patterns is a great
way to build your design experience and learn by copying time-tested structures.
Once you have some experience with identifying and applying these patterns, it
makes perfect sense to start to break away from them. Moving into new, uncharted
territory is exciting and important, but it is best done after you’ve gained some
experience.

Improving Your Designs
The most important thing you can do with design patterns is to use them to solve
problems in your design. For example, you might notice that your game produces
arbitrary outcomes because a strong positive, constructive feedback loop amplifies a
small random difference in luck early in the game. Looking at the patterns, a number of solutions suggest themselves. If the game has multiple resources, you might
introduce more negative feedback by using the trade pattern. Or you could apply
dynamic friction to counter the positive feedback.
To use design patterns in this way, it pays to study the library. Knowing the patterns
and their different implementations will enhance your understanding of common
problems in game design and provide you with a repertoire of potential solutions.
Design patterns represent general design lore in a concentrated form. After all, most
of these patterns have evolved in games over a long period. Design patterns allow you
to build on that experience without going through a long learning period yourself.

brainstorming with Design Patterns
Pattern languages make good brainstorming tools, and they allow all sorts of creative exercises. One simple technique is to choose two or three patterns at random
from the collection and try to design a game economy around them. There are
several ways to approach this exercise. You could choose a pattern at random,
implement it in a digital Machinations diagram, and then choose a new pattern
and add it to your diagram. You probably want to repeat this until you have implemented three or four patterns. You might also try to create paper prototypes for
every step. Don’t worry if you randomly select the same pattern again. Simply find
another resource or part of the diagram to apply it to. Alternatively, you can select
a number of patterns beforehand and design a game economy that implements all
patterns from the start.

desiGn PaT Terns

169

You can do a similar thing for games you are currently developing. The patterns suggest many generic terms for resources in your game based on their function in the
economy. Identifying what resource in your game functions as the main “energy”
that fuels the player’s core actions could help bring your game’s most important
economic structures into focus. Randomly pick a pattern and use it as a lens on the
game, asking yourself questions like, Is the pattern present in the current design,
and if so, does it work the way you want it to? If not, would adding it help counter
problems in the design?
You could also use the patterns as a lens to analyze and change existing games. For
example, what mechanisms act as a stopping mechanism in StarCraft? What would
happen if you changed the basic economy of that same game to include a converter
engine instead of a dynamic engine? What patterns would make a good addition?

What about player-centric desiGn?

When you create a game with highly complex interlocking systems and very little randomness, one like the board game Power Grid mentioned in chapter 6, you must understand
that your game will appeal to a certain type of player and not to others. Power Grid
appeals to what might be called mathematical strategists—people who enjoy deciphering
such systems and learning to optimize them. a shorter game in which randomness plays
a larger part will appeal more to casual players and young players. People choose a
game for the kind of gameplay that it offers, and mechanics create gameplay.
in other words, even though you can design a game around a mechanic, you must never
lose sight of the question, “Who likes this kind of game?” The player is still the center of
the designer’s world.

Summary
This chapter introduced the concept of design patterns: recurring structures that
appear in architecture, software, games, and other fields. After an overview of this
idea’s history, we identified 16 common patterns from game mechanics, in 3 categories (engines, friction, and escalation), plus several more patterns that don’t neatly
fit into a category. We ended the chapter by discussing some ways that you can use
the patterns in your own game design practice by combining them and brainstorming about them. The patterns can also be used to analyze games that you already

ChAptEr 7

in Fundamentals of Game Design, ernest adams proposed an approach to designing
games called player-centric design. The approach calls for the designer to imagine a
representative player and to judge all design decisions against his or her expectations
and hopes about the game. at first, this may seem to conflict with all our talk of feedback
loops and formal methods. But make no mistake: Player-centric design is still at the
heart of designing game mechanics, even at their most abstract.

170

Game mechanics: advanced Game desiGn

have in development. Another of their benefits is that they give you a common
vocabulary to discuss the characteristics of your game’s mechanics with other members of your team.
In the next chapter, we will introduce an even more powerful feature of
Machinations: the scripted artificial player. We’ll also conduct an in-depth analysis of two games, Monopoly and SimWar, showing how Machinations can be used to
model, simulate, and balance them.

Exercises
1. What design patterns did you use in recent game projects? What design patterns
might you have used that you didn’t? Could you have improved your game with
one of them? If so, how?

2. Think of a game that you know well. It can belong to any genre except pure
adventure games (which have no internal economy). What patterns can you find in
it? Try diagramming them in the Machinations Tool.

3. Choose two design patterns at random (we sometimes write the names of the
patterns on blank cards for this and then shuffle them and draw from the deck).
Can you identify a game in which they both appear? Alternatively, try to think of a
game concept that would use the two that you got. Create a Machinations diagram
for the game with appropriately labeled sources, drains, pools, and other elements.

ChAptEr 8
simulating and
Balancing Games
With simple games, you can compute the odds that a given player will win without
ever actually playing the game. This is commonly true of gambling games that have
trivial mechanics, such as blackjack or roulette. With more complex games, especially
those that include random factors, you have to play the game many times to find
out whether it is fairly balanced. In several of the examples in the earlier chapters,
we stated that the chance that a particular player might win or lose a game could
be simulated in a digital Machinations diagram. We arrived at the number we gave
based on data from thousands of simulated play tests. As you might guess, we didn’t
run through all those play tests manually. The Machinations Tool allows you to
define artificial players and run multiple sessions automatically to collect this type
of data. These techniques are especially helpful when you are balancing your game.
In this chapter, you will learn all about them.

As you learned in Chapter 5, “Machinations,” interactive nodes in Machinations
diagrams don’t operate until the user clicks them. (Interactive nodes are drawn with a
double line instead of a single one.) To simulate large numbers of play tests without
human intervention, the Machinations Tool offers a special feature that can act as an
artificial player. In a diagram, an artificial player is represented by a small square with
the letters AP inside (Figure 8.1). It should not be connected to anything. An artificial
player allows you to define a simple script to control other nodes in the diagram. This
way, you can automate the actions of a player; an artificial player can “virtually click,”
or activate, a node for you. (Artificial players are not limited to controlling interactive
nodes, however. An artificial player can activate any named node.) While running a
diagram with an artificial player, you can simply sit back and watch the action.

T I P The online
appendix c contains
a detailed tutorial
that shows you how to
create diagrams in the
machinations Tool.

FIGURe 8.1
a sample diagram with
an artificial player

171

ChAptEr 8

Simulated Play Tests

172

Game mechanics: advanced Game desiGn

Artificial Players in Machinations
N OT E machinations
artificial-player scripts
are not as powerful or
complex as the scripting languages used in
level design tools. You
don’t need to be a programmer to create an
artificial player script.

To add an artificial player to a diagram, select it from the Machinations menu and
place it somewhere on the diagram. Because it doesn’t need to be connected to anything, you can put it well out of the way.
Artificial players have a number of settings that allow you to control their behavior.
As with all Machinations nodes, you can set their color, line thickness, and label. An
artificial player has an activation mode like any other Machinations node (see the
section “Activation Modes” in Chapter 5 for more information). Most importantly,
an artificial player has a script that allows you to specify what other nodes the artificial player will activate when it fires. Executing this script is an artificial player’s
primary function.
When you select an artificial player node in your Machinations diagram, you will
see a script box in its element panel along with the artificial player’s other attributes.
This is where you enter its script.

T I P Because a script
stops the moment it
executes a command,
you cannot have two
direct commands in a
row in a script. The second one will never be
executed. But you can
have a sequence of if
statements. The script
will evaluate them in
order until it hits one
whose condition is true.
it will then execute that
command and stop.

A script consists of lines of instructions that tell the artificial player what to do.
They may take two forms: direct commands and if statements. A direct command
simply consists of an explicit order. An if statement begins with the word if followed
by a condition (explained in a moment) and then a command. When an artificial
player fires, it evaluates each line of its script in succession, starting at the top. If a
line is a direct command, it simply executes that command. If a line is an if statement, the artificial player checks whether the given condition is true, and if so, it
executes the command following the if statement. If the condition is not true, the
artificial player proceeds to the next line in the script. Once any command is executed, the
execution of the script stops; it does not evaluate the next line. The next time the artificial player fires, the script is evaluated again starting from the top.

direcT cOmmands
The most basic commands activate one or more nodes in the diagram as specified by
their parameters. Once a command has executed, the script stops. All the basic commands are variations on the word fire. Node names are case sensitive.
fire(node) This command looks for a node whose label matches the parameter and
fires it. For example, the command fire(Produce) will activate the source labeled
Produce in Figure 8.1. The fire() command can be called without parameters. If
you simply type fire() and don’t name a node within the parentheses, the script
terminates and no node is fired. The same happens if the parameter of the fire()
command doesn’t match any node in the diagram.

simULaT inG and BaLancinG Games

173

fireAll(node,node…) The fireAll() command does exactly the same thing as the
fire() command, but it accepts more than one parameter. When executed, it fires all
the named nodes simultaneously.
fireSequence(node,node…) The fireSequence() command is rather specialized: It activates the nodes listed in its parameters one at a time in order, changing to the next
node each time the command is executed. The first time the script executes fireSequence(), it will activate the first node in the parameter list. The second time the
script executes fireSequence(), it will activate the second node in the list, and so on.
It automatically keeps track of which one is next. If the command is executed more
times than it has parameters, it will simply start again from the first parameter. For
example, the command fireSequence(Produce, Produce, Upgrade, Produce, Consume)
will cycle through activating the source twice, the converter, the source again, and
then the drain in Figure 8.1.
fireRandom(node,node…) This command takes as parameters the names of multiple
nodes, but it selects one of them at random and fires it. To increase the probability
of it firing a given node, you can enter that node’s name more than once. For example, in Figure 8.1, the command fireRandom(Produce, Produce, Consume, Upgrade) has
a 50% chance of activating the source, a 25% chance of firing the drain, and a 25%
chance of firing the converter.

iF sTaTemenTs
The script of an artificial player also lets you specify conditional commands using if
statements. if statements consist of the word if, a condition specified in parentheses, and a command to execute if the condition is true.

There is no need for an else statement in the scripts for artificial players because the
script executes until it finds either an if statement that is true or one of the direct
commands. For example, the following script will fill the pool marked Resources in
Figure 8.1 with a few resources before randomly choosing between a Consume or
Upgrade action:
if(Resources>4) fireRandom(Consume, Upgrade)
fire(Produce)

ChAptEr 8

if(condition)command The condition in an if statement can refer to pools and registers to check the state of the diagram. For example, the script line if(Resources>3)
fire(Consume) activates the drain in Figure 8.1 when there are more than three
resources in the pool labeled Resources.

174

Game mechanics: advanced Game desiGn

An if statement allows you to perform calculations and string multiple conditions
together with logical operators. It works the way you would expect if you are already
familiar with if statements in programming languages like Java or C. Table 8.1 lists
the possible operators supported by the conditions in an if statement.

TAble 8.1
Possible Operators in
script conditions

perator

anation

e

==

equality

if(resources == 1) fire(consume)
Fire consume node when the number of resources equals one.

!=

nonequality

if(Upgrades != 0) fire(Upgrade)
Fire Upgrade node when the number of resources is not zero.

<=, <, >=, >

relational

if(resources <= 3) fire(Produce)
Fire Produce node as long as the number of resources is
equal to or smaller than three.

+, -

additive

if(Upgrades + 2 < resources - 1) fire(Produce)
Fire Produce node when the number of upgrades plus two is
smaller than the number of resources minus one.

*, /, %

multiplicative

if(Upgrades * 2 > resources / 3) fire(Upgrade)
Fire Upgrade node when the number of upgrades times two
is larger than the number of upgrades divided by three.
The % sign is used for modulo: if (resources % 4 == 2) fire
(Upgrade) Fire Upgrade node if the number of resources
equals 2, 6, 10, and so on.

&&

Logical and

if(resources > 4 && Upgrades < 2) fire(Upgrade)
Fire Upgrade node when there are more than four resources
and fewer than two upgrades.

||

Logical or

if (resources > 6 || Upgrades > 2) fire(consume)
Fire consume node when there are more than six resources
or more than two upgrades.

exTra cOmmands
Apart from the various kinds of fire commands, there are a few extra commands you
can use in a script for an artificial player:
stopDiagram(message)
Stops the execution of the diagram immediately, very much like an end condition
does. You can put a string of text in the parameter. If you have more than one artificial player, you might want to use a different message in the script of each player to
let you know which player stopped the diagram. When executing multiple runs (see
“Collecting Data from Multiple Runs”), the tool will keep track of how many times
each message appeared and let you know in a dialog box as the runs take place. This
will enable you to collect statistics on what causes a diagram to stop.

simULaT inG and BaLancinG Games

n

175

endTurn() Ends the current turn in a turn-based diagram.

activate(parameter) Deactivates the current artificial player and activates the
one identified by the parameter instead.

n

deactivate() Deactivates the artificial player.

Artificial players can also be used in a turn-based diagram (see the section “Time
Modes” in Chapter 5 for a discussion of turn-based diagrams). However, in that
case, their behavior changes a little. Most importantly, in a turn-based diagram, the
artificial player has a number of actions that indicate how many times it will fire
during a turn. When it has multiple actions per turn, these actions are executed at
one-second intervals.

NOT E When a
diagram uses colorcoding, the artificial
players may be colorcoded as well. in that
case, an artificial player
can fire only nodes
that are the same color
as itself.

special Values in conditions
if statements in a script allow you to use the following special values:

• random generates a random real number between 0 and 1. it is useful to create an
action that has a particular chance of occurring. For example, in the script if(random
< 0.25) fire(A), action a will have a 25% chance of firing. The random number generated can be used like any other value in a condition. For example, the script if(random
* 100 > Resources) fire(Produce) means that the chance of firing the Produce node
is inversely proportional to the number of resources in the resources pool. The more
resources there are, the smaller the chance that the condition will succeed; if there are
100 resources, it will never succeed, and the artificial player will never fire the Produce
node. This is useful for creating an artificial player that fires the Produce node only
when it detects that it needs more resources.
• pregen0 … pregen9 are ten special values that hold random values between 0 and 1.
however, in contrast to the random value, these values are filled only once when the
diagram starts and do not change while it plays.
• actions indicates the number of times the artificial player has fired.
• steps indicates the number of time steps that have been executed by the diagram.
• actionsOfCommand indicates the number of times the command after the if statement
has been executed.
• actionsPerStep indicates the number of times the artificial player has fired during the
current time step.

ChAptEr 8

n

176

Game mechanics: advanced Game desiGn

Collecting Data from Multiple Runs
Artificial players allow you to run diagrams
and test games automatically. To make the
best use of this option, the Machinations
Tool allows you to quick run the diagram
(Figure 8.2). You do this by switching to the
Run tab in the tool and clicking the Quick
Run button. While quick running, the diagram executes very quickly but doesn’t
allow any interaction. If you are using quick
run, you must make sure that the diagram
has an end condition and can actually reach
that end condition. If the diagram keeps on
running without reaching an end condition,
you can click the Quick Run button again
(which is now labeled Stop) to stop it manually. Click the same button once more to
reset the diagram back to its starting condition.

FIGURe 8.2 The run panel of the
machinations Tool

You also have the option to run a diagram multiple times. To do this, go to the Run
tab in the Machinations Tool and click the Multiple Runs button. By default, the
number of times that a diagram runs is set to 100, but you can easily change this
number in the Run tab. To prevent the tool from running endlessly, if a running
diagram in a multiple run batch doesn’t reach an end condition after 10,000 time
steps, it will stop automatically. When running multiple times, the diagram will
keep track of the number of times that each of its end conditions were reached. If
you have a game with two players that each have their own win condition (which
would be an end condition also), this makes it easy to determine who wins more
often. This feature was used to create the statistical data given in some of the examples in this book. When you run a diagram multiple times, the diagram also keeps
track of the elapsed time of each run and lets you know the overall average, which
can be useful when comparing different artificial player scripts to see which script
drives the economy toward a particular state (normally victory!) the fastest.
Finally, if your diagram contains a chart, the data from each run is stored in the
chart (Figure 8.3). By default, charts display the data from the last 25 runs, but they
store more. You can actually browse through all the data captured by the chart by
clicking the << and >> symbols below the chart. The data from the current run will
be bright while the other runs are dim. (Figure 8.3 is currently showing the results
from the 97th run.) To clear a chart’s data between simulations, click the word clear
on the chart. You can also save the collected data as a comma-separated values data
file (*.csv) for further analysis in a spreadsheet or statistics program. To do this, click
