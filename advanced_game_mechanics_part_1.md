Game Mechanics
Advanced Game Design

ptg8274339

Ernest Adams
Joris Dormans

Game Mechanics
Advanced Game Design

Ernest Adams
Joris Dormans

Game Mechanics: Advanced Game Design
Ernest Adams and Joris Dormans
New Riders Games
1249 Eighth Street
Berkeley, CA 94710
(510) 524-2178
Fax: (510) 524-2221
Find us on the Web at www.newriders.com
To report errors, please send a note to errata@peachpit.com
New Riders Games is an imprint of Peachpit, a division of Pearson Education
Copyright © 2012 Ernest Adams and Joris Dormans
Senior Editor: Karyn Johnson
Developmental Editor: Robyn Thomas
Technical Editor: Tobi Saulnier
Copy Editor: Kim Wimpsett
Production Editor: Cory Borman
Composition: WolfsonDesign
Proofreader: Bethany Stough
Indexer: Valerie Perry
Interior Design: Charlene Will, WolfsonDesign
Cover Design: Peachpit Press/Charlene Will
Notice of Rights
All rights reserved. No part of this book may be reproduced or transmitted in any form by
any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior
written permission of the publisher. For information on getting permission for reprints and
excerpts, contact permissions@peachpit.com. See the next page for image credits.
Notice of Liability
The information in this book is distributed on an “As Is” basis, without warranty. While every
precaution has been taken in the preparation of the book, neither the authors nor Peachpit
shall have any liability to any person or entity with respect to any loss or damage caused or
alleged to be caused directly or indirectly by the instructions contained in this book or by the
computer software and hardware products described in it.
Trademarks
Many of the designations used by manufacturers and sellers to distinguish their products are
claimed as trademarks. Where those designations appear in this book, and Peachpit was aware
of a trademark claim, the designations appear as requested by the owner of the trademark. All
other product names and services identified throughout this book are used in editorial fashion
only and for the benefit of such companies with no intention of infringement of the trademark. No such use, or the use of any trade name, is intended to convey endorsement or other
affiliation with this book.
ISBN-13: 978-0-321-82027-3
ISBN-10: 978-0-321-82027-4
9 8 7 6 5 4 3 2 1
Printed and bound in the United States of America

Respectfully dedicated to the memory of Mabel Addis Mergardt,
principal designer of The Sumerian Game (later made famous
as HAMURABI), the first game with an internal economy that
I ever played.
— Ernest W. Adams

To Marije van Dodeweerd for love.
— Joris Dormans

iv

Game mechanics: advanced Game desiGn

Acknowledgments
The genesis of this book was a late-night meeting between the two of us during the
G-Ameland student game jam festival on a small island off the north coast of the
Netherlands. Joris Dormans showed the Machinations framework to Ernest Adams,
and Ernest Adams promptly said, “We should write a book about game mechanics.”
But it took nearly two years and the advice and assistance of many other people
before we were done. Now it is time to thank them.
Our deepest appreciation goes to Mary Ellen Foley and Marije van Dodeweerd, our
beloved mates, who patiently tolerated very late nights, missed holidays and weekends, and the occasional rant about the vagaries of the writing process. We’ll make
it up to you if we can!
Stéphane Bura suggested that Joris should create an interactive tool when he saw the
original, static version of the Machinations diagrams.
Jesper Juul made the invaluable distinction between games of emergence and games
of progression that informs the entire book.
Remko Scha had a big impact on the formal scrutiny of the Machinations framework in his capacity as Joris Dormans’s PhD supervisor.
Mary Ellen Foley kindly checked and corrected all our references.
The colleagues and students at the Amsterdam University of Applied Sciences always
have been willing test subjects for much of the material that ended up in this book.
We must also thank a number of people for permission to reproduce images:
Alexandre Duret-Lutz, for his photo of The Settlers of Catan; Andrew Holmes, for
his photo of Kriegsspiel; Jason Lander, for his photo of Power Grid; Johan Bichel
Lindegaard, for his photo of Johan Sebastian Joust; Wikimedia Commons contributor
popperipopp, for his or her photo of the game Connect Four. We are also grateful
to the Giant Bomb website (www.giantbomb.com), for permission to reproduce screen
shots from their collection.
Thanks to Mika Palmu, Philippe Elsass, and all other contributors to FlashDevelop,
for creating the open source development tool that was used to program the
Machinations Tool.
We are extremely grateful to the many anonymous people who have helped to build
Inkscape, the open source Scalable Vector Graphics editor, without which it would
have been much more difficult to produce our illustrations.

