document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const progressBar = document.getElementById('progressBar');
    const counter = document.getElementById('slideCounter');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const notesToggle = document.getElementById('notesToggle');
    const notesPanel = document.getElementById('notesPanel');
    const notesContent = document.getElementById('notesContent');
    const fullscreenToggle = document.getElementById('fullscreenToggle');
    let current = 0;
    let notesVisible = false;

    function showSlide(index) {
        slides.forEach(s => s.classList.remove('active'));
        slides[index].classList.add('active');
        current = index;
        const pct = ((index + 1) / slides.length) * 100;
        progressBar.style.width = pct + '%';
        counter.textContent = `${index + 1} / ${slides.length}`;
        prevBtn.disabled = index === 0;
        nextBtn.disabled = index === slides.length - 1;
        if (notesVisible) {
            const note = slides[index].getAttribute('data-notes') || 'Sem notas para este slide.';
            notesContent.innerHTML = note;
        }
    }

    function next() { if (current < slides.length - 1) showSlide(current + 1); }
    function prev() { if (current > 0) showSlide(current - 1); }

    function toggleNotes() {
        notesVisible = !notesVisible;
        notesPanel.classList.toggle('visible', notesVisible);
        notesToggle.classList.toggle('active', notesVisible);
        if (notesVisible) {
            const note = slides[current].getAttribute('data-notes') || 'Sem notas para este slide.';
            notesContent.innerHTML = note;
        }
    }

    function toggleFullscreen() {
        if (!document.fullscreenElement) document.documentElement.requestFullscreen();
        else document.exitFullscreen();
    }

    prevBtn.addEventListener('click', prev);
    nextBtn.addEventListener('click', next);
    notesToggle.addEventListener('click', toggleNotes);
    fullscreenToggle.addEventListener('click', toggleFullscreen);

    document.addEventListener('keydown', e => {
        if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); next(); }
        else if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
        else if (e.key === 'n' || e.key === 'N') toggleNotes();
        else if (e.key === 'f' || e.key === 'F') toggleFullscreen();
    });

    showSlide(0);
});
