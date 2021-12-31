import flask
from flask import Flask, flash, Response, redirect, url_for, request, session, abort, render_template, make_response, jsonify
# from transformers import MarianTokenizer, MarianMTModel
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
tokenizer.src_lang = "en"

# model_name = f'Helsinki-NLP/opus-mt-en-mul'
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

###############################################
# ROUTINGS
###############################################

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_text = request.form['rawtext']
        source_l = request.form['sourcelang'].lower()
        target_l = request.form['targetlang'].lower()
        # Tokenize the text
        # batch = tokenizer([source_text], return_tensors="pt", padding=True)
                
        # tokenized text maximum allowed size of 512
        # batch["input_ids"] = batch["input_ids"][:, :512]
        # batch["attention_mask"] = batch["attention_mask"][:, :512]
        # translation_encoded = model.generate(**batch)
        # translation = tokenizer.batch_decode(translation_encoded, skip_special_tokens=True)
        
        encoded_hi = tokenizer([source_text], return_tensors="pt", padding=True).to(device)
        generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.get_lang_id(target_l))
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        # print(source_l, target_l)
        return render_template("index.html", target_text=translation[0], source_text=source_text, source_lang=source_l, target_lang=target_l )
    
    # return render_template("index.html", source_lang=source_lang, target_lang=target_lang)
    return render_template("index.html")

app.run(debug=True, host="0.0.0.0")
