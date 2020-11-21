movies_to_watch = int(input())

total_rating = 0
top_rated_movie = 0
lowest_rated_movie = 11
top_rated_movie_name = ''
lowest_rated_movie_name = ''

for movies in range(movies_to_watch):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating

    if movie_rating > top_rated_movie:
        top_rated_movie = movie_rating
        top_rated_movie_name = movie_name

    if movie_rating < lowest_rated_movie:
        lowest_rated_movie = movie_rating
        lowest_rated_movie_name = movie_name

print(f'{top_rated_movie_name} is with highest rating: {top_rated_movie:.1f}')
print(f'{lowest_rated_movie_name} is with lowest rating: {lowest_rated_movie:.1f}')
print(f'Average rating: {total_rating / movies_to_watch:.1f}')
