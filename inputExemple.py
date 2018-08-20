# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging
logging.basicConfig(level=logging.INFO)

bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[                
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db"
)
print("escreva algo")

while True: 
    try:
        bot_input = bot.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break