a more traditional lock-and-key mechanism: The player must have the bow and at
least one arrow. Using the lock consumes arrows (and has a chance of failing). As
with the lockpicks in the previous example, the game must include some sort of
mechanism to supply the player with enough arrows to prevent creating a situation
in which he cannot proceed.

FIGURe 11.11
The bow and arrow
in Zelda combines a
regular key (the bow)
and a consumable
skill key (the arrows)
mechanism.

This type of lock does not display dynamic behavior; it contains no feedback loops.
Even more elaborate game mechanics for locks and keys, such as the bombling creatures in Zelda (Figure 11.12), create more interesting gameplay, but they typically
do not create the dynamic behavior we are looking for.

FIGURe 11.12
Bombling keys. Try this
in the machinations
tool.

Throughout this book, we have stressed the importance of feedback loops in the
creation of emergent gameplay. You might have noticed that so far, the lock-andkey mechanisms discussed in this section include little feedback. The activators in
Figure 11.9 create some feedback, as does the trigger to spawn a new bombling in
Figure 11.12. However, in both cases this feedback is very local and does not affect
the lock-and-key mechanics much.

PrOGressiOn mechanisms

255

cataloGinG lock-and-key mechanics
The machinations diagrams for different lock-and-key mechanisms help identify the
subtle differences among them and the issues you might encounter using the mechanisms in a game. There are many more lock-and-key mechanisms than we can document
here. as a designer, creating these little diagrams and studying their mechanics will help
you to build a repertoire of design lore. having a large catalog of lock-and-key mechanics will be very useful when you have trouble coming up with the right mechanism for
your game: simply go through the mechanisms you found in other games and find interesting opportunities to apply to your own game. a catalog of mechanisms is the game
designer’s equivalent of a collection of reference art that many professional artists use to
get inspiration from or to explore new ideas.

Dynamic locks and Keys

ChAptEr 11

To create lock-and-key mechanisms that involve more feedback, start by treating
the keys as a resource that can be produced and consumed, rather than as a simple
item that either is or is not in the player’s inventory. For example, Figure 11.13 represents a mechanism in which the player needs to harvest ten keys before she can
open the lock. (In this case, harvesting is an automatic action that happens when
the player is in the right location.) Feedback takes place through the application of
dynamic friction on the number of keys the player has collected. The more keys that
are harvested, the quicker the keys are drained. In this case, we might think of the
key as a kind of magical energy the player needs to unlock a door. This mechanism
makes it somewhat harder to estimate how many keys need to be harvested to get
past the lock. Obviously, this gets even more difficult as the distance between the
location where keys can be harvested and the lock increases. Unfortunately, the mechanism is not very interesting in itself: It boils down to harvesting enough keys and
then dashing for the door. There is little strategy involved. But we can improve on it.

FIGURe 11.13
a simple feedback
mechanism for a lockand-key mechanism

256

Game mechanics: advanced Game desiGn

We can create a more interesting mechanism by applying the dynamic engine pattern
to the mechanism. Figure 11.14 represents such a mechanism. This time, the player
needs to collect 25 or more keys to proceed, but now she has the option to invest 5
keys to increase the harvest rate by 0.5. However, this mechanism is probably too
simple. It is not very difficult to find out what number of upgrades is ideal for this
scenario (which also depends on the speed with which the player can move between
the different locations in the game). Worse, a disadvantage of this mechanism is
that it is optional: The player can reach the goal without upgrading at all. These
weaknesses should not come as a surprise: As we argued in Chapter 6, one feedback
loop alone is generally not enough to create an interesting dynamic mechanism.

FIGURe 11.14
applying the dynamic
engine pattern to the
mechanism

N OT E if this idea of
dynamically generated
keys seems strange to
you, remember that
we don’t necessarily mean physical keys
for physical locks in
physical doors. many
construction and
management simulations require players
to master part of their
economy to unlock
new buildings or other
features. a role-playing
game could use such
a system as the key to
solving a quest: The
blacksmith will reward
you if you can take over
his business and make
it profitable.

The emergence of a dominant strategy in the form of an ideal number of upgrades is
the direct result of the dynamic engine pattern. We have seen similar patterns already
in our discussions of Monopoly and the Harvester game. Games that mostly rely on
a dynamic engine as their sole, or single most important, feedback loop, as is the
case with Monopoly, usually include random factors to make it more interesting
and unpredictable. That would be an option, but it is not the direction we want to
explore here.
To create a more interesting lock-and-key mechanism, we can complement the
dynamic engine pattern by some form of dynamic friction (Figure 11.15). In this case,
enemies spawn that will steal and consume the harvested keys from the player.
Now the player has to balance between three tasks: harvesting, upgrading, and
fighting the enemies, whose numbers increase over time unless the player destroys
them. This is no longer a trivial challenge; beating the interactive version of the
Machinations diagram is already fairly tough and less straightforward than it looks.
Simply harvesting will probably not bring the player very far, and although it is possible to achieve the goal by switching between harvesting and fighting, this requires
the player to maintain a delicate rhythm of switching between the two for a long
time; it is very hard to accomplish. The player needs to find a balance between the
three actions to reach the goal. When the fighting is made skill-based, then the
most effective balance can actually vary depending on the individual player’s level
of skill.

