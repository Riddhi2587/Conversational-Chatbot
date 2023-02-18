from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from clean import clean_corpus
from get_msg import msg

msg_file = "topical_chat.txt"

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
msg_tuple = msg(msg_file)
trainer.train(msg_tuple)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
