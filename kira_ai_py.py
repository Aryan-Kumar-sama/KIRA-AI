import subprocess
import speech_recognition as sr
import pyttsx3

# === Setup ===
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if 'english' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Initial voice settings
volume = 1.0  # Range: 0.0 to 1.0
mode = "cold"  # Options: cold / expressive
rate = 150     # Will be adjusted per mode

def speak(text):
    global volume, rate
    if mode == "cold":
        rate = 140
    elif mode == "expressive":
        rate = 170
    engine.setProperty('volume', volume)
    engine.setProperty('rate', rate)
    print(f"🧠 KIRA: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"🗣️ You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition failed.")
        return ""

def ask_ollama(prompt):
    full_prompt = (
        "You are KIRA, an AI assistant with a calm, cold, and precise personality. "
        "Give accurate and emotionless responses to the user's question.\n\n"
        f"User: {prompt}\nKIRA:"
    )
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3', full_prompt],
            capture_output=True,
            text=True,
            timeout=30,
            encoding='utf-8',
            errors='ignore'
        )
        if result.returncode == 0:
            response = result.stdout.strip().split("\n")[-1]
            return response
        else:
            return "Failed to get a response."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    global volume, mode
    speak("KIRA is online. Ask your question.")

    while True:
        query = listen()
        if query == "":
            continue

        if any(stop in query for stop in ["stop", "shutdown", "exit", "bye"]):
            speak("Powering down. Justice never dies.")
            break

        # 🎚️ Volume Control
        if "increase volume" in query or "turn up volume" in query:
            volume = min(volume + 0.2, 1.0)
            speak("Volume increased.")
            continue
        elif "decrease volume" in query or "turn down volume" in query:
            volume = max(volume - 0.2, 0.1)
            speak("Volume decreased.")
            continue

        # 📢 Mode Switching
        if "switch to emotionless mode" in query or "cold mode" in query:
            mode = "cold"
            speak("Emotionless mode activated.")
            continue
        elif "switch to expressive mode" in query or "friendly mode" in query:
            mode = "expressive"
            speak("Expressive mode activated.")
            continue

        # 🗣️ Whisper Mode
        if "whisper mode" in query:
            volume = 0.2
            engine.setProperty('rate', 100)
            speak("Whisper mode engaged.")
            continue
        elif "normal mode" in query:
            volume = 1.0
            engine.setProperty('rate', 140)
            speak("Back to normal mode.")
            continue

        # 🧠 Main KIRA Response (No wake word required anymore)
        response = ask_ollama(query)
        speak(response)

if __name__ == "__main__":
    main()
