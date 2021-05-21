# crowdplay-bot
This is a command line bot that allows chat messages from platforms such as
Discord and Twitch to control games, like FTL: Faster Than Light and any
Nintendo DS games (including Pokemon).

# Usage
The bot can be run just by running the compiled executable. Alternatively, it
can also be run via command line, although there aren't any arguments to be
aware of. A GUI will be used to configure, start, and stop the bot on demand,
but you must keep it open to keep the bot active.

# Supported Platforms
Figured that this would be important before going into the configuration. This
bot only supports Discord at the moment. Twitch implementation is VERY MUCH a
work-in-progress, and no other platforms are supported, although I have YouTube
planned.

# Configuration
Configuration can be done entirely within the GUI. That said, there are a few
important settings to take into account.

# General
These settings are required no matter what platform you plan to use.
- Prefix:
  - Default: ";"
  - Like most bots, this bot will only read messages that begin with this prefix.
- Platform:
  - Default: "none"
  - Specifies the platform this bot will function on. Must be one of "discord",
    "twitch" or "none".
- Token:
  - Default: ""
  - Bots on a platform like Discord or Twitch usually use OAuth tokens to sign
    into them and interact with the API directly. You'll have to acquire one of
    these on your own.

## Twitch-only
- Username:
  - Default: ""
  - Unfortunately, an OAuth token isn't the only thing you need for this bot to
    connect to Twitch. You'll have to provide the username to your bot's Twitch
    account.

# Background
One of my friends streamed FTL on Twitch, and tends to name their in-game crew
members after her viewers. There was a bit of a personal connection to our crew
members as a result of this, so I thought it would be cool to allow viewers to
control their respective crew members and have a direct impact on the game
through chat, just like how Twitch Plays Pokemon allowed viewers to control the
protagonist of the Pokemon games. Unfortunately, FTL's modding support is fairly
limited and without really dirty work, most of my initial ideas were close to
impossible. However, since much of FTL could still be controlled with just the
keyboard, I figured it was still possible for viewers to have a degree of
meaningful control over the game. Once I got FTL implementation done though, I
figured that it was best to let this support multiple games and not just FTL.
It's hardly an original idea (especially the Pokemon implementation), but I felt
it was probably a good way to simultaneously create something practical and have
fun doing it.

# Functionality
Using chat (only Discord is supported right now), people have some degree of
control over the game, namely power allocation and system activation. The
default prefix for each command is `;`.

## FTL
### Power Control
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

### System Activation
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

### System Name Abbreviation
System names can be abbreviated so you don't have to type the whole system name
out. For example, you can do `;cloak` instead of `;cloaking`, or `;mb` instead
of `;medbay`. There a lot more accepted abbreviations, but that's way too much
to type out.

### Weapon and Drone Control
Weapon and drone control are slightly different, since you can directly power or
depower a specific weapon/drone slot. `;weapons 2` will power the weapon in
weapon slot 2, and likewise `;weapons -2` will depower that slot.

### Door Control
Since you can only open or close individual doors using the mouse, people can
only use the keyboard shortcut of opening and closing ALL doors. For both
respectively, do `;doors open` and `;doors close`.

### Event Dialogue Options
Finally, in true anarchic fashion, people are able to choose the dialogue option
for an event. This is as simple as `;choose 1`, just replace the 1 with the
number of the option you want; don't worry, the game visibly gives the number
corresponding to each option.

To avoid conflicts between different people giving commands at the same time,
commands are put into a queue, so your command might not be processed
immediately. For a timing-centric game such as FTL, this will likely make things
much tougher, but it's better than nothing.

## Nintendo DS
More people will probably be familiar with Nintendo DS games and I happen to be
a bit of a Pokemon nerd, so DS game support has been added in addition to FTL
support. I don't condone emulation, but this assumes that you're emulating DS
games using DeSmuME.

Similar to FTL, commands can be made by giving the prefix combined with the name
of the button you want to press. `;a` will press the A button once, whereas 
`;a 5` will press the A button 5 times. I limited the amount of button presses
to 10 so someone's command can't just hog the queue.

Like the mouse situation with FTL, touch screen inputs aren't supported, since
usage differs from game to game and it would be difficult to capture touch
screen input as a message. Luckily, games like Pokemon don't really need the
touch screen outside a few specific minigames, so as long as you don't touch
those, you should be fine.

# Source Code
If you're a developer, feel free to look at and edit the source code for
yourself. The GPLv3 license covers most of what you can and can't do, but while
crediting me isn't necessary by any means, it would be appreciated if you did.

However, I use a few Python modules that aren't installed by default.
- `discord.py` to interface with the Discord API and create an asynchronous bot.
- `pydle` to create an asynchronous implementation of an IRC bot.
- `pywin32` to interface with Windows APIs and access Windows application
  information. 
- `pyautogui` to make keyboard inputs using Python.
- `pydirectinput` to make keyboard inputs if a game doesn't work with
  `pyautogui`.
- `pyqt5` to create the primary GUI, although this may be subject to change.
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
- The code is due for a MAJOR cleanup despite the fact that I literally just
  wrote this. Abstraction would be nice in several areas
- Although the asynchronous, Internet-facing parts of this code can't be tested
  easily, unit-testing everything else seems pretty feasible.
- It might be fun to play around with making this support other games too.
