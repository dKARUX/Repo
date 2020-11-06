//TODO: Convert all functions and any other possible elements to ES6

/**
 * Update the output text as you type in the textarea
 */
// function updateText(){
//   let text = document.getElementById("text-input").value;
//   document.getElementById('text-output').innerText = text;
// }

updateText = () => {
  var text = document.getElementById("text-input").value;
  document.getElementById('text-output').innerText = text;
}

/**
 * Toggle the bold class for the output text
 */
// function makeBold(elem){
//   elem.classList.toggle('active');
//   document.getElementById('text-output').classList.toggle('bold');
// }

makeBold = (elem) => {
  elem.classList.toggle('active');
  document.getElementById('text-output').classList.toggle('bold');
}

/**
 * Toggle the italic class for the output text
 */
// function makeItalic(elem){
//   elem.classList.toggle('active');
//   document.getElementById('text-output').classList.toggle('italic');
// }

makeItalic = (elem) => {
  elem.classList.toggle('active');
  document.getElementById('text-output').classList.toggle('italic');
}

/**
 * Toggle the underline class for the output text
 */
// function makeUnderline(elem){
//     elem.classList.toggle('active');
//     let output = document.getElementById('text-output');
//     if(output.classList.contains('underline')){
//       output.classList.remove('underline');
//     } else {
//       output.classList.add('underline');
//     }
// }

makeUnderline = (elem) => {
  elem.classList.toggle('active');
  var output = document.getElementById('text-output');
  output.classList.contains('underline') ? output.classList.remove('underline') : output.classList.add('underline');
}

/**
 * Toggle the style textAlign attribute
 * Toggle the active state for the align butttons
 */
// function alignText(elem, alignType){
//   document.getElementById('text-output').style.textAlign = alignType;
//   let alignButtons = document.getElementsByClassName('align');
//   for(let i = 0; i < alignButtons.length; i++ ){
//     alignButtons[i].classList.remove('active');
//   }
//   elem.classList.toggle('active');
// }

alignText = (elem, alignType) => {
  document.getElementById('text-output').style.textAlign = alignType;
  var alignButtons = document.getElementsByClassName('align');
  for(let i of alignButtons) {
    i.classList.remove('active');
  }
  elem.classList.toggle('active');
}