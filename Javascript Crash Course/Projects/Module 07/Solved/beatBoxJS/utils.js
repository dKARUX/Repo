/**
 * Beat class that keeps track of playing the audio
 * HINT: Make sure to pass in the audioSrc as parameter to create a new audio track
 * HINT: Create a play function to play the audio if called 
 */
class Beat {
    constructor (audioFile){
        this.audioFile = new Audio (audioFile);
    }

    getAudioFile = () => {
        return this.audioFile;
    }

    setAudioFile = (source) => {
        this.audioFile = source;
    }

    playAudio = () => {
        this.audioFile.currentTime = 0;
        this.audioFile.play();
    }
}



/**
 * Button class that keeps track of the button color based on a press
 */
class Button {
    constructor(color, keyCode){
        this.color = color;
        this.keyCode = keyCode;
        this.element = document.getElementById(keyCode);
        this.setButtonColorInHTML();
        this.setATransitionEndListener();
    }

    // Listens until all transitions ends
    setATransitionEndListener = () => {
        this.element.addEventListener('transitionend', () => {
            this.deselect();
        })
    }
    /**
     * Set the button color based on color specified
     */
    setButtonColorInHTML = () => {
        this.element.style.borderColor = this.color;
    }

    /**
     * Select function to set the background color and boxShadow
     */
    select = () => {
        this.element.style.background = this.color;
        this.element.style.boxShadow = `0px 0px 17px 0px ${this.color}`;
    }

    /**
     * Deselect function to reset background color and boxShadow
     */
    deselect = () => {
        this.element.style.background = "transparent";
        this.element.style.boxShadow = "none";
    }
}