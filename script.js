// ===== HAMBURGER MENU =====
function toggleMenu() {
    document.getElementById("sideMenu").classList.toggle("active");
    document.getElementById("overlay").classList.toggle("active");
}

function closeMenu() {
    document.getElementById("sideMenu").classList.remove("active");
    document.getElementById("overlay").classList.remove("active");
}

// Close menu on Escape key
document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenu();
});

// ===== SCROLL REVEAL =====
const revealElements = document.querySelectorAll(".reveal");

const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target); // animate once
            }
        });
    },
    { threshold: 0.15 }
);

revealElements.forEach((el) => observer.observe(el));

// ===== NAVBAR — darken on scroll =====
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 60) {
        navbar.style.background = "rgba(10, 10, 10, 0.95)";
    } else {
        navbar.style.background = "rgba(10, 10, 10, 0.75)";
    }
});