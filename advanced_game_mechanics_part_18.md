of the core mechanisms as a converter
engine is an example.
Worker placement can
be applied to any set
of sufficiently complex
mechanisms. Worker
placement requires only
that several stations for
workers be allocated to
activate or improve certain mechanisms.

Multiple stations that activate or
improve the core engine

n

A workers resource that can be allocated to different stations

n

An optional worker pool where
uncommitted workers are gathered

n

Collaborations
Workers are placed at different stations to activate or improve the core mechanisms;
the workers operate the core mechanisms. Workers can be moved between stations
relatively easily, making it possible to quickly change the core mechanism’s behavior.

Consequences
Worker placement requires that players spend time moving their workers between
stations. The pace of the game should allow for this, and the player should be able
to prepare for game events that require her to change the distribution.
Worker placement makes the most sense when the behavior of the core mechanisms
that the workers operate needs to be changed from time to time. This means that it
is best used in complex games that create different gameplay phases.
Worker placement usually requires the player to constantly manage her workers,
and as a result it can easily dominate a game’s economy.

deSiGn PAt tern LibrAry

B-39

implementation

When the number of workers is high or when players can produce extra workers
in the game, you have to be careful not to create a situation in which all the stations are manned and there is no longer any reason to change worker distribution.
One way to prevent this is to allow multiple workers to be placed at a single spot in
order to improve their effect further. In the structure diagram, this is the case for the
middle station.
Many games that implement worker placement have the players competing for the
same stations. For example, players need to place workers in the same gold mine to
produce gold for their economy. When players are competing for the same stations,
it is important to include a mechanism that forces workers to be removed from their
stations. This could be as simple as returning all workers to the pool automatically
after each turn or a more direct action that allows players to remove their opponents’ workers. Competition for stations creates a subtle and indirect competition
between players where they can block each other’s plans by blocking vital stations.
Worker placement creates many opportunities to add dynamic friction to the system.
Dynamic friction is created when placing workers consumes resources or when the
placement of a worker at a station costs a constant upkeep. In both cases, placing
more workers will consume more resources, countering the benefits of having more
workers in play. At the same time, when placing consumes resources (and there
is no upkeep), changing worker distribution is penalized. This creates a version of
worker placement that is less adaptive and rewards forward planning.

examples
In StarCraft, the workers are space construction vehicle (SCV) units that can be
assigned different tasks: They can harvest minerals or gas, the game’s two main
resources, or they can build and repair buildings for the player base. The player can
build as many SCV units as he sees fit and often can assign many SCV units to the
same (or similar) tasks. In StarCraft there is some competition for stations because all
players can harvest resources from the same locations on the map. This is an important feature in some levels, but in most levels the player starts with relatively safe
and exclusive access to some resources. Figure B.16 represents the worker placement
mechanics for StarCraft.

Online Appendix B

When implementing worker placement, it is important to balance the number of
workers with the number of stations. When the number of workers remains the
same for the duration of the game, this balance can make the difference between
constant changes to the worker distribution and players settling into a fixed distribution. Relatively low numbers of workers require the player to adapt more often,
whereas with high numbers the need to adapt is reduced.

B-40

GAme meChAniCS: AdvAnCed GAme deSiGn

Figure B.16
Worker placement in
StarCraft

In the board game Agricola, players build and operate a farm in the eighteenth century. The player starts with a family of two. Her family members are her workers.
They can be assigned to different tasks, such as sowing crops, building fences, gathering wood and other resources, and so on. Every turn she must assign workers to
new tasks. An important task is to collect enough food to feed the growing family.
In Agricola, players compete for the same stations; only one worker can be assigned
to each of the tasks. If no player performs a particular task in a turn, the resources
it generates build up (for example, wood piles up when nobody collects it). Because
this can happen, the relative benefits of each task shift constantly. Figure B.17 shows
some mechanisms for Agricola.

Figure B.17
Worker placement with
some of the mechanisms of Agricola

deSiGn PAt tern LibrAry

B-41

related Patterns
Worker placement can elaborate almost any other pattern, in particular the converter engine, engine building, attrition, and arms race patterns.

n

Dynamic friction initiated by the number of workers or by placing workers is a
good way to apply negative feedback to a worker placement pattern.

n

Slow Cycle
n

Type: Miscellaneous

Intent: A mechanism that cycles through different states slowly, creating periodic changes to the game’s mechanics.
Motivation: By introducing a slowly operating mechanism outside the player’s
control, the game’s economy shifts between different phases. This requires players
to adapt and develop more versatile strategies.

n

Applicability
Use a slow cycle when:
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

You want to introduce subtle, indirect strategic interaction by allowing players to
influence the cycle’s period or amplitude.

n

Collaborations
The state of the slow cycle interacts with the affected mechanism.

