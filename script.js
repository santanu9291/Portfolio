// Fade and slide sections in on scroll
function revealOnScroll() {
  const sections = document.querySelectorAll('.section');
  let delay = 0;
  sections.forEach(section => {
    const top = section.getBoundingClientRect().top;
    if (top < window.innerHeight - 100 && !section.classList.contains('visible')) {
      setTimeout(() => section.classList.add('visible'), delay);
      delay += 200;
    }
  });
}

$(document).ready(function(){
  // console.log("fsdfsd");
  // alert("JS working ✅");
  $('.projects-slider').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    autoplaySpeed: 2500,
    arrows: true,
    dots: true,
    centerMode: true,
    centerPadding: '0',
    responsive: [
      {
        breakpoint: 900,
        settings: { slidesToShow: 2 }
      },
      {
        breakpoint: 600,
        settings: { slidesToShow: 1 }
      }
    ]
  });
});

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// Smooth scroll for navbar links
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if(href.startsWith('#')) {
      e.preventDefault();
      const target = document.querySelector(href);
      if(target){
        window.scrollTo({
          top: target.offsetTop - 30,
          behavior: 'smooth'
        });
      }
    }
  });
});

// Contact form handler
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    // If using FormSubmit, let it submit normally
    // Just show a pending message
    const msg = document.getElementById('msg');
    msg.textContent = 'Sending your message...';
    msg.style.color = '#58a6ff';
    
    // Form will submit to FormSubmit and redirect
    // No need to prevent default or reset
  });
}

// Download CV button with pulse effect
const cvBtn = document.getElementById('cvBtn');
cvBtn.addEventListener('click', () => {
  if (cvBtn.classList.contains('btn-loading')) return;
  cvBtn.classList.add('btn-loading');
  setTimeout(() => {
    cvBtn.classList.remove('btn-loading');
    const link = document.createElement('a');
    link.href = 'cv.pdf';
    link.download = 'Your_Name_CV.pdf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }, 1000);
});

