purchase, which means it’s not necessary to have a card-clearing mechanism
in the market. Eventually, the first option will be worth taking for the coins
piled on it.
This implementation isn’t strictly a traditional Dutch Auction, since
more than one good is up for auction at the same time. It’s also typically
mediated by turn order: you can only make a purchase on your turn.
Because of different mechanisms for adjusting the market each turn, every
player does not have an equal opportunity to pay any price they wish for a
given good. In some cases, like Through the Ages, calculating at what cost

Auctions

305

a card will be available to you, or manipulating that by purchasing cards
that are cheaper and forcing cards to slide down multiple positions is a key
strategy.
Despite some of these issues, the market row has become a staple of game
design and a favorite method for reasonably fair resource allocation. The
logic of this mechanism can sometimes find its way into worker placement
games. For example, in Agricola, some buildings will accumulate resources
if nobody places a worker there. Eventually, the rewards available are so
rich that someone claims them. Through the lens of the Dutch Auction,
we’d say that the price per share kept going down until a buyer was willing
to purchase the whole lot. This isn’t quite a Dutch Auction, it’s really an
auction with a fixed price (one worker, though it could be a monetary price
in a different context), but in which the rewards increase. However, note
that unlike traditional auctions, this auction shares a primary feature with
Dutch Auctions, which is that the value moves in favor of the buyer. Dutch
Auctions use price to effectuate this, rather than size of return, but they are
conceptually quite similar.
Dutch Auctions as implemented through market rows are quite a robust
and durable solution for game designers. They typically don’t take up too
much board space, they’re ergonomic, decisive, quick, and make for interesting
decisions. In some games, like Morels, or Majesty: For The Realm, they can
be a bit tedious when it comes to constantly sliding down cards. Vikings uses
an ingenious wheel mechanism to address this situation elegantly, by placing
the prices on the wheel and rotating it to adjust the prices of the tiles laid
around its perimeter.
Designers will frequently turn to this river-of-lots mechanism when using
some non-monetary currency for resource acquisition. The aforementioned
Through the Ages uses an Action Point currency (ACT-01) for card acquisition.
Though Small World themes the cost as monetary, money is worth an equal
number of victory points, so the actual cost to acquire a lot is victory points.
This mechanism is also quite amenable to variations involving allowing players
to reserve a card in the market for purchase later at a lower price, or claiming
a card so that its eventual acquisition cost is paid directly to the player.

Sample Games
Agricola (Rosenberg, 2007)
Majesty: For the Realm (Andre, 2017)
Merchants of Amsterdam (Knizia, 2000)

306

Building Blocks of Tabletop Game Design

Morels (Povis, 2012)
Pax Porfiriana (Eklund, Eklund, and Gutt, 2012)
Small World (Keyaerts, 2009)
Suburbia (Alspach, 2012)
Through the Ages: A Story of Civilization (Chvátil, 2006)
Vikings (Kiesling, 2007)

Auctions

AUC-09

307

Second-Bid Auction

Description
This mechanism modifies other auctions, such as Turn Order Until Pass, or
Sealed Bid. The amount paid by the Highest Bidder is equal to the second
highest bid.

Discussion
In game theory, Second-Bid auctions, also called Second-Price auctions, or
Vickrey auctions, are well studied in relation to the question of how will the
choice of auction type impact the price of a good? If I have a car that I want to
sell, for example, which auction type will fetch me the best price? One way to
ensure the highest possible price for the seller is to use an auction mechanism
that encourages bidders to make mistakes in their bidding strategies. A Dutch
Auction (AUC-08) is a great example. The added pressure of the clock, and
the possibility of someone else making a bid that can’t be countered leads to
somewhat higher settlement prices than a traditional English Auction.
In many cases, there is a desire to create a fast and fair auction, in which the
best strategy for all bidders is to simply bid the highest price they are willing

308

Building Blocks of Tabletop Game Design

to pay. In a traditional auction, the correct strategy is to bid $1 more than the
previous bid until your reserve point is met. You don’t increase your bid by
more than $1 over the previous bid because maybe nobody will outbid you
and you’ll win the auction at a lower price than the amount you were willing
to pay. This makes for slow going at times.
A second-highest auction is the solution to the question of how to make
auctions fast and fair for buyers and sellers. In essence, your bid in a SecondPrice auction is not an offer to pay that amount, but to pay anything up to
that amount. Your bid of $1,000 is really a bid of $999, such that anyone who
wants to buy the item must pay $1,000 or more. The dominant strategy in a
Second-Price auction is to bid your true value for the lot. If all other players
value the lot at a lower price, you’ll pay their valuation, not your higher price.
If other players value the lot higher than you, you won’t win, but they’ll never
pay less than your true value.
Vickrey Auctions are extremely rare in board games. The only example
we were able to turn up was Reiner Knizia’s Das letzte Paradies (The Last
Paradise), a largely forgotten title. In part this is because Vickrey Auctions
aren’t that different from other auction types when it comes to board games.
In any non-blind auction method, a Vickrey settlement method will yield a
final price that is roughly the same as the non-Vickrey, or perhaps one bid
increment smaller. That’s a lot of rules overhead for such a small change
in price. In blind bidding systems, the Vickrey does impact actual prices
more substantially, but in many cases, the game design capitalizes on that
inefficiency in the auction. Put another way, the returns to bidding skill are
higher in Non-Vickrey Auctions, whereas Vickrey Auctions provide a clear
dominant strategy to the bidders. In a sense, the efficiency of Vickrey Auctions
may make them less interesting for gameplay.
Perhaps another important reason Vickrey Auctions aren’t used is because
their game-theoretical impact isn’t patently obvious to players. If you explain
the way the auction works, most players don’t intuitively understand that
their best bet is to bid their true value. A game that uses Vickrey to try and
make auctions more fair and less chaotic may find that players are simply
confused by it.
Where Vickrey Auctions really shine is in a situation that doesn’t come
up in board games very often, which is in allocating a large lot of identical
goods. Want to sell 100 tons of cinnamon? A Vickrey Auction is a great way
to find the settlement price at which all 100 tons will sell. Once that price is
found, even bidders who offered more for some portion of the lot will only
be charged the lowest price that clears the whole lot. In essence, the buyer is

