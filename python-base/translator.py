from translate import Translator

translator = Translator(to_lang = "zh")
try:
    with open('../test.txt',mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('../sample.txt',mode='w') as sample_file:
            sample_file.write(translation)
except FileNotFoundError as e:
    print('file not found')