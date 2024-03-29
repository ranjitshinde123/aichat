import json

from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
# from TextReader import chatbotContent
import collections.abc
import time
collections.Hashable = collections.abc.Hashable

# from openai import OpenAI
# time.clock = time.time

app = Flask(__name__)

chatbot=ChatBot('Chatpot')
trainer=ChatterBotCorpusTrainer(chatbot)

# trainer.train(r'/home/mobicloud/PycharmProjects/Chatbot/chatterbot_corpus/data/english/conversations.yml')

trainer.train(r'/home/mobicloud/Documents/conversations.yml')

# chatbot = ChatBot("Chatpot")

# trainer = ListTrainer(chatbot)

# chatbotContent = chatbotContent(chatbotFile)

# trainer.train(chatbotContent)

##############################  Backend with FrontEnd #######################

@app.route("/")
def index():	
	return render_template("index.html")

#
# @app.route("/get", methods=["GET","POST"])
# def chatbot_response():
#
#     message = request.form["message"]
#     response = chatbot.get_response(message)
#     return str(response)


# chatbot = initialize_and_train_chatbot()  # Initialize and train your chatbot here

# Route to handle the chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    if request.method == "POST":
        # Get the user's message from the form
        message = request.form["message"]

        # Check if the question exactly matches a question in the training data
        if message in chatbot.storage.get_question_texts():
            # If the question exists, get the response
            response = chatbot.get_response(message)
            print(response)
        else:
            # If the question doesn't exist, set a custom response
            response = "I'm sorry, I don't have an answer to that question."

        return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0")





