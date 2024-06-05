import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import time

load_dotenv()

#function detects speech from the microphone and returns the 1)recognized text and 2)duration of recording
def recognize_from_microphone():

    #confiuring speech_config parameter with key, region, and language
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language = "en-US"

    #configuring audio_config with using the default microphone
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    #recognized_text and duration will be returned at the end of this function
    recognized_text = ""
    duration = 0

    #taking a starting time right before recording starts
    start_time = time.time()

    #callback function for generating recognized_text and error handling
    def recognized_cb(evt):
        nonlocal recognized_text
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            recognized_text = evt.result.text
        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(evt.result.no_match_details))
        elif evt.result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = evt.result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    #callback function is called when speech is recognized
    speech_recognizer.recognized.connect(recognized_cb)

    #microphone is continuously listening for speech
    print("Speak into the microphone.")
    speech_recognizer.start_continuous_recognition()

    #function continuously runs until CTRL+C is pressed in terminal, leading to stoppage
    #upon CTRL+C, duration is calculated, and the continuous recognition is stopped
    #a 2 second delay is provided before the stoppage to allow the recognizer to interpret the last few seconds of speech
    try:
        # Keep the script running to listen continuously until interrupted
        while True:
            pass
    except KeyboardInterrupt:
        end_time = time.time()
        print("Stopping recognition...")
        duration = end_time - start_time
        time.sleep(2)
        speech_recognizer.stop_continuous_recognition()
    
    #dictionary with text and duration keys are returned
    return {"text":recognized_text, 
            "duration": duration}
