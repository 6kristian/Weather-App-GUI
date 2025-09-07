import sys # Import the sys module
import requests # Import the requests module
# Removed unused PyQt5 import
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout # Import the necessary classes from the PyQt5 module
from PyQt5.QtCore import Qt # Import the Qt class from the PyQt5 module

class WeatherApp(QWidget): #weather app class
    def __init__(self):
        super().__init__() # Call the __init__ method of the parent class
        
        
        
    
        
        
        
        self.city_label = QLabel("Enter City name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.wind_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.forecast_labels = [] 
        self.dark_mode_button = QPushButton("Dark Mode", self)
        self.clear_button = QPushButton("Clear", self)
        
        self.unit_toggle_button = QPushButton("°C/°F", self)
        self.unit_toggle_button.setCheckable(True)
        self.unit_toggle_button.clicked.connect(self.toggle_temperature_unit)
        
        
        
        
        
        
        self.initUI()
        
        
        
        
    #general styling and adding buttons
    def initUI(self):
        self.setWindowTitle("Weather By KF")  # Set the title of the window
        self.setGeometry(100, 100, 400, 200) # Set the size and position of the window
       
        vbox = QVBoxLayout(self)

      
        self.is_celsius = True  # Initialize the temperature unit as Celsius
        

        
    
        
        vbox.addWidget(self.city_label) # Add the city label to the layout
        vbox.addWidget(self.city_input) # Add the city input field to the layout
        vbox.addWidget(self.get_weather_button) # Add the get weather button to the layout
        vbox.addWidget(self.temperature_label) # Add the temperature label to the layout
        vbox.addWidget(self.emoji_label) # Add the emoji label to the layout
        vbox.addWidget(self.description_label) # Add the description label to the layout
        vbox.addWidget(self.wind_label) # Add the wind label to the layout
        vbox.addWidget(self.humidity_label) # Add the humidity label to the layout
        vbox.addWidget(self.dark_mode_button) # Add the dark mode button to the layout
        vbox.addWidget(self.clear_button) # Add the clear button to the layout
        vbox.addWidget(self.unit_toggle_button) # add the unit toggle button to the layout
        vbox.addStretch() # Add a stretch to the layout to make the window resize properly
        self.setLayout(vbox)
         
        
        
        
        
        
        
        self.forecast_layout = QHBoxLayout()
        for _ in range(5):  # Create labels for 5-day forecast
            label = QLabel("", self)
            label.setAlignment(Qt.AlignCenter)
            self.forecast_labels.append(label)
            self.forecast_layout.addWidget(label)
        vbox.addLayout(self.forecast_layout)

        self.setLayout(vbox)
        
        
        self.get_weather_button.clicked.connect(self.get_weather)
        self.dark_mode_button.clicked.connect(self.dark_mode)
        self.clear_button.clicked.connect(self.clear_ui)
        
        
        

        self.setLayout(vbox) # Set the layout of the window to the QVBoxLayout object 
        #set everything to align on center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.wind_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        
        
        #set label for styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.wind_label.setObjectName("wind_label")
        self.humidity_label.setObjectName("humidity_label")
        self.dark_mode_button.setObjectName("dark_mode_button")
        self.clear_button.setObjectName("clear_button")
        self.unit_toggle_button.setObjectName("unit_toggle_button")
         
        
        
        #STYLESHEEET
        self.setStyleSheet("""
            QWidget {
            background-color: #1E1E2F;
            color: #EAEAEA;
            font-family: 'Segoe UI', sans-serif;
            
            }
            QLabel, QPushButton {
            font-family: 'Segoe UI', sans-serif;
            font-weight: 500;
            }
            QPushButton {
            background-color: #0078D7;
            border: none;
            border-radius: 8px;
            color: #FFFFFF;
            padding: 12px 24px;
            font-size: 18px;
            }
            QPushButton#clear_button {
                background-color: #FF0000;
                }
            QPushButton#clear_button:pressed {
                background-color: #630a07;
            }
           
            
            QPushButton:hover {
            background-color: #005A9E;
            }
            QPushButton:pressed {
            background-color: #004578;
            }
            QPushButton#unit_toggle_button {
                background-color: #FFD700;
                border: none;
                border-radius: 8px;
                color: #FFFFFF;
                padding: 12px 24px;
                font-size: 18px;
                
                
                 
                
            }
            QLabel#city_label {
            font-size: 36px;
            font-style: italic;
            margin-bottom: 10px;
            }
            QLineEdit#city_input {
            font-size: 24px;
            padding: 8px;
            border: 2px solid #0078D7;
            border-radius: 5px;
            background-color: #2E2E3E;
            color: #EAEAEA;
            }
            QLineEdit#city_input:focus {
            border-color: #005A9E;
            outline: none;
            }
            QPushButton#get_weather_button {
            font-size: 24px;
            font-weight: bold;
            margin-top: 15px;
            }
            QLabel#temperature_label {
            font-size: 72px;
            font-weight: bold;
            margin-top: 20px;
            }
            QLabel#emoji_label {
            font-size: 96px;
            font-family: 'Segoe UI Emoji', sans-serif;
            margin-top: 10px;
            }
            QLabel#description_label {
            font-size: 32px;
            font-style: italic;
            margin-top: 10px;
            }
        """)
        
        
        
     
   
    def toggle_temperature_unit(self):
            # Toggle the temperature unit between Celsius and Fahrenheit
            self.is_celsius = not self.is_celsius
            if self.temperature_label.text():
                current_temp = float(''.join(filter(str.isdigit, self.temperature_label.text().split('°')[0])))
                if self.is_celsius:
                    converted_temp = (current_temp - 32) * 5 / 9
                    self.temperature_label.setText(f"{converted_temp:.0f}°C")
                else:
                    converted_temp = (current_temp * 9 / 5) + 32
                    self.temperature_label.setText(f"{converted_temp:.0f}°F")
            # Removed resetting self.is_celsius to True to allow proper toggling
     
     
    def clear_ui(self):
            # Clear the input field and reset all labels
            self.city_input.clear()
            self.temperature_label.clear()
            self.emoji_label.clear()
            self.description_label.clear()
            self.wind_label.clear()
            self.humidity_label.clear()
            for label in self.forecast_labels:
                label.clear()
     
     
        
        
        
    def get_weather(self):
        
        api_key = "7944e3736298da61602a82f31e468991" # replace with your api key
        city = self.city_input.text().strip()
        
        if not city: 
            city = self.get_user_location()
            if not city:
                self.display_error("Could not detect location")
                return        
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            forecast_response = requests.get(forecast_url)
            response.raise_for_status()
            forecast_response.raise_for_status()
            
            data = response.json()
            forecast_data = forecast_response.json()
            
            if data["cod"] == 200 and forecast_data["cod"] == "200":
                self.display_weather(data)
                self.display_forecast(forecast_data)
                
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 404:
                    self.display_error("City not found")
                case 401:
                    self.display_error("Invalid API key")
                case 403:
                    self.display_error("API request limit exceeded")
                case 405:
                    self.display_error("Invalid request method")
                case 500:
                    self.display_error("Internal Server Error")
                case 502:
                    self.display_error("Bad Gateway")
                case 503:
                    self.display_error("Service Unavailable")
                case 504:
                    self.display_error("Gateway Timeout")
                case _:
                    self.display_error(f"HTTP ERROR OCCURRED\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\n Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\n Check your internet connection.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects Error:\n Check your internet connection.")
        except requests.exceptions.RequestException:
            self.display_error("Something went wrong.\n Check your internet connection.")
            
            
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px;") 
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.wind_label.clear()
        self.humidity_label.clear()
        for label in self.forecast_labels:
            label.clear()
        
        
    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;") 
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        
        
        
        
        self.temperature_label.setText(f"{temperature_c:.0f}­°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
        self.wind_label.setText(f"💨 Wind Speed: {wind_speed} m/s")
        self.humidity_label.setText(f"💧 Humidity: {humidity}%")
        
    
       
   
        
        
        
        
        
    def display_forecast(self, data):
        forecast_list = data["list"]
        daily_forecast = {}
        
        for entry in forecast_list:
            date = entry["dt_txt"].split()[0]  # Extract the date
            if date not in daily_forecast:
                daily_forecast[date] = entry  # Store the first entry of each day
            if len(daily_forecast) == 5:
                break
        
        for i, (date, info) in enumerate(daily_forecast.items()):
            temp = info["main"]["temp"]
            weather_id = info["weather"][0]["id"]
            emoji = self.get_weather_emoji(weather_id)
            self.forecast_labels[i].setText(f"{date}\n{temp:.1f}°C {emoji}")
      
    
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌪"
        elif weather_id == 781:
            return "🌪️"
        elif 800 == weather_id:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return " "
        
        
        
    def dark_mode(self):
        # Toggle dark mode styling
        current_style = self.styleSheet()
        if "background-color: #1E1E2F;" in current_style:
            self.setStyleSheet("""
                QWidget {
                background-color: #FFFFFF;
                color: #000000;
                font-family: 'Segoe UI', sans-serif;
                }
                QLabel, QPushButton {
                font-family: 'Segoe UI', sans-serif;
                font-weight: 500;
                }
                QPushButton {
                background-color: #0078D7;
                border: none;
                border-radius: 8px;
                color: #FFFFFF;
                padding: 12px 24px;
                font-size: 18px;
                }
                QPushButton#clear_button {
                    background-color: #FFC107;
                }
                QPushButton#clear_button:pressed {
                    background-color: #FF9800;
                }
                QPushButton:hover {
                background-color: #005A9E;
                }
                QPushButton:pressed {
                background-color: #004578;
                }
                QLabel#city_label {
                font-size: 36px;
                font-style: italic;
                margin-bottom: 10px;
                }
                QLineEdit#city_input {
                font-size: 24px;
                padding: 8px;
                border: 2px solid #0078D7;
                border-radius: 5px;
                background-color: #F0F0F0;
                color: #000000;
                }
                QLineEdit#city_input:focus {
                border-color: #005A9E;
                outline: none;
                }
                QPushButton#get_weather_button {
                font-size: 24px;
                font-weight: bold;
                margin-top: 15px;
                }
                QLabel#temperature_label {
                font-size: 72px;
                font-weight: bold;
                margin-top: 20px;
                }
                QLabel#emoji_label {
                font-size: 96px;
                font-family: 'Segoe UI Emoji', sans-serif;
                margin-top: 10px;
                }
                QLabel#description_label {
                font-size: 32px;
                font-style: italic;
                margin-top: 10px;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                background-color: #1E1E2F;
                color: #EAEAEA;
                font-family: 'Segoe UI', sans-serif;
                }
                QLabel, QPushButton {
                font-family: 'Segoe UI', sans-serif;
                font-weight: 500;
                }
                QPushButton {
                background-color: #0078D7;
                border: none;
                border-radius: 8px;
                color: #FFFFFF;
                padding: 12px 24px;
                font-size: 18px;
                }
                QPushButton:hover {
                background-color: #005A9E;
                }
                QPushButton:pressed {
                background-color: #004578;
                }
                QLabel#city_label {
                font-size: 36px;
                font-style: italic;
                margin-bottom: 10px;
                }
                QLineEdit#city_input {
                font-size: 24px;
                padding: 8px;
                border: 2px solid #0078D7;
                border-radius: 5px;
                background-color: #2E2E3E;
                color: #EAEAEA;
                }
                QLineEdit#city_input:focus {
                border-color: #005A9E;
                outline: none;
                }
                QPushButton#get_weather_button {
                font-size: 24px;
                font-weight: bold;
                margin-top: 15px;
                }
                QLabel#temperature_label {
                font-size: 72px;
                font-weight: bold;
                margin-top: 20px;
                }
                QLabel#emoji_label {
                font-size: 96px;
                font-family: 'Segoe UI Emoji', sans-serif;
                margin-top: 10px;
                }
                QLabel#description_label {
                font-size: 32px;
                font-style: italic;
                margin-top: 10px;
                }
            """)
    def get_user_location(self):
        # Detect user city based on IP address.
        try:
            response = requests.get("https://ipinfo.io/json")
            data = response.json()
            return data.get("city", None)
        except requests.exceptions.RequestException:
            return None
        
        
            
              
if __name__ == "__main__": # Check if the __name__ variable is equal to __main__
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())