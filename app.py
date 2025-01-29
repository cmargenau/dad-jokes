from flask import Flask
import random

app = Flask(__name__)

jokes = [
    {"question": "When does a joke become a dad joke?", "answer": "When it becomes apparent."},
    {"question": "Why shouldn't you use a broken pencil?", "answer": "Because it's pointless."},
    {"question": "What’s Forrest Gump’s password?", "answer": "1forrest1"},
    {"question": "How does the moon cut his hair?", "answer": "Eclipse it."},
    {"question": "Why can't you trust the king of the jungle?", "answer": "Because he's always lion."},
    {"question": "Why couldn't the melons get married?", "answer": "They cantelope"},
    {"question": "Why do cows have hooves and not feet?", "answer": "They lactose"},
    {"question": "When does a duck wake up?", "answer": "At the quack of dawn!"},
    {"question": "What do you call a hippie’s wife?", "answer": "Mississippi"},
    {"question": "Why did an old man fall in a well?", "answer": "Because he couldn't see that well!"}
]


@app.route("/")
def randomjoke():
    app.logger.debug("randomjoke(): enter")

    joke = random.choice(jokes)
    question = joke["question"]
    answer = joke["answer"]

    js = """
        function toggleDiv() {
          const div = document.getElementById('a');
          if (div.style.display === "none") {
            div.style.display = "block";
          } else {
            div.style.display = "none";
          }}
    """
    html = "<html><body><script>" + js + "</script>"
    html += "<div style='font-size: 36px;'>"
    html += "<div><span id='q'>" + question + "</span>"
    html += "<button style='margin-left: 10px;' onclick='toggleDiv()'>Toggle Answer</button>"
    html += "<button style='margin-left: 5px;' onclick='location.reload()'>Next</button>"
    html += "</div><div id='a' style='margin: 20px 0 0 20px; display: none;'>" + answer + "</div>"
    html += "</div></body></html>"
    return html


if __name__ == "__main__":
    app.run(debug=True, port=8080)

