 # cogs/exampls.py
from discord.ext import commands
import discord
from bs4 import BeautifulSoup

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @commands.command(name = "ping")
    async def _ping(self, ctx):
        await ctx.send('pong!')


    @commands.command(name = "백준")
    async def quiz(ctx, self,data, quiz):

        registrant = ctx.author.name
        def checkMessage(message):
            return message.author == ctx.author and message.channel == ctx.channel
        
        
        embed = discord.Embed(tittle='문제 검색', description= '풀이 기간, 문제 번호 또는 이름을 입력 해주세요 ', color = discord.Color.blue())
        await ctx.send(embed = embed)

        message = await self.client.wait_for("message", check = checkMessage)
        
        await message.send("f{}기간 동안 {}문제를 풀어보아요", data, quiz)
  

def setup(client):
    client.add_cog(Example(client))
