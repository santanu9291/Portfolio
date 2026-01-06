// Basic interactive behaviors for the portfolio
(function(){
// Typewriter effect for the title
const typeElem = document.querySelector('.typewriter');
if(typeElem){
const txt = typeElem.dataset.text || typeElem.textContent;
let i=0; typeElem.textContent='';
const step = ()=>{
if(i<txt.length){ typeElem.textContent += txt.charAt(i++); setTimeout(step,24); } else { /* loop not needed */ }
};
step();
}


// Smooth scroll for internal anchors
document.querySelectorAll('a[href^="#"]').forEach(a=>{
a.addEventListener('click',e=>{ const id=a.getAttribute('href'); if(id==='#') return; const el=document.querySelector(id); if(!el) return; e.preventDefault(); el.scrollIntoView({behavior:'smooth',block:'start'}); });
});


// Skill bars animation on scroll
const bars = document.querySelectorAll('.bar-fill');
const animBars = ()=>{
bars.forEach(b=>{
const val = parseInt(b.dataset.fill||'0',10);
const rect = b.getBoundingClientRect();
if(rect.top < window.innerHeight - 80){ b.style.width = val + '%'; }
});
};
window.addEventListener('scroll', animBars); animBars();


// Modal logic for project preview
const modal = document.getElementById('projModal');
const modalTitle = document.getElementById('modalTitle');
const modalDesc = document.getElementById('modalDesc');
const modalTags = document.getElementById('modalTags');
const modalStore = document.getElementById('modalStore');
document.querySelectorAll('.open-modal').forEach(btn=>{
btn.addEventListener('click', function(e){
const card = this.closest('.proj-card');
const title = card.dataset.title || card.querySelector('h3')?.textContent || 'Project';
const desc = card.querySelector('.muted')?.textContent || '';
const tags = Array.from(card.querySelectorAll('.proj-tags span')).map(s=>s.textContent);
modalTitle.textContent = title; modalDesc.textContent = desc; modalTags.innerHTML = tags.map(t=>`<span class="tag">${t}</span>`).join(' ');
modalStore.href = '#';
modal.setAttribute('aria-hidden','false');
});
});
document.querySelectorAll('.modal-close').forEach(b=>b.addEventListener('click',()=>modal.setAttribute('aria-hidden','true')));
modal.addEventListener('click', e=>{ if(e.target===modal) modal.setAttribute('aria-hidden','true'); });


// Contact form simple handler (no backend)
const form = document.getElementById('contactForm');
form.addEventListener('submit', function(e){ e.preventDefault(); alert('Thanks! This demo form does not send messages. Replace with your backend integration.'); form.reset(); });


// Small parallax effect
const parallax = document.querySelector('.parallax-layer');
window.addEventListener('mousemove', function(e){ if(!parallax) return; const x = (e.clientX - window.innerWidth/2)/40; const y = (e.clientY - window.innerHeight/2)/40; parallax.style.transform = `translate(${x}px, ${y}px)`; });
})();
