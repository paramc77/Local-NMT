<p align="center"><img src="./static/favicon.png" alt="logo" width="220" height="100"/></p>

# Centre for Translation Studies NMT on Web (CTSNMT)

[![GitHub issues](https://img.shields.io/github/issues/surrey-nlp/Local-NMT?style=flat-square)](https://github.com/surrey-nlp/Local-NMT/issues)
[![GitHub stars](https://img.shields.io/github/stars/surrey-nlp/Local-NMT?style=flat-square)](https://github.com/surrey-nlp/Local-NMT/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/surrey-nlp/Local-NMT?style=flat-square)](https://github.com/surrey-nlp/Local-NMT/network)
[![GitHub license](https://img.shields.io/github/license/surrey-nlp/Local-NMT?style=flat-square)](https://github.com/surrey-nlp/Local-NMT)
[![Twitter](https://img.shields.io/twitter/url?style=flat-square&url=https://github.com/surrey-nlp/Local-NMT)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fsurrey-nlp%2FLocal-NMT)
[![Twitter Follow](https://img.shields.io/twitter/follow/CTS_Surrey?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/CTS_Surrey)
[![Twitter Follow](https://img.shields.io/twitter/follow/PeopleCentredAI?color=1DA1F2&logo=twitter&style=flat-square)](https://twitter.com/PeopleCentredAI)

<hr/>

### Welcome to the CTSNMT project repository. To use this codebase and host this application locally, simple clone the repository and follow the installation instructions provided below.

<hr/>

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
<hr/>

## Run
```bash
python app.py --port <VALUE>
```
(requires GPU for fast inference, slower inference with CPUs)

Now, you can open Browser and copy and paste URL indicated in prompt (http://localhost:5000)

<hr/>

## User Interface

<br/>

![alt text](./screen.png?raw=true "User Interface")

<hr/>

## Yet to be added

- Feedback support

## Changelog after forking

#### 20/03/2022 - 22/03/2022
 - Added support for uploading file and translating it, a download link is provided later.

#### 11/03/2022 - 15/03/2022
 - Sentence Generation on source side for each of the 99 languages supported by the FB model.
 - Language Identification via the JS-based [langid.py library](https://github.com/saffsd/langid.js). Supports 78 languages. Thanks to the developer! :)
 - Inference using trained NMT models from the folder "models" in CTSNMT root. 
 - PORT value to be passed as an `argparse` parameter now. Use --port <VALUE> otherwise it defaults to using PORT 5000.
 - Interface cleaning.

#### 10/03/2022
- Added [bertviz](https://github.com/jessevig/bertviz) based visualization. Thanks to the developer! :)

#### 09/03/2022
- Alert boxes for missing parameters.
- Copy button, and clear buttons added for ease.
- langauges order changed to alphabetical (mostly).
- Copy translation button to copy the translated text to clipboard.
- Back-translate button to reverse the language pairs and back-translate the previous translated output.

#### 08/03/2022
- **v1.0.0**: Asynchrounous translation finally!
- Use of Swagger API added, calls to API for translation (removed form submit).
- Source and Target language selection via Python dictionary; removed dependency of data-id from HTML. 
- Changed model to FB M2M 418M for quick debugging.
- resolved icon issue while selecting languages.
- resolved "hidden input" dependencies, jquery based language selection using semantic ui default hidden fields.
- navbar icon trimmed.
- added collection of translated text to a file (step towards feedback)

#### 01/01/2022
- Added Semantic UI for searchable dropdown.
- Added support for selection of source language.
- POST request sends back previous source/target language pair (system defaults to translating for the last language pair, if languages not selected).
- Added support for model change in HTML (Flask side pages to be added later).
- Added CTS logo.

#### 31/12/2021
- **v0.5.1**: Changed model to Facebook M2M for supporting 100+ languages.
- Tokenizer change.
- Added target language change support via dropdown (source language change to be added later).
- Flask hosting changed to 0.0.0.0 to support access throughout internal network.


## License
CC-BY-SA 4.0
 