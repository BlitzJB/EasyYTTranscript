from flask import Flask, request
from flask_cors import CORS
from scrape import get_transcript_from_youtube

app = Flask(__name__)
CORS(app)

@app.route('/api/ytTranscript', methods=['POST'])
def yt_transcript():
    url = request.get_json().get("url", False)
    
    if not url:
        return { "success": False, "message": "property `url` required in request body" }
    
    try:
        result = get_transcript_from_youtube(url)
    except ValueError:
        return { "success": False, "message": "`url` is not a valid youtube url" }
    except Exception as e:
        return { "success": False, "message": f"unknown error occoured: {str(e)}" }
    
    return { "success": True, "transcript": result }