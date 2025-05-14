from flask import Flask, render_template, jsonify
import requests
import config

app = Flask(__name__)

def get_server_status():
    """Получает статус сервера из MCSManager API"""
    headers = {
        "Authorization": f"Bearer {config.BEARER_TOKEN}"
    }
    
    try:
        # Получаем список серверов
        response = requests.get(config.MCSMANAGER_API_URL, headers=headers)
        servers = response.json()
        
        # Находим нужный сервер по UUID
        server = next((s for s in servers if s["uuid"] == config.SERVER_UUID), None)
        
        if not server:
            return {"error": "Сервер не найден"}
            
        # Получаем детали сервера
        detail_url = f"{config.MCSMANAGER_API_URL}/{server['uuid']}"
        detail_response = requests.get(detail_url, headers=headers)
        server_details = detail_response.json()
        
        return {
            "ip": server_details.get("host", "N/A"),
            "port": server_details.get("port", "N/A"),
            "online": server_details.get("online", False),
            "players": server_details.get("players", 0),
            "max_players": server_details.get("maxPlayers", 0),
            "name": server_details.get("name", "Minecraft Server")
        }
        
    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def index():
    server_info = get_server_status()
    return render_template("index.html", server=server_info)

if __name__ == "__main__":
    app.run(debug=True)