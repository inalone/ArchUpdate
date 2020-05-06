import feedparser
import os
from os import path
import re

fileName = "/home/" + os.environ.get("USER") + "/.archUpdate"

def getArticles():
    articleTitles = []
    articleDates = []
    articleSummaries = []

    newsFeed = feedparser.parse("https://www.archlinux.org/feeds/news/")
    feedEntries = newsFeed.entries

    for entry in feedEntries:
        articleTitles.append(entry.title)
        articleDates.append(entry.published)
        articleSummaries.append(entry.summary)

    articleSummaries = stripTags(articleSummaries)

    return articleTitles, articleDates, articleSummaries

def stripTags(articleSummaries):
    newSummaries = []

    clean = re.compile('<.*?>')

    for summary in articleSummaries:
        newSummaries.append(re.sub(clean, '', summary))
    
    return newSummaries 

def printArticles(articleTitles, articleDates, articleSummaries):
    lastTitle = lastReadArticle()

    for i in range(0, 5):
        if articleTitles[i] == lastTitle:
            if i == 0:
                print("No new articles since last time used")

            # write first article to the file as it's the latest one
            writeLastArticle(articleTitles[0])
            break

        print("\nArticle #" + str(i+1) + ": \n")
        print(articleTitles[i] + ": " + articleDates[i])
        print(articleSummaries[i])

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

printArticles(*getArticles())