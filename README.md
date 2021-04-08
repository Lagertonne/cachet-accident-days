# days_since_last_accident.py
## Description
This is a simple script that returns the days since the last entry from a Cachet-Status-Page.

## Arguments

* --blocklist
  * Optional. Comma-seperated-list. All Entrys that include a word from the blocklist are ignored
* -p
  * Optional. Only prints the days without any fancy stuff.

## Examples
```
python3 days_without_accident.py --blocklist "problem,maintenance" https://demo.cachethq.io/rss
```
```
python3 days_without_accident.py -p https://demo.cachethq.io/rss
```
```
python3 days_without_accident.py -p --blocklist "problem,maintenance" https://demo.cachethq.io/rss
```
```
python3 days_without_accident.py https://demo.cachethq.io/rss
```
