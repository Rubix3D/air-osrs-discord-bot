import praw
import random
import asyncio
import discord
from discord.ext import commands

class PullReddit:
    def __init__(self, client):
        self.client = client
        
    reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Reddit Pull Bot by Rubix')
    
    @commands.command()
    async def randomporngif(self):
        memes_submissions = self.reddit.subreddit('NSFW_GIF').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.send_message(self.client.get_channel('512132776049377280') ,submission.url)
        
    @commands.command()
    async def random4k(self):
        memes_submissions = self.reddit.subreddit('NSFW_4K').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.send_message(self.client.get_channel('512132776049377280') ,submission.url)
        
    @commands.command()
    async def randomles(self):
        memes_submissions = self.reddit.subreddit('Lesbian_gifs').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.send_message(self.client.get_channel('512132776049377280') ,submission.url)
    
    @commands.command()
    async def randommeme(self):
        memes_submissions = self.reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.say(submission.url)
        
    @commands.command()
    async def randomhentai(self):
        memes_submissions = self.reddit.subreddit('hentai').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.say(submission.url)    
        
    @commands.command()
    async def dadjoke(self):
        dadjokes = self.reddit.subreddit('dadjokes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in dadjokes if not i.stickied)
            
        await self.client.say(submission.title)
        asyncio.sleep(3)
        await self.client.say(submission.selftext)
    
    @commands.command()
    async def randomdankmeme(self):
        memes_submissions = self.reddit.subreddit('dankmemes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.say(submission.url)    

    @commands.command()
    async def random60(self):
        memes_submissions = self.reddit.subreddit('60fpsporn').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.send_message(self.client.get_channel('512132776049377280') ,submission.url)
        
        
    @commands.command()
    async def eyebleach(self):
        memes_submissions = self.reddit.subreddit('eyebleach').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(i for i in memes_submissions if not i.stickied)
    
        await self.client.send_message(self.client.get_channel('512132776049377280') ,submission.url)
        
def setup(client):
    client.add_cog(PullReddit(client))