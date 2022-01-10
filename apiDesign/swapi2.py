#!/usr/bin/env python3
"""
Star Wars API HTTP response parsing 2
"""

# imports
from pprint import pprint
import requests

# ============================================================
# The following URL is constructed incorrectly. It should be api/people/4/
# URL = "https://swapi.dev/api/people/four"
# ============================================================
# Not a valid URL
# URL = "https://swapi.dev/luke/force"
# ============================================================
# correct construct of line 12
URL = "https://swapi.dev/api/people/4/"

# =============== additionals =================
URL2 = "https://swapi.dev/api/films/1/"
URL3 = "https://swapi.dev/api/starships/13/"


def main():
    """sending GET request, checking response"""

    # SWAPI response stored in "resp" object
    resp = requests.get(URL)

    print(resp.status_code)
    if resp.status_code == 200:  # if resp is 'ok'
        # convert JSON content of response into python dictionary
        vader = resp.json()
        pprint(vader)
        print(
            f"String to show how to access data!!!: {vader['name']} was born "
            f"in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} "
            f"and his hair color is {vader['hair_color']}")
    else:
        print("That is not a valid URL.")



    movie = requests.get(URL2).json()
    movie_name = movie['title']
    # print(movie_name)

    ship = requests.get(URL3).json()
    ship_name = ship['name']
    # print(ship_name)
    print(f"He first appeared in the movie {movie_name} and could be found "
          f"flying around in his {ship_name}.")


if __name__ == "__main__":
    main()

