# 🔗 Elite-Short

Welcome to Elite-Short, a powerful URL shortening service built with Django. This application not only shortens URLs but also provides detailed analytics on clicks by country and device type.

Hosted at: [Elite-Short](http://thimanshusharma.pythonanywhere.com/)

## 🚀 Features

- **URL Shortening**: Convert long URLs into short, easy-to-share links.
- **Analytics**: Track clicks by country and device type.
- **Custom Short URLs**: Create custom short URLs.
- **Click Tracking**: Monitor the number of clicks for each short URL.
- **Date Tracking**: Automatically records the creation date of each short URL.

## 🛠️ Technologies Used

- **Django**: The web framework for perfectionists with deadlines.
- **SQLite**: Lightweight database for development.
- **HTML5 & CSS3**: Structuring and styling the web pages.
- **JavaScript**: Adding interactivity to the application.
- **ipinfo.io**: API for fetching geolocation data.

## 🗄️ Models

### `LongToShort`

| Field          | Type           | Description                                         |
|----------------|----------------|-----------------------------------------------------|
| `long_url`     | URLField       | The original long URL to be shortened.              |
| `short_url`    | CharField      | The custom or generated short URL.                  |
| `date`         | DateField      | The date the short URL was created (auto-added).    |
| `clicks`       | IntegerField   | The total number of clicks the short URL has received. |
| `country_clicks` | JSONField    | Click count by country in JSON format.              |
| `device_clicks`  | JSONField    | Click count by device type in JSON format.          |

## 🚧 Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/elite-short.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd elite-short
    ```
3. **Install virtualenv**:
    ```bash
    pip install virtualenv
    ```
4. **Create a virtual environment**:
    ```bash
    virtualenv venv
    ```
    - This will create a folder named `venv` in your directory.
5. **Activate the virtual environment**:
    ```bash
    venv\Scripts\activate  # On Windows
    ```
    - After this, you are inside the virtual environment.
7. **Install Django**:
    ```bash
    pip install django
    ```

8. **Change directory to the project folder**:
    ```bash
    cd URL_shortener
    ```
9. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
10. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

Your app will be running at `http://127.0.0.1:8000/`.

## 📝 Usage

### Shorten a URL

1. Go to the home page.
2. Enter the long URL and a custom name for the short URL (optional).
3. Click "Submit" to get your shortened URL.

### View Analytics

- **Individual Analytics**: Append `/analytics/<short_url>` to the base URL to view analytics for a specific short URL.
- **All Analytics**: Visit `/all-analytics` to view analytics for all short URLs.

## 📬 Contact

Feel free to reach out to me at [himanshusharma2002.2000@gmail.com](mailto:himanshusharma2002.2000@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/himanshu-sharma-dev).


Thank you for checking out Elite-Short! If you have any feedback or suggestions, feel free to open an issue or make a pull request.

Happy coding! 😊
