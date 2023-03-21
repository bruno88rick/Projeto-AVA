from gtts import gTTS

tts = gTTS(text='Oi, eu sou a Ava', lang='pt-br')
tts.save('audios/oi.mp3')