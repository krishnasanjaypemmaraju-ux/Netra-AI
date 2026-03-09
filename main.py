from camera import get_frame
from detector import analyze_frame
from alerter import send_alert
import time, json, datetime

print("=" * 50)
print("👁️  NETRA AI — CRIME DETECTION ACTIVE")
print("    नेत्र — The Eye That Never Sleeps")
print("=" * 50 + "\n")

alerts = []
last_alert_time = 0

THRESHOLD = {
    "THEFT": 75, "ASSAULT": 75,
    "HARASSMENT": 75, "RAPE_ATTEMPT": 60,
    "MURDER_ATTEMPT": 60, "KIDNAPPING": 60,
    "WEAPON": 50, "CHILD_DANGER": 50,
    "DISTRESS": 70, "STALKING": 75
}

COOLDOWN = {
    "CRITICAL": 0,
    "HIGH": 15,
    "MEDIUM": 30,
    "LOW": 60
}

while True:
    try:
        print(f"\n⏱️  Scanning... "
              f"{datetime.datetime.now().strftime('%H:%M:%S')}")

        # Step 1 — Take photo
        frame, _ = get_frame()
        if frame is None:
            time.sleep(2)
            continue

        # Step 2 — Send to Gemini AI
        result = analyze_frame()

        # Step 3 — Check threat
        if result["threat_detected"]:
            crime = result["crime_category"]
            severity = result["severity"]
            confidence = result["confidence"]
            threshold = THRESHOLD.get(crime, 75)
            cooldown = COOLDOWN.get(severity, 30)
            current_time = time.time()

            if (confidence >= threshold and
                    current_time - last_alert_time >= cooldown):

                timestamp = datetime.datetime.now().strftime(
                    "%H:%M:%S"
                )

                icon = "🆘" if severity == "CRITICAL" else "🚨"
                print(f"\n{icon} {severity} — {crime}")
                print(f"   {result['description']}")
                print(f"   Confidence: {confidence}%")

                # Step 4 — Send WhatsApp
                send_alert(
                    crime_category=crime,
                    severity=severity,
                    description=result["description"],
                    confidence=confidence,
                    victims=result.get("victims",""),
                    suspects=result.get("suspects","")
                )

                # Step 5 — Save to log
                alerts.append({
                    "time": timestamp,
                    "crime": crime,
                    "severity": severity,
                    "description": result["description"],
                    "confidence": confidence,
                    "victims": result.get("victims",""),
                    "suspects": result.get("suspects","")
                })
                with open("alerts.json","w") as f:
                    json.dump(alerts, f)

                last_alert_time = current_time

        else:
            print("✅ All clear")

        time.sleep(2)

    except KeyboardInterrupt:
        print("\n👁️  NETRA AI stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(2)