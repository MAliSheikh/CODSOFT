import re 
import long_responses as long   


def message_probablity(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    for words in user_message:
        if words in recognised_words:
            message_certainity += 1
    
    percentage = float(message_certainity) / float(len(recognised_words))

    for words in required_words:
        if words not in user_message:
            has_required_words = False
            break  

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    












