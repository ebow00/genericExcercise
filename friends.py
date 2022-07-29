friends = [
    {
        'Name': 'Shooki',
        'Location': 'Tel Aviv'
    },
    {
        'Name': 'Pooki',
        'Location': 'Tel Aviv'
    },
    {
        'Name': 'Looloo',
        'Location': 'Tel Aviv'
    },
    {
        'Name': 'Nookie',
        'Location': 'Tel Aviv'
    },
    {
        'Name': 'Scrotum',
        'Location': 'Albany'
    }
]

your_location = input("\nWhat city are you located in? \n")
friends_nearby = [friend for friend in friends if friend['Location'].lower() == your_location.lower()]
if friends_nearby:
    print("\nFriends found!")
    for friend in friends_nearby:
        print(friend['Name'])
else:
    print("\nNo friends nearby. Tough luck!")
