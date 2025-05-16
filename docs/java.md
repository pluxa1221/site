# 📦 Установка и управление Java в Debian (через APT)

> Полное руководство по добавлению репозиториев, установке и переключению версий Java в Debian через `apt`.

## 📌 Описание

Это руководство поможет:
- Добавить репозитории Java (OpenJDK, Adoptium, Azul Zulu).
- Установить несколько версий Java.
- Переключаться между версиями.
- Устранить распространённые ошибки.

## 🧰 Предварительные требования

1. **ОС**: Debian 11+ (Bullseye/Bookworm).
2. **Права администратора**: Убедитесь, что у вас есть доступ к `sudo`.
3. **Установленные утилиты**:
   ```bash
   sudo apt install gnupg wget curl software-properties-common -y
   ```

## 🔁 Добавление репозиториев

### 1. OpenJDK (официальный репозиторий Debian)

> Java доступна в официальных репозиториях Debian. Подходит для базовых версий.

```bash
# Обновите список пакетов
sudo apt update

# Поиск доступных версий Java
apt-cache search openjdk

# Пример: установка OpenJDK 17
sudo apt install openjdk-17-jdk -y

# Проверка установки
java -version
```

### 2. Adoptium (ранее AdoptOpenJDK)

> Поддерживает современные версии Java (включая 17, 19, 21 и выше).

```bash
# Добавление GPG-ключа
wget -O - https://packages.adoptium.net/artifactory/api/security/keypair/gpg/public  | sudo gpg --dearmor -o /usr/share/keyrings/adoptium.gpg

# Добавление репозитория
echo 'deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb  $(awk -F= '/^VERSION_CODENAME/{print $2}' /etc/os-release) main' | sudo tee /etc/apt/sources.list.d/adoptium.list

# Обновление пакетов
sudo apt update

# Установка нужной версии (например, 17)
sudo apt install temurin-17-jdk -y

# Проверка
java -version
```

### 3. Azul Zulu (коммерческая поддержка)

> Рекомендуется для корпоративных сред и продакшена.

```bash
# Загрузка и установка репозитория Azul
wget -qO - https://repos.azul.com/azul-repo.key  | sudo gpg --dearmor -o /usr/share/keyrings/azul.gpg
echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb  stable main" | sudo tee /etc/apt/sources.list.d/zulu.list

# Обновление пакетов
sudo apt update

# Установка версии (например, Zulu 17)
sudo apt install zulu-17 -y

# Проверка
java -version
```

## 📦 Установка Java
> Установка JDK или JRE
 * JDK (Java Development Kit): для разработки.
 * JRE (Java Runtime Environment): только для запуска приложений.

> Примеры:

```bash
# Установка JDK (Adoptium 17)
sudo apt install temurin-17-jdk -y

# Установка JRE (Adoptium 17)
sudo apt install temurin-17-jre -y
```

## 🔄 Переключение между версиями Java

> Использование `update-alternatives`

```bash
# Список установленных версий
sudo update-alternatives --config java

# Выберите нужную версию, введя её номер
```

> Пример вывода:

```
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                      Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-17-openjdk-amd64/bin/java   1711      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java   1111      manual mode
  2            /usr/lib/jvm/java-17-temurin/bin/java         1700      manual mode
```

## 📋 Проверка установленных версий

```bash
# Проверка Java
java -version

# Проверка компилятора Javac
javac -version

# Проверка установленных пакетов
dpkg --list | grep -i jdk
```

## 🗑️ Удаление Java

> Удаление пакета

```bash
# Пример: удаление Adoptium 17
sudo apt remove temurin-17-jdk -y

# Очистка неиспользуемых зависимостей
sudo apt autoremove -y
```

## 🛠️ Советы по использованию

> Управление версиями
 * Для одного пользователя : `jEnv`
 * Для всех пользователей : `update-alternatives`
 * Универсальный менеджер версий : `SDKMAN`

> Пример установки SDKMAN:

```bash
# Установка SDKMAN
curl -s "https://get.sdkman.io " | bash

# Перезапустите терминал или выполните:
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Просмотр доступных версий Java
sdk list java

# Установка версии (например, 17)
sdk install java 17.0.8-tem

# Переключение версии
sdk use java 17.0.8-tem
```