PrOGressiOn mechanisms

257

FIGURe 11.15

The lock-and-key mechanism we have now leads to a gameplay that is very similar
to the gameplay of a real-time strategy game: Players must balance between harvesting raw materials, fighting, and upgrading their units to keep the enemies under
control and make the final push to complete the game. The combination of a dynamic
engine and some form of dynamic friction is the heart of most real-time strategy
games. For a multiplayer game, you might replace dynamic friction with attrition
(another form of friction) and add an arms race pattern to introduce more basebuilding options.

desiGn challenGe
can you design a lock-and-key mechanism that is built around the multiple feedback
pattern? Or any other design pattern that we haven’t applied to a lock-and-key
mechanism yet?

Structuring levels Around Dynamic locks and Keys
Level design that is built on relatively simple and nondynamic lock-and-key
mechanisms has to string many of these mechanics together. The big advantage
of dynamic lock-and-key mechanisms is that one or two of them can serve as the
backbone of a level; you don’t need as many mechanisms to create a compelling
and lasting gameplay experience. You can already notice this from playing around
with the diagram in Figure 11.15. Simply getting past its single lock will take a lot
of actions and considerably more time than most simple locks. More importantly,
the choice of actions available offers more freedom and requires more strategy from
the player to solve than a nondynamic lock-and-key mechanism that simply hides

ChAptEr 11

a multiple feedback
mechanism for locks
and keys

258

Game mechanics: advanced Game desiGn

many keys for a single lock in a maze, even though the actions that the player performs (navigating through a maze) are almost the same.
You don’t always have to create the dynamic lock-and-key mechanism for each
single level to structure a level around it. If the game you are working on already has
dynamic core mechanics, it makes sense to look at those mechanics first. Perhaps
there are already structures in them that would function perfectly as a dynamic
lock-and-key mechanism. If there are, it allows you to create levels efficiently, because
you don’t have to add extra mechanics to create locks and keys (assuming you want
them), and you can keep the game focused on the core mechanics. In other cases, a
few simple additions or changes do the trick. In those cases, you could add different
mechanics to the core to create different levels. When done right, this creates games
with variations in their gameplay and in which each level has its own unique feel.
Another advantage of using dynamic lock-and-key mechanisms to control progression, rather than simple static ones, is that you can change the difficulty of
the challenge by adjusting the numbers in the mechanism. One of the weaknesses
of simple lock-and-key adventure games is that it’s almost impossible to offer the
player a choice of difficulty levels because the relationships in the game are purely
binary: Either the player has the key or he doesn’t. A dynamic system is adjustable.
Structuring levels around a single lock-and-key mechanism is more common
than you might think. It works even for lock-and-key mechanisms that are not so
dynamic at all. For example, the level structure of dungeons in The Legend of Zelda is
built around the weapon you win from the midlevel mini-boss and the way it functions as a key to several doors. Most levels simply add one mechanism that requires
the player to collect multiple keys. Of course, lock-and-key mechanisms are not the
only form of challenge found in these levels, but they do play an important role in
creating the right structure of progression for the level. This combination of mental
and physical challenges creates the excellent gameplay experience of being a heroic
adventurer.

Emergent Progression
In many games of progression, the goal of the game is to reach a certain location
(and perhaps to perform an action there). Progress in these games is mapped to the
game space; the game is a journey. Figure 11.16 represents this type of progress in
its simplest form. The game informs the player of his progress, either directly with
a measure of distance traveled or indirectly by exposing the player to novel and
interesting locations. In designing a game that maps progress to space, lock-andkey mechanisms are the most important tool you have to structure the gameplay
experience.

PrOGressiOn mechanisms

259

FIGURe 11.16
Progress as a journey

However, there are more ways to look at progress in games. In the previous chapter,
we described progress in terms of how close the player is to reaching a victory condition. In this case, progress is not measured as space traversed but in terms of some
aspect of the game’s state. It can be convenient to think about how many actions
the player needs to perform or how much time he needs to bring about the target
state. Figure 11.17 represents this structure in its most elementary form.

FIGURe 11.17
Progress as an aspect
of the game’s state

Framing progress as a relationship to a particular game state allows us to think about
creating dynamic forms of progress from new angles.

