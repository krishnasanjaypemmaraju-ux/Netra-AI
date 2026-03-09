import google.generativeai as genai
import json
import PIL.Image

# ⬇️ CHANGE 1 — Paste your Gemini API key here
genai.configure(api_key="AIzaSyBw1fkYYLryAu5wbQuehXe8GD-Y6GIuAvY")
model = genai.GenerativeModel('gemini-1.5-flash')

def analyze_frame():
    try:
        image = PIL.Image.open("current_frame.jpg")
        
        prompt = """
You are NETRA AI — a crime detection system.
Analyze this image and detect any of these crimes:

THEFT — person hiding item, avoiding billing, rushing to exit
ASSAULT — punching, kicking, violent attack
HARASSMENT — woman being grabbed, cornered, followed forcefully
RAPE_ATTEMPT — woman being dragged, pinned, forcefully held
MURDER_ATTEMPT — weapon being used, choking, stabbing
KIDNAPPING — person being dragged or forced into vehicle
WEAPON — knife or gun visible and threatening
CHILD_DANGER — child being grabbed by unknown adult
DISTRESS — person collapsed, unconscious, calling for help
STALKING — person being followed repeatedly

RULES:
- Friends together = NOT a crime
- Normal shopping = NOT theft
- Couples = NOT harassment
- For RAPE, MURDER, KIDNAPPING alert at 60% confidence
- For WEAPON, CHILD_DANGER alert at 50% confidence
- For others alert at 75% confidence

Reply ONLY in this JSON format, nothing else:
{
    "threat_detected": true or false,
    "crime_category": "THEFT/ASSAULT/HARASSMENT/RAPE_ATTEMPT/MURDER_ATTEMPT/KIDNAPPING/WEAPON/CHILD_DANGER/DISTRESS/STALKING/NONE",
    "severity": "LOW/MEDIUM/HIGH/CRITICAL",
    "confidence": 0 to 100,
    "description": "one sentence of what is happening",
    "victims": "description of victim or empty string",
    "suspects": "description of suspect or empty string"
}
"""
        
        response = model.generate_content([prompt, image])
        text = response.text.strip()
        text = text.replace("```json","").replace("```","").strip()
        result = json.loads(text)
        
        print(f"🧠 Gemini: {result['crime_category']} | Confidence: {result['confidence']}%")
        return result
        
    except Exception as e:
        print(f"Detection error: {e}")
        return {
            "threat_detected": False,
            "crime_category": "NONE",
            "severity": "LOW",
            "confidence": 0,
            "description": "",
            "victims": "",
            "suspects": ""
        }