""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

from discord.ext import commands
from discord.ext.commands import Context
import discord
from helpers import checks
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
import os
# Here we name the cog and create a new class for the cog.
class Server(commands.Cog, name="aternos"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="start",
        description="Start the server in aternos.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    async def testcommand(self, context: Context):
        chrome_options = Options()
        with open('config.txt', 'r') as f:
            userdatadir = f.read()        
        userdatadir = userdatadir.replace('\n', '')
        chrome_options.add_argument("user-data-dir=" + userdatadir)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--start-maximized")
        driver = uc.Chrome(use_subprocess=True, options=chrome_options)
        driver.get("https://aternos.org/server/")
        # locate the button with id "start"
        time.sleep(2)
        start_button = driver.find_element(By.ID, "start")
        if start_button is None:
            await context.send("Ошибка element wasn't found")
        if start_button.value_of_css_property("display") == "none" or start_button.value_of_css_property("display") == "None":
            await context.send("Сервер уже запущен или только запускается.")
        else:
            start_button.click()
            await context.send("Сервер запущен, подождите пару минут.")


        driver.save_screenshot('screen.png')
        await context.send(file=discord.File('screen.png'))
        os.remove('screen.png')
        driver.quit()




# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Server(bot))
