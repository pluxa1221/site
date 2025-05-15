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
    // Реализуйте запрос к Flask API для получения актуального статуса
    alert("Статус обновлен!");
}
