const flashMessage = document.querySelectorAll(".flash-message");

flashMessage.forEach ((message) => {
    setTimeout(() => {
        message.style.display = "none";
    }, 3000);
});