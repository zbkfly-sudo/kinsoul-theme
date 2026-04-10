/* ============================================
   KINSOUL ENERGY — Scroll Reveal & Micro-interactions
   Intersection Observer based, respects prefers-reduced-motion
   ============================================ */

(function() {
  'use strict';

  // Respect reduced motion preference
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Scroll Reveal --- */
  function initScrollReveal() {
    const revealElements = document.querySelectorAll('[data-kinsoul-reveal]');
    if (!revealElements.length) return;

    if (prefersReducedMotion) {
      revealElements.forEach(el => {
        el.classList.add('kinsoul-revealed');
        el.style.opacity = '1';
        el.style.transform = 'none';
      });
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const delay = parseInt(el.dataset.kinsoulDelay || '0', 10);
          setTimeout(() => {
            el.classList.add('kinsoul-revealed');
          }, delay);
          observer.unobserve(el);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -60px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
  }

  /* --- Stagger children reveal --- */
  function initStaggerReveal() {
    const staggerParents = document.querySelectorAll('[data-kinsoul-stagger]');
    if (!staggerParents.length) return;

    if (prefersReducedMotion) {
      staggerParents.forEach(parent => {
        const children = parent.querySelectorAll('[data-kinsoul-stagger-child]');
        children.forEach(child => {
          child.classList.add('kinsoul-revealed');
          child.style.opacity = '1';
          child.style.transform = 'none';
        });
      });
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const parent = entry.target;
          const children = parent.querySelectorAll('[data-kinsoul-stagger-child]');
          const staggerDelay = parseInt(parent.dataset.kinsoulStagger || '100', 10);
          children.forEach((child, i) => {
            setTimeout(() => {
              child.classList.add('kinsoul-revealed');
            }, i * staggerDelay);
          });
          observer.unobserve(parent);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    staggerParents.forEach(el => observer.observe(el));
  }

  /* --- Parallax-lite on scroll (subtle) --- */
  function initParallaxLite() {
    const parallaxElements = document.querySelectorAll('[data-kinsoul-parallax]');
    if (!parallaxElements.length || prefersReducedMotion) return;

    let ticking = false;
    function onScroll() {
      if (!ticking) {
        requestAnimationFrame(() => {
          const scrollY = window.scrollY;
          parallaxElements.forEach(el => {
            const speed = parseFloat(el.dataset.kinsoulParallax || '0.08');
            const rect = el.getBoundingClientRect();
            const elCenter = rect.top + rect.height / 2;
            const windowCenter = window.innerHeight / 2;
            const offset = (elCenter - windowCenter) * speed;
            el.style.transform = `translateY(${offset}px)`;
          });
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* --- Text split reveal for headings --- */
  function initTextReveal() {
    const textElements = document.querySelectorAll('[data-kinsoul-text-reveal]');
    if (!textElements.length || prefersReducedMotion) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('kinsoul-text-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.3
    });

    textElements.forEach(el => observer.observe(el));
  }

  /* --- Image reveal with clip-path --- */
  function initImageReveal() {
    const images = document.querySelectorAll('[data-kinsoul-image-reveal]');
    if (!images.length || prefersReducedMotion) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('kinsoul-image-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.2,
      rootMargin: '0px 0px -30px 0px'
    });

    images.forEach(el => observer.observe(el));
  }

  /* --- Section counter for numbered sections --- */
  function initSectionCounters() {
    const sections = document.querySelectorAll('.kinsoul-care__section');
    sections.forEach((section, i) => {
      const num = section.querySelector('.kinsoul-care__section-number');
      if (num) {
        num.textContent = String(i + 1).padStart(2, '0');
      }
    });
  }

  /* --- Initialize all on DOM ready --- */
  function init() {
    initScrollReveal();
    initStaggerReveal();
    initParallaxLite();
    initTextReveal();
    initImageReveal();
    initSectionCounters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Re-init on Shopify section render (theme editor)
  document.addEventListener('shopify:section:load', init);
})();
