import random

r_eating = 'I dont like eating anything Because I am a bot!'

def unknown():
    response = ['Could you please re-phrase that',
                '....',
                'Sound about right',
                'What does that mean?'][random.randrange(4)]
    
    return response
    