import feedparser
import os
from os import path

fileName = "/home/" + os.environ.get("USER") + "/.archUpdate"

def getArticles():
    articleTitles = []
    articleDates = []
    articleLinks = []
    articleSummaries = []

    newsFeed = feedparser.parse("https://www.archlinux.org/feeds/news/")
    feedEntries = newsFeed.entries

    for entry in feedEntries:
        articleTitles.append(entry.title)
        articleDates.append(entry.published)
        articleLinks.append(entry.link)
        articleSummaries.append(entry.summary)

    return articleTitles, articleDates, articleLinks, articleSummaries

def getLink(link):
    return f"\u001b]8;;{link}\u001b\\Click to see more\u001b]8;;\u001b\\"

def printArticles(articleTitles, articleDates, articleLinks, articleSummaries):
    lastTitle = lastReadArticle()

    for i in range(0, 5):
        if articleTitles[i] == lastTitle:
            if i == 0:
                print("No new articles since last time used")

            # write first article to the file as it's the latest one
            writeLastArticle(articleTitles[0])
            break

        print("\n Article #" + str(i+1) + ":")
        print(articleTitles[i] + ": " + articleDates[i])
        print(articleSummaries[i])
        print(getLink(articleLinks[i]))

        if i == 4:
            writeLastArticle(articleTitles[0])

def lastReadArticle():
    if path.exists(fileName):
        with open(fileName, "r") as file:
            return file.readline()

def writeLastArticle(title):
    if not path.exists(fileName):
        open(fileName, "x")

    with open(fileName, "w") as file:
        file.writelines([title])
