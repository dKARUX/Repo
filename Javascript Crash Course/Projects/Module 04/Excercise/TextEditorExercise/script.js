/**
 * TODO: Update the text in the "Formatted Text" section as a user types in the textarea
 * TODO TOGETHER: Add a .bold, .italic classes to "Formatted Text" when the appropriate button is clicked
 * TODO: Add an .underline class to "Formatted Text" when Underline button is clicked
 * TODO: Toggle the align style for "Formatted Text" when the appropriate button is clicked
 */


/**
 * Update the output text as a user types in the textarea
 * HINT: Use the onkeydown function inside HTML
 */
function updateText(){
  // CODE GOES HERE
  let inputText = document.getElementById('text-input').value;
  document.getElementById('text-output').innerText = inputText;
}

/**
 * Toggle the bold class for the output text
 * HINT: Use the onclick function insite HTML
 * HINT: Look into using this keyword
 * HINT: Use the classList property
 * HINT: Toggle .active class for the button
 */
function makeBold(elem){
  //CODE GOES HERE
  elem.classList.toggle('active');

  let inputElement = document.getElementById('text-output');
  inputElement.classList.toggle('bold');
}

/**
 * Toggle the italic class for the output text
 */
function makeItalic(elem){
  elem.classList.toggle('active');

  let inputElement = document.getElementById('text-output');
  inputElement.classList.toggle('italic');
}

/**
 * Toggle the underline class for the output text
 * HINT: Toggle the .active class for the button
 * HINT: Use the classList property
 * HINT: Use contains, remove, and add functions
 */
function makeUnderline(elem){
  //CODE GOES HERE
  elem.classList.toggle('active');

  let inputElement = document.getElementById('text-output');
  
  if (inputElement.classList.contains('underline') == false){
    inputElement.classList.add('underline');
  } else {
    inputElement.classList.remove('underline');
  }
}

/**
 * Toggle the style textAlign attribute
 * Toggle the active state for the align butttons
 * HINT: Use the style property of the element
 * HINT: Make sure to untoggle the active state for all other align buttons
 */
function alignText(elem, alignType){
  // CODE GOES HERE
  elem.classList.toggle('active');

  let alignElemLeft = document.getElementById('left-align');
  let alignElemCenter = document.getElementById('center-align');
  let alignElemRight = document.getElementById('right-align');
  
  switch (alignType){
    case 'left':
      alignElemCenter.classList.remove('active');
      alignElemRight.classList.remove('active');
      break;
    case 'center':
      alignElemLeft.classList.remove('active');
      alignElemRight.classList.remove('active');
      break;
    case 'right':
      alignElemLeft.classList.remove('active');
      alignElemCenter.classList.remove('active');
      break;
    default:
  }
  
  let inputElement = document.getElementById('text-output');
  inputElement.style.textAlign = alignType;
  
}