v

As Elrond said, the last place is the place of honor. We thank Margot Hutchison,
Ernest Adams’s agent, for assistance with the contract. Tobi Saulnier was our wise
and sharp-eyed technical editor. Her suggestions are present but invisible throughout the book, and we’re deeply grateful that the CEO of a game company would be
willing to take the time to help us. Robyn G. Thomas, our tireless (and seemingly
sleepless) development editor, pleaded, cajoled, threatened, and oversaw the whole
process with her usual flair and attention to detail. And finally, special thanks to
Karyn Johnson, senior editor at Peachpit Press, for having the faith in us to let us
write the book in the first place.
We hasten to add that the blame for any errors or omissions belongs entirely to us
and not to any of the foregoing.
We welcome all comments, questions, and criticism; please write to Joris Dormans
at jd@jorisdormans.nl and to Ernest W. Adams at ewadams@designersnotebook.com.

About the Authors
Ernest W. Adams is an American game design consultant and teacher residing in
England. In addition to his consulting work, he gives game design workshops and
is a popular speaker at conferences and on college campuses. Mr. Adams has worked
in the interactive entertainment industry since 1989 and founded the International
Game Developers’ Association in 1994. He was most recently employed as a lead
designer at Bullfrog Productions, and for several years before that, he was the audio/
video producer on the Madden NFL line of football games at Electronic Arts. In his
early career, he was a software engineer, and he has developed online, computer,
and console games for machines from the IBM 360 mainframe to the present day.
Mr. Adams is the author of four other books, including Fundamentals of Game Design,
the companion volume to this book. He also writes the Designer’s Notebook series
of columns on the Gamasutra game developers’ webzine. His professional website is
at www.designersnotebook.com.
Joris Dormans (PhD) is a Dutch lecturer, researcher, and gameplay engineer based
in Amsterdam, the Netherlands, working in industry and higher education since
2005. For the past four years, he has been researching formal tools and methods to
design game mechanics. His other area of research focuses on how to leverage formal design methods to generate games procedurally. Dr. Dormans has presented
papers and hosted workshops on game design on many academic and industry
conferences. As an independent freelance game designer, he published and worked
on several video and board games. Among these are story-driven adventure games,
physical platform games, and a satirical political card game. He has also participated
in all Global Game Jams to date. His professional website is at www.jorisdormans.nl.

vi

Game mechanics: advanced Game desiGn

About the Technical Editor
Tobi Saulnier is founder and CEO of 1st Playable Productions, a game development
studio that specializes in design and development of games tailored to specific
audiences. Games developed by 1st Playable span numerous genres to appeal to
play styles and preferences of each group and include games for young children,
girls, middle schoolers, young adults, and some that appeal to broad audiences.
The studio also creates games for education. Before joining the game industry in
2000, Tobi managed R&D in embedded and distributed systems at General Electric
Research and Development, where she also led initiatives in new product development, software quality, business strategy, and outsourcing. She earned her BS, MS,
and PhD in Electrical Engineering from Rensselaer Polytechnic Institute.

Contents
Introduction ......................................................... xi
Who Is This Book For? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .xii
How Is This Book Organized? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .xii
Companion Website . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xiii

ChAptEr 1

Designing Game Mechanics ...................................1
Rules Define Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Discrete Mechanics vs. Continuous Mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
Mechanics and the Game Design Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Prototyping Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

ChAptEr 2

Emergence and progression................................ 23
The History of Emergence and Progression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23
Comparing Emergence and Progression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .24
Games of Emergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26
Games of Progression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .30
Structural Differences. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
Emergence and Progression Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

ContEnts

Exercise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .42

ChAptEr 3

Complex systems and the structure
of Emergence ..................................................... 43
Gameplay as an Emergent Property of Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
Structural Qualities of Complex Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
Harnessing Emergence in Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

