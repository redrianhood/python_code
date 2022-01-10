rooms = {
    'Hall': {
        'north': 'Bathroom',
        'east': 'Dining Room',
        'south': 'Kitchen',
        'west': 'Bedroom',
        'item': 'key'
    },
    'Bathroom': {
        'south': 'Hall'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Bedroom': {
        'east': 'Hall',
        'north': 'Balcony'
    },
    'Balcony': {
        'south': 'Bedroom'
    }
}

