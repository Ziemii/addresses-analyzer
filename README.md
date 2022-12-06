# Addresses analyzer by Łukasz Ziemacki
mail: lukasz.ziemacki@gmail.com

# Usage
Windows:
```
> python addresses.py [optional arguments] [email files directory]
```
Linux/macOS:
```
$ python3 addresses.py [optional arguments] [email files directory]
```
# About 

Analyzes email addresses file packs provided in emails folder and returns information based on command line arguments.

## Examples

### Command:
Windows:
```
> python addresses.py --incorrect-emails emails
```
Linux/macOS:
```
$ python3 addresses.py --incorrect-emails ./emails
```
#### Output:
```
Invalid emails (10):
        brad84gmail.com
        yahoo.com
        .com
        com
        @hegmann.info
        wyman.com
        ynolanjones.com
        nernserhickle.biz
        com
        com
```

### Command:
Windows:
```
> python addresses.py -feil email-sent.logs emails
```
Linux/macOS:
```
$ python3 addresses.py -feil ./email-sent.logs ./emails
```
#### Output:
```
Emails not sent (240):
    abogisich@skiles.com
    addie.okon@oconnell.com
    aditya.murazik@gorczany.com
    ahagenes@gmail.com
    alayna29@gmail.com
    alexandra.bayer@larkin.com
    ...
```

## List of optional arguments
Arguments below are optional, they can be used all at once or not at all.

#### Show incorrect emails
```
--incorrect-emails 

-ic 
```
#### Search for addresses with phrase
```
--search PHRASE 

-s PHRASE
```
#### Group addresses by domain
```
--group-by-domain 

-gbd
```
#### Find emails that are not in the logs file
```
--find-emails-not-in-logs PATH_TO_LOGS_FILE 

-feil PATH_TO_LOGS_FILE
```
