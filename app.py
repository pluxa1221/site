import urllib.request
from flask import Flask, render_template, abort
import mistune, os, urllib, ssl, mctools
from pprint import pprint

app = Flask(__name__)
app.config['DOCS_FOLDER'] = 'docs'

# Инициализируем парсер Markdown
markdown = mistune.create_markdown()

def load_wiki_pages():
    """Читает все .md файлы из ./docs и формирует словарь"""
    pages = {}
    docs_path = app.config['DOCS_FOLDER']

    for filename in os.listdir(docs_path):
        if filename.endswith(".md"):
            slug = filename[:-3]  # убираем .md
            file_path = os.path.join(docs_path, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                title = filename.split('.')[0].capitalize()  # заголовок по названию файла

                pages[slug] = {
                    "title": title,
                    "markdown": content,
                    "html_content": markdown(content),
                    "url": get_service_url(slug)
                }

    return pages

def get_service_url(slug):
    """Возвращает URL сервиса по slug"""
    urls = {
        "plane": "http://103.88.242.164:1610/nevetime/",
        "mcsmanager": "http://192.168.31.113:23333/",
        "telegram": "https://t.me/+QS7d55g7SO41MDZ ",
        "minecraft": "minecraft://109.174.55.9:25575",
        "playit": "https://playit.gg/",
        "java": "not found"
    }
    return urls.get(slug, "#")

# Загружаем страницы при старте приложения
WIKI_PAGES = load_wiki_pages()

# Данные сервисов
SERVICES = [
    {
        "id": 0,
        "name": "Plane",
        "description": "Система управления проектами",
        "url": "http://103.88.242.164:1610/nevetime/",
        "type": "http",
        "icon": "fas fa-project-diagram"
    },
    {
        "id": 1,
        "name": "MCSManager",
        "description": "Панель управления серверами",
        "url": "http://192.168.31.113:23333/",
        "type": "http",
        "icon": "fas fa-server"
    },
    {
        "id": 2,
        "name": "Telegram-чат",
        "description": "Группа для общения",
        "url": "https://t.me/+QS7d55g7SO41MDZ ",
        "type": "no status",
        "icon": "fab fa-telegram"
    },
    {
        "id": 3,
        "name": "Minecraft-сервер",
        "description": "IP: 109.174.55.9:25575",
        "url": "minecraft://109.174.55.9:25575",
        "type": "minecraft",
        "icon": "fas fa-gamepad"
    }
]

def check_http_service(url, timeout=3):
    """Проверяет доступность HTTP-сервиса."""
    try:
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, timeout=timeout, context=context)
        return response.status == 200
    except Exception:
        return False

def check_minecraft_service(host, port, timeout=3):
    """Проверяет доступность Minecraft-сервиса."""
    try:
        ping = mctools.PINGClient(host, port, proto_num=0, timeout=timeout)

        ping.ping()
        return True 
    except TimeoutError:
        return False

    # try:
    #     with socket.create_connection((host, port), timeout=timeout):
    #         return True
    # except Exception:
    #     return False

def get_server_statuses():
    """Динамически получает статусы серверов."""
    statuses = []

    # Проверка HTTP-сервисов
    for service in SERVICES:
        status = False
        match service["type"]:
            case "http":
                status = check_http_service(service["url"])
            case "minecraft":
                host_port = service["url"][12:].split(":")
                if len(host_port) == 2:
                    host, port = host_port[0], int(host_port[1])
                    status = check_minecraft_service(host, port)
            case "no status":
                status = True

        statuses.append({
            "name": service["name"],
            "status": status
        })

    return statuses

# Статический статус серверов (временно)
# SERVER_STATUSES = [
#     {"name": "Plane", "status": True},  # Пример: Plane онлайн
#     {"name": "MCSManager", "status": True},  # Пример: MCSManager оффлайн
#     {"name": "Minecraft", "status": True}  # Пример: Minecraft онлайн
# ]

@app.route("/")
def index():
    SERVER_STATUSES = get_server_statuses()

    return render_template(
        "index.html", 
        services=SERVICES, 
        server_status=SERVER_STATUSES  # Передача статических данных
    )

@app.route("/wiki")
def wiki_index():
    return render_template("wiki_index.html", wiki=WIKI_PAGES)

@app.route("/wiki/<service>")
def wiki_page(service):
    if service not in WIKI_PAGES:
        abort(404)
    page = WIKI_PAGES[service]
    return render_template("wiki_page.html", page=page)

@app.route("/api/status")
def api_status():
    return {"status": "ok", "data": get_server_statuses()}

if __name__ == "__main__":
    app.run(debug=True)
