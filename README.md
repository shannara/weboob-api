## Requirements
Python 3
- python3-venv

## Installation

```shell
git clone https://github.com/shannara/weboob-api.git
python3 -m venv weboobapi-venv
source weboobapi-venv/bin/activate
cd weboob-api
pip3 install -r requirements.txt
python run.py
```

## Configure weboob

### Update weboob repository
```shell
weboob-config update
```

### Init weboob bank capability
```shell
weboob bank
Warning: there is currently no configured backend for boobank
Do you want to configure backends? (Y/n):
```
Respond y or simple type enter
In list of bank backend choose your self bank (in my case creditmutuel 34)
```shell
Select a backend to create (q to stop): 34
Module "creditmutuel" is available but not installed.
=== [ 20%] Module creditmutuel is not installed yet
=== [ 30%] Downloading module...
=== [ 50%] Checking module authenticity...
=== [ 70%] Setting up module...
=== [ 90%] Downloading icon...
=== [100%] Module creditmutuel has been installed!


Configuration of backend creditmutuel
-------------------------------------
[login] Identifiant:
     c: Run an external tool during backend load
     p: Prompt value when needed (do not store it)
     s: Store value in config
*** How do you want to store it? (c/P/s):
```
Respond s, and in Prompt type your account id and press enter

```shell
Identifiant: xxxxxxx
````

```shell
[password] Mot de passe:
     c: Run an external tool during backend load
     p: Prompt value when needed (do not store it)
     s: Store value in config
*** How do you want to store it? (c/P/s):
```
Respond s, and in Prompt type your password id and press enter

```shell
Mot de passe (hidden input):
```

After save backend, you return to list of backend, you need type q to finish setup
```shell
Select a backend to create (q to stop):
```

You switch to boobank prompt, bank follow DSP2 directive that need to accept
new connection with app of bank (mobile, sms code, ...) and renewed 90 days

type list in prompt to list accounts and launch DSP2 authent if required
```shell
boobank> list
                 Account                     Balance    Coming
------------------------------------------+----------+----------
2020-04-09 14:35:50,265:WARNING:backend.creditmutuel.browser.mobileconfirmationpage:2.0:pages.py:142:check_bypass This connexion cannot bypass mobile confirmation
Démarrez votre application mobile Crédit Mutuel depuis votre appareil " XXXX XXXX " pour vérifier et confirmer votre identité.
```

After accept new connection we have list of accounts

```shell

 #1 (creditmutuel) Compte Courant Jeune Acti    222.22  
 #2 (creditmutuel) Livret De Developpement D  13855.35  
------------------------------------------+----------+----------
```

We can now quit boobank, type quit in Prompt
```shell
boobank> quit
```
