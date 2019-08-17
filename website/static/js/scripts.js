let btnpaciente = document.getElementById('first');
let btnorganization = document.getElementById('second');
let container = document.getElementById('container');
let x = document.getElementById('paciente');
let y = document.getElementById('instituicao');
let a = document.getElementById('formulários');

x.style.display = 'none';
y.style.display = 'none';

btnpaciente.addEventListener('click', function(){
    a.style.display =  'flex';
    container.style.display = 'none';
    x.style.display =  'flex';
    // y.style.display =  'none';
    console.log('clicou1');
});

btnorganization.addEventListener('click', function(){
    a.style.display = 'flex';
    // x.style.display =  'none';
    y.style.display =  'flex';
    container.style.display = 'none';
    console.log('clicou2');
});


// função do carrosel ///

