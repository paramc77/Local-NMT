# Centre for Translation Studies NMT on Web (CTSNMT)

## Changelog after forking

#### 03/08/2021
- **v1.0.0**: Asynchrounous translation finally!
- Use of Swagger API added, calls to API for translation (removed form submit).
- Source and Target language selection via Python dictionary; removed dependency of data-id from HTML. 
- Changed model to FB M2M 418M for quick debugging.
- resolved icon issue while selecting languages.
- resolved "hidden input" dependencies, jquery based language selection using semantic ui default hidden fields.
- navbar icon trimmed.
- added collection of translated text to a file (step towards feedback)
#### 31/12/2021
- **v0.5.1**: Asynchrounous translation finally!
- Changed model to Facebook M2M for supporting 100+ languages.
- Tokenizer change.
- Added target language change support via dropdown (source language change to be added later).
- Flask hosting changed to 0.0.0.0 to support access throughout internal network.

#### 01/01/2022
- Added Semantic UI for searchable dropdown.
- Added support for selection of source language.
- POST request sends back previous source/target language pair (system defaults to translating for the last language pair, if languages not selected).
- Added support for model change in HTML (Flask side pages to be added later).
- Added CTS logo.

## To be added
- Feedback support
- Internal CTS NMT systems
- Model change support
- Domain-level Support

## Installation ( necessary; but easy :) )

#### Step 1
```bash
git clone https://github.com/surrey-nlp/Local-NMT.git
cd Local-NMT
```
#### Step 2
```bash
pip install -r requirements.txt
```
## Run
```bash
python app.py
```
 (requires GPU for fast inference, relatively slower inference with CPUs)

Now, you can open Browser and copy and paste URL indicated in prompt (http://localhost:5000)

## User Interface

![alt text](screen.png?raw=true "User Interface")

## License
Apache License 2.0 (as per the original creator of the Flask template)
 
