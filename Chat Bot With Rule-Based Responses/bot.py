from chatterbot import ChatBot


chatbot = ChatBot('My Bot')

exit_conditionos = (":q", "quit", "exit")

while True:
    Q = input('> ')

    if Q in exit_conditionos:
        break
    else:
        print(f'{chatbot.get_response(Q)}')


chatbot = ChatBot('My Bot')

exit_conditionos = (":q", "quit", "exit")

while True:
    Q = input('> ')

    if Q in exit_conditionos:
        break
    else:
        print(f'{chatbot.get_response(Q)}')

