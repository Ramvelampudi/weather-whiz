# Weather Whiz
Weather Whiz is a Python program designed to fetch and display real-time weather data for a city using the WeatherAPI. The program provides a user-friendly interface that allows users to enter the name of a city and instantly receive the current temperature in degrees Celsius. Moreover, it leverages text-to-speech technology to read the temperature aloud, making it accessible to users with visual impairments or those who prefer audio feedback.
## Flowchart
![untitled (1)](https://github.com/Ramvelampudi/weather-whiz/assets/111103944/ad2e7f18-eb74-4081-a2ef-a6ec23a498f3)

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [API Key](#api-key)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Real-time weather data:** Weather Whiz fetches real-time weather data from the WeatherAPI, ensuring that the temperature information is up-to-date.
- **User input:** The program prompts the user to enter the name of the city they want to check the weather for.
- **Temperature display:** It displays the current temperature of the specified city in degrees Celsius.
- **Text-to-speech:** Weather Whiz uses the `pyttsx3` library to read the temperature aloud, providing an audio output along with the visual display.

## Getting Started

### Prerequisites

- Python 3.x
- Install the required Python libraries: `requests`, `json`, and `pyttsx3`.

### API Key

Weather Whiz relies on the WeatherAPI to fetch weather data. To use the program, you need to obtain your own API key from WeatherAPI.com and replace `<YOUR_API_KEY>` in the script with your key. Without a valid API key, the program will not be able to fetch weather data. The specific API endpoint may not be valid anymore, as this code uses a specific API key and endpoint from the past. You might need to replace these with a working API key and endpoint if you plan to use this code with an actual weather API.

### Installation

1. Clone the repository to your local machine or download the `weather_whiz.py` file directly.

2. Install the required Python libraries:

## Usage

1. Run the script `weather_whiz.py` from the command line.

2. Enter the name of the city when prompted. To quit the program, type 'q' and press Enter.

3. The program will display the current temperature in Celsius for the specified city, and it will also read the temperature aloud.

## API Documentation

- WeatherAPI: [WeatherAPI Documentation](https://www.weatherapi.com/docs/)

## Contributing

Contributions to Weather Whiz are welcome! If you find a bug, have a feature request, or want to contribute to the project, feel free to open an issue or submit a pull request.

## License

Weather Whiz is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The WeatherAPI team for providing the weather data API.
- The developers of `requests`, `json`, and `pyttsx3` libraries for their useful Python packages.

---

With this README file, users and potential contributors can quickly understand what the project is about, how to set it up, and how to use it. It also provides information on how to obtain the API key and how to contribute to the project. Make sure to keep the README up to date as the project evolves and new features are added.

1. Clone the repository to your local machine or download the `weather_whiz.py` file directly.

2. Install the required Python libraries:
