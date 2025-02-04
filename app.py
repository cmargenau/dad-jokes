from flask import Flask, request, jsonify, json
import random

app = Flask(__name__)
app.json.sort_keys = False

jokes = [
    {"question": "When does a joke become a dad joke?", "answer": "When it becomes apparent."},
    {"question": "Why shouldn't you use a broken pencil?", "answer": "Because it's pointless."},
    {"question": "What’s Forrest Gump’s password?", "answer": "1forrest1"},
    {"question": "How does the moon cut its hair?", "answer": "Eclipse it."},
    {"question": "Why can't you trust the king of the jungle?", "answer": "Because he's always lion."},
    {"question": "Why couldn't the melons get married?", "answer": "They cantelope"},
    {"question": "Why do cows have hooves and not feet?", "answer": "They lactose"},
    {"question": "When does a duck wake up?", "answer": "At the quack of dawn!"},
    {"question": "What do you call a hippie’s wife?", "answer": "Mississippi"},
    {"question": "Why did an old man fall in a well?", "answer": "Because he couldn't see that well!"}
]


@app.route("/",  methods=["GET"])
def get_one_joke():
    app.logger.debug("get_one_joke()")
    return [random.choice(jokes)]


@app.route("/jokes/<int:number>",  methods=["GET"])
def get_number_of_jokes(number):
    app.logger.debug("get_number_of_jokes()")
    return random.sample(jokes, number)


@app.route("/jokes", methods=["GET"])
@app.route("/jokes/", methods=["GET"])
def get_all_jokes():
    app.logger.debug("get_all_jokes()")
    return jokes


if __name__ == "__main__":
    app.run(debug=True, port=8080)

