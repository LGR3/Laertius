from gtts import gTTS

# Input text in Portuguese
text_to_audio = "asdasdasd"

# Generate audio in Portuguese
tts = gTTS(text=text_to_audio, lang='pt-br')
tts.save("audio_ptbr.mp3")

print("Arquivo de áudio salvo como audio_ptbr{number}.mp3")