Online Appendix B

n

B-42

GAme meChAniCS: AdvAnCed GAme deSiGn

Structure

Participants
A slow cycle mechanism oscillates
between two (or conceivably more)
states.

n

N OT E the structure here is just an
example. there are
many different ways to
build slow cycles, and
there are many ways it
can affect other game
mechanisms.

The affected mechanism depends
on the state of the slow cycle.

n

Consequences
The effects of a slow cycle are often hard to see, especially for new players. This creates a long learning curve that might aggravate the difference between more and
less experienced players.
In most cases, players have little, if any, impact on the slow cycle mechanism. This
means that it is important to communicate the current state of the cycle clearly to
the player. Slow cycles that cause seemingly random changes to the game economy
are generally not considered to be fair.

implementation
There are many ways to implement slow cycles. A slow cycle might alternate
between two binary states (for example, it might activate or deactivate another
mechanism periodically), or it might shift between two states more gradually.
It is best if a slow cycle affects all players equally. This tests the players’ ability to
predict and prepare for phase shifts in the game’s economy. In the context of a
game world, slow cycles can easily be characterized as changes in the seasons, tides,
or business cycles beyond the control of the players.
Slow cycles can be made less deterministic by introducing random periods in the
cycle. This requires players to pay more attention to the current state of the cycle.
Another way to make cycles less deterministic is by randomizing the amplitude of
the cycle. For example, a slow cycle might produce some sort of energy for a short
period every ten turns. In this case, either the short period can be randomized or the
number of resources can be randomized without affecting the cycle’s rhythm.

deSiGn PAt tern LibrAry

B-43

examples

In the board game Caylus, the players build a castle and the accompanying town.
The game is divided into three phases, and at the end of each phase players are
rewarded for their contribution to the castle or penalized for the lack thereof. The
three phases create a subtle slow cycle mechanism. Players need to plan their contributions carefully, especially because the players are also competing to place their
workers to harvest the resources needed to help build the castle (Caylus also implements the worker placement pattern). In addition, the combined actions of the
players might speed up or slow down the current cycle. Being able to predict the
cycle and how it affects the plans of other players is an effective but advanced strategy in this game.

related Patterns
A slow cycle elaborates the static engine, static friction, and stopping mechanism
patterns.

n

Because a slow cycle causes shifts in the game’s economic phases, it combines
well with the worker placement pattern to allow the player to respond to these shifts.

n

Online Appendix B

As was mentioned in the section “Focusing on Different Structures in Your
Mechanics” in Chapter 10, “Integrating Level Design and Mechanics,” StarCraft II
uses a variety of different slow cycle mechanisms in different levels.

This page intentionally left blank

Online Appendix C
Online Appendix C

Getting Started
with Machinations
You can create and simulate Machinations diagrams in the Machinations Tool, a
graphical editor and simulator created by Joris Dormans. This tutorial will get you
up to speed creating diagrams in the tool. First we’ll introduce the user interface,
and then we’ll show you, step by step, how to create a diagram. However, our
tutorial doesn’t include a detailed discussion of how and why all the elements of
the diagram work. The basic elements of Machinations diagrams are explained
in Chapter 5, “Machinations.” Chapter 6, “Common Mechanisms,” discusses a
few more advanced elements, and Chapter 8, “Simulating and Balancing Games,”
explains how to use charts and artificial players.
You can also download many of the diagrams in this book from our companion
website, www.peachpit.com/gamemechanics.

Where to Find the Machinations tool
The Machinations Tool is written in Adobe Flash, and the easiest way to use it is to run it
in a web browser that has Flash enabled. You can find an online version of the tool, and
a wiki with additional information, at www.jorisdormans.nl/machinations. You can also
download an offline version of the tool there in a Flash format (.swf) file. It does not need
to go through an installation process, and you can store it anywhere on your computer.
If you want to run the tool offline, simply tell your browser to open Machinations.swf on
your own system.
Using Machinations Without a Browser
You don’t have to have Adobe Flash installed in a web browser to use the Machinations
Tool. You can also download the stand-alone Flash Player. It is available for Windows,
Macintosh, and Linux. You can download the latest version free on the Adobe website at
www.adobe.com/support/flashplayer/downloads.html (where it is called the Projector).
When you have the Flash Player installed, you can load the Machinations Tool instantly
by double-clicking the Machinations.swf file.
The Flash Player also enables you to create an executable program containing the
Machinations Tool itself. Start the Flash Player and load the Machinations.swf file. Then
select the Create Projector option from the player’s File menu (not the Machinations
Tool’s File menu). This will prompt you to save an executable file somewhere on your
system. When you have saved the executable, you can run it to start the Machinations
Tool in the Flash Player automatically.
C-1

