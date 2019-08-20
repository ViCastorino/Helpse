var currentQuestion = 0;
var score1 = 0;
var score2 = 0;
var score3 = 0;
var totQuestions = questions.length;
let resposta1 = document.getElementById('resposta1');
let resposta2 = document.getElementById('resposta2');

var container = document.getElementById('quizContainer');
var questionEl = document.getElementById('question');
var opt1 = document.getElementById('opt1');
var opt2 = document.getElementById('opt2');
var opt3 = document.getElementById('opt3');
var nextButton = document.getElementById('nextButton');
var resultCont = document.getElementById('result');

var cont1 = 0;
var cont2 = 0;
var cont3 = 0;

function loadQuestion (questionIndex){
    var q = questions[questionIndex];
    questionEl.textContent = [questionIndex +1] + '. ' + q.question;
    opt1.textContent = q.opcao1;
    opt2.textContent = q.opcao2;
    opt3.textContent = q.opcao3;
}

function loadNextQuestion () {
    var selectOption = document.querySelector('input[type=radio]:checked');
    if(!selectOption){
        alert('Por favor selecione sua resposta!');
        return;
    }
    var answer1 = selectOption.value;
    var answer2 = selectOption.value;
    var answer3 = selectOption.value;

    if(questions[currentQuestion].answer1 == answer1){
        score1 += 1;
    }
    if(questions[currentQuestion].answer2 == answer2){
        score2 += 1;
    }
    if(questions[currentQuestion].answer3 == answer3){
        score3 += 1;
    }

    selectOption.cheked = false;
    currentQuestion++;
    if(currentQuestion == totQuestions -1){
        nextButton.textContent = 'Fim';
    }
    if(currentQuestion == totQuestions){
        container.style.display =  'none';
        resultCont.style.display = '';
        // resultCont.textContent = 'Seu placar: ' + score;
        return;
    }
    if(score1>score2>score3){
        resposta1.style.display = 'block';
    }else if(score2>score1<score3){
        resposta1.style.display = 'block';
    }else if(score2>score3<score1){
        resposta3.style.display = 'block';
    }else if(score3>score2>score1){
        resposta2.style.display = 'block';
    }else if(score3>score1>score2){
        resposta2.style.display = 'block';
    }

    loadQuestion(currentQuestion);
}

loadQuestion(currentQuestion);


// function Results (){
//     if(questions[currentQuestion].opcao1 = opt1){
//         cont1++;
//     }
//     if(questions[currentQuestion].opcao2 = opt2){
//         cont2++;
//     }
//     if(questions[currentQuestion].opcao3 = opt3){
//         cont3++;
//     }
//     alert('Seu placar: ' + cont1 + cont2 + cont3);
//     return;
// }