Board games seem to use emergent mechanisms of progression more frequently than
video games do. Board games cannot rely on many rules or vast predesigned levels
the way video games can. They are restricted to the materials that fit into a single
box and cannot burden their players with a large set of rules to govern many different
individual cases. however, a number of board games aim to entertain their players for
long periods of time, sometimes even days! modern board games use a mixed bag of
techniques to achieve these results. They often come with boards that are built from
randomized tiles to create different starting positions (for example The Settlers of Catan,
shown in Figure 11.19), and they include rules that divide the game into different phases
with different gameplay in each (for example, Power Grid). however, the best, but also
the most difficult, way to create progression in such games is to set them up so that different gameplay phases emerge naturally from the mechanics rather than from arbitrary
rules. an example of this effect, one that we discussed in more detail in chapter 4,
“internal economy,” is chess: chess goes through distinct opening, middle, and endgame
phases. designing games that exhibit that type of emergent behavior is something of
a holy grail for almost every game designer and has the potential to turn your games
into modern classics. There is no reason why video games shouldn’t aim for that type of
gameplay as well.

ChAptEr 11

board Games rely on emerGent proGression
more Frequently

260

Game mechanics: advanced Game desiGn

Progress as a Resource
N OT E most roleplaying games don’t
let their players trade
or otherwise manipulate experience points,
but experience points
are absolutely central
to the game, figuring
in all sorts of calculations—they are simply a
resource that the player
cannot directly modify.
if the idea of progress
as a resource seems
strange, think of it in
terms of experience
points. (depending on
the game, they need
not be visible to the
player.)

To measure progress in terms of the game’s state rather than in terms of the player’s location, it’s best to treat progress as a resource in its own right. This offers you
many more opportunities to create interactions between the player’s progress and
other mechanics in the game. Experience points and character levels are classic
examples from role-playing games; they’re numbers that not only tell the player
how he’s doing but also can be used for internal computations. (Many RPGs include
weapons that are available only to characters above a certain level, for example.)
You can let players trade their progress points away for some long-term benefit
that will help them progress faster. If the object of a game is to be the first to earn
a stated amount of money, smart players might invest their money (thus apparently losing progress) in schemes that will earn new money faster. You can also use
a player’s progress to vary the difficulty of the game’s challenges as she plays. This is
exactly the way Space Invaders works: The speed at which the aliens move in a given
wave is proportional to the number the player has already shot. The more the player
kills, the faster they move and the harder they become to kill. Their speed also
increases from wave to wave.
Games that measure progress in terms of travel through space have to rely on
careful placement and ordering of the game’s challenges to create an appropriate
difficulty curve, and it will usually be the same every time the player plays the
game. Determining progress from the state of the game allows the mechanics to
adjust the difficulty automatically and to offer a different experience on each playthrough. You can also use the slow cycle design pattern to create oscillating degrees
of difficulty throughout the level.

proGress as a resource Vs. dynamic locks and keys
Treating progress as a resource is similar to, but more powerful than, using a dynamic
lock-and-key mechanism. With a lock-and-key mechanism, even a dynamic one, progress
toward unlocking that one lock is like optimizing a single resource. however, the way
that a lock-and-key mechanism affects the gameplay always depends on the mission
structure (when the player encounters the lock and what it unlocks) and its state is
binary—either the player has access to the goal or not. Treating progress as a resource
can have more subtle effects on the game and allow a wider range of effects than simple
wins or losses. For example, in a game in which the objective is to score a number of
points before the game ends, you can win by barely making that target or win by a large
margin. These differences are subtle but make progress as a resource more versatile.

PrOGressiOn mechanisms

261

storytellinG: When proGress as a Journey
still makes sense
We have made a number of arguments for representing progress in your games as
a function of the state of the game, and perhaps even as an independent, abstract
resource. it offers you more power and flexibility as a designer and enables you to give
the player more varied, less predictable experiences and, sometimes, more freedom to
choose her own goals. There is one game design situation, however, in which characterizing progress as a journey is still useful: when the game tells a story and the player
really cares about the quality of that story.
Good storylike experiences possess certain qualities that games do not always offer:

•
A story must not be repetitious. Every event in a good story should be unique and
created by the author for a specific purpose. even in stories that are about repetitive activities, authors describe the activity only once or twice and then jump ahead to a point
at which something new happens. Games, however, and especially simulations, often
include many repetitive events in the game world and repetitive actions by the player.
•
Stories must not move backward in time (except for rare, author-planned flashbacks). They must maintain novelty and momentum. a story’s world should never simply
return to a state it was in before; even if the protagonist has failed to achieve a goal, he
has learned something by his failure. While a game obviously cannot go backward in
real-world time, it can return to a state identical to one it was in earlier, which effectively
feels like going back to an earlier moment in game-world time.
•
Stories are about characters, and characters in good stories must behave in psychologically credible ways. The nonplayer characters in most games are simple automata
whose behavior is not believable.
This serves to illustrate an important point: dramatic tension (“what will happen next?”)
and gameplay tension (“am i going to succeed?”) are not the same thing, even if they appear superficially similar. dramatic tension dies if a story exhibits any of the weaknesses
mentioned earlier.
continues on next page

ChAptEr 11

•
The events of a story must hang together as a coherent whole; they must not feel
arbitrary, mechanistic, or random. The protagonist may experience reversals of fortune,
but they must be dramatic reversals; they should not feel as if they were caused by a
purely mechanical process. in contrast, game events are often produced by simple luck or
chaotic factors.

