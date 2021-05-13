# chat-plays-ftl
This is a command line bot that allows chat messages from Discord to control 
the game FTL: Faster Than Light, much like Twitch Plays Pokemon.

# Usage
Here's a quick primer on usage. As per command line programs, you'll have to run
this in something like Windows PowerShell or a terminal emulator.
```
./chat-plays-ftl
```
This doesn't take command line arguments yet, but this will probably change in
the future.

You'll need your own Discord bot set up via the Discord Developer Portal. Paste
your bot's token as the value for `TOKEN` in `main.py`. I will not give you mine.

# Background
## What's FTL?
In short, it's a game where you get to be a spaceship commander and have to
travel across space to beat the final boss.

For those who would want a slightly more in-depth explanation, it's a real-time
strategy roguelike game developed by Subset Games, where you control a spaceship
and its crew across randomly generated locations in space. At each location, you
get a pick-your-own-adventure-esque dialogue choice, where you could potentially
fight other ships, lose your crew members, get new crew members, and various
other random events that may (or may not) directly contribute to your success as
you travel to the final boss.

Gameplay-wise, you have a pool of "power bars" you can allocate to individual
systems. This means that if you have a limited amount of power (which is most of
the time), you can choose to take away power from a system such as oxygen, and
use that power in a system that might be more important in the moment (engines
for dodge chance, cloaking to completely avoid a dangerous attack). You can use
"scrap" gained from fights and random events to upgrade these systems -- which
increases the maximum power you can allocate to them --- increase the number of
total power bars available, or spend it at stores to get new weapons or systems.
For example, a ship that completely lacks cloaking can buy it at a store to get
access to it. There's much more to it than that, but that should give you the
gist of what gameplay is like. While it's real-time, you're allowed to pause the
game and plan your next move.

## What inspired you to do this?
One of my friends regularly streams FTL on Twitch, and tends to name her in-game
crew members after her viewers. There was a bit of a personal connection made as
a result of this, so I thought it would be cool to allow viewers control their
respective crew members through chat, like how Twitch Plays Pokemon allowed
people to control the main character through Twitch chat. I went for Discord
chat support first though, since I'm already pretty familiar with Discord bot
development. Problem is, my initial idea was way too ambitious.

## Why was your initial idea too ambitious?
While much of the game can be played with the keyboard, several crucial elements
of gameplay require the mouse. You need the mouse to move crew between different
rooms, and especially for aiming weapons at rooms in the enemy ship. If I wanted
to let people control individual crew members, I would have to somehow use
simulated mouse input to allow them to be moved. Fortunately, FTL already
provides some keybindings for selecting a specific crew member, and layouts are
consistent between the selectable ships. Unfortunately, the ship itself is in a
different place on-screen depending on whether the player is currently in a
fight or not, and figuring out that out (if the player is in a fight) requires
memory editing. Considering I figured I had to deal with the game state one way
or another --- such as for viewing crew member health and telling a person if
their respective crew member has died --- memory editing was a given, but the
modding/cheating scene is limited, plus I spent a whole day trying to figure
this out and got pretty much nowhere. So pretty much, anything involving mouse
input and direct access to the game state was a bust. Like I said though, much
of the game can still be played via keyboard, which is what led to the work done
on this bot.

# Functionality
Using chat (only Discord is supported right now), people have some degree of
control over the game, namely power allocation and system activation. The
default prefix for each command is `;`.

## Power Control
To add power to a system, your message must be the prefix, combined with
the name of the system you want to target and the amount of power you want to
add. For example, if you wanted to add 2 power to engines, you would do this:
```
;engines 2
```
To remove power from a system, use the same format, but with a negative number.
```
;engines -2
```

## System Activation
If you played or watched FTL before, you might know that systems can be
activated, such as cloaking. Systems that require a room to target --- and
therefore mouse usage --- cannot be activated, but systems that don't can just
be activated by giving the prefix combined with the name of the system, like so:
```
;cloaking
```
You can still add or remove power by providing a number after the command, like
so:
```
;cloaking -3
```

