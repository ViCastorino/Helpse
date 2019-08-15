let btnpaciente = document.getElementById('first');
let btnorganization = document.getElementById('second');
let container = document.getElementById('container');
let x = document.getElementById('paciente');
let y = document.getElementById('instituicao');
let a = document.getElementById('formulários');

x.style.display =  'none';
y.style.display =  'none';

btnpaciente.addEventListener('click', function(){
    a.style.display =  'flex';
    container.style.display = 'none';
    x.style.display =  'flex';
    y.style.display =  'none';
    console.log('clicou1');
});

btnorganization.addEventListener('click', function(){
    a.style.display = 'flex';
    x.style.display =  'none';
    y.style.display =  'flex';
    container.style.display = 'none';
    console.log('clicou2');
});

// função do carrosel ///

let slideIndex = 1;
// slideShow(slideIndex);


function plusSlides(n) { slideShow(slideIndex += n); }

function currentSlide(n) { slideShow(slideIndex = n); }

function slideShow(n) {
    let i;
    let slides = document.getElementsByClassName("text-box");
    // let dots = document.getElementsByClassName("bar");

    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // for (i = 0; i < dots.length; i++) {
    //     dots[i].className = dots[i].className.replace(" activate", "");
    // }
    // slides[slideIndex - 1].style.display = "block";
    // dots[slideIndex - 1].className += " active";

}



