---

# Twitter Sheet Poster with Gemini AI Integration

This project integrates Google Gemini AI to generate tweets and posts them to Twitter using the **Tweepy** library. It pulls data from a Google Sheet and automates tweet generation and posting with AI-generated content.

---

## 🚀 **Features**

- Generate tweet content using **Google Gemini AI** (`gemini-1.5-flash`).
- Fetch data from a Google Sheet to prepare multiple tweets.
- Automatically post tweets to Twitter using the **Tweepy** API client.
- REST API endpoint using **Flask** for easy integration.

---

## 🛠️ **Technologies Used**

- **Python 3.x**
- [Flask](https://flask.palletsprojects.com/) - For creating REST APIs.
- [Tweepy](https://docs.tweepy.org/) - For interfacing with the Twitter API.
- [Google Generative AI](https://developers.generativeai.google.com/) - For generating AI-generated tweet content.
- [Pandas](https://pandas.pydata.org/) - For processing and reading Google Sheet data.
- [Flask-Cors](https://flask-cors.readthedocs.io/) - Cross-Origin requests support for REST API.
- **Google Sheets integration via URL-based CSV fetch**

---

## 📜 **How It Works**

1. **API Endpoint**:
   - The Flask server has an endpoint `/post_tweet`.
   - Input your Twitter credentials, Google Sheet ID, and sheet name into a POST request payload.

2. **Tweet Generation with AI**:
   - The AI model generates tweet drafts based on data in the Google Sheet.
   - These drafts are then posted using the Twitter API.

3. **Google Sheet Integration**:
   - The application fetches tweets and hashtags from the provided Google Sheet URL.

4. **Error Handling**:
   - Includes exception handling for authentication and rate-limiting errors.

---

## 💻 **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/SairajRajput12/X_API_Google_Sheet.git
cd X_API_Google_Sheet
```

---

### 2. Set Up the Environment
Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure your `.env` file is created and contains these keys:

```
consumer_key=your_twitter_consumer_key
consumer_secret=your_twitter_consumer_secret
access_token=your_twitter_access_token
access_token_secret=your_twitter_access_token_secret
GEMINI_API_KEY=your_gemini_api_key
```

---

### 3. Start the Flask Server
Run the Flask application:

```bash
python app.py
```

The server will start at [http://localhost:5000](http://localhost:5000).

---

### 4. Send a POST Request
Use Postman, CURL, or any HTTP client to send a POST request to:

```
POST http://localhost:5000/post_tweet
```

With payload:

```json
{
  "consumer_key": "your_consumer_key",
  "consumer_secret": "your_consumer_secret",
  "access_token": "your_access_token",
  "access_token_secret": "your_access_token_secret",
  "sheet_name": "Tweeter data",
  "sheet_id": "your_google_sheet_id"
}
```

---

## 🛠️ **Technologies and Libraries**

### 1. Flask
REST API creation for tweet handling.

### 2. Tweepy
Handles communication with Twitter's API to post tweets.

### 3. Google Generative AI
Generates tweet drafts via AI model `gemini-1.5-flash`.

### 4. Pandas
Processes Google Sheet data for tweet generation.

---

## 🎯 **Error Handling**

- Handles authorization errors when posting tweets (`401 Unauthorized`).
- Handles rate-limiting issues (`429 Too Many Requests`) with retry logic.
- Checks for permission errors before posting.

---

## 📁 **Project Structure**

```
├── .env                     # Environment variables for credentials
├── app.py                   # Flask application handling the REST endpoint
├── fetch_sheet_data.py      # Handles Google Sheets reading logic
├── gemini.py                # Interface for Google Gemini
├── requirements.txt         # List of dependencies
├── MicrosoftWebDriver.exe  # WebDriver for browser compatibility
├── test.py                  # Test file (Optional testing code)
├── Tweeter.csv              # Input CSV with Google Sheet data
└── README.md                # Documentation
```

---

## 🧰 **Dependencies**

To install dependencies, run:

```bash
pip install flask flask-cors tweepy google-generativeai pandas python-dotenv
```

---

## 🤝 **Contributing**

If you'd like to contribute to this project:

1. Fork this repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature/<feature-name>
   ```
3. Make your changes.
4. Open a Pull Request.

---

## 📜 **License**

This project is licensed under the MIT License. You are free to use, distribute, and modify this code.

---

## 📧 **Contact**

Sairaj Rajput  
GitHub: [https://github.com/SairajRajput12](https://github.com/SairajRajput12)  
Email: [sairajrajput6@gmail.com]

---

