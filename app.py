import database
import datetime
menu = """
1) Add a new movie.
2) view upcoming movies.
3) view all movies.
4) watch a movie.
5) view watched movies.
6) Exit.

Your Selection:"""
welcome = "welcome to the watchlist app!"

print(welcome)
database.create_tables()

def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release Date (DD-MM-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title,timestamp)
def print_movie_list(heading , movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("----- \n")

def prompt_watch_movie():
    movie_title = input("Enter Movie Title You Have Watched: ")
    database.watch_movie(movie_title)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movie(True)
        print_movie_list("Upcoming",movies)
    elif user_input == "3":
        movies = database.get_movie()
        print_movie_list("All",movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movie_list("-- Watched --",movies)
    else:
        print("Invalid input , Please try again!")


        