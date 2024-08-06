from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(yt_url):
    yt_id = yt_url.split('=')[1]
    transcript = YouTubeTranscriptApi.get_transcript(yt_id)
    
    full_text = ' '.join(entry['text'] for entry in transcript)
    print("Got transcript...")
    return full_text