262

Game mechanics: advanced Game desiGn

storytellinG: When proGress as a Journey
still makes sense continued
To make a video game feel storylike, the vast majority of storytelling games map the
game’s progress and the story onto a space. The space is deliberately constructed to
provide novelty, and the player seldom spends very long in one location, which keeps
the story moving forward. such games often lock doors behind the player too, to prevent
her from returning to an earlier point in the story. Finally, the tasks in storytelling games
often consist of unique puzzles to avoid repetitiveness. adventure games typically have
no internal economy at all, only simple lock-and-key mechanics.
however, this does not mean that our suggestion about progress as a resource can
never be used in games with a story. some game stories are merely framing narratives
between levels and so cannot be harmed by the mechanics. Other games integrate their
plots more tightly with the gameplay but don’t expect the players to take them too seriously. action-adventure games such as our oft-cited Legend of Zelda series usually tell
a story to provide motivation and context for the player’s actions, but the players are
mostly interested in gameplay tension, not dramatic tension. even if they appreciate the
context that the story provides for the gameplay, literary quality is not the point.
emergent storytelling, which we mentioned briefly in chapter 10, is a research field
that seeks to resolve the inconsistency between traditional gameplay experiences and
traditional story experiences. a hypothetical emergent storytelling game would use
gamelike emergent mechanics to create gameplay and an emergent progression system
to generate dramatically interesting plot events without an author’s involvement. at the
same time, it would somehow guarantee that the experience feels properly storylike,
without repetition, randomness, reversals in time, or noncredible characters. some efforts to create such a system have used artificial intelligence to search through possible
future events in a plot the way a chess program searches for possible future moves in a
chess game. instead of trying to checkmate the king, the search algorithm tries to find
an enjoyable plot. To date, no one has succeeded in building a full-game-sized emergent
storytelling system. all the efforts thus far have produced only small prototypes.

Producing Progress Indirectly
We can take the idea of progress as a resource one step further by having the players produce progress indirectly and measure progress over multiple resources. In this
case, there isn’t one particular action that produces progress. Instead, the process to
produce progress involves multiple steps and multiple resources.

PrOGressiOn mechanisms

263

This approach is common in open-ended simulation games. For example, in the
space trading classic Elite (Figure 11.18), players fly space ships to trade across a
vast galaxy. It inspired many space trading games such as the Privateer series and the
MMO Eve Online. Most of the money the player earns will be invested back into her
ship. A better ship allows the player to travel farther and into more dangerous, but
also more lucrative, quadrants of space. The player’s progress in the game is measured
by the quality and capacity of her ship—a collection of concrete resources. Although
the open-ended nature of the game permits players to choose their own goals,
acquiring a powerful space ship and amassing wealth seems to be a common target
for most players.

ChAptEr 11

FIGURe 11.18
Elite

In Elite, it is also possible to lose progress: The player’s ship may be attacked and
destroyed, the player can fire precious missiles to fight off pirates, or the player
might use an expensive one-time intergalactic hyperdrive. Losing progress in this
way is fairly uncommon in games in which progress is represented as a journey, but
it’s entirely normal in simulation games.
Another good example can be found in the board game The Settlers of Catan (Figure
11.19). The objective of this game is to score ten points. Points are scored for building villages, upgrading villages to cities, building the longest road, playing the most
knights, or being lucky in the purchase of development cards. All these point-scoring
mechanics are interrelated. The player can’t simply build a new village and get a
point any time he wants; he must build roads to suitable locations and acquire the
right set of resources. Building a village isn’t the endpoint of the process, either. It
increases the player’s chance to gain new resources, while upgrading a village to a
city increases its resource output.

264

Game mechanics: advanced Game desiGn

FIGURe 11.19
The Settlers of Catan
with the Seafarers
extension.
Photo courtesy of alexandre
duret-Lutz under a creative
commons (cc BY-sa 2.0)
attribution license.

Figure 11.20 represents most of the economy of The Settlers of Catan, though certain mechanics, such as the extra points scored by building the longest road and
by playing the most knights, have been omitted. Figure 11.20 is turn-based and
uses color-coding to distinguish among the five resources in the game. The production mechanism reflects the fact that both cities and villages generate a chance to
produce a resource every turn, while every city increases the chance that the production rate is doubled. We advise you to play around with the online version of
the diagram to fully grasp the way the game’s internal economy works.
The economy of The Settlers of Catan is dominated by a dynamic engine that is also
subjected to a engine building pattern and that interacts with a trade pattern. The
game manages to avoid the typical gameplay signature associated with a dynamic
engine by creating several options to invest and by having all these investments add
to the game’s progress. The simple accumulation of resources is not the point of the
game. Another side effect of using an indirect measure of progress is that it’s not
trivial for players to accurately read the state of the game. Although it’s fairly easy to
see how many cities, villages, and resources each player has, because of the indirect
way that points are computed, it’s hard to guess who is actually closest to winning,
especially because the number of available building sites is limited. A player might
need just one extra village to score the extra point, but if all building locations have
been taken by other players, it will be impossible. The player will need many ore
and wheat resources to build a city, and those resources might not be easy to come

