# main.py
import discord
from discord.ext import commands
import os

def main2():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents = intents)

    for filename in os.listdir('파일경로'):
        if '.py' in filename:
            filename = filename.replace('.py', '')
            client.load_extension(f"command.{filename}")

    with open('토큰 파일 경로', 'r') as f:
        token1 = f.read()
    

    client.run(token1)  #여기서 오류가 뜬다면 디스코드 봇 설정에 가서 확인해보기 중요!!

if __name__ == '__main__':
    main2()
