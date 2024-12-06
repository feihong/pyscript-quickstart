import random
from js import SpeechSynthesisUtterance
from pyscript import when, window, document, web


speech = window.speechSynthesis

title = document.querySelector('main h1')
title.innerText = '你好世界！'

textarea = web.page.find('textarea')[0]
textarea.value = ''.join(chr(random.randint(0x4e00, 0x9fff)) for _ in range(8))

select = web.page.find('select')[0]

voices = [v for v in speech.getVoices() if v.lang.lower() == 'zh-cn']

for voice in voices:
  select.options.add(html=voice.name, value=voice.name)

@when('click', 'button')
def click():
  utterance = SpeechSynthesisUtterance.new(textarea.value)
  utterance.voice = next(v for v in voices if v.name == select.value)
  speech.speak(utterance)
