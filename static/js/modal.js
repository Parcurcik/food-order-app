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
    let hasCost = false;

    checkboxes.forEach(checkbox => {
        const cost = parseFloat(checkbox.getAttribute('data-cost'));
        if (!isNaN(cost) && checkbox.checked) {
            total += cost;
            if (cost !== 0) {
                hasCost = true;
            }
        }
    });

    if (!isNaN(total) && hasCost) {
        totalPriceElement.textContent = total.toFixed(2);
    } else {
        totalPriceElement.textContent = "???";
    }
}


checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateTotalPrice);

});


