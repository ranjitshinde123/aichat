from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import collections.abc
collections.Hashable = collections.abc.Hashable
app = Flask(__name__)

# SQLite database setup
Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


engine = create_engine('')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create a new chatbot instance
chatbot = ChatBot('Chatpot')

# Create a new trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using a corpus file
# trainer.train("chatterbot.corpus.english.conversations")


# Route to render the index.html template
@app.route("/")
def index():
    return render_template("index.html")


# Route to handle the chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    if request.method == "POST":
        # Get the user's message from the form
        message = request.form["message"]
        print(message)

        # Save the message to the database
        new_message = Message(text=message)
        session.add(new_message)
        session.commit()

        # Get the chatbot's response
        response = chatbot.get_response(message)
        print(response)
        # Return the response as JSON
        return str(response)
        # return jsonify({"response": str(response)})
    else:
        # Return an error message if the request method is not POST
        return jsonify({"error": "Invalid request method"}), 405


if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0")
