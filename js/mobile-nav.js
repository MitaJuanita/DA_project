document.getElementById('menu-toggle').addEventListener('click', () => {
    const navList = document.getElementById('nav-list');
    navList.classList.toggle('show');
    
    // Update aria attributes
    const isExpanded = navList.classList.contains('show');
    document.getElementById('menu-toggle').setAttribute('aria-expanded', isExpanded);
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
    const navList = document.getElementById('nav-list');
    const menuToggle = document.getElementById('menu-toggle');
    
    if (!navList.contains(e.target) && !menuToggle.contains(e.target)) {
        navList.classList.remove('show');
        menuToggle.setAttribute('aria-expanded', 'false');
    }
});
