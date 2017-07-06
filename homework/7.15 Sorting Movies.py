# globals
# (1) Make movies dictionary
movies = {
2005:[["Munich", "Steven Spielberg"]],
2006:[["The Prestige", "Christopher Nolan"],["The Departed", "Martin Scorsese"]],
2007:[["Into the Wild", "Sean Penn"]],
2008:[["The Dark Knight", "Christopher Nolan"]],
2009:[["Mary and Max", "Adam Elliot"]],
2010:[["The King's Speech", "Tom Hooper"]],
2011:[["The Artist", "Michel Hazanavicius"],["The Help", "Tate Taylor"]],
2012:[["Argo", "Ben Affleck"]],
2013:[["12 Years a Slave", "Steve McQueen"]],
2014:[["Birdman", "Alejandro G. Inarritu"]],
2015:[["Spotlight", "Tom McCarthy"]],
2016:[["The BFG", "Steven Spielberg"]]
}

def movie_and_director_by_year(year):
    if year not in movies.keys():
        print ("N/A")
    else:
        values = movies[year]
        values.sort()
        
        for title, director in values:
            print("{0}, {1}".format(title, director))
    print("")

def show_menu():    
    print("MENU\n\
Sort by:\n\
y - Year\n\
d - Director\n\
t - Movie title\n\
q - Quit\n")    

def sort_by_year():
    years = list(movies.keys())
    years.sort()
    
    for year in years:
        values = list(movies[year])
        values.sort(key=lambda x: x[1])

        print("{0}:".format(year))
        for title, director in values:
            print("\t{0}, {1}".format(title, director))
        print("")

def sort_by_director():
    values = list(movies.values())
    directors = []

    for value in values:
        if len(value) > 1:
            for item in value:
                directors.append(item[1])
        else:
            directors.append(value[0][1])

    # remove duplicates
    directors = list(set(directors))
    directors.sort()

    for director in directors:
        movie_and_year = []
        for year, value in movies.items():            
            if len(value) > 1:
                for item in value:
                    if item[1] == director:
                        movie_and_year.append([item[0], year])
            else:
                if value[0][1] == director:
                    movie_and_year.append([value[0][0], year])

        movie_and_year.sort(key=lambda x: x[1])

        print("{0}:".format(director))
        for title, year in movie_and_year:
            print("\t{0}, {1}".format(title, year))

        print("")


def sort_by_title():
    values = list(movies.values())
    titles = []

    for value in values:
        if len(value) > 1:
            for item in value:
                titles.append(item[0])
        else:
            titles.append(value[0][0])

    # remove duplicates
    titles = list(set(titles))
    titles.sort()

    for title in titles:
        director_and_year = []
        for year, value in movies.items():            
            if len(value) > 1:
                for item in value:
                    if item[0] == title:
                        director_and_year.append([item[1], year])
            else:
                if value[0][0] == title:
                    director_and_year.append([value[0][1], year])

        director_and_year.sort()

        print("{0}:".format(title))
        for director, year in director_and_year:
            print("\t{0}, {1}".format(director, year))

        print("")

def main():
    # (2) Prompt user for a single year
    year = int(input("Enter a year between 2005 and 2016:\n"))
    movie_and_director_by_year(year)

    # (3) Show menu
    menu_options = {'y': sort_by_year,
                    'd': sort_by_director,
                    't': sort_by_title
                    }

    user_exit = False
    while not user_exit:
        show_menu() 
        selection = input('Choose an option:') 

        # quit if selection is q
        if selection == "q":
            user_exit = True
            print('')
            quit
            
        # otherwise check if the selection is a valid menu option
        elif selection in menu_options.keys():
            print('')
            # execute the menu option if it's available
            menu_options[selection]()

# Call main function
if __name__ == "__main__":
    main()