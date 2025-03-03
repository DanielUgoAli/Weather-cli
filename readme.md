# Weather CLI

```bash
 _       __           __  __              ________    ____
| |     / /__  ____ _/ /_/ /_  ___  _____/ ____/ /   /  _/
| | /| / / _ \/ __ `/ __/ __ \/ _ \/ ___/ /   / /    / /  
| |/ |/ /  __/ /_/ / /_/ / / /  __/ /  / /___/ /____/ /   
|__/|__/\___/\__,_/\__/_/ /_/\___/_/   \____/_____/___/   
```

A **command-line interface (CLI) application** to check weather information for any city directly from your terminal.

## **Features**
✅ Get **current weather** information for any city  
✅ View **temperature details** in metric units  
✅ Check **humidity levels**  
✅ See **sunrise and sunset** times for any location  
✅ Generate **ASCII art** with customizable fonts  

---

## **Prerequisites**
- **Python 3.10+**
- **OpenWeatherMap API key**
- **Virtual Environment (Recommended)**

---

## **Installation**
### **1. Clone This Repository**
```bash
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
```

### **2. Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Mac/Linux
```

### **3. Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure API Key**
- Get a **free API key** from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
- Open the `config.py` file and add your API key:
  ```python
  # config.py
  API_KEY = "your_actual_api_key_here"
  BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
  ```

---

## **Usage**
### **Windows**
Run the application using the batch script:
```cmd
cd weather-cli\bin
run.bat
```

### **PowerShell**
Alternatively, run using PowerShell:
```powershell
cd weather-cli\bin
.\run.ps1
```

### **Linux / macOS**
For Linux and Mac users, run the following command:
```bash
cd weather-cli/bin
./run.sh
```

When the application starts, you will see the ASCII art title and a prompt:

```bash
Prompt🧝>>
```

---

## **Available Commands**
| Command        | Description |
|---------------|------------|
| `hi`          | Start the weather retrieval process |
| `temperature` | Display temperature details for a city |
| `humidity`    | Show humidity levels for a city |
| `suninfo`     | Show sunrise & sunset times for a city |
| `art <text>`  | Generate ASCII art from text |
| `help`        | Display available commands |
| `exit`        | Exit the application |

---

## **Examples**
### **1. Get Weather for a City**
```bash
Prompt🧝>> hi
🌍 City's Name: London
Weather in London: Clear Sky
Temperature: 15°C
Humidity: 76%
Wind: 3.6 m/s
Sunrise in London at 06:30 AM, local time.
Sunset in London at 06:45 PM, local time.
```

### **2. Get Temperature for a City**
```bash
Prompt🧝>> temperature
🌍 City's Name: Tokyo
Current Temperature: 25°C
Feels Like: 26°C
Min Temperature: 23°C
Max Temperature: 27°C
```

### **3. Get Humidity for a City**
```bash
Prompt🧝>> humidity
🌍 City's Name: New York
Humidity: 65%
Pressure: 1013 hPa
```

### **4. Get Sunrise & Sunset Information**
```bash
Prompt🧝>> suninfo
🌍 City's Name: Sydney
Sunrise: 05:48 AM
Sunset: 07:52 PM
```

### **5. Generate ASCII Art**
```bash
Prompt🧝>> art Hello --font slant
   __  __     ____           
  / / / /__  / / /___       
 / /_/ / _ \/ / / __ \      
/ __  /  __/ / / /_/ /      
/_/ /_/\___/_/_/\____/
```

---

## **API Key Issues & Fix**
If you get a **401 Unauthorized Error**, follow these steps:
1. **Check your API key** in `config.py`
2. **Ensure the API key is valid** from OpenWeatherMap
3. **Restart the script** after updating the key:
   ```bash
   ./bin/run.sh
   ```

---

## **Dependencies**
- `requests` (for making API calls)
- `pyfiglet` (for ASCII art generation)

---

## **Contributing**
Contributions, issues, and feature requests are welcome!  
Feel free to submit a pull request. 🎉

---

## **Acknowledgments**
🙏 Special thanks to [ziverch](https://github.com/ziverch) for the original project inspiration.  
This project was improved with **better error handling, a fixed API key system, and optimized CLI experience**. 🚀

