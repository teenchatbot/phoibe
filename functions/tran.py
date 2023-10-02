import deepl
from functions import settings

key = settings.keys.deeplKey

class tran:
    def translate(text, language):
        translator = deepl.Translator(key)
        try:
            translation = translator.translate_text(text=text, target_lang=language)
            return str(translation)
        except:
            return "An error has occured please check the available languages"