PrOGressiOn mechanisms

265

by. So, even though he seems to be close to victory, he might be far from reaching
it. Also, the nature (but not the number) of each player’s trade goods is hidden, and
the dynamic engine relies on a random mechanism, which further complicates trying to assess who’s ahead. By comparison, it’s obvious in Monopoly, because all the
players’ possessions are in plain view.

FIGURe 11.20
The economy of The

Because The Settlers of Catan measures progress indirectly, it is possible to win in
more than one way. Players might go for many villages and cities or, alternatively,
bet on getting the right development cards. The first option is a fairly safe choice
but requires many resources, while the cards become a good option when the player
has fewer resources; it represents something of a high-risk, high-reward strategy.
The Sims also measures indirect progress over many different resources. The player
takes control of a number of sims: simulated people who live in something that is
best described as a virtual dollhouse (Figure 11.21). The player’s success is measured
in terms of the material goods (furniture and features of the house) that the player
accumulates for his sims but also by the advancement of the sims’ professional
careers. The Sims is a time-management game in which the player must use the limited time available to perform all the activities necessary to keep them happy and
healthy. By taking good care of his sims, they will find jobs. If they make it to work
on time and in good health and good spirits, they will advance their careers. Better
jobs means they will bring home more money that the player can spend on items
to entertain the sims and to make their daily routine run more efficiently. Although
the game does not state that the goal is to guide the sims toward material and professional success, it is implicit in the mechanics, and many players play it that way.

NOT E many people
have criticized The Sims
for its relentlessly materialistic approach. Your
sims have no spiritual
life and seem not to be
able to derive happiness from anything but
extravagant furnishings. a close reading
of the tongue-in-cheek
descriptions of the
furniture in the game
shows that the developers were perfectly
well aware of what they
were doing. The game
is a satire.

ChAptEr 11

Settlers of Catan

266

Game mechanics: advanced Game desiGn

FIGURe 11.21
The Sims 3 in a mode
showing the furnishings and elements of
the economy in the
overlay at the bottom

emergent Progress and Gameplay Phases
One of the jobs of traditional, nonemergent level design is to create varied, wellpaced gameplay. When progress is measured by movement through space, the level
designer’s ability to craft that space gives him a lot of control over this aspect of the
game. But when progress is an emergent property of the dynamic system formed by
the game mechanics, this type of direct control over the gameplay becomes impossible. However, that is not to say that games with emergent progression cannot have
varied and well-paced gameplay. It only means that pacing and variation need to be
created differently.
In games of emergence, variation and pacing have to come from different phases
that the game goes through. In this case, a gameplay phase is a period of time in
which the dynamic behavior of the game follows a certain pattern. When a significant shift in the dynamic behavior occurs, the game progresses to a new phase.
For example, in a typical real-time-strategy game, the initial phase is dominated by
resource harvesting and base building. The player quickly accumulates resources
and invests in defensive buildings and units. At a certain point, the player’s behavior will change: He will start building an offensive force to explore the map. During
this phase, the focus is more on capturing strategic points on the map and perhaps
on securing access to future resources. Once the player has accumulated enough
resources and has found the location of the enemy base, he will probably launch a
massive attack to try to overcome his opponent.
Figure 11.22 maps these phases to distinct patterns in the resources and production
rate of the player. The chart shows that during each phase the changes to the state
of the game follow a particular pattern that is relatively stable. During the building

PrOGressiOn mechanisms

267

phase, the player spends his resources fast, while his production rate grows quickly.
During the exploration phase his resources accumulate because his focus is on a different aspect of the game. During the offensive phase, the number of resources go
up and down as the player switches between building and launching attack waves.

FIGURe 11.22

These three phases do not have to occur in the game, and when they do occur, they
might occur in a different order. The rushing strategy (see the section “Balancing
SimWar” in Chapter 8, “Simulating and Balancing Games”) partly depends on
executing a very short building phase and then skipping the exploration phase
and going on the offensive immediately. There are also other possible phases. For
example, a level that requires that the player capture and use resources spread
around the landscape might have consolidation phases that are mixed in between
different exploration phases. If there are multiple enemy bases, the first offensive
phase is probably followed by a similar consolidation phase. Games that emphasize
technology tree mechanics probably have a research phase, a period during which
neither offensive activity nor construction takes place, but players invest resources
to upgrade their units and production buildings.

