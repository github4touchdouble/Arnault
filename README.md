This is a ultra basic implementation of an awfully bad chatbot.

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
And then run
```console
python chat.py
```
Then finally ask:
```console
Is anyone there?
```
#### (PLEASE don't be shocked if someone answers)
Arnault is also available as an API via:
```console
https://arnaultapi.onrender.com/
```
*(TODO)*

## What's next

> __NOTE__: _See [GitHub issues](https://github.com/carlobortolan/Embloy/issues) for more information_

- Utilize the API with a web frontend
- Enhance language model with more data (and focus it n one discipline)
- ...

---

---

© Jan Hummel

> Jan Hummel &nbsp;&middot;&nbsp;
> GitHub [@github4touchdouble](https://github.com/github4touchdouble) &nbsp;&middot;&nbsp;
> contact via [@jan.hummel@tum.de](jan.hummel@tum.de)