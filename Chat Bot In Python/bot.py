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
    



def check_all_message(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list

        highest_prob_list[bot_response] = message_probablity(
            message, list_of_words, single_response, required_words
            )
    
    # response ---------------------
    response('Hello!', ['hello','hey','sup','hey','heyo'], single_response=True )
    response('I\'m doing fine and you?',['how','are','you', 'doing'], required_words=['how'])
    response('Yes! I like coding',['Do','you','coding'],required_words=['you','coding'])
    response(long.r_eating,['what','you','eat'],required_words=['you','eat'])

    best_match = max(highest_prob_list,key=highest_prob_list.get)

    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response = check_all_message(split_message) 
    return response