C-2

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Exploring the Interface
We’ll start with an overview of the Machinations interface. It is divided into four parts.

The title bar runs across the top of the interface and contains version information and the Run button. Clicking the Run button starts a simulation running;
clicking it again stops it.

n

The drawing area is the largest part of the screen. This is where you will draw
the diagrams.

n

The Graph, Edit, File, and Run panels are tabbed on the top right. The Graph
panel allows you to select drawing tools; the Edit panel shows options to cut, copy,
and paste images; and the File panel allows you to save and open local files and
even to export the diagrams to Scalable Vector Graphics (.SVG) files. The Run panel
provides additional options for running a simulation.

n

The element panel is on the bottom right. Here you will find the controls that
allow you to change attributes of the nodes and connections in the diagram. The
element panel is context-sensitive and changes depending on which type of element is currently selected in the drawing area. When no node or connection is
selected, the element panel shows controls that allow you to change the attributes
of the diagram as a whole.

n

GeT T InG STArTed WITh MAChInAT IonS

C-3

The Graph panel consists of 16 tool buttons that allow you to select and add
elements to the diagram. If you allow the mouse to hover over a tool, a tooltip will
pop up to tell you its meaning.

Select tool (the arrow) selects elements in the diagram.
Text Label inserts text in the diagram for explanatory purposes. Has no
effect on the simulation. Not to be used for setting labels on elements of the
diagram, which is done in the element panel.
Group Box inserts a resizable dotted-line box in the diagram for illustration
purposes. Has no effect on the simulation.
Chart inserts a resizable chart into the diagram for collecting and displaying
data from simulation runs.
Pool inserts a pool into the diagram.
Gate inserts a gate into the diagram.
Resource Connection inserts a resource connection into the diagram. After
selecting this tool button, click a node in the diagram that will send resources
along the new resource connection you are inserting (the new connection
will become an output of the node). Then click another node that will receive
the resources.
State Connection inserts a state connection into the diagram. After
selecting this tool button, click a node in the diagram that will transmit
its state along the new state connection. Then click either another node, a
resource connection, or a state connection to serve as the target of the state
connection.
Source inserts a source into the diagram.

Online Appendix C

Graph Panel

C-4

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Drain inserts a drain into the diagram.
Converter inserts a converter into the diagram.
Trader inserts a trader into the diagram.
Delay inserts a delay into the diagram. A delay may be converted into a queue
by clicking the Queue button in the delay’s element panel.
Register inserts a register into the diagram.
End Condition inserts an end condition into the diagram.
Artificial Player inserts an artificial player into the diagram. Because these do
not need to be connected to other elements, they can be placed conveniently
out of the way.

Edit Panel
The Edit panel offers buttons to implement the familiar features of any digital
editing tool. These features are also available through keyboard shortcuts, which are
listed on the buttons. Note that Adobe Flash, which implements the Machinations
Tool, does not permit using the Control key, so the keyboard shortcuts are just
letters. For example, to copy the currently selected elements in the diagram, simply
press C. It is not case-sensitive.

n

Select All (A) selects and highlights all the elements of the diagram.

n

Copy (C) copies all selected elements to the clipboard.

Paste (V) pastes all the elements on the clipboard into the diagram, down and to
the right of the elements they were copied from.

n

GeT T InG STArTed WITh MAChInAT IonS

C-5

Undo (Z) will undo previous actions in inverse order. Note that the Undo button
can even undo clearing the diagram with the New button and opening a new file
with the Open button (both described in the next section).

n

Redo (Y) will redo previously undone actions.

Online Appendix C

n

Zoom (M) toggles between a zoomed-out and a zoomed-in view. If a
Machinations diagram is very large, the elements may be too small to work with
conveniently. Zoom permits you to zoom into a view where they are all a standard
size. Press M again to zoom back out.

n

In addition to these commands, the Backspace and Delete (or Del) keys on your
keyboard will delete the currently selected elements of the diagram.

File Panel
The File panel provides buttons to create new empty diagrams and to save and load
files containing diagrams.

caUtion: closing YoUr BroWser can lose YoUr Work!
Adobe Flash does not provide any means to warn you if you have unsaved work on your
diagram. If you close your browser or the stand-alone Flash Player with unsaved work, it
will be lost without warning. Get in the habit of saving your diagrams frequently.

New (N) clears the current Machinations diagram and starts a new one.
Caution: The Machinations Tool provides no warning if you do this without
having saved your work. However, you can undo the effect of the New button
using the Undo button on the Edit panel.

n

Open (O) clears the current Machinations diagram and loads a new one from a
Machinations file. Caution: The Machinations Tool provides no warning if you
do this without having saved your work. However, you can undo the effect of the
Open button using the Undo button on the Edit panel.

n

