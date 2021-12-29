 # cogs/exampls.py
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import json
col =  "파일경로"
class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
        #데이터 파일 불러오기
        with open(col,"r", encoding="utf-8") as f:
            self.quizDict = json.load(f)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @commands.helpcommend(name = "백준")
    async def quiz(self, ctx):
        
        embed = discord.Embed(tittle = '선택지', descripition="문제등록, 이번주 문제, 지난주 문제 중 원하시는 기능을 입력해주세요", color= discord.Color.blue())
        await ctx.send(embed = embed)


    @commands.quizregistration(name = "문제등록")
    async def quiz(self, ctx):
        def checkMessage(message):
                return message.author == ctx.author and message.channel == ctx.channel

  

def setup(client):
    client.add_cog(Bot(client))
