mega_charizard_x = {
    'types':
        {
            'type 1': 'fire',
            'type 2': 'dragon'
        },

    'weakness':
        {
            'weakness 1': 'ground',
            'weakness 2': 'rock',
            'weakness 3': 'dragon'
        },

    'name': 'Mega Charizard X',
    'index': '006',
    'height': '1.7m',
    'weight': '110.5 kg',
    'category': 'flame pokemon',
    'gender': 'male/female',
    'ability': 'tough claw',
    'moves':
        [
            {
                'name': 'air splash',
                'damage': '14',
                'EPS': '8.3',
                'DPS': '11.7'
            },
            {
                'name': 'fire spin',
                'damage': '14',
                'EPS': '9.1',
                'DPS': '15.3'
            },
            {
                'name': 'dragon claw',
                'damage': '50',
                'EPS': '-19.4',
                'DPS': '35.3'
            },
            {
                'name': 'fire blast',
                'damage': '140',
                'EPS': '-23.8',
                'DPS': '40'
            },
            {
                'name': 'overheat',
                'damage': '160',
                'EPS': '-25',
                'DPS': '48'
            }
        ]

}

print(mega_charizard_x['moves'][4]['name'])
