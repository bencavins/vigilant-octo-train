import random


def random_phrase():
    adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return adj + ' ' + noun


def random_float(a, b):
    return random.uniform(a, b)


def random_bowling_score():
    return random.randint(0, 300)


def silly_tuple():
    return (random_phrase(), round(random_float(1.0, 5.0), 1), random_bowling_score())