vii

viii

Game mechanics: advanced Game desiGn

ChAptEr 4

Internal Economy................................................59
Elements of Internal Economies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
Economic Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
Uses for Internal Economies in Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

ChAptEr 5

Machinations ...................................................... 79
The Machinations Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
Machinations Diagram Basic Elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
Advanced Node Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
Modeling Pac-Man . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

ChAptEr 6

Common Mechanisms ....................................... 107
More Machinations Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
Feedback Structures in Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Randomness vs. Emergence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
Example Mechanics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145

ChAptEr 7

Design patterns ................................................ 147
Introducing Design Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
Machinations Design Pattern Language . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
Leveraging Patterns for Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

ix

ChAptEr 8

simulating and Balancing Games......................... 171
Simulated Play Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
Playing with Monopoly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179
Balancing SimWar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
From Model to Game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196

ChAptEr 9

Building Economies............................................ 197
Economy-Building Games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197
Analyzing Caesar III . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
Designing Lunar Colony . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .206
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .220

ChAptEr 10

Integrating Level Design and Mechanics .............221
From Toys to Playgrounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Missions and Game Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
Learning to Play . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .238
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .244

ChAptEr 11

progression Mechanisms .................................. 247
Lock-and-Key Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
Emergent Progression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .258
Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270

ContEnts

Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246

x

Game mechanics: advanced Game desiGn

chapter 12

Meaningful Mechanics ....................................... 271
Serious Games  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 271
Communication Theory .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 276
The Semiotics of Games and Simulations  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .282
Multiple Layers of Meaning  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 294
Summary .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .299
Exercises  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .300

appendix a

Machinations Quick reference ........................... 301
appendix B

design pattern Library ...................................... 303
Static Engine  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .303
Dynamic Engine  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .305
Converter Engine  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .308
Engine Building  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 311
Static Friction  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 314
Dynamic Friction  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 316
Stopping Mechanism  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 319
Attrition  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 321
Escalating Challenge  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 325
Escalating Complexity  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 327
Arms Race  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .330
Playing Style Reinforcement  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 333
Multiple Feedback  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 336
Trade  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 336
Worker Placement  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 336
Slow Cycle  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 336

appendix c

Getting Started with Machinations ..................... 337
references....................................................... 338
index ................................................................. 341
Online appendix B...............................................B-1
Online appendix c ............................................... c-1

Introduction
This is a book about games at their deepest level. No matter how good a game looks,
it won’t be fun if its mechanics are boring or unbalanced. Game mechanics create
gameplay, and to build a great game, you must understand how this happens.
Game Mechanics will show you how to design, test, and tune the core mechanics of
a game—any game, from a huge role-playing game to a casual mobile phone game
to a board game. Along the way, we’ll use many examples from real games that you
may know: Pac-Man, Monopoly, Civilization, StarCraft II, and others.
This book isn’t about building Unreal mods or cloning somebody else’s app that’s
trending right now. It’s called Advanced Game Design for a reason. We wrote Game
Mechanics to teach you the timeless principles and practice of mechanics design
and, above all, to give you the tools to help you do it—for a class, for a career, for
a lifetime.
We also provide you with two unique features that you won’t find in any other
textbook on game design. One is a new tool called Machinations that you can use to
visualize and simulate game mechanics on your own computer, without writing any
code or using a spreadsheet. Machinations allows you to actually see what’s going
on inside your mechanics as they run and to collect statistical data. Not sure if your
internal economy is balanced correctly? Machinations will let you perform 1,000
runs in a few seconds to see what happens and put all the data at your fingertips.
Machinations was created by Joris Dormans and is easy to use on any computer
that has Adobe Flash Player installed in its web browser. You don’t have to use the
Machinations Tool to benefit from the book, though. It’s simply there to help reinforce the concepts.

IntroDuCtIon

