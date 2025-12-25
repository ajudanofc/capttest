# 📢Capture & Track Location

![Preview](https://files.catbox.moe/bu3x9j.jpg)

This project is a **Python Flask–based web application** that utilizes the **browser camera** to capture images and send them to the backend server.  
It also uses **Cloudflared Tunnel** to provide **SSL (HTTPS)** and make the application **publicly accessible without requiring a public IP address**.

---

## Features
- Capture images directly from the browser camera
- Send captured data to a Flask backend
- Public access via Cloudflared Tunnel (HTTPS)
- Suitable for testing and educational purposes

---

## Source
This project is intended for **testing and learning purposes only**.

---

## Installation

### 🐧 Linux
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip -y
pip install flask colorama
git clone https://github.com/ajudanofc/capttest.git
cd captest
python3 index.py

Make It Publicly Accessible

wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared-linux-amd64
mv cloudflared-linux-amd64 cloudflared
./cloudflared tunnel --url http://(YOUR_IP):8080


---

📱 Termux

pkg update && pkg upgrade
pkg install python git wget openssl -y
pip3 install flask colorama
git clone https://github.com/ajudanofc/capttest.git
cd captest
python3 index.py

Make It Publicly Accessible

pkg install cloudflared
cloudflared tunnel --url http://127.0.0.1:8080


---

Notes

Ensure the Flask application is running on port 8080

Cloudflared Tunnel provides HTTPS and public access

Do not expose sensitive data or credentials



---

Disclaimer

This project is provided for educational and testing purposes only.
Any misuse or illegal use is not the responsibility of the developer.

