// Плавный скролл
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Обновление статуса серверов
function updateStatus() {
    // Запрос к Flask API для получения актуального статуса
    fetch('/api/status') // Укажите актуальный путь к API
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка сети');
            }
            return response.json();
        })
        .then(data => {
            // Пример обновления статуса на странице
            data.servers.forEach(server => {
                const statusElement = document.getElementById(`status-${server.id}`);
                if (statusElement) {
                    statusElement.textContent = server.status;
                    statusElement.className = `status ${server.status}`; // Добавление класса для стилизации
                }
            });
        })
        .catch(error => {
            console.error('Ошибка загрузки статуса:', error);
            alert('Не удалось обновить статус серверов');
        });
}