Auctions

309

trading away the highest possible returns for speed and certainty in the sales
process. An echo of this idea can be found in Harbour, where a player must
sell their entire lot of goods when they choose the sell action, but this sale
is to the bank. One might imagine that this transaction is the end result of
a Vickrey Auction that happened off-sceen, so to speak. Vickrey Auctions,
though important for study and for understanding auction strategies, have
relatively few practical applications in board games, at least so far.

Sample Games
Das letzte Paradies (Knizia, 1993)
Harbour (Almes, 2015)

310

Building Blocks of Tabletop Game Design

AUC-10

Selection Order Bid

Description
Selection Order Bid is a form of multiple-lot auction in which players are not
directly bidding on the lots themselves, but the order in which they’ll draft
the lots. As the bid increases, players may pass and accept a later place in the
order. In some cases, players must pay their entire current bid (an all-pay
mechanism), and in others they may recover some of their bid.

Discussion
There are many systems for auctioning off multiple lots, but Selection Order
Bid may be the most elegant. An elegant example is For Sale, where players
bid to draft first from a collection of property cards. The cards range in value
substantially, and a given flop of cards can either cluster closely, with the

Auctions

311

lowest being separated from the highest by only a few dollars, or they can
be spaced quite widely apart. Players bid in turn order for the right to draft
first. A player may choose to pass and collect the lowest-value card remaining.
When passing, the y pay half their previous bid. The last player to remain
in the auction receives the most valuable card but must also pay his or her
full bid.
Another way to think of the pay-half-when-pass variant is that it’s actually a
simultaneous bid on two lots: a full-price bid on the most valuable money card,
and a half-price bid on the least valuable remaining money card. Considered
in this fashion, Selection Order Bid is a type of constrained bidding system, or
even a sort of ante. If you want to bid $10 on the high-value card at the open
of the auction, you’re essentially agreeing to pay $5 for the lowest-value card,
which you could have had for free. This is somewhat analogous to a penny
auction, where players must pay a fee for each bid they make, even if it is not
the winning bid. The halved value of the bid that will certainly be spent can
be seen as the bid fee, rather than a bid itself.
In certain games this type of auction also forces players to evaluate how
much lots may be worth to other players. For example, if players are collecting
different symbols or colors, the lots will have different values to different
players. If a certain lot is only good for one player, that player can take a
chance and bid low assuming that the lot will be remaining when the player’s
selection opportunity comes.

Sample Games
Age of Steam (Wallace, 2002)
Eggs & Empire (Pinchback and Riddle, 2014)
For Sale (Dorra, 1997)

312

Building Blocks of Tabletop Game Design

AUC-11

Multiple-Lot Auction

Description
An auction in which players simultaneously bid on Multiple Lots in parallel,
instead of bidding for one lot at a time serially.

Discussion
Multiple-Lot Auctions are very common in tabletop board games because
they compress the amount of time it takes to allocate lots among the players,
and because the physical affordances of board games, like tableaus and playercolored tokens, lend themselves to organizing and displaying information
needed to run these types of auctions clearly.
Multiple-Lot Auctions ask players to manage two different axes of decision
making at the same time: which lots to bid on, and how to divide money
between those lots, without knowing which lots they might win or lose. In

Auctions

313

a serial auction, a player’s valuation of a later lot might change dramatically
based on winning or losing a previous lot. In an extreme case, like Fresh
Fish, once a player has won a fish market stall, he or she does not bid at all
for a second fish market stall. Simultaneous auctions don’t have this kind of
rebalancing of player valuations.
Another interesting characteristic of Multiple-Lot Auctions is that the
lots themselves may be of entirely different types. A classic Gamemaster
game, originally called Shogun (and later Samurai Swords and Ikusa) features
a Multiple-Lot Bid in which players secretly allocate money to a mix of
auctions and market purchases. Players can assign money to bid for turn
order and for the services of the ninja. The rest of their money can be
allocated to build fortifications, hire ronin and levy additional units. Upon
revealing their secret allocations, the auctions for turn order and ninja are
resolved, and players can then use the other allocated funds to purchase their
fortifications, ronin and other units. Not only are the benefits of turn order
and the ninja quite different from purchasing units or defensive structures,
the auctions themselves operate by somewhat different rules. Any players
bidding on turn order will receive priority over non-bidders in choosing
their preferred ordering—their money grants them some benefit. However,
the ninja auction is an all-pay auction, but only one player will receive the
services of the ninja. If the top bidders are tied, they will pay, but none of
them get to use the ninja!
Multiple-Lot Auctions bear a very close resemblance to another game
mechanism: Area Majority (ARC-02). Though area majority games often
model military conflicts, as in El Grande, they are mathematically similar to
Multiple-Lot Auctions. The troops, or influence cubes, etc. can be abstracted
to bidding tokens, and the player with the highest bids wins the lot. Area
majority games typically offer rewards to more than only the highest bidder.
This is a nested Multiple-Lot Auction. Each different area that players seek
to influence houses its own set of lots, worth different amounts of victory
points to bidders.
Multiple-Lot Auctions are compatible with many other auction
mechanisms like Fixed-Placement Auction (AUC-15), Sealed-Bid Auction
(AUC-04), and Dutch Priority Auction (AUC-16). Their resolution can be
all-pay, winner-pay, cancellation, and others. In some Multiple-Lot Auctions,
players are limited in how many lots or how many types of lots they can win
too. This mechanism is among the most common and most flexible in the
auction family.