## System Name Abbreviation
System names can be abbreviated so you don't have to type the whole system name
out. For example, you can do `;cloak` instead of `;cloaking`, or `;mb` instead
of `;medbay`. There a lot more accepted abbreviations, but that's way too much
to type out.

## Door Control
Doors however are a little different. Since you can only open or close
individual doors using the mouse, people can only use the keyboard shortcut of
opening and closing ALL doors. For both respectively, do `;doors open` and
`;doors close`.

## Event Dialogue Options
Finally, in true anarchic fashion, people are able to choose the dialogue option
for an event. This is as simple as `;choose 1`, just replace the 1 with the
number of the option you want; don't worry, the game visibly gives the number
corresponding to each option.

To avoid conflicts between different people giving commands at the same time,
commands are put into a queue, so your command might not be processed
immediately. For a timing-centric game such as FTL, this will likely make things
much tougher, but it's better than nothing.

# Code Approach
For those who are interested, the design behind this code isn't really that
complicated. An instance of a bot is created using `discord.py`, and using an
event handler that's called every time a message is sent, every incoming message
is converted into a class instance representing an action in FTL (such as
powering a system). That instance is passed to and queued up in an input handler
that is constantly looping. Every loop, the next action in the queue is
processed and converted into an keystroke (or a series of such), which is
executed using `pywin32`. However, this is only done if FTL is the currently
focused window on the bot's host's computer. I could go on and on about the
object-oriented design, but either way I didn't apply the MVC design pattern
that much to this, given the relatively small scale of this project.

# Source Code
If you're a developer, feel free to look at and edit the source code for
yourself. However, I use a few Python modules that aren't installed by default.
- `discord.py` to interface with the Discord API and create a bot.
- `pywin32` to interface with Windows APIs and access Windows application
  information. 
- `pyautogui` to make keyboard inputs using Python.
Since `pywin32` works with the Windows APIs, you might not be able to run the
source code on any operating system other than Windows.

## Compilation
I use PyInstaller to compile my Python projects into a binary executable. A
version of PyInstaller for Windows is provided with the source --- which is
allowed under the GPL license, which PyInstaller uses --- and a `Makefile` is
given. As long as you have `GNU Make` installed on your Windows 10 (unsure if
this works on 7 or 8) computer, you should be able to call `make` to compile the
source. I'm not sure if `pywin32` has any use on other OS's, or even equivalent
modules, but you have to acquire a version of PyInstaller for your OS and modify
`Makefile` appropriately, since executables compiled using the Windows version
of PyInstaller will not work on other OS's. Just note that Windows Defender
might see it as a virus of some kind, which apparently happens a ton with
programs compiled using PyInstaller. Add it as an exception if this happens.

## Running Directly With Python
If you can't use the compiled Windows binary or still don't want to compile it,
you can run `main.py` if you've got a command line and Python 3 (3 is required)
on your computer. You can just run it with the same command line syntax,
assuming your current directory is the root (chat-plays-ftl folder):
```
python src/main.py
```
Or if you have Python added to your PATH variables as `python3`:
```
python3 src/main.py
```

## To-do's
A lot of the existing to-do's generally have to do with the ideas from the
original idea, which again I can't really do until I get direct access to the
game's state and related information through an API or something. I do have a
few things that are well within the realm of possibility, however.
- Code's due for a cleanup despite the fact that I literally just wrote this.
  It's kinda been done with the intent of just getting it to work, and as a
  result, there are some things that could be made... more efficient, to say
  the least. As it stands, it's not really indicative of how I would usually
  structure a bot like this, so it'd be nice to refactor a bunch of stuff and
  encapsulate individual jobs in classes.
- I'll add an easier way to change the bot's prefix, which will probably involve
  command line arguments or a configuration file. Maybe both.
- Although the asynchronous, Internet-facing parts of this code can't be tested
  easily, unit-testing everything else seems pretty feasible.