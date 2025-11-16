import asyncio
import edge_tts

async def TextToSpeech(text):
    """
    Converts text to speech using Edge TTS and plays it.
    """
    voice = "en-US-AriaNeural"  # You can change this to other voices
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("Data/speech.mp3")

    # Play the audio file
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("Data/speech.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

def speak(text):
    """
    Synchronous wrapper for TextToSpeech.
    """
    asyncio.run(TextToSpeech(text))
