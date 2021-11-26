import random

list_of_movies = [
    'Your Name',
    'Grave of Fireflies',
    'Get Out',
    'Howl\'s Moving Castle',
    'Totoro',
    'Invincible',
    'Scary Movie',
    'Invader Zim',
    'A-Teen',
    'Mean Girls',
    'Zombieland',
    'Clueless',
    'JJK',
    'Hellbound',
    'Scott Pilgrim',
    'Spiderman Movie',
    'Your Lie In April',
    'Beastars',
    'Forgotten',
    'School of Rock',
    'Some Type of Scary movie like insidious'
]

number = random.randint(0, len(list_of_movies))

print(list_of_movies[number])