phase transitions and complexity theory
shifts between multiple stable states in dynamic systems are an important research
topic in the science of complexity. For example, congestion in traffic is often studied
in the same terms. There are two main phases of the system, normal flow and traffic
jams, with some intermediate states. researchers hope to learn what triggers the shifts
between these phases. Phase shifts in traffic flow seem to be somewhat analogous to the
phase transition between solids, fluids, and gasses in chemistry. For example, when you
gradually heat water, nothing much happens until you reach the boiling point, when it
suddenly changes into a gas. something similar happens with roads. if you increase the
“traffic pressure” by adding more cars, the flow and average speed will be normal for a
while, until it suddenly drops and the road is jammed. shifting back to a noncongested
state might require decreasing the traffic pressure far below the point where the jam
started in the first place. in many complex systems, you see a similar asymmetry in the
changes required to go from one state to another. if this asymmetry is large, the phases
tend to be more stable; if the asymmetry is small, the system can oscillate between the
phases more easily.

ChAptEr 11

charting phases in an
rTs game

268

Game mechanics: advanced Game desiGn

Composing Gameplay Phases
When you are designing levels for a game that has a number of these emergent
gameplay phases, your job is to compose a desired gameplay experience from them.
Suppose that, in our real-time strategy game, your design goal for a particular level
is to emphasize the first building phase. You can achieve this by harassing the
player early on with small groups of enemies that attack frequently. This forces the
player to maintain a delicate balance between increasing production and building
up defenses, and it slows down the former considerably. The effect will be that the
building phase will probably be much longer. By creating a map in which resources
are relatively scarce and scattered, the player is more likely to go through several
exploration and consolidation phases.

scriptinG Vs. emerGence
When you are composing the gameplay phases for a game or a level, you can try to
have all the different phases emerge naturally from playing the game. however, in
many cases, it is more effective to force a few changes through deterministic or dynamic
scripts. For example, in many levels of the single-player campaign of StarCraft (and many
other rTs games), the game designers planned specific attack waves to be launched
against the player by the ai. some of these events simply occur at a fixed time, while others are triggered when the player reaches particular points on the map. even when you
are aiming for dynamic, emergent gameplay, don’t be afraid to mix in some more direct
forms of progression in this way. When done subtly, you create a highly dynamic game or
level that offers great variation and has a high replay value.

It often requires a major event to initiate a shift between gameplay phases. While a
game is in a particular phase, it is in balance, and the player probably settles into a
certain rhythm of play. We have identified several design patterns that are commonly
used to create significant events that can cause the game to shift to a new phase.
Slow cycle. In the previous chapter, we discussed the slow cycle pattern in
StarCraft II to shift the game between distinct defensive and offensive phases. In
general, a slow cycle is effective but also a little lacking in subtlety, especially when
the player has little impact on the slow cycle mechanism. (According to legend,
King Canute demonstrated the limits of monarchical power by showing that he
could not hold back the tide, a classic slow cycle.) On the other hand, the slow cycle
pattern tends not to produce events as dramatic as those we describe next.

n

Static friction/static engines. When static friction is infrequent but has a high
impact, it can cause phase shifts. Caesar III contains a good example (see Chapter 9,
“Building Economies”), in which periodic invaders and periodic demands for trade
goods by the emperor create high-impact static friction. Because the balance of the
city economy is delicate, these events can easily throw the economy into a phase
of decline, where lost access to resources causes citizens to leave town, reducing the
labor force and lowering production.

n

PrOGressiOn mechanisms

269

The opposite case is a static engine that infrequently produces many resources. This
can cause the game economy to shift from periods of scarcity to periods of abundance. In Caesar III, the arrival of trade caravans from neighboring cities can have
this effect.
Escalating complexity. The escalating complexity pattern depends on a transition between two gameplay phases. As long as the player can keep up with the rate
at which complexity is created, everything seems under control, but as soon as the
pace passes a certain threshold, the positive feedback mechanism will push the
game to a rapid conclusion; it creates a short losing phase in which the player suffers reverses. In Tetris, these two phases are easily recognizable. Most of time the
player is in control, but as soon as the blocks start dropping faster than he can field
them, the game shifts to the losing phase. In Tetris, the complexity production
involves a random factor: the type of block that is being produced. This means that
through some luck and extra effort on the part of the player, she can push the game
back from a losing phase to the normal phase.

n

Stopping mechanism/multiple feedback. When a gameplay phase depends
on a particular action to continue, you can use a stopping mechanism to make that
action less effective because it is used more often. This means that the phase cannot last forever and will cause a shift to a new phase. In The Seven Cities of Gold, a
game about exploring (and exploiting) the New World, the player could avoid conflict with the Native Americans by using a feature called “Amaze the natives.” This
worked well at first but became less effective over time, and the player soon had to
use other strategies to succeed, a phase shift. The stopping mechanism is normally
quite subtle. In addition, if the effect of the stopping mechanism does not last, the
game might shift back to the earlier gameplay phase. In most cases, any subtle and
slow form of multiple feedback will have a similar effect.

desiGn challenGe
The previous list is not complete or exhaustive. What mechanisms/patterns can you think
of that create gameplay shifts in games like Caesar III or StarCraft II?

