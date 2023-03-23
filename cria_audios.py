from gtts import gTTS ## Para criar os audios
from subprocess import call ## Para executar o comando de reprodução no mac e linux
#from playsound import playsound ## Para executar o comando de reprodução no windows

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br') ## Cria o audio
    tts.save('audios/'+ audio + '.mp3') ## Salva o audio

    call(["afplay", "audios/" +audio+ ".mp3"]) ## Executa o comando de reprodução no mac
    #call(["aplay", "audios/oi.mp3"]) ## Executa o comando de reprodução no linux
    #call(["cmdmp3", "audios/oi.mp3"]) ## Executa o comando de reprodução no windows
    #playsound('audios/oi.mp3') ## Executa o comando de reprodução no windows

cria_audio('Olá! Tudo bem?') # Chama a função
cria_audio('Bem vindo') # Chama a função

