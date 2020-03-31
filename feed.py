import feedparser

def getArticles():
    articleTitles = []
    articleDates = []
    articleLinks = []
    articleSummaries = []

    newsFeed = feedparser.parse("https://www.archlinux.org/feeds/news/")
    feedEntries = newsFeed.entries

    for entry in feedEntries:
        print(entry.keys())
        articleTitles.append(entry.title)
        articleDates.append(entry.published)
        articleLinks.append(entry.link)
        articleSummaries.append(entry.summary)

    return articleTitles, articleDates, articleLinks, articleSummaries

def getLink(link):
    return f"\u001b]8;;{link}\u001b\\Click to see more\u001b]8;;\u001b\\"

# TODO: store last seen article and only show articles since then
def printArticles(articleTitles, articleDates, articleLinks, articleSummaries):
    for i in range(len(articleTitles)):
        print("\n Article #" + str(i) + ":")
        print(articleTitles[i] + ": " + articleDates[i])
        print(articleSummaries[i])
        print(getLink(articleLinks[i]))