from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import collections.abc
import time
collections.Hashable = collections.abc.Hashable

app = Flask(__name__)

# Assuming you have initialized your chatbot and trained it elsewhere
chatbot=ChatBot('Chatpot')
trainer=ChatterBotCorpusTrainer(chatbot)

# trainer.train(r'/home/mobicloud/PycharmProjects/Chatbot/chatterbot_corpus/data/english/conversations.yml')

trainer.train(r'/home/mobicloud/Documents/conversations.yml')
# Function to check if a message exactly matches any question in the training data
@app.route("/")
def index():
	return render_template("index.html")


def message_matches_training_data(message):
    for statement in chatbot.storage.filter():
        if statement.text == message:
            return True
    return False


# Route to handle the chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    if request.method == "POST":
        # Get the user's message from the form
        message = request.form["message"]

        # Check if the message exactly matches any question in the training data
        if message_matches_training_data(message):
            # If the question exists, get the response
            response = chatbot.get_response(message)
        else:
            # If the question doesn't exist, set a custom response
            response = "I'm sorry, I don't have an answer to that question."

        return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")