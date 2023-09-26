var modal = document.getElementById("makeOrder");
var orderButton = document.querySelector(".order-button");
var closeButton = document.querySelector(".close");

orderButton.onclick = function () {
    modal.style.display = "block";
}

closeButton.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const totalPriceElement = document.getElementById('total-price');

function updateTotalPrice() {
    let total = 0;
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            total += parseFloat(checkbox.getAttribute('data-cost'));
        }
    });
    totalPriceElement.textContent = total.toFixed(2);
}

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateTotalPrice);
});


