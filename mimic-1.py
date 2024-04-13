import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import google.generativeai as genai

def ai(prompt):

    genai.configure(api_key="AIzaSyC9BBMNK5FeUXCcHpuEMqdiN_iP9IjPJsA")

    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 1024,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        }
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[])

    convo.send_message(prompt)
    print(convo.last.text)
    return convo.last.text

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            query= r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "some error has occurred, sorry from jarvis"
while 1:
    while True:
        speaker.Speak("Hello my name is mimic 1")
        print("listening....")
        text= takecommand()
        #add more sites
        sites= [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],["spotify","https://www.spotify.com"],["chatgpt","https://chat.openai.com/"]]
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                speaker.Speak(f"opening {site[0]}")
                webbrowser.open(site[1])
            elif "the time" in text.lower():
                strftime= datetime.datetime.now().strftime("%H:%M:%S")
                speaker.Speak(f"Sir the time is {strftime}")
            elif "using gemini".lower() in text.lower():
                ai(text)
                speaker.Speak(ai(text))