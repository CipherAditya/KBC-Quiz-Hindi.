# INTERACTION BLOCK
from gtts import gTTS
import pygame
import tempfile
import os

# 1. INTRO BLOCK

intro = "तुम्हारा नाम क्या है मेरे दोस्त??"
tmp_file= tempfile.NamedTemporaryFile(delete=False,suffix=".mp3")
file = tmp_file.name
tmp_file.close()
tts1= gTTS(text=intro,lang="hi")
tts1.save(file)
# 2. Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

# 3. Wait until the speech finishes
while pygame.mixer.music.get_busy():
     pygame.time.Clock().tick(10)
pygame.mixer.music.stop()
pygame.mixer.quit()
name = input("Name--->>")

os.remove(file)




# GREETING BLOCK
text = f"नमस्ते, {name} आपका स्वागत है KBC के खेल में! इस गेम में मैं आपसे तीन प्रश्न पूछूंगी, प्रत्येक प्रश्न के लिए आपको 1 अंक मिलेगा। यदि आप उन सभी का सही उत्तर देते हैं तो मैं आपको इनाम दूंगी लेकिन अगर आप एक भी सवाल का सही जवाब देने में विफल रहते हैं तो मेरे पास आपके लिए सजा भी है"
tmp_file2= tempfile.NamedTemporaryFile(delete=False,suffix=".mp3")
file2=tmp_file2.name
tmp_file2.close()
tts2 = gTTS(text=text, lang='hi')
tts2.save(file2) 

# 2. Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load(file2)
pygame.mixer.music.play()

#  3. Wait until the speech finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.mixer.music.stop()
pygame.mixer.quit()
os.remove(file2)

def speak(text):
     temp_file= tempfile.NamedTemporaryFile(delete=False,suffix=".mp3")
     q= temp_file.name
     temp_file.close()
     speech= gTTS(text=text,lang="hi")
     speech.save(q)

     pygame.mixer.init()
     pygame.mixer.music.load(q)
     pygame.mixer.music.play()

    
     while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
     pygame.mixer.music.stop()
     pygame.mixer.quit()
     os.remove(q)

# QUESTION-ANSWER FLOW



     
questions={1:{"ques":"अगर रोबोट डॉक्टर बन जाए तो उसका सबसे पहला इलाज क्या होगा?",
             "opts":["A. Error 404: Patient Not Found",
            "B. System Reeboot Therapy ",
            "C. Reboot Therapy",
            "D. Binary Bandage"],
            "ans":"A"},

            2:{"ques":"कंप्यूटर को बुखार आ जाए तो क्या करना चाहिए?","opts":["A. Antivirus दवाई देना",
            "B. Restart करना",
            "C. CPU को ठंडा करना",
            "D. Debug Injection"],
            "ans":"C"},

            3:{"ques":"अगर इंटरनेट अचानक से गायब हो जाए तो सबसे पहले लोग क्या करेंगे?",
               "opts":[ "A. WiFi राउटर को बार-बार रीस्टार्ट करेंगे",
            "B. अपने पड़ोसी का नेटवर्क चेक करेंगे",
            "C. डेटा पैक रिचार्ज करेंगे",
            "D. भगवान से प्रार्थना करेंगे"],
            "ans":"A"}}

speak(f"{name} आपका पहला प्रश्न है !!")

# 🎙️ Run the quiz
score=0
for qno, qdata in questions.items():
    print(f"\nQ{qno}: {qdata['ques']}")
    speak(qdata['ques'])  # speak the question

    speak("आपके विकल्प हैं")
    print("\n\nOptions:")
    for opt in qdata["opts"]:
        print(opt)
        speak(opt)   
    speak(f"तो {name} आपका उत्तर क्या है ए, बी, सी या डी??")
    answer = input("What is your Answer A/B/C/D-->").strip().upper()
    if answer==qdata["ans"]:
        speak(f"बधाई हो {name}  आपने सही जवाब दिया")
        print("\ncongrats you did great ")
        score+=1
        print(f"\nyour score is{score}")
    else:
        speak(f"नहीं!, {name} आपका जवाब गलत है!")
        print("\nyour answer is wrong buddy")
    if qno < len(questions):
     speak(f"{name} आपके टर्मिनल पर अगला प्रश्न है!!")
speak(f"बहुत बढ़िया {name} | खेल अब ख़त्म हो गया है आपका स्कोर है {score}")
if score == 3:
    speak(f"वाह!{name} क्या शानदार प्रदर्शन किया आपने! सभी सवाल सही जवाब दिए, सच में वाह! अब आपकी इनाम की बारी है… मैग्नम आइसक्रीम! लेकिन हाहा, इसे पाने के लिए खुद ही किसी ग्रोसरी ऐप में जाकर आर्डर करना होगा और भुगतान पेज पर डिस्काउंट कोड में यह लिखना: 'आपसे प्रैंक हो गया, मैं सिर्फ तीन सवालों के लिए कोई मुफ्त आइसक्रीम नहीं दे रही, खुद ही भुगतान करो, और अगर ऑर्डर कर रहे हो तो मेरे लिए भी एक ऑर्डर कर देना!")
    print("\nprank ho gaya😂😂😂🤣🤣🫵🫵🫵")
else:
    speak(f"{name} आप सभी सवालों का जवाब नहीं दे सके इसलिए सजा यह है। आपको मेरे लिए आइसक्रीम ऑर्डर करनी होगी ")



            

