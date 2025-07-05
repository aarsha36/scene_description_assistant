# 🎯 Scene Description and Navigation Assistant for the Visually Impaired

This project is a real-time assistant for the visually impaired, capable of detecting objects, describing scenes, and optionally speaking them aloud using text-to-speech. Built using **YOLOv8**, **BLIP** (Bootstrapped Language Image Pretraining), and **Python**, it runs entirely on local hardware using a webcam.

## 📽️ Demo Video

▶️ Watch it in action here: https://drive.google.com/drive/folders/1V5nQmyKNc8ZrlDdZQXrghpXVdTBuEH7s?usp=sharing

---

## 📂 File Structure

├── main.py # Entry point script
├── object_detection.py # Handles YOLOv8-based object detection
├── scene_caption.py # Uses BLIP to generate image captions
├── text_to_speech.py # Converts text output to speech (optional)
├── requirements.txt # Python dependencies
└── README.md


---

## 🔧 Installation

# 1. Clone the repository

bash
git clone https://github.com/your-username/scene-assistant.git
cd scene-assistant

2. Create and activate a virtual environment (recommended)

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

---

##Usage
Run the project:
python main.py
This will open your webcam, detect objects, generate a scene caption, and speak the result (if TTS is enabled).

---

##Components
🔍 object_detection.py
Uses YOLOv8 for real-time object detection.
Returns bounding boxes and detected labels.

🖼️ scene_caption.py
Loads a BLIP model from Hugging Face.
Generates a descriptive caption for the image or webcam frame.

🔊 text_to_speech.py
Converts captions or object descriptions into speech using pyttsx3.

🧩 main.py
Integrates all components into a working pipeline.

---

##Sample Output
Detected Objects: person, cup, keyboard
Caption: "A person sitting at a desk with a keyboard and a cup."
Speech: The caption is read aloud automatically.

---

##Future Work
Add voice command support
Export logs of detected scenes
Deploy on Raspberry Pi or Jetson Nano
Create a mobile/web interface with Streamlit

---

##Credits
Ultralytics YOLOv8
Salesforce BLIP via Hugging Face
OpenCV
pyttsx3 TTS

---

##License
This project is licensed under the MIT License.

---

##Author
Aarsha