N ot E Most computer
art tools do not allow
the user to undo and
redo past a file being
opened, so this may
be unfamiliar to it you.

C-6

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Import (I) imports other diagrams into the one you are currently working on. All
the elements of the imported diagram will be selected at the time they are imported,
which permits you to move them around as a group.

n

n

Save (S) saves your diagram into a Machinations file.

Export Selection (E) exports a subset of your diagram to a new Machinations
file. Only the currently selected elements will be exported.

n

t I p Inkscape is
available for download
at www.inkscape.org.
It is available for
Linux, Windows, and
Mac oS X.

Save as SVG (G) saves your diagram as a Scalable Vector Graphics (SVG) file.
These files cannot be reloaded into Machinations later but are convenient for incorporating your diagrams into other documents. All the Machinations diagrams in
this book were saved as SVG files. You can edit SVG files in a free, open source editing tool called Inkscape.

n

aBoUt Machinations Files
The Machinations Tool saves diagrams in extensible Markup Language (XML) files.
This is an open standard format for storing any kind of data in text files designed to be
readable by computers and humans. however, Machinations does not format its XML files
for easy reading by humans. Because we may change the file format in the future, we do
not document it here. We also discourage trying to edit your Machinations files in a text
editor or any tool other than Machinations itself.

Run Panel
The Run panel permits you to change how you run your diagram and how much
data will be displayed at a time by any charts that it contains. We discuss the Run
panel in more detail in the section “Quick Runs and Multiple Runs” later in this
appendix. We also described it in the section “Collecting Data from Multiple Runs”
in Chapter 8, “Simulating and Balancing Games.”

GeT T InG STArTed WITh MAChInAT IonS

C-7

Each element of the diagram, plus the Machinations diagram as a whole, has its
own element panel. When no element is selected, the diagram element panel
appears. In this section, we will explain the functions of the boxes and settings that
can appear in the element panels. Because many elements share the same boxes,
to avoid redundancy we have listed them in alphabetical order and included in
parentheses the names of the elements to which they apply.
Actions specifies the number of action points that a node uses in a turn-based
diagram. Zero is a legitimate value. (All node elements except registers.)

n

Actions/Turn, when on the diagram panel in a turn-based diagram, specifies the
number of action points available to be used before it is time for the next turn. If
set to zero, a new turn will never occur unless the player interactively fires a node
whose name is end turn. When on the artificial player panel, Actions/Turn sets the
number of times in a given turn that the artificial player will fire. (Artificial player
nodes and diagram panel only, and visible only when Time Mode is turn-based.)

n

Activation. See the section “Activation Modes” later in this appendix and also
the section “Activation Modes” in Chapter 5, “Machinations.” (All node elements
except registers and end conditions.)

n

Author records the name of the author of the diagram. No simulation function.
(Diagram panel only.)

n

Color Coding toggles color-coding on and off for the diagram. See the section
“Color-Coded Diagrams” in Chapter 6, “Common Mechanisms.” (Diagram panel
only.)

n

Color sets the color of the element. See the section “Changing Colors” later in
this appendix. (All elements.)

n

Dice sets the default randomness for all die symbols in the diagram. (Diagram
panel only.)

n

Distribution toggles the visibility of resource movements on or off. The choices
are fixed speed and instantaneous. If instantaneous, resources jump from node to
node and are not seen to move along resource connections. (Diagram panel only.)

n

n

Height sets the height of the drawing area in pixels. (Diagram panel only.)

Interactive toggles on and off to determine whether a register is interactive or
passive. (Register nodes only.)

n

Interval sets the number of seconds per time step for the diagram. Fractional
values are allowed. (Diagram panel only, and visible only when Time Mode is not
turn-based.)

n

Formula stores the formula by which the value of a noninteractive register is calculated from its inputs. Not available on interactive registers. (Register nodes only.)

n

Online Appendix C

Element Panels

C-8

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Label names nodes, sets flow rates on resource connections, sets many kinds of
values on state connections. See Chapter 5, “Machinations.” (All elements.)

n

Max sets the maximum number of resources a pool can hold. The default is -1,
meaning unlimited. (Pool nodes only.)

n

t I p You can make
a line break appear
in Label text in the
diagram by inserting a vertical bar, as
in |, where you want
the line to break. For
example, the text
predator|birth rate
would be rendered on
two lines, with birth
rate centered below
predator.

Max. Value sets the maximum value that a register can display, whether interactive or passive. (Register nodes only.)

n

Min. Value sets the minimum value that a register can display, whether interactive or passive. (Register nodes only.)

n

Multiplayer sets the default randomness for all multiplayer symbols in the diagram. (Diagram panel only.)

n

Name records the name of the diagram. No simulation function. (Diagram panel
only.)

n

