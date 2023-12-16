from googletrans import Translator

def googleTranslate(inputText):
    translator = Translator()
    text_ja = inputText
    text_en = translator.translate(text_ja, src='ja', dest='en').text
    return(text_en)