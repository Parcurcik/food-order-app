    document.addEventListener('DOMContentLoaded', function () {
        var messagesElement = document.querySelector('.messages');

        if (messagesElement) {
            messagesElement.style.display = 'block';
            setTimeout(function () {
                messagesElement.style.display = 'none';
            }, 5000);
        }
    });