Number sets the number of resources already in a pool at the time the simulation
starts running. (Pool nodes only.)

n

Pull Mode sets the behavior of most nodes with respect to pulling and pushing resources. See the section “Pulling and Pushing Resources” in Chapter 5,
“Machinations.” (All nodes except delays, registers, and artificial players.)

n

n

Queue toggles conversion of a delay node into a queue node. (Delay nodes only.)

Resources see the sidebar “Understanding the Resources Box” later in this appendix. (Pools, sources, and converters only.)

n

n

Scale X fixes the horizontal scale of a chart. (Charts only.)

n

Scale Y fixes the vertical scale of a chart. (Charts only.)

Script is the box in which artificial player scripts are entered. See the section
“Simulated Playtests” in Chapter 8, “Simulating and Balancing Games.”

n

Skill sets the default randomness for all skill symbols in the diagram. (Diagram
panel only.)

n

n

Starting Value sets initial value of interactive register nodes. (Register nodes only.)

Step sets the amount by which an interactive register node changes when its up
or down arrows are clicked. (Register nodes only.)

n

Strategy sets the default randomness for all strategy symbols in the diagram.
(Diagram panel only.)

n

Thickness sets the line thickness of many elements. Cosmetic; no simulation
function. (All elements except groups, charts, and text labels.)

n

Time Mode sets the time mode of the diagram. The choices are asynchronous,
synchronous, and turn-based. See the section “Time Modes” in Chapter 5,
“Machinations.” (Diagram panel only.)

n

GeT T InG STArTed WITh MAChInAT IonS

C-9

Display Limit sets the number of resource tokens that a pool will display before
switching to showing digits instead. The default is 25. Cosmetic; no simulation
function. (Pool nodes only.)

n Type controls whether a gate is deterministic or non-deterministic. See the section
“Gates” in Chapter 5, “Machinations.” (Gate nodes only.)
n

Width sets the height of the drawing area in pixels. (Diagram panel only.)

Creating a Diagram
In the next few sections, we’ll take you through the process of actually building
a Machinations diagram, explaining a few more details about the Machinations
Tool as we go. To use this as a tutorial, open the Machinations Tool and follow
these instructions.

Adding, Selecting, and Deleting Elements

Online Appendix C

n

C-10

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Adding nodes to a diagram is very simple. Select the type of node you want to draw
from the Graph panel and click the drawing area to add the node. You can add
multiple nodes by clicking multiple times. The Machinations Tool automatically
selects the last node you added and shows its attributes in the element panel.

1. Click the Source tool

; then click somewhere on the left side of the

drawing area.
You can select additional elements by holding down the Shift key as you click.
Pressing the Shift key also automatically selects the select tool from the graph
panel. You can also draw a box around elements in the diagram to select them, as
in most art tools.
To delete elements, select them with the Select tool from Graph panel and press
the Delete or Backspace key on your keyboard.
To deselect all currently selected elements, single-click an empty space in
the diagram.

2. Add a pool to the right of the source by selecting the Pool tool
the drawing area.

Adding Connections

and clicking

Connections are added in a similar way. First, select the resource connection tool
from the Graph panel. Next, click the node where you want the connection to
start and then click the node where you want the connection to end. Resource
connections transfer resources in only one direction, so you must enter them in
this order. The connection will lock to the nodes at each end and will stretch if you
move either node.

3. Select the Resource Connection tool

; then click first on the source that you
entered and then the pool that you entered.
When you end a connection at an element of the diagram (a node or another
connection’s label), the element will be highlighted as you move your mouse
over it. If no element is highlighted, your new connection will not be connected
up properly.
You can also start and end connections anywhere in the drawing area, assuming
that you will connect them later. Simply click an empty spot in the diagram
to start a connection and then double-click at another empty spot to end the
connection there. (Clicking once will only create a way point in your connection,
as described in the next paragraph.)
If you have started drawing a connection and want to add a bend, or way point
(also called a control point), in the connection to make it look nicer as you draw,
move the mouse to an empty spot in the diagram where you want it to bend,
and single-click. The connection will continue from that point. You can continue
inserting as many way points as you like. Double-click to end the connection.
If you have already entered a complete connection, you can insert a way point
into it by selecting it and pressing the Insert key or the W key. (Macintosh users
will have to use the W key.)
You can change the start and end points of a connection by selecting them and
dragging them to different nodes. You can also move way points around the
diagram by dragging them.

C-11

Online Appendix C

GeT T InG STArTed WITh MAChInAT IonS

C-12

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Running Your Diagram

If you’ve connected the source to the pool, your diagram is ready to run.

4. Click the Run button in the title bar.
This should cause the source to start producing resources that accumulate in the
pool, and the Run button will change into a Stop button. (If you don’t see any
resources arriving in the pool, your resource connection is not connected up
properly.) While running, you cannot edit a diagram, and all the panels will be
grayed out.