The other unique feature of Game Mechanics is our design pattern library. Other authors
have tried to document game design patterns before, but ours is the first to distill
mechanics design to its essence: the deep structures of game economies that generate challenge and the many kinds of feedback loops. We have assembled a collection
of classic patterns in various categories: engines of growth, friction, and escalation,
plus additional mechanisms that create stability cycles, arms races, trading systems,
and many more. We’ve made these general enough that you can apply them to
any game you build, yet they’re practical enough that you can load them in the
Machinations Tool and see how they work.
Game mechanics lie at the heart of all game design. They implement the living
world of the game; they generate active challenges for players to solve in the game
world, and they determine the effects of the players’ actions on that world. It is the
game designer’s job to craft mechanics that generate challenging, enjoyable, and
well-balanced gameplay.
We wrote this book to help you do that.

xi

xii

Game mechanics: advanced Game desiGn

Who Is This Book For?
Game Mechanics is aimed at game design students and industry professionals
who want to improve their understanding of how to design, build, and test the
mechanics of a game. Although we have tried to be as clear as we can, it is not
an introductory work. Our book expands on the ideas in another book by Ernest
Adams called Fundamentals of Game Design (New Riders). We refer to it from time
to time, and if you lack a grounding in the basics of game design, you might find it
helpful to read the current edition of Fundamentals of Game Design first.
The chapters in Game Mechanics end with exercises that let you practice the principles we teach. Unlike the exercises in Fundamentals of Game Design, many of them
require a computer to complete.

How Is This Book Organized?
Game Mechanics is divided into 12 chapters and 2 appendixes that contain valuable
reference information. There is also a quick reference guide to Machinations in
Appendix A.
Chapter 1, “Designing Game Mechanics,” establishes key ideas and defines terms
that we use in the book, and it discusses when and how to go about designing game
mechanics. It also lists several forms of prototyping.
Chapter 2, “Emergence and Progression,” introduces and contrasts the important
concepts of emergence and progression.
Chapter 3, “Complex Systems and the Structure of Emergence,” describes the nature
of complexity and explains how complexity creates emergent, unpredictable game
systems.
Chapter 4, “Internal Economy,” offers an overview of internal economies. We show
how the structure of an economy creates a game shape and produces different phases
of gameplay.
Chapter 5, “Machinations,” introduces the Machinations visual design language and
the Machinations Tool for building and simulating mechanics. It includes an extensive example using Pac-Man as a model.
Chapter 6, “Common Mechanisms,” describes a few of the more advanced features
of Machinations and shows how to use it to build and simulate a wide variety of
common mechanisms, with examples from many popular game genres.
Chapter 7, “Design Patterns,” provides an overview of the design patterns in our
design pattern library and offers suggestions about how to use them to brainstorm
new ideas for your designs.

xiii

Chapter 8, “Simulating and Balancing Games,” explains how to use Machinations
to simulate and balance games, with case studies from Monopoly and Will Wright’s
SimWar.
Chapter 9, “Building Economies,” explores economy-building games, using Caesar
III as an example, and takes you through the design and refinement process for a
new game of our own, Lunar Colony.
Chapter 10, “Integrating Level Design and Mechanics,” moves into new territory,
looking at how game mechanics integrate with level design and how properly
sequenced challenges help the player learn to play.
Chapter 11, “Progression Mechanisms,” discusses two kinds of progression. We start
with traditional lock-and-key mechanics and then consider emergent progression
systems in which progress is treated a resource within the economy of the game.
Chapter 12, “Meaningful Mechanics,” concludes the book with an exploration of the
role of mechanics in transmitting meaning in games that have a real-world message
to send. This topic is increasingly important now that game developers are making
more serious games: games for health care, education, charity, and other purposes.
Appendix A, “Machinations Quick Reference,” lists the most commonly used
elements of the Machinations Tool.
Appendix B, “Design Pattern Library,” contains several patterns from our design
pattern library. You can find the completed design pattern library in the online
Appendix B at www.peachpit.com/gamemechanics and a much more extensive discussion of each design pattern in Chapter 7.

Companion Website
At www.peachpit.com/gamemechanics you’ll find material for instructors, digital copies
of many of the Machinations diagrams used in this book, more design patterns,
and a step-by-step tutorial to get you started with Machinations. To get access to
this bonus material, all you need to do is register yourself as a Peachpit reader. The
material on the website may be updated from time to time, so make sure you have
the latest versions.

IntroDuCtIon

Appendix C, “Getting Started with Machinations,” is available online at
www.peachpit.com/gamemechanics and provides a tutorial for using the
Machinations Tool.

