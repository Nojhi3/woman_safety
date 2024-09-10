# Safe Route Finder

**Safe Route Finder** is a web application designed to enhance women's safety by providing optimized travel routes that avoid areas with higher crime rates. Using Google Maps API and Dijkstra's algorithm, the app identifies the safest and shortest paths for users.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

Safe Route Finder aims to address the safety concerns of women by helping them navigate urban areas with increased confidence. The application leverages real-time crime data and advanced algorithms to avoid routes that pass through potentially dangerous areas, ensuring a safer journey.

---

## Features

- **Safe Route Calculation**: Avoids roads with higher crime rates.
- **Shortest Path Optimization**: Utilizes Dijkstra's algorithm to find the shortest and safest path.
- **Google Maps Integration**: Seamless integration with Google Maps for accurate and up-to-date routing.
- **User-Friendly Interface**: Intuitive UI for easy navigation and route selection.
- **Real-Time Updates**: Provides real-time crime rate updates to ensure safety.

---

## Installation

### Prerequisites

- Python 3.10
- Django 5.1.1
- Google Maps API key

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/saferoutefinder.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd woman_safety/safe_route
   ```

3. **Set up the Google Maps API key**:
   - Add your API key to the environment variables or directly in the Django settings file.

4. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the app**:
   - Open your browser and go to `http://127.0.0.1:8000/`.

---

## Usage

1. Enter your starting point and destination in the input fields.
2. The app will calculate the safest route based on real-time crime data and display it on the map.
3. Follow the suggested route for a safer journey.

---

## Technologies Used

- **Django**: Backend framework for building the web application.
- **Google Maps API**: For mapping and routing functionalities.
- **Dijkstra's Algorithm**: For finding the shortest and safest path.
- **JavaScript**: For front-end interactivity and map rendering.
- **HTML/CSS**: For structuring and styling the web pages.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
