from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os
from modules.getTranscript import get_transcript

def summarize_video(youtube_url):
    load_dotenv()
    api_key = os.getenv('MISTRAL_API_KEY')
    model = "mistral-large-latest"
    client = MistralClient(api_key=api_key)

    init_prompt = (
        "You are an AI assistant helping students to summarize educational videos. "
        "You are fed the transcript of the video and you should provide a summary of the video, "
        "as if a student was taking down the notes. You will reveal the key points of the video in a concise manner, "
        "backing each point with evidence if possible. You should also provide actionable steps that the student can take. "
        "Here is the transcript: "
    )

    transcript = str(get_transcript(youtube_url))
    print("Summarizing...")
    
    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=init_prompt + transcript)]
    )

    return chat_response.choices[0].message.content