This page intentionally left blank

ChAptEr 1
ChAptEr 1

Designing Game
Mechanics
Game mechanics are the rules, processes, and data at the heart of a game. They
define how play progresses, what happens when, and what conditions determine
victory or defeat. In this chapter, we’ll introduce five types of game mechanics and
show how they’re used in some of the more common video game genres. We’ll
also discuss at what stage during the game design process you should design and
prototype mechanics, and we’ll describe three kinds of prototyping, addressing
the strengths and weaknesses of each. By the end of the chapter, you should have
a clear understanding of what game mechanics are for and how to think about
designing them.

Rules Define Games
There are many different definitions of what a game is, but most of them agree that
rules are an essential feature of games. For example, in Fundamentals of Game Design,
Ernest Adams defines games as follows:
A game is a type of play activity, conducted in the context of a pretended reality, in
which the participants try to achieve at least one arbitrary, nontrivial goal by acting in
accordance with rules.
In Rules of Play, Katie Salen and Eric Zimmerman write the following:
A game is a system in which players engage in artificial conflict, defined by rules, that
results in a quantifiable outcome.
In Half-Real, Jesper Juul says this:
A game is a rule-based system with a variable and quantifiable outcome, where different outcomes are assigned different values, the player exerts effort in order to influence the
outcome, the player feels emotionally attached to the outcome, and the consequences of
the activity are negotiable.
(Emphasis added in all cases.) We don’t intend to compare these different definitions
or to claim that one of them is the best. The point is that they all refer to rules. In
games, rules determine what players can do and how the game will react.

1

2

Game mechanics: advanced Game desiGn

Games as state machines
many games, and game components, can be understood as state machines (see, for
example, Järvinen 2003; Grünvogel 2005; Björk & holopainen 2005). a state machine
is a hypothetical machine that can exist in a certain number of different states, each
state having rules that control the machine’s transition from that state into other states.
Think of a dvd player: When a dvd is playing, the machine is in the play state. Pressing
the pause button changes it to the paused state, while pressing the stop button causes
it to return to the dvd menu—a different state. Pressing the play button does nothing
at all—the player remains in the play state.
a game begins in an initial state, and the actions of the player (and often the mechanics,
too) bring about new states until an end state is reached. in the case of many single-player
video games, the player either wins, loses, or quits. The game’s state usually reflects
the player’s location; the location of other players, allies, and enemies; and the current
distribution of vital game resources. By looking at games as state machines, researchers
can determine which rules cause the game to progress from one state to another. several
successful methods allow computer scientists to design, model, and implement state
machines with a limited (finite) number of states. however, in contrast to dvd players,
games can exist in a vast number of states, far too many to document.
Finite state machines are sometimes used in practice to define the behavior of simple
artificially intelligent non-player characters. Units in a war game often have states such
as attacking, defending, and patrolling. however, because this is not a book about artificial intelligence, we won’t be addressing those techniques here. state machine theory is
not useful for studying the kinds of complex mechanics that this book is about.

Games Are Unpredictable
N OT E in games and
simulations, processes
that include elements
of chance (such as
moving a certain distance based upon a
die roll) are called
stochastic processes.
Processes that do not
include chance, and
whose outcome can be
determined from their
initial state, are called
deterministic processes.

A game’s outcome should not be clear from the start: To a certain extent, games
should be unpredictable. A game that is predictable is usually not much fun. A simple
way of creating unpredictable outcomes is to include an element of chance, such as
a throw of the dice or the twirl of a spinner in a board game. Short games such as
blackjack or Klondike (the most familiar form of solitaire played with cards) depend
almost entirely on chance. In longer games, however, players want their skills and
their strategic decisions to make more of a difference. When players feel that their
decisions and game-playing skills do not matter, they quickly become frustrated.
Pure games of chance have their place in a casino, but for most other games, skill
should also contribute to victory. The longer the game is, the more true this is.
In addition to chance, there are two other, and more sophisticated, ways to make
games unpredictable: choices made by players and complex gameplay created by the
game’s rules.

