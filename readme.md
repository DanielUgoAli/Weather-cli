# Weather CLI

```bash
 _       __           __  __              ________    ____
| |     / /__  ____ _/ /_/ /_  ___  _____/ ____/ /   /  _/
| | /| / / _ \/ __ `/ __/ __ \/ _ \/ ___/ /   / /    / /  
| |/ |/ /  __/ /_/ / /_/ / / /  __/ /  / /___/ /____/ /   
|__/|__/\___/\__,_/\__/_/ /_/\___/_/   \____/_____/___/   
```

A command-line interface application to check weather information for any city directly from your terminal.

## Features

- Get current weather information for any city
- View temperature details in metric units
- Check humidity levels
- See sunrise and sunset times for any location
- Generate ASCII art with customizable fonts

## Prerequisites

- python 3.10 or higher
- pip package manager
- OpenWeatherMap API key

## Installation

1. Clone this repository

```bash
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
```

2. Install required dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Windows

Run the application using the batch script:

```cmd
cd weather-cli\bin
run.bat
```

### PowerShell

Alternatively, run using PowerShell:

```powershell
cd weather-cli\bin
.\run.ps1
```

### Linux/Mac

For Linux and Mac users, run the following command:

```bash
cd weather-cli/bin
./run.sh
```

When the application starts, you will see the ASCII art title and a prompt:

```bash
Prompt🧭>> 
```

### Available Commands

- `hi` - Start the weather retrieval process (this is the main entry point)
- `temperature` - Display temperature information for a city
- `humidity` - Show humidity information for a city
- `suninfo` - Display sunrise and sunset times for a city
- `art <text> [--font <font_name>]` - Generate ASCII art from text
- `help` - Display available commands and their descriptions
- `exit` - Exit the application

### Examples

```bash
Prompt🧭>> hi
City's Name: London
Weather in London: Clear Sky
Temperature: 15°C
Humidity: 76%
Wind: 3.6 m/s

Prompt🧭>> temperature
City's Name: Tokyo
Current Temperature: 25°C
Feels Like: 26°C
Min Temperature: 23°C
Max Temperature: 27°C

Prompt🧭>> humidity
City's Name: New York
Humidity: 65%
Pressure: 1013 hPa

Prompt🧭>> suninfo
City's Name: Sydney
Sunrise: 05:48 AM
Sunset: 07:52 PM

Prompt🧭>> art Hello --font slant
   __  __     ____           
  / / / /__  / / /___       
 / /_/ / _ \/ / / __ \      
/ __  /  __/ / / /_/ /      
/_/ /_/\___/_/_/\____/
```

## API Key

This application uses the OpenWeatherMap API. You'll need to get your own API key from [OpenWeatherMap](https://openweathermap.org/api) and add it to the `config.py` file. For reasons, I did not decided to remove the default API key in the repository.

```python
# config.py
API_KEY = "your_api_key_here"
```

## Dependencies

- requests
- pyfiglet (for ASCII art generation)

## Contributing

Contributions, issues, and feature requests are welcome!

🙏 [ziverch](https://github.com/ziverch) for original project at [repository](https://github.com/ziverch/Weather-cli)
