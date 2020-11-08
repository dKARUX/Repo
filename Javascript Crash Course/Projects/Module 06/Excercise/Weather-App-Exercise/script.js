/**
 * Weather App
 * TODO: Complete getWeatherData() to return json response Promise
 * TODO: Complete searchCity() to get user input and get data using getWeatherData()
 * TODO: Complete showWeatherData() to set the data in the the html file from response
 */

// API_KEY for maps api
const API_KEY = "a8e71c9932b20c4ceb0aed183e6a83bb";

/**
 * Retrieve weather data from openweathermap
 * HINT: Use fetch()
 * HINT: URL should look like this: 
 * https://api.openweathermap.org/data/2.5/weather?q=detroit&appid=a8e71c9932b20c4ceb0aed183e6a83bb&units=imperial
 */
getWeatherData = (city) => {
  // Define URL constants
  const URL = "https://api.openweathermap.org/data/2.5/weather";
  const COMPLETE_URL = `${URL}?q=${city}&appid=${API_KEY}&units=imperial`;
  //HINT: Use template literals to create a url with input and an API key
  //CODE GOES HERE
  var fetchFromWeatherAPI = fetch(COMPLETE_URL);
  // Fetch data from API with the goal of getting a Promise
  outputResponse = fetchFromWeatherAPI.then((response) => {
    // Converting Response Object in JSON
    return response.json();
  })
  return outputResponse; 
}

/**
 * Retrieve city input and get the weather data
 * HINT: Use the promise returned from getWeatherData()
 */
searchCity = () => {
  // Define city constant which will be storing the input data from form
  const CITY = document.getElementById('city-input').value;
  // CODE GOES HERE
  document.getElementById("city-name").innerHTML = CITY;

  // Declare variables for Error handling
  var getErrorCatcherElem = document.getElementsByClassName("error-catcher")[0];
  var errorMsg = "ERROR! Please try again later...";
  var errorMsgHTML = `<h3>${errorMsg}</h3>`;

  // Retrieve Response Object data as JSON collection
  getWeatherData(CITY).then((data) => {
    // Sends the JSON data to the function by calling it
    showWeatherData(data);
    // Clears the UI from Error messages if the element is not empty
    if (getErrorCatcherElem.innerHTML == errorMsgHTML) {
      getErrorCatcherElem.innerHTML = null
    }
  }).catch(() => {
    // Add Error handler
    // Print Error message into console
    console.log(errorMsg);
    // Display Error in Document
    getErrorCatcherElem.innerHTML = errorMsgHTML;
  })
}

/**
 * Show the weather data in HTML
 * HINT: make sure to console log the weatherData to see how the data looks like
 */
showWeatherData = (weatherData) => {
  //CODE GOES HERE
  // Declare variables for API data retrieval
  var weather = weatherData.weather[0].main;
  var mainTemp = weatherData.main.temp;
  var mainTempMin = weatherData.main.temp_min;
  var mainTempMax = weatherData.main.temp_max;

  // Print data into console
  console.log(`Weather: ${weather}`);
  console.log(`Temp: ${mainTemp}°`);
  console.log(`Min Temp: ${mainTempMin}°`);
  console.log(`Max Temp: ${mainTempMax}°`);

  // Add API to the Elements
  document.getElementById("weather-type").innerHTML = weather;
  document.getElementById("temp").innerHTML = mainTemp;
  document.getElementById("min-temp").innerHTML = mainTempMin;
  document.getElementById("max-temp").innerHTML = mainTempMax;
}
