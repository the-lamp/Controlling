from flask import Flask, request, jsonify

app = Flask(__name__)

# Latest Command Storage
latest_command = {"action": None, "params": {}}

@app.route("/")
def home():
    return "CyberTracker Flask Server is Running!"

# API to send command from Control Panel
@app.route("/send_command", methods=["POST"])
def send_command():
    global latest_command
    data = request.json
    latest_command = {
        "action": data.get("action"),
        "params": data.get("params", {})
    }
    return jsonify({"message": "Command Sent", "command": latest_command})

# API for Android App to fetch latest command
@app.route("/get_command", methods=["GET"])
def get_command():
    return jsonify(latest_command)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
