# lembrete - instalar SpeechRecognition , pipwin, pyaudio(pelo pipwin)

import speech_recognition as sr

# - criar um "reconhecedor"
rec = sr.Recognizer()

# - ouvir o audio do microfone

# para escolher qual microfone vamos usar, rode:
# print(sr.Microphone().list_microphone_names())


# importante configurar o device_index com o microfone disponvel na lista
with sr.Microphone(device_index=2) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar:")
    
    # coloque isso se quiser que ele demore mais para entender que uma pausa é o fim do audio
    # rec.pause_threshold = 1 

    audio = rec.listen(microfone)
try:
    # reconhece esse audio e traduz ele pra texto
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
except:
    print("Não peguei áudio nenhum")