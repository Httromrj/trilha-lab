const cards = document.querySelectorAll(".step, .challenge-grid article, .example-grid a");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.12 }
);

cards.forEach((card) => observer.observe(card));
