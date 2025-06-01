# KIRA-AI
"Voice AI Assistant using LLM and Python"
# 🧠 KIRA – Personal Voice AI Assistant

KIRA is a sleek, offline-capable voice-based AI assistant powered by **LLaMA 3** and Python. Designed to operate with calm precision, KIRA listens, responds, and adapts to your voice commands — all while looking sharp in your DIY wearable gear.

---

## 🎯 Features

- 🎙️ **Voice Activation**: Interact using natural speech via microphone
- 🧠 **Local AI (LLaMA 3)**: No need for the internet — runs entirely on your system
- 🤖 **Personality**: Calm, emotionless, and focused — like a true sci-fi assistant
- 🎚️ **Volume Control**: “Kira, increase/decrease volume”
- 🎭 **Voice Modes**: 
  - Cold/Emotionless Mode
  - Expressive Mode
  - Whisper Mode (low volume + speed)
- 🎵 **Custom Sound Effects** *(optional)*: Add beeps or start tones
- ❌ **No Wake Word Needed**: Continuous voice interaction
- ⚙️ **Fully Customizable & Open Source**

---

## 🚀 How It Works

1. Uses `speech_recognition` to take your voice input.
2. Sends your query to **LLaMA 3 (via Ollama)**.
3. Converts LLaMA’s reply into voice using `pyttsx3`.
4. Listens again — no restart or reactivation needed.

---

## 🛠️ Requirements

- Python 3.9+
- [Ollama](https://ollama.com) with `llama3` model installed
- `pyttsx3`, `speech_recognition`, `pyaudio` (install via pip)
- Microphone and speaker/headset

---

## 📦 Installation

```bash
git clone https://github.com/Aryan-Kumar-sama/KIRA-AI.git
cd KIRA-AI
pip install -r requirements.txt
python kira.py
