# Reddit Comment Bot
This Reddit Comment Bot is a python-based auto-responder.
  - Pick a subreddit to scan
  - Designate a specific comment to search for
  - Set your bot's reply

this bot has been updated to run with python 3 and will constantly check new comments. Please be sure to follow reddit 
etiquette, for [more information check out r/redditdev](https://www.reddit.com/r/redditdev/).  

### Requirements
  - [Python](https://www.python.org/downloads/)
  - [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)
  - A Reddit Account

### Setup
###### Reddit App:
1. [Navigate to the Apps page ](https://www.reddit.com/prefs/apps/)
2. Click *create an app*
3. **name:** Set a name for your app
4. **type:** Script
5. **description:** Optional
6. **about url:** Optional
7. **redirect uri:** http://localhost:8080
8. Note the outputted *client id* and *secret*, example: https://imgur.com/a/a2OuA6o

###### config.py:
1. **username:** your Reddit username
2. **password:** your Reddit password
3. **client_id:** the outputted client id
4. **client_secret:** the outputted secret
5. **subreddit:** the subreddit to scan
6. **comment_reply:** your reply when a comment contains a string
7. **search_strings [list]:** the strings to search for in the scanned comments

### Usage

Navigate into the bot directory. (in the terminal: cd path\reddit-comment-bot)
Run your bot:
```sh
$ python reddit_bot.py
```
