// Intersection Observer for fade-in animations
const fadeInElements = document.querySelectorAll('.fade-in');
const slideUpElements = document.querySelectorAll('.slide-up');

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1
});

fadeInElements.forEach(element => fadeInObserver.observe(element));
slideUpElements.forEach(element => fadeInObserver.observe(element));

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});