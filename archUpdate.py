from feed import printArticles, getArticles

def main():
    printArticles(*getArticles())
    
main()