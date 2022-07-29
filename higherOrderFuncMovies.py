movies = [
    {"name": "The Shining", "director": "Stanley Kubric"},
    {"name": "The Matrix", "director": "The Wachowskis"},
    {"name": "The Irishman", "director": "Martin Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "Another movie by Pablos", "director": "Pablos"}
]


def find_movie(expected, finder):
    found = []
    for movie in movies:
        try:
            if finder(movie) == expected:
                found.append(movie)
        except KeyError:
            return "No such key in the library. Try again"

    return found


find_by = input("What property are we searching by? ")
looking_for = input("What are we looking for? ")

movies = find_movie(looking_for, lambda movie: movie[find_by])
print(movies or "No movies found.")
