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
cd weather-cli
run.bat
```

### PowerShell

Alternatively, run using PowerShell:

```powershell
cd weather-cli
.\run.ps1
```

When the application starts, you will see the ASCII art title and a prompt:

```bash
Prompt🧭>> 
```

### Available Commands

- `hi` - Start the weather retrieval process (this is the main entry point)
- `tempurature` - Display temperature information for a city
- `humidity` - Show humidity information for a city
- `suninfo` - Display sunrise and sunset times for a city
- `art <text> [--font <font_name>]` - Generate ASCII art from text
- `help` - Display available commands and their descriptions
- `exit` - Exit the application

### Examples

```bash
Prompt🧭>> hi
City's Name: London
[Temperature information will be displayed]

Prompt🧭>> tempurature
[Temperature information will be displayed]

Prompt🧭>> humidity
[Humidity information will be displayed]

Prompt🧭>> suninfo
[Sunrise and sunset times will be displayed]

Prompt🧭>> art Hello --font slant
[ASCII art will be generated]
```

## API Key

This application uses the OpenWeatherMap API. The repository includes a default API key, but if you plan to use this application extensively, it's recommended that you get your own API key from [OpenWeatherMap](https://openweathermap.org/api) and update it in the `soon` file.

## Dependencies

- requests
- pyfiglet (for ASCII art generation)

## Contributing

Contributions, issues, and feature requests are welcome!

## 🙏

 [@ziverch](https://github.com/ziverch) for original project at [repository](https://github.com/ziverch/Weather-cli)
