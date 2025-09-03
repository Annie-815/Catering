// Optional: Highlight active link
document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".nav-links a");
    links.forEach(link => {
        if (link.href === window.location.href) {
            link.style.color = "#ff9800";
        }
    });
});

