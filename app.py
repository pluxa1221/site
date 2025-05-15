from flask import Flask, render_template, abort
import mistune, os

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
        "minecraft": "minecraft://109.174.55.9:25575"
    }
    return urls.get(slug, "#")

# Загружаем страницы при старте приложения
WIKI_PAGES = load_wiki_pages()

# Данные сервисов
SERVICES = [
    {
        "name": "Plane",
        "description": "Система управления проектами",
        "url": "http://103.88.242.164:1610/nevetime/",
        "icon": "fas fa-project-diagram"
    },
    {
        "name": "MCSManager",
        "description": "Панель управления серверами",
        "url": "http://192.168.31.113:23333/",
        "icon": "fas fa-server"
    },
    {
        "name": "Telegram-чат",
        "description": "Группа для общения",
        "url": "https://t.me/+QS7d55g7SO41MDZ ",
        "icon": "fab fa-telegram"
    },
    {
        "name": "Minecraft-сервер",
        "description": "IP: 109.174.55.9:25575",
        "url": "minecraft://109.174.55.9:25575",
        "icon": "fas fa-gamepad"
    }
]

# Статический статус серверов (временно)
SERVER_STATUSES = [
    {"name": "Plane", "status": True},  # Пример: Plane онлайн
    {"name": "MCSManager", "status": True},  # Пример: MCSManager оффлайн
    {"name": "Minecraft", "status": True}  # Пример: Minecraft онлайн
]

@app.route("/")
def index():
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

if __name__ == "__main__":
    app.run(debug=True)
