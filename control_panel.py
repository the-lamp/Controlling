from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/send_command", methods=["POST"])
def send_command():
    data = request.get_json()
    action = data.get("action")
    params = data.get("params", {})

    # Handle Different Actions
    if action == "fetch_device_info":
        return jsonify({"status": "success", "data": "Device Info Data"})
    elif action == "fetch_sms_logs":
        return jsonify({"status": "success", "data": "SMS Logs Data"})
    elif action == "fetch_call_logs":
        return jsonify({"status": "success", "data": "Call Logs Data"})
    elif action == "fetch_contacts":
        return jsonify({"status": "success", "data": "Contacts Data"})
    elif action == "fetch_notifications":
        return jsonify({"status": "success", "data": "Notifications Data"})
    elif action == "capture_photo":
        return jsonify({"status": "success", "message": "Photo Captured"})
    elif action == "take_screenshot":
        return jsonify({"status": "success", "message": "Screenshot Taken"})
    elif action == "send_sms":
        number = params.get("number")
        message = params.get("message")
        return jsonify({"status": "success", "message": f"SMS sent to {number}: {message}"})
    elif action == "make_call":
        number = params.get("number")
        return jsonify({"status": "success", "message": f"Calling {number}"})
    elif action == "change_wallpaper":
        url = params.get("url")
        return jsonify({"status": "success", "message": f"Wallpaper changed to {url}"})
    else:
        return jsonify({"status": "error", "message": "Invalid command"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
