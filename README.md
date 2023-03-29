# Aternos-Manager-Discord-Bot

This is a Discord Aternos manager bot. Aternos is an free minecraft server hosting with some restrictions in managing it automaticly.

What this bot does is it makes posible to run an aternos server by a command in discord.

Notice: You must have installed Chrome on your pc so the bot will work.
        Only for Windows os.

## Disclaimer

Slash commands can take some time to get registered globally, so if you want to test a command you should use
the `@app_commands.guilds()` decorator so that it gets registered instantly. Example:

```py
@commands.hybrid_command(
  name="command",
  description="Command description",
)
@app_commands.guilds(discord.Object(id=GUILD_ID)) # Place your guild ID here
```

When using the template you confirm that you have read the [license](LICENSE.md) and comprehend that I can take down
your repository if you do not meet these requirements.

Please do not open issues or pull requests about things that are written in the [TODO file](TODO.md), they are **already** under work for a future version of the template.

## How to download it

This repository is now a template, on the top left you can simply click on "**Use this template**" to create a GitHub
repository based on this template.

Alternatively you can do the following:

* Clone/Download the repository
    * To clone it and get the updates you can definitely use the command
      `git clone`
* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token
* Invite your bot on servers using the following invite:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  Replace `YOUR_APPLICATION_ID_HERE` with the application ID and replace `PERMISSIONS` with the required permissions
  your bot needs that it can be get at the bottom of a this
  page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)

## How to set up

To set up the bot I made it as simple as possible. I now created a [config.json](config.json) file where you can put the
needed things to edit.

Here is an explanation of what everything is:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |


## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
python -m pip install -r requirements.txt
```
1. Login to aternos account from your chrome browser
2. Go to cogs\ and edit the userdata.txt by replacing the default path to your own path of AppData\\Local\\Google\\Chrome\\User Data

```

After that you can start it with

```
python bot.py
```

> **Note** You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.


## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see
the [tags on this repository](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/tags).

## Built With

* [Python 3.9.12](https://www.python.org/)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
