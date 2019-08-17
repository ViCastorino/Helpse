let slideIndex = 1;
let indice = 1;
showSlides(indice);

function plusSlides(n) {
  showSlides(indice += n);
}

function currentSlide(n) {
  showSlides(indice = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("box-text");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {indice = 1} 
    if (n < 1) {indice = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
  slides[indice-1].style.display = "block"; 
  dots[indice-1].className += " active";
}