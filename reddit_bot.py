import praw
import config
import time
import os


def bot_login():
    print("Logging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="The Reddit Commenter v1.0")
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to, subreddit, search_strings, comment_reply):
    for comment in r.subreddit(subreddit).stream.comments(skip_existing=True):
        print("parsing {}".format(comment.id))

        if comment.id not in comments_replied_to and comment.author != r.user.me():
            for search_string in search_strings:
                if search_string in comment.body.lower():
                    print("String with \"{}\" found in comment ".format(search_string) + comment.id)
                    comment.reply(comment_reply)
                    print("Replied to comment " + comment.id)

                    list(comments_replied_to).append(comment.id)

                    with open("comments_replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")

                    time.sleep(20)

                    break

    print("Search Completed.")
    print(comments_replied_to)
    print("Sleeping for 10 seconds...")
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to


r = bot_login()
subreddit = config.subreddit
comment_reply = config.comment_reply
search_strings = config.search_strings
comments_replied_to = get_saved_comments()

run_bot(r, comments_replied_to, subreddit, search_strings, comment_reply)
