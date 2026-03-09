from twilio.rest import Client
import datetime

# Keys directly here — no .env needed
ACCOUNT_SID = ""
AUTH_TOKEN  = ""
FROM_NUMBER = ""
YOUR_NUMBER = ""

CRIME_EMOJI = {
    "THEFT":          "🦹",
    "ASSAULT":        "👊",
    "HARASSMENT":     "⚠️",
    "RAPE_ATTEMPT":   "🆘",
    "MURDER_ATTEMPT": "🔪",
    "KIDNAPPING":     "🚨",
    "WEAPON":         "🔫",
    "CHILD_DANGER":   "👶",
    "DISTRESS":       "😱",
    "STALKING":       "👁️"
}

def send_alert(crime_category, severity,
               description, confidence,
               victims="", suspects=""):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        time_now = datetime.datetime.now().strftime("%I:%M:%S %p")
        emoji = CRIME_EMOJI.get(crime_category, "🚨")
        crime_name = crime_category.replace("_", " ")

        if severity == "CRITICAL":
            header = "🆘🆘🆘 CRITICAL EMERGENCY 🆘🆘🆘"
            footer = "🚔 DISPATCH POLICE IMMEDIATELY"
        elif severity == "HIGH":
            header = "🚨🚨 URGENT ALERT 🚨🚨"
            footer = "⚠️ Police response required now"
        else:
            header = "⚠️ NETRA AI ALERT"
            footer = "Police response required"

        message = f"""
{header}

{emoji} Crime     : {crime_name}
🔴 Severity  : {severity}
🕐 Time      : {time_now}
📍 Location  : Main Camera
📊 Confidence: {confidence}%

📋 What Happened:
{description}
"""
        if victims:
            message += f"\n👤 Victim  : {victims}"
        if suspects:
            message += f"\n🕵️ Suspect : {suspects}"

        message += f"\n\n{footer}"
        message += "\n\n👁️ NETRA AI — The Eye That Never Sleeps"

        client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=YOUR_NUMBER
        )
        print(f"✅ WhatsApp alert sent — {crime_name}")

    except Exception as e:
        print(f"❌ Alert failed: {e}")

def test_alert():
    print("Sending test message to your phone...")
    send_alert(
        crime_category="THEFT",
        severity="MEDIUM",
        description="This is a test. NETRA AI is working correctly.",
        confidence=100
    )

if __name__ == "__main__":
    test_alert()