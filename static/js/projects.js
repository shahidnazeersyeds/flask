// Project filtering and animations
document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.projects__card');
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    // Add hover animations
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.classList.add('hover');
        });
        
        card.addEventListener('mouseleave', () => {
            card.classList.remove('hover');
        });
    });
    
    // Filter functionality
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.dataset.filter;
            
            projectCards.forEach(card => {
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'block';
                    setTimeout(() => card.classList.add('visible'), 100);
                } else {
                    card.classList.remove('visible');
                    setTimeout(() => card.style.display = 'none', 300);
                }
            });
        });
    });
});