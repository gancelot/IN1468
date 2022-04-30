"""
        client_test.py

        This client tests out the server found in this chapter.  To run the server,
        run wsgi.py from the ch08_network_apis/server folder.

"""
from functools import lru_cache
import requests


@lru_cache
def get_genre(genre_id):
    """ Lookups are slow, so this will cache lookups once they've occured
        (See details in next chapter)
    """
    return requests.get(f'http://localhost:8051/genre/{genre_id}').json().get('genre', '')


def get_movies():
    year = input('Enter year (1990-2020): ')
    movies = requests.get(f'http://localhost:8051/{year}').json()

    for movie in movies.get('results', []):
        title = movie.get('title')
        genre_ids = movie.get('genre_ids')
        genres = []
        for genre_id in genre_ids:
            genre = get_genre(genre_id)
            genres.append(genre)
        print(f'{title:<50}{" ".join(genres):<40}')


@lru_cache
def get_schools(search_term, search_column:str = 'fullname', sort_by: str='state'):
    """ Lookups are slow, so this will cache lookups once they've occured
        (See details in next chapter)
    """
    return requests.get(f'http://localhost:8051/school?value={search_term}&column={search_column}&sort_by={sort_by}').text


@lru_cache
def get_simpsons(char_name: str):
    return requests.get(f'http://localhost:8051/simpsons?char_name={char_name}').text


if __name__ == '__main__':
    # these can take a few seconds to run
    get_movies()
    print(get_schools('Loyola'))
    print(get_simpsons('Burns'))
