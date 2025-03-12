from gtts import gTTS

# Texto a ser convertido em áudio
texto = "Olá Daniel, bem-vindo ao tutorial do Google Text-to-Speech!"

# Define o idioma (pt para português)
lingua = "pt"

tts = gTTS(text=texto, lang=lingua, slow=False)

tts.save("audio.mp3")
print("Áudio salvo como 'audio.mp3'")