314

Building Blocks of Tabletop Game Design

Sample Games
El Grande (Kramer and Ulrich, 1995)
Fresh Fish (Friese, 2014)
Revolution! (duBarry, 2009)
Shogun/Samurai Swords/Ikusa (Gray, 1986)

Auctions

AUC-12

315

Closed-Economy Auction

Description
Closed-Economy is a meta-mechanism that can modify any auction type. In
a Closed-Economy Auction, all the money spent in the auction is paid out to
the auction participants themselves. The total amount of money in the system
never changes.

Discussion
While many auctions feature the winning bid being paid to one of the players
at the table (such as MarraCash or Modern Art), a true Closed Economy is
relatively rare. There’s typically some way to earn more money or inject money
into the system. However, Closed-Economy systems do exist, and are perhaps
more common in constrained bidding systems that feature unique bidding
markers, like Ra.
True Closed Economies create a zero-sum game where each player’s loss
is one or more players’ gain. The auction mechanism provides players with

316

Building Blocks of Tabletop Game Design

opportunities to convert their paper wealth, their opportunity capital, into
actual wealth in the form of in-game resources or benefits. The core dynamic
for players is timing the game properly, and being wealthy at the right time
and poor at the right time.
In some implementations, like Dream Factory, money paid is split among
all the players. In this case, the “remainder” issue needs to be dealt with for
sums of money that don’t divide evenly among the players. Typically this is
handled by leaving the remainder in the center of the table, where it is added
to the next winning bid before being distributed.

Sample Games
Dream Factory (Knizia, 2000)
Modern Art (Knizia, 1992)
No Thanks! (Gimmler, 2004)
Ra (Knizia, 1999)

Auctions

AUC-13

317

Reverse Auction

Description
Players bid to avoid taking the lot up for bid because it has some negative effect.
Common effects include a negative victory point value, or a requirement to
discard something of value such as a resource or special ability. Typically, in
a Reverse Auction all players, except the claimant of the lot, pay their bids.
Sometimes, the lot claimant will receive those payments.

Discussion
No Thanks! is a classic example of Reverse Auctions. The structure of the
auction is Turn Order Until Pass, with a constrained bid of 1 victory point
per bid. Each lot is worth some number of points, but the winner of the game

318

Building Blocks of Tabletop Game Design

is the player with the fewest points. Bidding tokens cancel out one of these
“bad” points, so they’re helpful towards winning the game. When a player
passes, they take both the card and all the bidding tokens placed on the card.
The key mechanism in the game is that each sequence of consecutive cards is
worth bad points equal to the lowest card in the sequence. Thus, a “9” card
is worth 9 bad points to all players, except for the player who already has the
“’10.” For that player, the “9” is actually worth a good point, because the “10”
card will no longer count for them, and instead they’ll get only 9 bad points.
This twist, which leads to players having sharply different values for a given
lot, creates a fascinating auction dynamic.
In the world of classic card games, Hearts stands out as the ReverseAuction variant of the familiar trick-taking genre. In Hearts, players play
with straightforward trick-taking rules, but seek to avoid winning any hearts
in the tricks they collect. Hearts are worth bad points… unless a player
collects all of them (and the Queen of Spades) to “shoot the moon.” In that
case, all the other players collect the bad points for that hand. While trick
taking is its own mechanism, and indeed a genre of games unto itself, it has
a close relationship with auctions, which is a topic we’ll explore in greater
depth in Trick-Taking Games (CAR-01) in Chapter 13. Suffice it to say that
trick taking is almost like a Once-Around Bidding Auction with multiple
currencies. In most games, the tricks are inherently valuable, but in Hearts
they are only meaningful based on whether they contain hearts or the queen
of spades.
In High Society, players bid for valuable possessions and title cards in
traditional auctions, but have reverse auctions for Misfortune cards. The
claimant of the Misfortune card recovers any money cards previously bid to
avoid the lot, but all other players must discard their money cards. In this
implementation, the lot up for bid defines the auction procedure.
By contrast, Eggs & Empire, a simultaneous-bid multilot auction game,
provides auctions that have both positive and negative lots mixed into the same
auction. The player bidding the lowest will be forced to accept the negatively
valued lot. One can think of this auction as a Reverse Auction in which
bidders who avoid the negative lot receive an extra reward, or as a traditional
all-pay auction in which the lowest bidder receives a penalty. Another similar
hybrid auction can be seen in the Game of Thrones board game. Players make
simultaneous sealed bids of power to defeat the Wildlings. If the sum of the
power bid by the players is equal to or greater than the Wildlings’ strength,
the Wildlings are defeated, and the highest bidder receives the benefit of
reclaiming a discarded leader back into their hand. If, however, the sum of