5. Click the Stop button to stop the simulation running.

GeT T InG STArTed WITh MAChInAT IonS

C-13

Online Appendix C

Changing Flow Rates

You can change the flow rate of a resource connection by adding a label to it. In
our example, the production rate of a source is governed by the label of its output
resource connection.

6. Select your resource connection, and then type the letter D into its Label box in
the element panel. Press the Run button.
The source will produce a random number of resources varying between one and
six, every time step (by default, one second) instead of the default rate of one.

7. Press the Stop button.

C-14

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

UnCerTAIn FLoW rATeS
To indicate that a resource connection has a random or uncertain flow rate, you can
type special one- or two-letter values into the Label box. Different values indicate
different types of uncertainty, as follows:
D stands for Dice. The label changes to a die symbol. This indicates
uncertainty caused by a random number generator: dice or a spinner in a
board game or a random number generator in a computer game.
S stands for Skill. The label changes to a joystick symbol. This indicates
uncertainty caused by the varying level of skill that different players possess.
M stands for Multiplayer. The label changes to two pawns. This indicates
uncertainty caused by direct tactical interactions among players and a player’s
inability to predict what the others will do.
ST stands for Strategy. The label changes to a light bulb. This indicates
uncertainty caused by strategic interactions among players or variations in
one player’s strategy.
These different labels are intended for illustration to make your diagram clearer. For
example, if you want to indicate that a drain on some of your player’s resources is
caused by hostile actions by other players, you might use the M (multiplayer) label
on the resource connection leading to the drain.
Note that the difference between these symbols is only cosmetic. Functionally,
the Machinations Tool implements them all the same way, as a random number
generator.
In the next section, we explain what happens when you run a diagram containing
any of these symbols.

GeT T InG STArTed WITh MAChInAT IonS

C-15

Online Appendix C

s

When you use a symbol to indicate uncertainty and run the diagram, the Machinations
Tool generates a random value for it according to the contents of one of the boxes
in the diagram’s element panel. (This is the element panel visible when nothing is
selected in the diagram.) The boxes are labeled Dice, Skill, Multiplayer, and Strategy.
Each box defines the behavior of the symbols of its type in the diagram. By default,
the Dice box contains D6 (indicating a six-sided die), and the other boxes are empty.
If a box is empty, when you run the diagram, any symbols controlled by that box
will produce a value of zero, meaning no resources will flow.
You can control the generated values for all the symbols in the diagram by changing
the settings in the boxes. The format to use is described in the sidebar “Random
Flow Rates” in Chapter 5, “Machinations.”

8. Deselect all elements by clicking an empty space in the drawing area and type
D3-1 in the Dice box.
This will generate a random value by rolling a virtual three-sided die and
subtracting 1 from the result; in other words, it generates values from 0 to 2.

C-16

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

9. Run the diagram to observe the effect. Stop it when you are ready.
Every time step (normally one second), zero, one, or two resources will be
generated.
For the next step, we’ll switch from a symbol to an explicit percentage notation.

10. Select the resource connection and type 50% in its Label box, replacing the D3-1
that was there before.
This means that every time step, there is a 50% chance that the source will
produce a resource.

Activation Modes

When a node performs an action, we say that it fires. Each node in a diagram can
be set to one of four different activation modes that determines when and why the
node fires. To change the activation mode of a node, select the node and then click
one of the four small buttons next to the word Activation in the node’s element
panel. The four activation modes of a node of an element are as follows:
Passive. The node does not fire unless triggered by an external process.
Interactive. The node can be clicked by a player to make it fire.
Automatic. The node fires every time step.
Starting. The node fires only once, when the diagram first begins to run.

11. Place a converter in the diagram by selecting the Converter tool

and clicking
below the pool you inserted earlier. Connect a resource connection from the pool
to the converter.

12. Place another pool to the left of the converter. Connect a resource connection
from the converter to the new pool.

13. Now change the converter to interactive mode by selecting it and then selecting
the interactive mode button

from its element panel.

The converter will change to show a double outline instead of a single one. By
changing the converter to interactive mode, you can fire the converter while the
diagram is running by clicking it.

14. Run the diagram, wait a few seconds for resources to build up in the upper pool,
and then click the converter a few times.
When a converter fires, it will pull resources through its inputs to create new
resources for its outputs.

C-17

N ot E By default,
sources and artificial
players are set to the
automatic activation
mode when you first
place them in the
diagram. The other
nodes are passive by
default.

Online Appendix C

GeT T InG STArTed WITh MAChInAT IonS

C-18

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Adding State Connections

