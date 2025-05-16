function updateStatuses() {
  fetch('/api/status')
    .then(response => response.json())
    .then(data => {
      const statuses = data.data;

      // Очищаем текущий вывод
      const container = document.getElementById('server-status');
      container.innerHTML = ''; // Очистка старых данных

      // Вставляем обновленные статусы
      statuses.forEach(service => {
        const div = document.createElement('div');
        div.className = 'server-item';
        div.dataset.service = service.name;

        const statusText = service.status ? '🟢 Онлайн' : '🔴 Оффлайн';
        div.innerHTML = `<strong>${service.name}</strong>: ${statusText}`;
        
        container.appendChild(div);
      });
    })
    .catch(err => {
      console.error("Ошибка при получении статуса:", err);
    })
}

// Первый вызов сразу
updateStatuses();

// Обновление каждые 10 секунд
setInterval(updateStatuses, 10000);