Progression through emergent phases is difficult to control. But by creating mechanisms that are likely to create phase shifts in those systems, you can set up economies
in which you can predict what type of phase progressions might occur. For example,
in Tetris you don’t know when the game is going to shift to the losing phase, but
because one of the mechanisms that causes this shift (the drop rate of the blocks)
slowly increases, you know that it will eventually happen. As you gain experience
and confidence as a designer, you will find that you will become much better at
designing this type of emergent progression and can use it to build engaging systems
that don’t depend on scripted events.

ChAptEr 11

n

270

Game mechanics: advanced Game desiGn

Summary
In this chapter, we continued our exploration of ways to more closely integrate
game mechanics with progression techniques. We first examined a variety of
traditional lock-and-key mechanisms and showed how they can be extended by
creating dynamic systems that serve as keys to unlock new regions or new features
of the game.
In the second half of the chapter, we considered ways to make game progression
an emergent property of the game rather than a simple factor based on a player’s
position in the game space. By treating progress itself as a resource, or as a value
computed from a combination of factors, it becomes possible to create games with
much less predictable progression patterns. Using the slow cycle and other design
patterns, you can also break the game’s progress into distinct phases, which creates
variety in the gameplay for the player.
In the next chapter, we turn our attention to the ways you can use game mechanics to transmit a meaningful message from the designer to the player. As people start
using games more and more to teach, inform, and persuade, this is an increasingly
important topic.

Exercises
1. Review your recent game designs. Find a lock-and-key mechanism. Without
adding new mechanisms to the game, try to find at least three different ways to
create different locks for the same key.

2. Pick two random design patterns from Appendix B and use them to create
a dynamic lock-and-key mechanism. Can you use that mechanism as the basic
structure for an entire level?

3. Find a published game of emergence that clearly has a distinct number of gameplay phases. Can you identify what mechanisms work to stabilize a phase, and what
mechanisms work to create transitions between phases?

4. What patterns can you use to create emergent gameplay phases in the Lunar
Colony game? (See the section “Designing Lunar Colony” in Chapter 9, “Building
Economies.”)

ChAptEr 12
Meaningful Mechanics
The conventional video game industry devotes its attention to creating entertaining
(and profitable) games, but games can be used for much more than entertainment.
An increasing number of companies are dedicated to building games to teach, persuade, enlighten, and even heal. Many of these games try to transmit a message of
some kind to their players. They can do this in various ways, but here we are concerned with mechanics and their interaction with the other parts of the game—the
setting, the artwork, and the story (if any).
In this chapter, we will discuss how you can create mechanics that are meaningful.
First we’ll look at serious games and what they do. Then we’ll examine communication theory and semiotics and apply the lessons learned from these disciplines
to game design. Finally we’ll look at games that offer multiple layers of meaning,
including meanings that contradict each other, a phenomenon known as intertexual
irony. Even if you’re primarily interested in building entertainment games, you can
use the lessons in this chapter to create entertainment games that are more meaningful and have a message of their own.

Serious Games

ChAptEr 12

Play and learning share a long history. Humans, and many animals too, have always
used play to prepare for more serious tasks in later life. When children play hideand-seek, they exercise some of the same skills that hunters use. Hunting skills are
not as vital as they once were, but other children’s games such as playing house and
driving pedal cars are still relevant and prepare them for activities that will probably
be in their futures.
When play evolved into the more structured activity that we call gaming, it retained
this learning aspect. Game designer Raph Koster wrote a book called A Theory of Fun
for Game Design (2005) about the relationship between fun and learning in games.
He argues that, no matter what game you play, learning and mastering the game is
what triggers our fun experience. You probably recognize the triumphant feeling you
get when you figure out a puzzle in a game and execute the right moves to beat that
level. Playing games is a constant process of learning: learning the goals, learning the
moves, learning the strategies to achieve those goals. This goes for all types of games,
even if they are abstract puzzle games like Tetris that have no obvious similarities to
tasks in real life. Although Koster’s viewpoint is a bit overstated (there are many sources
of fun in games besides learning, such as social interaction and aesthetic pleasure),
his essential point is correct: Gameplay involves learning in an enjoyable form.

271

272

Game mechanics: advanced Game desiGn

the Gamer Generation
video games are now ubiquitous in the developed world. an entire generation has grown
up playing them. The lessons these games taught them has changed their stance in life.
in their book The Kids Are Alright (2006), John Beck and mitchell Wade argue that the
current gamer generation has a different attitude toward work than previous generations
did, produced by their experience as gamers. For example, gamers are likely to regard
failure as a temporary setback rather than a disaster. a lifelong diet of failed attempts
and restored game sessions has reduced their fear of failing. in addition, in games every
problem has a solution. The player might not see it immediately but has an implicit trust
that the game is fair and the designer has included a way of overcoming its challenges.
This has trained gamers to approach real-life problems with more confidence and with a
can-do mentality, even though life is less fair than games are.

The term serious game was devised in recognition that games can be used for purposes
other than light entertainment. There is no standard definition of serious game, but
Ben Sawyer, a well-known proponent, suggests an inclusive description: “Serious
games solve problems.” A serious game is designed to achieve a real-world effect of
some kind. Many of them use the player’s openness to learning while playing games
and use the game to teach something. Games also offer an opportunity to experiment
with new approaches to problems safely, inexpensively, and without consequences.

