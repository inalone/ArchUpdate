import feedparser
import os
from os import path
import re

file_name = "/home/" + os.environ.get("USER") + "/.cache/arch_update"

def get_articles():
    article_titles = []
    article_dates = []
    article_summaries = []

    news_feed = feedparser.parse("https://www.archlinux.org/feeds/news/")
    feed_entries = news_feed.entries

    for entry in feed_entries:
        article_titles.append(entry.title)
        article_dates.append(entry.published)
        article_summaries.append(entry.summary)

    article_summaries = strip_tags(article_summaries)

    return article_titles, article_dates, article_summaries

def strip_tags(article_summaries):
    new_summaries = []

    clean = re.compile('<.*?>')

    for summary in article_summaries:
        new_summaries.append(re.sub(clean, '', summary))
    
    return new_summaries 

def print_articles(article_titles, article_dates, article_summaries):
    last_title = last_read_article()

    for i in range(0, 5):
        if article_titles[i] == last_title:
            if i == 0:
                print("No new articles since last time used")

            # write first article to the file as it's the latest one
            write_last_article(article_titles[0])
            break

        print("\nArticle #" + str(i+1) + ": \n")
        print(article_titles[i] + ": " + article_dates[i])
        print(article_summaries[i])

        if i == 4:
            write_last_article(article_titles[0])

def last_read_article():
    if path.exists(file_name):
        with open(file_name, "r") as file:
            return file.readline()

def write_last_article(title):
    if not path.exists(file_name):
        open(file_name, "x")

    with open(file_name, "w") as file:
        file.writelines([title])

print_articles(*get_articles())