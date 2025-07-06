from flask import Flask, Response

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def voice_webhook():
    response = """
        <Response>
            <Play>https://dl.dropboxusercontent.com/scl/fi/cwk5o2xgnh09v389avb37/demo.mp3?rlkey=wy652l55oyesmrv8zhmfkohna</Play>
        </Response>
    """
    return Response(response, mimetype="application/xml")

@app.route("/", methods=["GET"])
def index():
    return "Voice Webhook is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
