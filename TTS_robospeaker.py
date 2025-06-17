import os
if __name__=="__main__":

    print("Welcome to the robospeaker created by Sameer")
    while(True):
        s=input("Enter what you want me to speak :\n ")
        if(s=="q"):
             break
        command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{s}');"
        os.system(command)