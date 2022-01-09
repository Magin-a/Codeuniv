 # cogs/exampls.py
from discord.ext import commands
import discord
from bs4 import BeautifulSoup
import json

col =  "파일위치"
class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
        #데이터 파일 불러오기
        with open(col,"r", encoding="utf-8") as f:
            self.quizDict = json.load(f)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    
    @commands.command(name = "백준")
    async def quiz(self, ctx):
        embed = discord.Embed(title ="★고양이도우미★", description="아래기능을 사용할 수 있습니다.", color=discord.Color.blue())
        
        embed.add_field(name="1.문제등록", value="'!문제등록' 키워드를 사용하시면 됩니다.", inline=False)
        embed.add_field(name="2.이번주문제", value="'!이번주문제' 키워드를 사용하시면 됩니다.", inline=False)
        embed.add_field(name="3.지난주문제", value="'!지난주문제' 키워드를 사용하시면 됩니다.", inline=False)
        await ctx.send(embed = embed)


    @commands.command(name = "문제등록")
    async def quizreg(self, ctx):
        def checkMessage(message, user):
                return user == message.author 
        
        embed = discord.Embed(title = '문제등록', description = '마감 기한-문제번호-문제명 순으로 입력해주세요.', color=discord.Color.blue())
        embed.add_field(name="예시", value="'20220101\0 1237\0 정ㅋ벅ㅋ'", inline=False)
        embed.add_field(name="다음 입력: 문제 수", value="이번주의 문제는 몇문제 인가요?")
        # embed.add_field(name="다음 명령어", value="위 예시처럼 입력을 해주세요. 주의사항) 입력 순서!!", inline=False)
        await ctx.send(embed = embed)

        quiz_num = await self.client.wait_for("message", check = checkMessage)
        for _ in range(int(quiz_num)):
            

        await ctx.send()


def setup(client):
    client.add_cog(Bot(client))
