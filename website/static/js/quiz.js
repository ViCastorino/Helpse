const questionElement = document.getElementById('question');
const startButton = document.getElementById('start-btn');
const nextButton = document.getElementById('next-btn');

let shuffledQuestions, currentQuestionIndex;



startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})


function startGame() {
  startButton.classList.add('hide');
  shuffledQuestions = questions;
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  setNextQuestion()
}

function setNextQuestion() {
  showQuestion(shuffledQuestions[currentQuestionIndex]);
}

function showQuestion(question){
    questionElement.innerText = question.question;
}

const questions = [
  {question: 'What is 2 + 2?'},
  {question: 'Who is the best YouTuber?'},
  {question: 'Is web development fun?'},
  {question: 'What is 4 * 2?'}
];