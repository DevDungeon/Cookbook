# Print all available voices
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

# Example usage of voice ids:

# # Voice IDs pulled from engine.getProperty('voices')
# # These will be system specific
# en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

# # Use female English voice
# engine.setProperty('voice', en_voice_id)
# engine.say('Hello with my new voice')

# # Use female Russian voice
# engine.setProperty('voice', ru_voice_id)
# engine.say('Привет. где хакер')

# engine.runAndWait()