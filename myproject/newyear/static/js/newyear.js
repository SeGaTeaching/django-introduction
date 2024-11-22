document.addEventListener('DOMContentLoaded', () => {
    // Abfrage des Betriebssystem-Themes
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark');
    }

    // Listener für Theme-Änderungen (z. B. wenn der Benutzer das Systemtheme ändert)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (event) => {
        if (event.matches) {
            document.body.classList.add('dark');
        } else {
            document.body.classList.remove('dark');
        }
    });
});