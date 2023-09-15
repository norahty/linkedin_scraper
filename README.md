# linkedin_scraper
This is a linkedin_scraper webstie that scrapes the public information from linkedin.com when the user provides a url
# LinkedIn Scraping Project Readme

This project is a LinkedIn web scraping application designed to extract information from LinkedIn profiles. It utilizes Python, Selenium, BeautifulSoup, and Flask to achieve its functionality. Below, you'll find information on how to use the project, its structure, and important considerations.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Web Scraping Process](#web-scraping-process)
- [Web Interface](#web-interface)
- [Styling](#styling)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project consists of the following main components:

1. `main.py`: This Python script contains the core web scraping functionality. It logs in to LinkedIn using credentials from a `login.txt` file, scrapes profile information, including name, title, location, about section, experiences, education, and recommendations, and stores the data in a JSON file (`profile.json`).

2. `app.py`: This script is the entry point for the Flask web application. It provides a web interface for users to input LinkedIn profile URLs and initiate the scraping process.

3. `templates` folder: Contains HTML templates used for rendering the web interface.

4. `static` folder: Contains CSS styles for the web interface.

## Prerequisites

Before using this project, make sure you have the following prerequisites installed:

- Python 3.x
- Selenium (`pip install selenium`)
- BeautifulSoup (`pip install beautifulsoup4`)
- Flask (`pip install Flask`)
- Chrome WebDriver: You need to have the Chrome WebDriver installed and its path set in your system. Download it from [Chrome WebDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and make sure it's available in your system's PATH.

## Usage

Follow these steps to use the LinkedIn scraping project:

1. Clone or download this project to your local machine.

2. Install the required Python packages mentioned in the [Prerequisites](#prerequisites) section.

3. Set up your LinkedIn login credentials by creating a `login.txt` file in the project directory. Add your LinkedIn email address on the first line and your password on the second line.

4. Run the Flask web application using the following command:

   ```
   python main.py
   ```

5. Access the web interface by opening a web browser and navigating to `http://127.0.0.1:5000/`.

6. Enter the LinkedIn profile URL you want to scrape, and click the "Extract" button.

7. Wait for the scraping process to complete. The extracted profile data will be displayed on the web interface and saved to `profile.json` in the project directory.

## Web Scraping Process

The web scraping process in this project includes the following steps:

1. Logging into LinkedIn using the provided credentials.

2. Accessing the LinkedIn profile provided by the user.

3. Extracting various profile details, including name, title, location, about section, experiences, education, and recommendations.

4. Saving the extracted data to a JSON file (`profile.json`).

Please note that web scraping LinkedIn may violate LinkedIn's terms of service, and it's essential to use this tool responsibly and in compliance with LinkedIn's policies. Ensure that you have the necessary permissions to access and scrape LinkedIn profiles.

## Web Interface

The project includes a web interface powered by Flask, which allows users to input LinkedIn profile URLs and initiate the scraping process. The web interface provides feedback on the scraping progress and displays the extracted data.

## Styling

The styling for the web interface is defined in the `static` folder within the project. You can modify the CSS styles in the `style.css` file to customize the appearance of the web interface to your liking.

## Contributing

If you'd like to contribute to this project, feel free to open issues or submit pull requests on the project's GitHub repository.

## To Run:
input the url you want to scrape from:
<img width="1429" alt="Screen Shot 2023-03-12 at 11 13 05 AM" src="https://user-images.githubusercontent.com/94091909/224553903-5592c268-ca9b-45e1-bb6d-4a610d2e631b.png">

The result will be displayed on the output page
<img width="1429" alt="Screen Shot 2023-03-12 at 12 52 15 PM" src="https://user-images.githubusercontent.com/94091909/224559746-2d396e41-5aaa-40c2-9078-4539013f4102.png">