Auctions

319

power bid is less than the strength of the Wildlings, all players must remove
armies from the board equaling two points of unit strength. The lowest bidder
must remove armies equaling four points of unit strength.
As these examples demonstrate, a Reverse Auction is usually implemented
within some more complex auction environment. In part this may be because
Reverse Auctions are inherently negative in experience. The “winner” receives
a negative effect, and the “losers” all pay money. Everyone’s a loser! Because of
this negative experience, designers use Reverse Auctions as a seasoning, a way
to flavor a game, rather than as its central mechanism. No Thanks! remains
the seminal example of a Reverse Auction as the central mechanism of play.

Sample Games
Eggs & Empire (Pinchback and Riddle, 2014)
A Game of Thrones (Petersen and Wilson, 2003)
Hearts (Unknown, 1850)
High Society (Knizia, 1995)
No Thanks! (Gimmler, 2004)

320

Building Blocks of Tabletop Game Design

AUC-14

Dexterity Auction

Description
A Dexterity Auction requires performance of some act of dexterity to submit
a valid bid. Typically, this would involve the bid marker itself being placed
into some valid bidding area, but other methods for implementing this may
be used.

Discussion
Going, Going, GONE! by Dr. Scott Nicholson is the design that most readily
comes to mind because of its explicit auction theming. In the game, multiple
items are up for bid simultaneously, and players bid in real time by dropping
their bid tokens into cups corresponding to each lot. Only tokens that land
in the cups count, and the time available for bidding can be fast enough that
placing a bid is not assured.
While Going, Going, GONE! is squarely a Dexterity Auction, one could
perhaps view games like Crokinole and Shuffleboard as being Dexterity
Auctions.
Consider Crokinole, where players flick their bid markers, attempting to
acquire points by occupying board areas. Each side only scores when more of
its markers are in a given scoring zone than the other side. The main difference
between this and an auction is that in Crokinole, if you land 2 more markers
than your opponent in a scoring zone, you score points for each marker. That

Auctions

321

would be like bidding on a diamond and winning one diamond for each
dollar by which you outbid your opponent.
One can readily imagine a mechanism which awards to the player with the
most darts, or stones or markers in some area a singular benefit. This would
be a Dexterity Auction where player skill in landing the bid would be more
important than player intent to bid some amount.
Dexterity Auctions have been implemented in video games that are
boardgame-like in nature, most notably M.U.L.E. and Sumer. In these games,
players move on-screen avatars against the clock, representing offers to buy or
sell. This allows players to “fake” a bid by moving far ahead and then pulling
just behind their opponents as time runs out, to force them into winning an
item at a higher price than they might have intended.
It’s worth noting that dexterity is one of those mechanisms, like memory,
that can be deeply polarizing, and potentially inaccessible to those with
physical disabilities. It can be especially dissonant when it is one component
in a multimechanism game. A game that otherwise emphasizes planning and
calculation may frustrate players when their plans are ruined by an errant toss.

Sample Games
Crokinole (unknown, before 1876)
Going, Going, GONE! (Nicholson, 2013)
M.U.L.E. (Berry, 1983)
Sumer (Favorov, Gunnarrson, Raab, and Suthers, 2017)

322

Building Blocks of Tabletop Game Design

AUC-15

Fixed-Placement Auction

Description
Fixed Placement is a meta-mechanism that modifies a multiple-lot auction
by creating rules about which lots players may bid on, and representing bids
visually on a board or cards. It is often combined with constrained-value bids.
A Fixed-Placement auction ends when every player passes and/or no player has
the right to bid further. The highest bidder for each lot wins the lot.

Discussion
Multiple-Lot Auctions are a fairly common type of auction in board games.
These auctions introduce a new wrinkle into bidding by forcing players to

Auctions

323

evaluate several lots at once. Depending on bid timing rules, there may also be
strategic elements to sequencing your bids or forcing an auction to close early.
Multiple-Lot Auctions present some challenges to tracking. How should
the top bid be represented for each lot? What rules should govern bid order?
How can the game prevent multiple-lot bidding from devolving into a series
of one-lot auctions, in which players ignore all but one lot up for bid at a time?
Fixed Placement can help solve all these problem. Visually, Fixed-Placement
Auctions provide a track on which players can mark the value of their bid
using a player pawn. The right to bid can be governed by turn order. In some
games, like Amun-Re, turn order is interrupted whenever a player is outbid.
That player becomes the active player, who takes the bid marker representing
the bid that was just surpassed and makes another valid bid with it. The entire
auction ends when each player is the top bidder for some lot. In Cyclades,
there are more lots than there are players, but each player has only a single
bidding token, so each player will win exactly one auction, and some lots will
go unpurchased each turn.
Critically, in both of these games, a player may not immediately rebid
on the lot for which they were just outbid. This rule encourages players to
bid close to their actual value for a lot, since if they bid lower, they may not
have an opportunity to return to rebid on that lot. In theory this should
speed these auctions, though in practice, new players may evaluate this
dynamic incorrectly, leading to frustration and overlong analysis. Both of
these games also feature triangular increases in valid bid increments, which
prevents the tit-for-tat, raise-by-one bidding that can grind an auction to
a near-halt.
In Vegas Showdown, bids are submitted strictly in turn order. Bidding too
low has multiple consequences: not only will a player be outbid, but they
will have to wait until the next turn to bid. In the meantime, other players
will get to place bids, potentially raising the costs of lots the passed player
was interested in purchasing. Vegas Showdown does allow immediately
rebidding on the same lot, though the value of the next valid bid increases
in a delayed triangular pattern (each interval is repeated three times before
increasing).
Perhaps the greatest strength of Fixed Placement is that it offers an
opportunity to integrate bidding with other game actions. Since there is a
visible record of current bids, a design can invite players to take unrelated
actions, instead of restricting bidding to its own phase. While Vegas
Showdown takes advantage of this feature, there remains a lot of design
space here.

