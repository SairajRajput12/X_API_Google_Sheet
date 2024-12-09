from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from flask_cors import CORS
import google.generativeai as genai
import tweepy
from urllib.parse import quote
import pandas as pd
import time

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/post_tweet": {"origins": "*"}})

@app.route('/')
def show_credentials():
    """Root endpoint providing basic information about the API."""
    return jsonify({"message": "This API takes a sheet name and access tokens and posts all the tweets from the sheet!"})

@app.route('/post_tweet', methods=['POST'])
def post_tweets():
    try:
        # Extract data from the POST request
        data = request.json
        consumer_key = data.get("consumer_key")
        consumer_secret = data.get("consumer_secret")
        access_token = data.get("access_token")
        access_token_secret = data.get("access_token_secret")
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        sheet_name = data.get("sheet_name")
        sheet_id = data.get("sheet_id")
        
        # Initialize Gemini and Tweepy clients
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        
        # Fetch Google Sheet data
        encoded_sheet_name = quote(sheet_name)
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_sheet_name}"
        sheet_data = pd.read_csv(url)
        
        for ind, row in sheet_data.iterrows():
            tweet_content = row['Tweet']
            hashtag = row['Hashtag']
            print(f"Preparing tweet: {tweet_content} with hashtag: {hashtag}")
            
            try:
                # Generate tweet using Gemini
                response = model.generate_content(
                    f"Generate a tweet from this text: '{tweet_content}' and this hashtag: '{hashtag}'"
                )
                final_response = response.text.strip()
                print(f"Generated tweet: {final_response}")
                
                # Post the tweet using Tweepy
                client.create_tweet(text=final_response)
                print("Tweet posted successfully!")
                
                # Wait to avoid hitting rate limits
                time.sleep(5)
            except Exception as e:
                print(f"Error occurred while posting tweet: {e}")
                continue
        
        return jsonify({"message": "Tweets posted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
