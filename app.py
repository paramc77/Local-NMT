import flask
from flask import Flask, flash, Response, redirect, url_for, request, session, abort, render_template, make_response, jsonify
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import torch
from typing import List
import os
import json

app = flask.Flask(__name__)
app.secret_key = '1234abcd#'

#initiate language pair for translator
#the corresponding language model will be automatically downloaded from Huggingface
# source_lang = "en"
# target_lang = "de"

device = "cuda:0" if torch.cuda.is_available() else "cpu"
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_1.2B")
model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_1.2B").to(device)


# model_name = f'Helsinki-NLP/opus-mt-en-mul'
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

###############################################
# ROUTINGS
###############################################

@app.route('/', methods=['GET', 'POST'])
def index():
    source_l = "en"
    target_l = "de"
    if request.method == 'POST':
        source_text = request.form['rawtext']
        
        
        source_l = request.form['sourcelang'].lower()
        if(source_l == ''):
            tokenizer.src_lang = "en"
        else:
            tokenizer.src_lang = source_l

        target_l = request.form['targetlang'].lower()
        if(target_l == ''):
            target_l = "de"
        encoded_hi = tokenizer([source_text], return_tensors="pt", padding=True).to(device)
        generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.get_lang_id(target_l))
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        # print(source_l, target_l)
        return render_template("index.html", target_text=translation[0], source_text=source_text, source_lang=source_l, target_lang=target_l )
        # return jsonify(target_text=translation[0], source_text=source_text, source_lang=source_l, target_lang=target_l)
    # return render_template("index.html", source_lang=source_lang, target_lang=target_lang)
    return render_template("index.html")

app.run(debug=True, host="0.0.0.0")