324

Building Blocks of Tabletop Game Design

Sample Games
Amun-Re (Knizia, 2003)
Cyclades (Cathala and Maublanc, 2009)
Vegas Showdown (Stern, 2005)

Auctions

AUC-16

325

Dutch Priority Auction

Description
A Dutch Priority Auction, a term of our own invention, is a multiple-lot
auction in which prices for the lots are determined based on the number of
bids placed on the lots up for bid. The winning bidder is the first player, in bid
priority, who chooses to pay the current price for a lot, which is equal to the
number of bidding tokens there. Priority may be determined by a variety of
factors, including global turn order or turn order for each lot based on order
of bid placement. Players may typically pass on the purchase when they are
the priority bidder by removing their bidding token. This has the effect of
reducing the price for the lot by one.

Discussion
A Dutch Priority Auction has features of a Dutch, or descending-bid auction,
coupled with an ordered, turn-based bidding system to help direct traffic and
coordinate the sale of multiple lots simultaneously. In this system, prices will
initially move towards the seller (i.e., they’ll rise) as bids are added, and then
move back towards the buyers, as prices descend when bidders decline to buy
at a given price.
Unlike a traditional Dutch auction, in which any player may accept the
going price and end the auction by calling out, a Dutch Priority Auction
determines an active player, the priority player, who may choose to accept
the going price or pass. In Die Speicherstadt (available in the United States as

326

Building Blocks of Tabletop Game Design

Jórvík, with a Viking theme and some minor balance tweaks), this priority is
determined in an initial round of bid-marker placement. Earlier placement
provides earlier priority in the auction resolution phase.
The priority player may choose to pass. In most cases, passing means
removing a bid marker, and thus lowering the asking price by one. Usually,
passing in this kind of auction simply means not acting at this time. If the
passing player has another bid marker at a lower priority, should the auction
continue until that marker comes up, the player will be allowed to purchase
the lot at that time.
Spyrium adds another element to this core, which is that a player, when
passing, receives money equal to the bid markers remaining on the lot. The
choice is between a current purchase at a higher price, or receiving an equal
amount of money, but passing on the purchase. In some cases, an early pass
can fund a later purchase of the same lot!
The effect of this style of auction is to require players to declare the lots
they’re interested in, somewhat separately from the price. Players may not
have enough bid markers to claim the right to bid on every lot they like, and
must restrict themselves to only those lots that are most meaningful to them.
However, bid markers must do double-duty. They cannot only be used to
stake out lots a player desires, they must also be used to raise prices on other
players. There is no other way to raise the price for a lot except to place a bid
marker on it. Bid markers placed late in the first phase may have no other
function, since they are late in the priority order for auction resolution too.

Sample Games
Die Speicherstadt (Feld, 2010)
Jórvík (Feld, 2016)
Spyrium (Attia, 2013)

9

Worker Placement

ӶӶ
Worker Placement, a type of Action Drafting (ACT-02), is often credited
to designer Richard Breese and his game, Keydom, in 1998. Nonetheless, it
was Caylus, by William Attia, that popularized the mechanism and inspired
its name.
Mechanically, Worker Placement is isomorphic to action drafting. Players
select actions in turn order by placing one of their pawns, or workers, into the
action space, or building. This is the core mechanical concept and thematic
conceit, and the mechanism has proven so durable because of that tight
theme-mechanism correspondence. It’s easy to understand why placing the
worker in the sawmill will generate wood.
Worker Placement can be described as action drafting, or even as a highly
specialized type of auction, but while resource allocation mechanisms may
share mathematical similarities and incentivize similar player behavior, the
experience of these mechanisms can vary a great deal based on how they’re
presented. Their intelligibility to the player will also vary a great deal based on
the setting, theme, and logical coherence of the mechanism. For Sale’s auction
is readily understood by players, as it is squarely in context. An auction for
property is a familiar concept, even if most players haven’t ever bought a
house at an auction. The thematic scaffolding, provided by Dungeon Petz,
on the other hand, falls short in terms of making its mechanism intelligible.
Why is it that the largest group of workers secretly assigned to an action get
to take the action first? There’s no strong connection to a real-world dynamic
that helps players remember and understand the rule. The Worker Placement
metaphor of placing a worker in a production building to generate a good
helps players understand the structure and incentives of the underlying game
system, which is one reason why it is such a popular core mechanism.
327

328

Building Blocks of Tabletop Game Design

