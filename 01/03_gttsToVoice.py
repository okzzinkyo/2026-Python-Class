from gtts import gTTS #gtts 라이브러리에서 gTTS클래스를 불러옵니다.

tts = gTTS(text="안녕하세요? 잘 부탁드립니다.", lang="ko")
tts.save("test_2.mp3")