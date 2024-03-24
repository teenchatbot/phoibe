# QUICK SIDENOTE - If you would like these docs translated into another language, please contact michaelangelo or another dev

# Bot Docs

## Ladies and gentlemen, this is long overdue, this is going to be a complete overview of the bot and how to work it and use commands
### as always if you have any questions please either contact a mod or one of the devs
### the devs are:
### R_Powell - Lead Developer and creator
### Mikaelvussy - Error handling and JSON
## These people will know the most about the bot, if you cant get ahold of one of them then ask a mod, who are all well versed in the operations of the bot

# Main usage
### The bot goes under many names, a derivitave of phoibe or deepestthroats is the most common, if you think a user is the bot but arent quite sure, ask someone else, they may be able to clarify for you

# Basic usage
### whenever a command is mentioned it will be specially formatted here, for example the drink command:
```
.drink
```
### Whenever a command is mentioned it will also have an identifier before it (.) this is to tell the bot that what you are saying is in fact a command and not a random message, think of it like this, if you have a series of messages;

UserA: hello

UserB: hey there

UserA: time

UserB: I don't know what the time is



### what UserA is trying to do wont make any sense, right? This is why when you use a command you must put the identifier before it



## Commands
### There are many commands to be used ranging from translation to the time, the most common ones are .time, .joke, .drink and .insult. Some of these commands have special optional commands, if you need more info on the command please use the wheelie command to look at it

## wheelie
### This is probably the most important command here, as it gives you more information about the other commands, sending the name of the command, a brief description and other info and how to use it. If you have any questions simply wheelie wheelie
### btw this is done with
```
.wheelie wheelie
```

## How to read the wheelie command outputs
### suprisingly some people get confused when trying to decipher the information that wheelie is giving us. For this example we will using wheelie to get info on the fight command, if we do
```
.wheelie fight
```
### this will return us with this:

#### name: fight
#### description: does some math based on the usernames provided and determines a winner based on a higher score
#### usage: (.)fight [username1] [username2]

### As we can see the identifier is seperated from the command, this is simply to not make the bot do the command that someone wants info on, we can also see that there are arguments for the fight command, these are put in brackets ( [] ) so that they can be easily identifiable, you should not put the brackets whenever you use the command as this will mess up the bot. So if we take this and we try to use it, you should get something like this:

```
.fight R_Powell Mikaelvussy
```

### This will then give you the results of the fight. Using this very basic example you should be able to aptly use the wheelie command to use any other commands that you would like to
### For more commands, please see either wheelie.json (if you can read json), or see commands.md