early Serious Games
Serious games drove the development of modern board games, long before the computer was invented. What we know as Monopoly today originated as a serious game.
It borrows heavily from an earlier work called The Landlord’s Game (Figure 12.1).
The game was designed in 1904 by Elizabeth Magie to show the consequences of an
unrestrained capitalist economy. She wanted to demonstrate that the system of purchasing property and renting it out enriches the people who own the property while
impoverishing the tenants. The name Monopoly is an ironic reversal of the original
game’s intended message, but the game’s history does explain why its victory condition requires bankrupting the other players rather than simply amassing the largest
fortune.
Most modern war games, either computer-based or tabletop, can trace their history to another serious game: Kriegsspiel (which is simply German for “war game”).
Kriegsspiel was first developed by the Prussian Lieutenant Georg Leopold von
Reiswitz in 1812. Later, he and his son refined it for the Prussian army to train their
officers in battle tactics and strategy (Figure 12.2). In Kriegsspiel, players take turns
to move colored wooden pieces over a map representing the battleground. Rules
restrict how far pieces can move, and dice are used to determine the effects of one
unit firing at another unit or engaging in close combat. If you have ever played a
tabletop war game, this should sound familiar.

meaninGFUL mechanics

273

FIGURe 12.1
The Landlord’s Game board
from the original patent

FIGURe 12.2
Kriegsspiel.

ChAptEr 12

Photo courtesy of
andrew holmes.

274

Game mechanics: advanced Game desiGn

Kriegsspiel was a revolutionary innovation in the training of military officers. Despite
its simplistic rules that replaced gun battles with die rolls, it actually improved the
strategic skills of the officers who played it. Kriegsspiel allowed its players to try different battle strategies and explore their strengths and weaknesses without any
consequences. It also gave them a chance to step into the shoes of their adversaries
and think through strategies from their perspective. After a series of successful military campaigns throughout the nineteenth century, many nations in Europe and
beyond adopted war gaming as a method for training military officers.

takinG Games seriously
some nations had trouble taking war games seriously. They did not understand how a
comparatively simple game that used dice to resolve combat could possibly be relevant
for the chaos and complexity of real-life battles. The history of war games is riddled
with interesting anecdotes of success and failure caused by taking war games seriously
or ignoring them. in 1960, U.s. admiral chester nimitz asserted that the conflict with
Japan during the second World War was so thoroughly tested in war games that the
only unanticipated event was the appearance of the kamikaze fighters. in contrast, the
russians ignored their own war game results early in the First World War and suffered
a disastrous defeat at the Battle of Tannenberg. (For more information, see the history
of war gaming on the website of the historical miniatures Gaming society: www.hmgs.
org/history.htm.) an important lesson from the history of war games in preparing for real
military conflict is that games with relatively simple and quite unrealistic rule systems
can still accurately capture the essence of the real situation they represent and can be an
excellent learning tool.

Serious Video Games

N OT E an excellent
modern game that
teaches fractions is
Refraction. You can
play it online at
www.kongregate.com/
games/GameScience/
refraction.

People have designed video games for serious purposes since the 1980s, originally
as educational tools. Unfortunately, in the rush to embrace new technology, many
early educational games proved to be a disappointment, and the term edutainment,
once popular, is now avoided. Too many of the early educational games were nothing but thinly veiled multiple-choice tests. This produced games whose gameplay
was constrained and uninteresting. (Of course, there were exceptions, such as the
highly-regarded Oregon Trail.)
Modern educational games are better designed, and now they’re used in schools
and at home to teach everything from mathematics to typing. They integrate their
gameplay more closely with their subject matter, and they use the power of emergent mechanics to teach principles, not just facts.

meaninGFUL mechanics

275

Serious games go far beyond education, however. Online you can find many advergames: games designed as an advertisement to sell a product. Today, many political
campaigns commission games that make fun of their opponents, and both news
agencies and game companies have started to experiment with short games that
comment on current affairs as a new version of the editorial cartoon in newspapers.
Games have found many uses in the field of health care, from psychological and
physical therapy to training physicians and surgeons.
It is not easy to deliver a particular message in a game that offers the kind of
dynamic freedom that games of emergence create, but we are convinced that it is
possible. As we mentioned at the beginning of this chapter, playing a game (especially for the first time) is a process of enjoyable learning. There is no reason why
a game cannot be fun and meaningful at the same time. In fact, there are many
good examples of commercial games, such as SimCity or Civilization, that have been
used as part of educational programs to teach social geography or political history.
In the 1980s the U.S. State Department used Balance of Power, a game about the geopolitical struggle between the United States and the Soviet Union, as a training tool
for diplomats.
To explain how serious game designers can use game mechanics to send messages, we
turn to communication theory and semiotics, the study of signs and their meanings.

GamiFication

