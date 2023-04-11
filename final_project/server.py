from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedTextToFrench = translator.english_to_french(textToTranslate)
    # Write your code here
    return translatedTextToFrench

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedTextToEnglish = translator.french_to_english(textToTranslate)
    return translatedTextToEnglish


@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
