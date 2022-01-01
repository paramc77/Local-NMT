# Centre for Translation Studies NMT Systems (CTSNMT)

## Changelog after forking

#### 31/12/2021
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
- Support for multiple languages on the source side.
- Model change support
- Internal CTS NMT systems
- Domain-level Support
## Run
- open Terminal/Shell
- navigate to App directory
- python app.py
- open Browser and copy and paste URL indicated in prompt (http://131.227.176.164:5000)

## User Interface

![alt text](screen.png?raw=true "User Interface")

## License
Apache License 2.0 (as per the original creator of the Flask template)
 
