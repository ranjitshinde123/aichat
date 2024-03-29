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

# chatbot=ChatBot('Chatpot')
# trainer=ChatterBotCorpusTrainer(chatbot)

chatbot=ChatBot('Chatpot')
trainer=ChatterBotCorpusTrainer(chatbot)

# trainer.train('chatterbot.corpus.english')
# trainer.train(r'/home/mobicloud/PycharmProjects/Chatbot/chatterbot_corpus/data/english/conversations.yml')
trainer.train(r'/home/mobicloud/Documents/conversations.yml')


####################  only for backend ########################
@app.route("/get", methods=["POST"])
def chatbot_response():
    if request.method == "POST":
        data = request.get_json()  # Get JSON data from request body
        print(data)
        message = data.get("message")  # Extract message from JSON data
        print(message)

        response = chatbot.get_response(message)
        print(response)

        # Prepare response as JSON
        response_json = {
            "message": message,
            "response": str(response)
        }
        return response_json

        # return jsonify(response_json)

if __name__ == "__main__":
    app.run()



