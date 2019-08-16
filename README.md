# About

This program deletes all public links from files shared in Dropbox

## Requirements

Requires Python (with `-m venv` support) or Docker installed to execute the script.

> **Note:** You need to create an app in Dropbox to use for authentication and authorization. Follow this link: https://www.dropbox.com/developers/apps  
> Takes less than a minute, trust me...

## Local Installation without Docker

If you don't want to run the [pre-built](#local-installation-without-docker) container follow these steps:

```bash
$ git clone https://github.com/embano1/dropbox-link-cleaner
$ cd dropbox-link-cleaner
$ python -m venv .
$ source bin/activate
$ pip install -r requirements.txt
```

## Run without Docker

```
usage: python link-remover.py [-h] [-t TOKEN] [-d]

This program deletes all public links from files shared in Dropbox

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Dropbox app security token (key) to use for
                        authentication (see
                        https://www.dropbox.com/developers/apps)
  -d, --dryrun          don't delete just print links that would be removed
```

## Run with Docker

```bash
# dry-run with dummy API token, usage see above
$ docker run --rm -it embano1/dropbox-link-remover:latest -d -t ABCDEFGHIJK12345678
```