In this chapter we’ll talk about other implications and expectations of
the mechanism, including blocking, gaining workers, adding buildings, and
more, as we delve deeply into this touchstone of modern design.
The term “Worker Placement” has lost some of its cohesion, and today, it is
often used as a synonym for a Euro-style game, irrespective of the presence of
workers or action drafting. Thus, it would not be out-of-place for Terraforming
Mars or Roll for the Galaxy to be described as “Worker Placement.” We will
restrict our analysis to games which use action drafting, recognize some form
of blocking, and conceive thematically of some kind of worker. This narrower
definition also excludes quite a few games which employ the worker metaphor
but not its underlying mechanism. For example, we exclude cooperative
games like Charterstone and Robinson Crusoe: Adventures on the Cursed Island,
because these games lack a true drafting or blocking element. Games with
workers placed onto private tableaus like Orleans and Through The Ages:
A Story of Civilization, or games in which workers represent a currency or bid
marker rather than a draft marker, as in Jórvík, Spyrium, and Keyflower are
also outside the scope of our definition. However, our definition is intended
only to limit the scope of our analysis, and not to stake a claim in how the
term should be used by anybody else. Whatever words we use, we believe
these elements of drafting, blocking, and thematic coherence are important
distinguishers that deserve a term by which to refer to them.

Worker Placement

WPL-01

329

Standard Worker Placement

Description
Players select actions, in turn order, by placing a worker from their supply
on a building associated with a specific action and then execute that action
immediately. The round ends when all workers have been placed, at which
point they return to their owners’ pools and a new round begins.

Discussion
This familiar structure, typified by games like Lords of Waterdeep and
Agricola, is an improvement over the ur-game, Caylus, in which buildings
resolved after all Worker Placements were complete. Immediate resolution
makes for faster play, and obviates the need for players to remember which
resources they will receive when making their next placement. Later games,
like The Manhattan Project and Tzolk’ in: The Mayan Calendar, have workers
returning only when their owners recall them. In the former, players get the
building’s reward on placement, while in the latter, the reward is tied to the
moment of recall, since the reward escalates the longer the worker is left out
on the board. With each passing turn in Tzolk’ in, workers rotate over on the
ingenious gear system to a higher tier of rewards that will be distributed when
the worker is recalled.
Most Worker Placement games employ the mechanism for all actions
in the game. Turn order is typically set by placing a worker on a building
that grants turn order priority. Increasing the number of actions that may
be taken in a turn is themed as getting new workers, which is an action tied

330

Building Blocks of Tabletop Game Design

to a building. Maintenance costs are represented as feeding or paying for
your workers. Increasingly, there are games that incorporate some Worker
Placement elements in the context of a broader game. Examples include
Copycat, Rococo and Belfort.

Sample Games
Agricola (Rosenberg, 2007)
Belfort (Cormier and Lim, 2011)
Caylus (Attia, 2005)
Charterstone (Stegmaier, 2017)
Copycat (Friese, 2012)
For Sale (Dorra, 1997)
Jórvík (Feld, 2016)
Lords of Waterdeep (Lee and Thompson, 2012)
The Manhattan Project (Tibbetts, 2012)
Mint Works (Blaske, 2017)
Orleans (Stockhausen, 2014)
Robinson Crusoe: Adventures on the Cursed Island (Trzewiczek, 2012)
Rococo (Cramer, Malz, and Malz, 2013)
Roll for the Galaxy (Huang and Lehmann, 2014)
Spyrium (Attia, 2013)
Terraforming Mars (Fryxelius, 2016)
Through the Ages: A Story of Civilization (Chvátil, 1986)
Tribune: Primus Inter Pares (Schmiel, 2007)
Tzolk’ in: The Mayan Calendar (Luciani and Tascini, 2012)

Worker Placement

WPL-02

331

Workers of Differing Types

Description
Workers can differ in abilities, or can be upgraded and downgraded, or are
valid for placement in different areas and buildings.

Discussion
Improved workers are a common variation on standard worker placement.
Improved workers can count as more than one basic worker as in Belfort,
or they may allow you to break standard placement rules, like in Leonardo
Da Vinci. Tzolk’ in puts a different spin on this idea by having the rewards
for a space improve the longer that a worker is allowed to stay out on that
space. Thematically, this can be understood as a worker spending more time
working. Another take on this idea is the notion that workers can improve.
In both Praetor, and Euphoria: Build a Better Dystopia, workers, represented
as dice, are more capable and provide better returns when they show higher
numbers. Players can take actions to increase the values of these worker
dice. In Village, workers can age and gain experience, which improves their
effectiveness.
Some games have workers who participate in different placement contests,
or have buildings that can only be accessed by certain types of workers. Pillars
of the Earth has workers who can collect resources, and master builders, who
are placed during a second round of placement, and who can access other
actions besides resource collection. The Manhattan Project similarly features

332

Building Blocks of Tabletop Game Design

specialists, like scientists and engineers, and certain buildings require those
specialists to operate. Glenn Drover’s Empires: Galactic Rebellion (previously
known as Age of Empires III: The Age of Discovery), and Viticulture, feature as
many as eight different kinds of workers who might participate in majority
contests and even battles, in addition to taking actions.

Sample Games
Age of Empires III: The Age of Discovery (Drover, 2007)
Belfort (Cormier and Lim, 2011)
Euphoria: Build A Better Dystopia (Stegmaier and Stone, 2013)
Glenn Drover’s Empires: Galactic Rebellion (Drover, 2016)
Leonardo Da Vinci (Acchittocca, Brasini, Gigli, Luperto, and Tinto, 2006)
The Manhattan Project (Tibbetts, 2012)
Pillars of the Earth (Rieneck and Stadler, 2006)
Praetor (Novac, 2014)
Tzolk’ in: The Mayan Calendar (Luciani and Tascini, 2012)
Village (Brand and Brand, 2011)
Viticulture (Stegmaier and Stone, 2013)

Worker Placement

WPL-03

333

Acquiring and Losing Workers

