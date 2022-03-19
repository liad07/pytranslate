from translate import Translator
x=input('enter sentece\n')
y=input('to which lang convert\n')
translator= Translator(to_lang=f"{y}")
translation = translator.translate(f"{x}")
print(translation)