You add state connections in the same way that you add resource connections
(including way points). Select the state connection tool from the Graph panel, click
the node where you want the state connection to start, and click the element where
you want it to end. State connections must always begin at a node, but they may
end at a node or at either type of connection.
In our example, we want a new state connection to start from the lower pool and
end at the source’s output.

15. Select the State Connection tool

; then click the lower pool to start the state
connection, and click the upper resource connection (not the pool) to end it.
State connections often end at resource connections like this. In this way, state
connections can affect the flow rate of those resource connections. The state
connection you have just added is a label modifier, one of the four types of
state connections documented in the section “State Changes” in Chapter 5,
“Machinations.”

GeT T InG STArTed WITh MAChInAT IonS

C-19

Online Appendix C

l

Notice that the label of the state connection is automatically set to +1. This means
that for every resource added to the lower pool, the flow rate of the source’s output
is increased by one. However, as the flow rate is currently 50%, it is better to change
the state connection’s label to +10%.

16. Select the state connection, and then type +10% in its Label box.
17. Run the diagram, and click the converter occasionally.
Now the flow rate is increased by 10% for every resource on the pool. Watch
what happens to the label on the source’s output as resources arrive in the lower
pool. In addition to the resource connection’s label changing, you can see the
source producing more resources.
Note that you can drag a label of any connection to a different nearby location to
improve the legibility of your diagram.

18. Select the +10% label to the left of the state connection, and try dragging it
elsewhere.

C-20

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

g

19. Change the label of the converter’s input connection to 3. (Select the resource
connection going into the converter, and then type 3 in its Label box.)
This means that the converter changes three resources from the upper pool into
one resource going to the lower pool.

20. Run the diagram again, and click the converter occasionally.

GeT T InG STArTed WITh MAChInAT IonS

C-21

N ot E It is
theoretically possible to
track any element with
a chart, but it is only
meaningful to track
pools and registers
because they are the
only nodes that store
resources (or values).

Machinations diagrams enable you to keep track of the state of a pool or a register
over time in a chart. We discussed charts in detail in the section “Collecting Data
From Multiple Runs” in Chapter 8, “Simulating and Balancing Games.”

21. Select the chart tool

from the Graph panel, and place a chart in the diagram.

You can drag the chart’s corners to change its size.

22. Connect a state connection from the upper pool to the chart.
To avoid visual clutter, state connections between a pool and a chart are represented by two small arrows when they are not selected.

23. Run the diagram again to see how the chart tracks the resources accumulating in
the upper pool.

t I p You can hide any
state connection if you
want. Simply select
the state connection
and type a 0 in the
Thickness box in the
connection’s element
panel. Beware, though:
This will effectively hide
part of the structure of
your diagram. don’t
do it unless you really
need to reduce clutter
and already understand
your diagram well.

Online Appendix C

Adding a Chart

C-22

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

By default the chart will automatically scale the values on its x- and y-axes as the
diagram runs. If you want to create a chart with a fixed scale, you can enter numbers in the Scale X and Scale Y boxes on the chart’s element panel.

Adding an Activator
As our diagram is drawn so far, the flow rate from the source can exceed 100%.
This is permitted, because in a Machinations diagram percentages higher than 100%
are interpreted as meaning that the value is 1 plus a probability of whatever fraction
over 100% the label is. In other words, a flow rate on a source’s output of 130%
means that every time step, the source will generate one resource and has a 30%
chance of generating a second one.
However, if we want to prevent the source’s flow rate from going over 100%, we
have to stop the player from clicking more than five times on the converter. To do
this, we have to add an activator that will prevent the interactive converter from
firing again (even if you click it) after it has done so five times. Remember that an
activator is one type of state connection. An activator dictates the circumstances in
which its target (the element it points to) may operate and deactivates the target if
the conditions are not right.

C-23

Online Appendix C

GeT T InG STArTed WITh MAChInAT IonS

The activator will connect the lower pool to the converter. However, because
there already is a connection between them, it is better to make sure it follows a
different route.

24. Select the State Connection tool

, click the lower pool, and then single-click
the empty space in the diagram below the pool to create a way point. Then click
the converter to complete the state connection.

25. Finish the activator by changing its label to read <5.

C-24

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

26. Run the diagram again to see how it works.
You will be able to click the converter only when the number of resources in the
lower pool is less than five. When it equals or exceeds five, the converter is deactivated.
Note that deactivated elements are rendered light gray when the diagram is
running. This gives you a much better view of the diagram’s current state.

Adding an End Condition

Next we’ll add an end condition and an activator to specify what causes the
simulation to end.

27. Select the End Condition tool

, and add an end condition to the diagram
above the upper pool. Label it win. Connect a state connection from the upper
pool to the end condition. Label the new state connection >50 to indicate that
the player wins when she accumulates 50 resources.
Note that we moved the end condition’s label above the end condition node to
make the diagram clearer.