A simple game such as rock-paper-scissors (or roshambo/rochambeau) is unpredictable because its outcome depends on the decisions made by the players. The rules
do not favor one choice or another; they do not suggest a particular strategy. Trying
to second-guess or influence the choice of your opponent might involve empathy
or reverse psychology, but it remains largely outside the individual player’s control.
The classic board game Diplomacy uses a similar mechanism. In this game, players
control only a handful of armies and fleets. Victory in battle simply goes to the side
that committed the largest number of units to a battle. However, because all the
players write down their moves secretly and resolve their turns simultaneously, the
players must use their social skills to find out where their opponent will strike and
to convince their allies to support their offensive and defensive maneuvers.
When the rules of a game are complex, they can also make a game unpredictable,
at least to human beings. Complex systems usually have many interacting parts.
The behavior of individual parts might be easy to understand; their rules might be
simple. However, the behavior of all the parts combined can be quite surprising and
difficult to foresee. The game of chess is a classic example of this effect. The movement rules of the 16 chess pieces are simple, but those simple rules produce a game
of great complexity. Whole libraries have been written about chess strategies. Expert
players try to lure opponents into traps involving many pieces that might take multiple turns to execute. In this type of game, the ability to read a game’s current state
and understand its strategic complexities is the most important game-playing skill.
Most games mix these three sources of unpredictability. They include an element of
chance, player choices, and complex rules. Different players prefer different combinations of these techniques. Some like games that involve many random factors,
while others prefer games where complexity and strategy are key. Of these three
options, chance is the easiest to implement but not always the best source of unpredictability. On the other hand, complex rule systems that offer many player choices
are difficult to design well. This book will help you with that task. We devote most
of the chapters to designing rule systems that create, among other things, interesting choices for players. In Chapter 6, “Common Mechanisms,” we cover random
number generators (the software equivalent of dice) and discuss them at several other
points as well, but we feel that chance serves a supporting, rather than a central,
role in mechanics design.

From Rules to Mechanics
The video game design community usually prefers the term game mechanics to game
rules because rules are considered printed instructions that the player is aware of, while
the mechanics of video games are hidden from the player, that is, implemented in
software for which the player is given no direct user interface. Video game players
don’t have to know what the game’s rules are when they begin; unlike board and card
games, the video game teaches them as they play. Rules and mechanics are related
concepts, but mechanics are more detailed and concrete. For example, the rules of
Monopoly consist of only a few pages, but the mechanics of Monopoly include the

3

ChAptEr 1

desiGninG Game mechanics

4

Game mechanics: advanced Game desiGn

prices of all the properties and the text of all the Chance and Community Chest
cards—in other words, everything that affects the operation of the game. Mechanics
need to be detailed enough for game programmers to turn them into code without
confusion; mechanics specify all the required details.
The term core mechanics is often used to indicate mechanics that are the most influential, affecting many aspects of a game and interacting with mechanics of lesser
importance, such as those that control only a single game element. For example,
the mechanics that implement gravity in a platform game are core mechanics; they
affect almost all moving objects in the game and interact with mechanics for jumping or the mechanics that control damage to falling characters. On the other hand,
a mechanic that merely enables players to move items around in their inventories
would not be a core mechanic. The artificial intelligence routines that control the
behavior of autonomous non-player characters are also considered not core mechanics.
In video games, the core mechanics are mostly hidden, but players will learn to
understand them while playing. Expert players will deduce what the core mechanics must be by watching the behavior of the game many times; they will learn
how to use a game’s core mechanics to their advantage. The distinction between
core mechanics and non-core mechanics is not clear-cut; even for the same game,
interpretation of what is core and what is not can vary between designers or even
between different contexts within the game.

mechanic or mechanism
Game designers are perfectly comfortable talking about a game mechanic in the singular
form. They don’t mean a person who repairs game engines! instead, they are referring to
a single game mechanism that governs a certain game element. in this book, we prefer
to use mechanism as the singular form, indicating a single set of game rules associated
with a single game element or interaction. One such mechanism might include several
rules. For example, the mechanic of a moving platform in a side-scrolling platform game
might include the speed of the platform’s movement, the fact that creatures can stand on
it, the fact that they are moved along with it when they do, and the fact that the platform’s
velocity is reversed when it bounces into other game elements or perhaps after it has
traveled a particular distance.

