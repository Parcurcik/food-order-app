// Получаем элементы DOM для открытия и закрытия второго модального окна
const openReportButton = document.getElementById('openModalButton'); // Предполагается, что это кнопка "Cкачать отчёт"
const closeModalButton2 = document.querySelector('#downloadReport .close');
const modal2 = document.getElementById('downloadReport');

// Открываем второе модальное окно
openReportButton.addEventListener('click', () => {
  modal2.style.display = 'block';
});

// Закрываем второе модальное окно по нажатию на крестик
closeModalButton2.addEventListener('click', () => {
  modal2.style.display = 'none';
});

// Закрываем второе модальное окно, если пользователь кликает за его пределами
window.addEventListener('click', (event) => {
  if (event.target == modal2) {
    modal2.style.display = 'none';
  }
});
