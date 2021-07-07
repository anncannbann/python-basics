print('hello')

#****************************
# FACTORIAL
#****************************

# def factorial(num):
#     product = 1
#     if(num<0):
#         print('Negative number, factorial doesnt exist')
#     elif num==0:
#         return 1
#     else:
#         return factorial(num-1) *num



# # how to write Assertions 
# def equals(actual,expected):
#     assert actual == expected, f'Expected {expected}, got {actual}'



# # print(equals(factorial(0),1))
# # print(equals(factorial(1),1))
# # print(equals(factorial(2),2))
# # print(equals(factorial(4),24))
# print(factorial(5))

#****************************
# DICTIONARY
#****************************

book_1 = {"title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960}
book_2 = {"title": "Jane Eyre", "author": "Charlotte Brontë", "published_year": 1847}
book_3 = {"title": "1984", "author": "George Orwell", "published_year": 1949}

books = [book_1, book_2, book_3]

def book_sort_key(book):
    return book['published_year']

books.sort(key=lambda book: book['published_year'])

# Dictionaries as maps
canadian_capitals = {
    'AB': 'Edmonton',
    'BC': 'Victoria',
    'MB': 'Winnipeg',
    'NB': 'Fredericton',
    'NL': 'St. John\'s',
    'NS': 'Halifax',
    'NT': 'Yellowknife',
    'NU': 'Iqaluit',
    'ON': 'Toronto',
    'PE': 'Charlottetown',
    'QC': 'Quebec City',
    'SK': 'Regina',
    'YT': 'Whitehorse'
}

canadian_capitals.keys()    # ['AB', 'BC', ...]
canadian_capitals.values()  # ['Edmonton', 'Victoria', ...]

print(canadian_capitals['ON'])  # Get an item
del canadian_capitals['AB']  # Delete an item
canadian_capitals['NU'] = 'Bob'  # Update an item
canadian_capitals['XX'] = 'New capital'  # Add an item

# Get value if the key exists, else return None
print(canadian_capitals.get('AA'))

# Get value if the key exists, else return a default value
print(canadian_capitals.get('AA', 'N/A'))

for code in canadian_capitals:
    print(f'The capital of {code} is {canadian_capitals[code]}')

for capital in canadian_capitals.values():
    print(capital)

for province, capital in canadian_capitals.items():
    print(f'The capital of {province} is {capital}')

if 'AA' in canadian_capitals:
    print('Found key')



