import search

largest = search.most('population')
highest = search.most('elevation')

print(f'Largest city: {largest.name}, {largest.country} with: {largest.population:,} people')
print(f'Highest city: {highest.name}, {highest.country} at: {highest.elevation} meters ({highest.elevation * 3.28} feet)')

search_term = input('Enter the (partial) name of the city: ')
search.search(search_term, 'name')