Description
Workers beyond the original complement may be acquired in some manner,
either temporarily or permanently. Workers may also be lost as the game
progresses.

Discussion
Rather than improving existing workers, many games allow acquisition of
new workers. These new workers represent a substantial growth in a player’s
overall action budget, and as such, acquiring more workers is often a dominant
strategy. In Stone Age, the reproduction hut is typically chosen first or second
in every round. Because of the power of adding workers, designers have
taken to metering worker growth. In Lords of Waterdeep, all players receive
a new worker on a fixed turn in the middle of the game. Caverna requires
that players build housing for new workers to acquire them—an investment
of resources up-front that the new worker’s productivity will pay for in the
future. Any kind of purchase price on a worker has to be considered in light
of the number of actions that worker will be able to take and the returns those
actions will provide. Usually, buying workers early has a higher payout than
buying them late for this reason.
In Last Will, the number of workers a player may deploy varies each turn
based on the place in turn order that they choose. More workers means going
later in the turn order, thus reducing the expected value of those additional

334

Building Blocks of Tabletop Game Design

workers, since the best spots will be taken by the time those extra workers are
up for placement. Euphoria sets a hard cap on the total value of pips that can
be showing in a player’s pool of available worker-dice, which sharply limits a
player’s incentive to collect more workers.
Temporary additional workers are featured in Snowdonia, Russian Railroads,
and Power Grid: Factory Manager. These workers will return to the general
pool after use, and must be hired or acquired again for reuse. A similar way
to throttle player appetites for more workers is through a feeding or worker
upkeep cost for permanent workers. Agricola is famous for the unforgiving
tightness of its feeding mechanism, and the substantial penalties incurred
for failing to feed your family, while Stone Age’s toothless approach makes a
starvation strategy quite viable.
Worker attrition is the flipside of this dynamic of gaining workers.
Euphoria’s workers may get too smart and, as a group, have too high a pip
value, at which point one escapes (or perhaps, is sent for re-education…). The
aging workers of Village eventually pass on, and the workers in Praetor retire.
Other games actively encourage sacrificing workers for a benefit. Asgard is a
visceral example, but discarding a die in Alien Frontiers, themed as landing a
spaceship (the die) on a planet to establish a colony, is mechanically identical.

Sample Games
Agricola (Rosenberg, 2007)
Asgard (Zizzi, 2012)
Caverna: The Cave Farmers (Rosenberg, 2013)
Euphoria: Build a Better Dystopia (Stegmaier and Stone, 2013)
Last Will (Suchy, 2011)
Lords of Waterdeep (Lee and Thompson, 2012)
Power Grid: Factory Manager (Friese, 2009)
Praetor (Novac, 2014)
Russian Railroads (Ohley and Orgler, 2013)
Snowdonia (Boydell, 2012)
Stone Age (Brunnhofer, 2008)
Village (Brand and Brand, 2011)

Worker Placement

WPL-04

335

Workers-As-Dice

Description
Workers are represented by dice whose pip values impact play.

Discussion
Workers-As-Dice is a broad genre, and it is frequently accompanied by the
mechanism of playing a combination of workers in a building. In Alien
Frontiers, players allocate all of their dice on their turns to buildings that take
a different combination of dice and values, and have different requirements for
placement. This approach leads to some analysis paralysis because of the large
number of combinations that are possible with as many as six dice. Other
titles, like Kingsburg, limit the dice pools to three dice. Each roll presents a
substantially smaller set of placement permutations for players to consider, not
only because of the smaller number of dice but because there are fewer valid
buildings for any given combination.
Workers-As-Dice can also function to determine the effectiveness of
workers. In The Artemis Project, worker dice collect a number of resources
equal to their pip value—as long as resources remain available in the supply.
However, the higher pip value dice are awarded resources last, which may
leave the placing player out of luck if the resources run out before they can
collect the reward.
Champions of Midgard features warrior dice whose faces represent attack
strength. The dice are assigned to overcome monsters, and are rolled together,

336

Building Blocks of Tabletop Game Design

summed, and compared to the monster’s strength. For some players, this is
an unacceptable level, and type, of randomness in a worker placement game.
Whatever your position on the matter, it is representative of the ongoing
hybridization of game styles and game mechanisms.
The manner in which the dice change values over the course of the game
can vary. In some games the dice are rolled each turn, giving a random
distribution that players need to work with. Alien Frontiers works in this way.
In other games, the players obtain the dice on a certain side, or have to expend
resources to change them to other, perhaps more powerful, sides.

Sample Games
Alien Frontiers (Niemann, 2010)
The Artemis Project (Chow and Rocchi, 2019)
Champions of Midgard (Steiness, 2015)
Kingsburg (Chiarvesio and Iennaco, 2007)

Worker Placement

WPL-05

337

Adding and Blocking Buildings

Description
Buildings, and their corresponding actions, may be added to the pool of
actions players may select from. Buildings may also be occupied to prevent
or hinder players from accessing those actions.

Discussion
Buildings define available actions in a worker placement game, and how
designers manage the availability of actions is critical to the overall flow of
the game. Some games retain a static set of actions throughout the game,
like Stone Age. Other games introduce new actions in a set pattern. Agricola
features new actions that reveal themselves each round, but the actions are
drawn from a very small subset, guaranteeing, for example, that the “Family
Expansion” action will reveal itself in one of three consecutive rounds.
Many games allow players to add buildings, and to claim ownership for
them. As early as Caylus, players could add a building and receive victory
points when another player occupied it. Lords of Waterdeep has variable owner
rewards for building usage by others. Some games break the core notion of
action drafting by introducing private actions. Russian Railroads themed these
as engineers, rather than buildings, but private buildings, themed as buildings,
exist in The Manhattan Project. On the opposite end of the spectrum are
public actions that are always available to all players, like the resource-gather
actions in Stone Age, which are in a public area, or the brewery actions in Brew

