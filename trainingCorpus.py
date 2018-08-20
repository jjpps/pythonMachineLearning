from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Trainer",
logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    filters=["chatterbot.filters.RepetitiveResponseFilter"],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(    
    "chatterbot.corpus.portuguese.conversations"
    
)

while True: 
    try:
        bot_input = chatterbot.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break