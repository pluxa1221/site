# 🚀 PlayIt — Сервис для туннелирования портов

> Простой и бесплатный инструмент для проброски локальных портов в интернет.  
> Идеально подходит для тестирования веб-приложений, игр, API и других сервисов без настройки роутера или фаервола.

## ✅ Основные возможности

 🔁 Автоматическое создание публичного URL 
 🖥️ Поддержка TCP и HTTP(S) 
 🧱 Обход NAT/Firewall 
 📦 Лёгкий клиент. Для Windows, Linux, macOS.
 📈 Бесплатное использование 
 🔐 TLS/SSL автоматически предоставлен сервисом 
 🌍 Доступ из любой точки мира

---

## 🔄 Как это работает?

1. Вы запускаете локальный сервер, например на `localhost:8080`.
2. Запускаете клиент `playit`, указав нужный порт.
3. PlayIt создаёт уникальный публичный URL и перенаправляет трафик на ваш локальный порт.
4. Любой человек может открыть этот URL и получить доступ к вашему локальному серверу.

## 🛠️ Установка клиента

### Linux/macOS:
```bash
curl -fsSL https://playit.gg/install.sh  | sh
```

### Windows (PowerShell):
```powershell
iwr https://playit.gg/install.ps1  | iex
```

> После установки клиент будет доступен в командной строке как playit. 
> Просто введите playit в терминале, чтобы увидеть список доступных команд. 
> Клиент автоматически подключается к облачному серверу PlayIt и готов к использованию без дополнительной настройки. 
> Все необходимые зависимости и конфигурации обрабатываются установщиком, поэтому вы можете сразу приступить к созданию туннелей.

