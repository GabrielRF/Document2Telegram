[![](https://dockerbuildbadges.quelltext.eu/status.svg?organization=gabrielrf&repository=document2telegram)](https://hub.docker.com/r/gabrielrf/document2telegram/builds)

# Document to Telegram

* [About](#about)
* [Setup](#setup)
  * [Docker Compose](#docker-compose)
  * [Python](#python)
* [Contribute](#contribute)
* [Contact](#contact-me)

## About

This docker container checks if a new file is created on a folder and sends it to a person/group/channel using [Telegram Messenger](https://telegram.org).

## Setup

### Docker Compose

```
doc2tg:
    image: gabrielrf/document2telegram
    environment:
        - BOT_TOKEN=
        - FOLDER=/
        - EXTENSION=
        - DESTINATION=
    restart: always
    volumes:
        - host_folder:container_folder
```

`BOT_TOKEN`: Token given by [@BotFather](https://t.me/BotFather) on Telegram.

`FOLDER`: Folder that will be monitored by the script. In case of a folder tree, set the top-level folder.

`EXTENSION` (optional): The extension of the file that should be sent. Usually `mp4` is the case.

`DESTINATION`: To whom the message will be sent.

`volumes`: The same folder used on `FOLDER`:Some folder that exists on the container. Suggested: `/mnt`

### Python

First, run 

```
pip install inotify
pip install pytelegrambotapi
```

to install the libraries needed. Then, open `file2gif.py` and make the necessary adjustments on `BOT_TOKEN`, `FOLDER`, `EXTENSION` and `DESTINATION` as listed above. 

Run the Python Script.

```
python doc2tg.py
```

## Contribute

Pull requests and issues are welcome! 

## Contact me

[GabRF.com](https://gabrf.com)

[@GabrielRF](https://t.me/gabrielrf) on Telegram.