338

Building Blocks of Tabletop Game Design

Crafters, which are depicted on each player’s board. The section on Ownership
(ECO-14) has more details on this concept.
Underlying the difference between these actions is the concept of blocking.
Worker placement is a kind of action drafting, and drafting denotes a
dwindling set of possible choices. Worker placement depicts claimed actions
as a building staffed by a worker, so a building that cannot take an additional
worker is considered blocked. The typical worker placement game allows
each building to be used by one player each round, and is blocked when
one worker is in it. Modest exceptions allow for two or three players to use a
building—an easy way to scale the actions available in a game as the player
count increases.
Some games eschew “hard” blocking in favor of “soft” blocking. In Coal
Baron, players don’t block buildings by occupying them, they simply increase
the costs of other players accessing them. Carson City, a Western-themed
game, has workers in the same space duel to see who claims its reward.
Bumping, another kind of soft blocking, allows an occupied building to be
reused, but the worker currently occupying the building is removed, and
the owner gains some kind of bonus. In Euphoria, a game which otherwise
requires players to spend a turn recalling workers, simply the act of being
bumped is beneficial to the player being bumped—an especially elegant
combination of mechanisms.
Blocking is a player-driven placement restriction, but the game itself may
impose placement restrictions as well. Some games require multiple workers
to be played in order to activate a space, as in Russian Railroads or Francis
Drake. This is especially common among Worker-As-Dice games. Sometimes,
players must exceed a particular pip value with one or more dice. Other
times, a building calls for a sequential run of dice or a pair or larger set of
values, like in Alien Frontiers. Both Egizia and Francis Drake establish a linear
relationship between buildings, such that once you skip over a closer building
to activate one further down the river or road, respectively, you can never
go back. A more prosaic placement restriction is a cost, like in the case of a
resource-conversion or building action, which requires inputting resources
to build some finished product or obtain some advanced resource. Kingdom
of Solomon offers players bonus action buildings that are substantially more
powerful than the standard spaces, but which require assigning all remaining
workers. This can be viewed as a declining price auction (AUC-08) for these
bonus actions, with the price expressed in terms of workers, that is folded into
the larger worker placement structure.

Worker Placement

Sample Games
Agricola (Rosenberg, 2007)
Alien Frontiers (Niemann, 2010)
Brew Crafters (Rosset, 2013)
Carson City (Georges, 2009)
Caylus (Attia, 2005)
Coal Baron (Kiesling and Kramer, 2013)
Egizia (Acchittocca, Brasini, Gigli, Luperto, and Tinto, 2009)
Euphoria: Build a Better Dystopia (Stegmaier and Stone, 2013)
Francis Drake (Hawes, 2013)
Kingdom of Solomon (duBarry, 2012)
Lords of Waterdeep (Lee and Thompson, 2012)
The Manhattan Project (Tibbets, 2012)
Russian Railroads (Ohley and Orgler, 2013)
Stone Age (Brunnhofer, 2008)

339

340

WPL-06

Building Blocks of Tabletop Game Design

Single Workers

Description
Players control only a Single primary Worker and cannot acquire more
workers.

Discussion
On the far end of the worker placement spectrum are the Single-Worker
games, which we include in our definition only when they retain a
blocking element—otherwise, we characterize these as Action Point games
(ACT-01) when players can’t interfere with or block each other at all,
and Action Drafting games (ACT-02) when players can block each other
absolutely.
In the intermediate space between these lies a game like Kanban. Players
block and influence each other’s placements along at least three different
axes: (1) players cannot take an action space occupied by another player,
(2) they cannot take an action space in the same department they occupied
last turn, and (3) they must consider the role Sandra, the neutral boss,
will play. In Easy mode, Sandra’s presence in a department may encourage
players to work in that department in order to win her approval. In Hard
mode, they may choose to avoid Sandra’s critical eye and the penalties that
accompany it.
Another Vital Lacerda game, The Gallerist, takes an opposite approach
to Single-Worker blocking. Players have a primary worker, and can acquire

Worker Placement

341

several assistants. When players move their primary worker to a new space,
they may choose to leave an assistant behind. If that assistant gets bumped by
another player, the assistant will be able to take an action as compensation.
In a sense, the game records a kind of history of where each player has been,
and enforces consequences for collisions, snake-like, between the head of one
player and the tail of another. It is arguable whether this actually qualifies
for our definition of worker placement, though, since no cost is imposed on
the placing player in a manner that could be construed as blocking. Instead,
a benefit is given to the player whose assistant is being bumped. Istanbul
implements this trail concept more fully, and is perhaps the game that most
successfully implements substantial movement and spatial relationships
within a worker placement framework. Here, blocking is more fully realized,
as the placing player must pay the blocker to use the space.
Single-Worker games are quite similar not only to role-selection games,
as mentioned above, but also to Rondel Games (ACT-10) and Time Track
Games (TRN-13). The worker metaphor and the use of meeples and similar
tokens has as much to do with how we categorize the games as the underlying
action selection method itself.

Sample Games
Fabled Fruit (Friese, 2016)
