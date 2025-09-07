import unittest
from PyQt5.QtWidgets import QApplication
from main import WeatherApp

class TestDarkMode(unittest.TestCase):
    def setUp(self):
        # Create a QApplication instance (required for PyQt5 widgets)
        self.app = QApplication([])
        self.weather_app = WeatherApp()

    def test_dark_mode_toggle_to_light(self):
        # Initially set to dark mode
        self.weather_app.setStyleSheet("background-color: #1E1E2F;")
        self.weather_app.dark_mode()
        # Check if the stylesheet has been updated to light mode
        self.assertIn("background-color: #FFFFFF;", self.weather_app.styleSheet())

    def test_dark_mode_toggle_to_dark(self):
        # Initially set to light mode
        self.weather_app.setStyleSheet("background-color: #FFFFFF;")
        self.weather_app.dark_mode()
        # Check if the stylesheet has been updated to dark mode
        self.assertIn("background-color: #1E1E2F;", self.weather_app.styleSheet())

    def tearDown(self):
        # Clean up the QApplication instance
        self.app.quit()

if __name__ == "__main__":
    unittest.main()