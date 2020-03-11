# Team 11 Telegram Bot

This is a repository for Telegram bot that will be developed by 11th team during Intel Academic Program Python Course.

## Table of Contents
- [Search](#search)
- [Features](#features)
- [Support](#support)
 - [Bugs](#bugs--issues)
 - [Pull Requests](#pull-requests)
- [Credits](#credits)

## Search

1. Open Telegram
2. Search for `БОТ_НЕЙМ` bot.
3. Click `Start bot`.

## Features

* `/start` - get started with your new bot;
* `/help`- receive some instructions about the bot;
* `/history` - get your 5 last actions;

## Support

### [Bugs / Issues]
If you discover a bug in the bot, please [search our issue tracker](https://github.com/nn-students-2020h1/11-command/issues) first. If it hasn't been reported, please [create a new issue](https://github.com/nn-students-2020h1/11-command/issues/new).

### [Pull Requests](https://github.com/nn-students-2020h1/11-command/pulls)
If you'd like to make your own changes, make sure you follow the pull request template.
If this is your first time making a PR or aren't sure of the standard practice of making a PR, here are some articles to get you started:
 - [GitHub Pull Request Tutorial](https://www.thinkful.com/learn/github-pull-request-tutorial/)
 - [How to write the perfect pull request](https://github.com/blog/1943-how-to-write-the-perfect-pull-request)

## Credits
- [trifonovDmitry](https://github.com/trifonovDmitry): Team Leader
- [sesorov](https://github.com/sesorov): Programmer
- [NadyStrelnikova](https://github.com/NadyStrelnikova): Programmer

## Set up Python environment

1. Create virtual environment `python -m venv venv`
2. Activate virtual environment and install requirements: 

    `venv\Scripts\activate` - on Linux
    
    `venv\Scripts\activate.bat` - on Windows
    
    `pip install -r requirements.txt`

## Create your Telegram Bot

1. Follow official [Telegram instructions](https://core.telegram.org/bots#6-botfather) to create your bot and obtain token.
2. Insert obtained token to `setup.py` `TOKEN` variable.

## Run your bot

1. Execute ``python chat_bot_template.py``
2. Try your bot - find it in Telegram and press `/start`.
