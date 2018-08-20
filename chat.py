from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Ron Obvious")

conversation =[
    "Hello",
    "oi",
    "ola",

]
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
response = chatbot.get_response("Good morning!")
print(response)

