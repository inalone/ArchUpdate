from feed import printArticles, getArticles
from update import update

def main():
    printArticles(*getArticles())
    
    choice = input("Would you like to update? [y/n]")

    if choice == "y" or choice == "Y":
        update()

main()