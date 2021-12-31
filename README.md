# Run a pre-trained Huggingface Machine Translation engine with UI on your local computer

## Changelog after forking

- Changed model to Facebook M2M for 100 language support.
- Tokenizer change.
- Added target language change support via dropdown (source language change to be added later).
- Flask hosting changed to 0.0.0.0 to support access throughout internal network.

## To be added

- Feedback support
- Support for multiple languages on the source side.
- Model change support
- Internal CTS NMT systems
- Domain-level Support
## Run
- modify the desired language combination directly in app.py, where `source_lang`is the language code for the source and `target_lang` for the target language (as in the model name). The corresponding language model will be automatically downloaded.
- open Terminal/Shell
- navigate to App directory
- pipenv shell
- python app.py
- open Browser and copy and paste URL indicated in prompt (http://131.227.176.164:5000)

## User Interface

![alt text](screen.png?raw=true "User Interface")

## License
Apache License 2.0 (as per the original creator of the Flask template)
 