Mechanics Are Media-Independent
The mechanics of a game can be implemented through many different media. In
the case of a board game, the mechanics are implemented through the medium of
the game’s paraphernalia: board, counters, playing pieces, spinners, and so on. The
same game can also be published as a video game. In that case, the same mechanics
will be implemented in software, which is a different medium.

Because mechanics are media-independent, most game scholars do not distinguish
between video games, board games, and even physical games. The relationships
between different entities in the game is much the same whether implemented on a
board, with pieces you move by hand, or on a computer screen, with images moved
for you by software. Not only can the same game be played in different media,
sometimes a single game can use more than one medium. Today more and more
games are hybrids: board games that include simple computers, or physical games
facilitated by clever devices hooked up to remote computers.
In addition, the media independence of game mechanics allows designers to create
mechanics for one game but then implement that game in several different media;
this cuts down on development time, since the design work is done only once.

hybrid Game example
The game Johann Sebastian Joust, developed by the copenhagen Games collective, is an
excellent example of hybrid game design. The game uses no screen, only speakers, and
takes place in an open area in which each player holds a Playstation move controller
(Figure 1.1). Players who move their controller too fast are eliminated from the game, so
players try to eliminate each other by shoving other players’ controllers, while maneuvering
carefully to protect their own controllers, all in slow motion. Occasionally the tempo of
the background music speeds up, indicating the speed at which the player can move safely.
Johann Sebastian Joust is a hybrid multiplayer game that blends physical performance
with simple computer-implemented mechanics to create a satisfying player experience.

FIGURe 1.1 Johann Sebastian Joust in full swing.
image courtesy of Johan Bichel Lindegaard under a creative commons (cc BY 3.0) license.

5

ChAptEr 1

desiGninG Game mechanics

6

Game mechanics: advanced Game desiGn

Using different media can help when creating prototypes. Programming software
usually takes much more work than simply writing down mechanics as rules for
a board game. If the same game can be played in a board game or physical game
form, it’s a good idea to try the rules/mechanics in one of those forms before going
to the trouble and expense of implementing them on a computer. As you’ll see in
the next section, efficient prototyping techniques are important tools in the game
designer’s toolbox.

Five Different Types of Mechanics
The term mechanics has come to indicate many different types of underlying relationships between entities in games. Here are five different types of mechanics that
you might expect to find in a game:
Physics. Game mechanics sometimes define physics—the science of motion and
force—in the game world (which can be different from the physics of the real world).
In games, characters commonly move from place to place, jump up and down, or
drive vehicles. Computing a game element’s position, the direction in which it is
moving, and whether it intersects or collides with other elements makes up the bulk
of the calculations in many games. Physics plays a large role in many modern games,
from ultrarealistic first-person shooters to the popular physics-puzzle games such
as Angry Birds. The implementation is seldom strict; however, games with so-called
cartoon physics use a modified version of Newtonian mechanics so that characters
can do non-Newtonian things such as change direction while in midair. (We also
consider such things as timing and rhythm challenges to be part of a game’s physics.)

n

Internal economy. The mechanics of transactions involving game elements
that are collected, consumed, and traded constitute a game’s internal economy.
The internal economy of a game typically encompasses items easily identified as
resources: money, energy, ammunition, and so on. However, a game’s economy
is not limited to concrete, tangible items; it can also include abstractions such as
health, popularity, and magical power. In any Zelda game, Link’s hearts—a visible
measure of his life energy—are part of the internal economy. Skill points and other
quantified abilities in many role-playing games also qualify; these games have very
complex internal economies.

n

Progression mechanisms. In many games, level design dictates how a player can
move through the game world. Traditionally, the player’s avatar needs to get to a
particular place to rescue someone or to defeat the main evil-doer and complete the
level. In this type of game, the progress of the player is tightly controlled by a number of mechanisms that block or unlock access to certain areas. Levers, switches, and
magical swords that allow you to destroy certain doors are typical examples of such
progression mechanisms.

n

desiGninG Game mechanics