28. Run the diagram, clicking the converter if you want, but do not stop it.
The diagram will stop running by itself when the end condition is fulfilled.

GeT T InG STArTed WITh MAChInAT IonS

C-25

Online Appendix C

Adding an Artificial Player

Machinations diagrams allow you to define artificial players. Artificial players are
used to automate the process of playing. They work by specifying simple commands
and conditions.

29. Select the artificial player tool

, and place an artificial player somewhere out of

the way in the diagram.
We’re going to set up our artificial player to fire the converter every time the upper
pool has collected more than five points. To do this, however, both the upper pool
and the converter need to have names so that the artificial player can fire them.

30. Select the upper pool, and type points in its Label box. Select the converter, and
type upgrade in its Label box.

31. Now select the artificial player, and type if(points > 3) fire(upgrade) in the Script
box in the element panel.

32. Run the diagram again. Do not click the upgrade converter.
Sit back and watch how your artificial player saves you from the effort of having
to play yourself.

C-26

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Using Additional Features
In addition to all of the foregoing, the Machinations Tool offers a few miscellaneous features.

Making Quick Runs and Multiple Runs

Diagrams with end conditions and artificial players are suitable to run quickly and
multiple times, because they can play themselves and stop themselves. This is a
useful feature to quickly collect data over many simulated play sessions. In the Run
panel, the Runs box controls how many runs the tool will perform, and the Visible
Runs box controls how many runs any charts in the diagram will display.

33. Switch to the Run panel, and click the Multiple Runs button to start a multiple
run of the diagram.
When you run a diagram multiple times, the tool keeps track of which end
condition stopped the diagram and how long it ran on average. A pop-up box
shows this information while the runs are being performed. The chart also
collects the data for each run for you to review when the runs are done. In our
example, there is some randomness in the source’s production rate, so the chart
looks a little different on each run.

GeT T InG STArTed WITh MAChInAT IonS

C-27

34. Click the Reset button in the Run panel to return the diagram to its normal
editable state.

35. Click the word clear in the top-right corner of the chart to clear all the
Online Appendix C

collected data.
You can find full details of how to perform quick runs and multiple runs in the
section “Collecting Data from Multiple Runs” in Chapter 8, “Simulating and
Balancing Games.”

Changing Colors

You can change the colors of the elements in the diagram and also of the resources
in the diagram. Simply select the element you want to change and set a new color.
Colors can be specified by typing the name of the color into the Color box in the
element panel.
The Machinations tool uses the following color names: Black, White, Red, DarkRed,
Orange, OrangeRed, Yellow, Gold, Green, Lime, Blue, LightBlue, DarkBlue, Purple, Violet,
Teal, Gray, DarkGray, and Brown. These names are not case-sensitive.
We explained how to use color-coded diagrams in the section “Color-Coded
Diagrams” in Chapter 6, “Common Mechanisms.”

t Ip You can also use
hexadecimal notation
for more precise control
over your colors.
Make sure that the
hexadecimal color
follows the following
format: 0x000000. For
example, 0xff0000 is
red, 0x00ff00 is green,
and so on.

C-28

GAMe MeChAnICS: AdvAnCed GAMe deSIGn

Understanding the resoUrces Box
Pools, sources, and converters all have a special resources box in their element panels.
In a color-coded diagram, it can be used to override the default behavior of these nodes
with respect to colored resources.
normally, if you place a pool in the diagram, then change its color to blue with the Color
box, and then use the number box to place some resources in the pool, those resources
will be black, not blue. This is because, by default, the resources box contains the word
black. To place blue resources in a blue pool, you must type blue into the resources box.
The situation with sources and converters is a bit more complex. The color of the
resources that a source or a converter generates is governed by the color of the node’s
output, not by the node’s own color. This is what makes it possible for a single source to
generate resources of more than one color, as shown here:

The source is black, while the colors of the two resource connections are red and
blue. Clicking the source will produce one resource of each color traveling along their
respective outputs to the pool.
however, if a source or converter node and its output are the same color, the color of the
resource that travels along the output will be overridden by the color in the resource box
in the node’s element panel (which is black by default). In the previous diagram, if you
turn the source red, it will start to send black resources along the red output, but if you
type green into its resources box, the source will produce green resources along the red
output. It will continue to produce blue resources along the blue output, because the
blue output does not match the red source.

GeT T InG STArTed WITh MAChInAT IonS

C-29

Online Appendix C

Adding Text Labels and Group Boxes

Finally, Machinations allows you to add text labels with the TextL button
and
group boxes with the Group button
. These elements have no effect on how the
diagram behaves. However, they can be useful to clarify your diagram by identifying
specific mechanisms.

