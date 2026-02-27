function copyCommand() {
    const code = document.getElementById('npm-fix').innerText;
    navigator.clipboard.writeText(code).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalText = btn.innerText;
        btn.innerText = 'Copied!';
        btn.style.background = '#00c853';

        setTimeout(() => {
            btn.innerText = originalText;
            btn.style.background = '#7c4dff';
        }, 2000);
    });
}

// Subtle parallax effect on background
window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const bg = document.querySelector('.bg-image');
    if (bg) {
        bg.style.transform = `scale(1.05) translateY(${scrolled * 0.1}px)`;
    }
});

console.log('Antigravity System Initialized.');
