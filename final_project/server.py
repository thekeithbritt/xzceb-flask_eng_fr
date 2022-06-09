from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['GET'])
def englishToFrench(englishText):
    textToTranslate = request.args.get(englishText)
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish", methods=['GET'])
def frenchToEnglish(frenchText):
    textToTranslate = request.args.get(frenchText)
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