Tactical maneuvering. Games can have mechanics that deal with the placement
of game units on a map for offensive or defensive advantages. Tactical maneuvering
is critical in most strategy games but also features in some role-playing and simulation games. The mechanics that govern tactical maneuvering typically specify what
strategic advantages each type of unit may gain from being in each possible location.
Many games restrict the location of units to discrete tiles, as is the case for a classic
board game like chess. Even modern strategy games played on the computer often
implement tiles, although they do a good job of hiding them behind a detailed
visual layer. Tactical maneuvering appears in many board games such as chess and
Go but also in computer strategy games such as StarCraft or Command & Conquer:
Red Alert.

7

Social interaction. Until recently, most video games did not govern social interaction among the players, apart from prohibiting collusion or requiring that players
keep certain knowledge secret. Now, however, many online games include mechanics that reward giving gifts, inviting new friends to join, and participating in other
social interactions. In addition, role-playing games might have rules that govern
the play-acting of a character, and a strategy game might include rules that govern
the forming and breaking of alliances between players. Board games and folk games
played by children have a longer history of game mechanisms that guide the interactions among players.

n

Mechanics and Game Genres
The game industry categorizes games into genres based on the type of gameplay the
game offers. Some games derive their gameplay mostly from their economy, others
from physics, level progression, tactical maneuvering, or social dynamics. Because
the gameplay is generated by the mechanics, it follows that the genre of a game
has a significant effect on the kinds of rules it implements. Table 1.1 shows a typical game classification scheme and how these genres and their associated gameplay
relate to different types of mechanics. The game genres in the table are taken from
Fundamentals of Game Design, Second Edition and correlate to the five different types
of game rules or structures. The thickness of the outlines indicates relative importance of those types of rules for most games in that genre.

ChAptEr 1

n

8

Game mechanics: advanced Game desiGn

TAble 1.1
Game mechanics and
Game Genres

desiGninG Game mechanics

9

We’ve listed five types of mechanics, but there’s another important distinction to
be made: Mechanics can be discrete or continuous. Modern games tend to simulate
physics (including timing and rhythm) with precise mechanics that create a smooth,
continuous flow of play. A game object might be positioned half a pixel more to the
left or right, and this can have a huge effect on the result of a jump. For maximum
accuracy, physical behaviors need to be computed with high-precision fractional
values; this is what we mean by continuous mechanics. In contrast, the rules of an
internal economy tend to be discrete and represented with integer (whole-number)
values. In an internal economy, game elements and actions often belong to a finite
set that does not allow any gradual transitions: In a game you usually cannot pick up
half a power-up. These are discrete mechanics. This difference between game physics
and game economies affects a game’s level of dependence on its medium, the nature
of the player interaction, and even the designer’s opportunities for innovation.

Understanding the Mechanics of Physics
Accurate physics computations, especially in real time, require a lot of high-speed
mathematical operations. This tends to mean that physics-based games must be
implemented on a computer. Creating a board game for Super Mario Bros., in which
the gameplay requires moving and jumping from platform to platform, would be
difficult. In platform games, physical dexterity matters, just as it does in playing
real-life football; those skills would be lost in a board game. Super Mario Bros. is probably better mediated as a physical course testing players’ real running and jumping
abilities. The point is, a rule that states that you can jump twice as high after picking up a certain item can be easily translated between different media, but actually
implementing that jump cannot. The continuous, physical mechanics of a game
need computing power more than the discrete rules that govern a game’s economy.
Interestingly, when you look back at the early history of platform games and other
early arcade games, the physics calculations were more discrete than they are today.
The moves in Donkey Kong were much less continuous than they were in Super Mario
Bros. In Boulder Dash, gravity is simulated by moving boulders down at a constant
speed of one tile every frame. It might play slowly, but it is possible to create a board
game for Boulder Dash. In those days, the rules that created the game’s physical
mechanics were not that different from other types of game rules. The early game
computers did not have any floating-point arithmetic instructions, so the game
physics had to be simple. But times have changed. Today the physics in a platform
game have grown so accurate and detailed that they have become impossible, or at
least inconvenient, to represent with a board game.

ChAptEr 1

Discrete Mechanics vs. Continuous Mechanics

10

Game mechanics: advanced Game desiGn

Mixing Physical Mechanics with Strategic Gameplay
