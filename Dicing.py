import json
import random
from discord.ext import commands

class Dicing:
    def __init__(self, client):
        self.client = client
                
    async def update_data(self, users, user):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['gp'] = 10000
    
    async def addgp(self, users, user, gp):
        users[user.id]['gp'] += gp
    
    async def subtractgp(self, users, user, gp):
        users[user.id]['gp'] -= gp
        
    @commands.command(pass_context=True)
    async def nogpleft(self, ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        if users[message.author.id]['gp'] == 0:
            await self.client.send_message(message.channel, "100gp has been added to your account. Please be more careful next time.")
            await self.addgp(users, message.author, 100)
        else:
            await self.client.send_message(message.channel, "Sorry, I only give money to people who have no gp left.")
            
        with open('users.json', 'w') as f:
            json.dump(users, f)

    
    @commands.command(pass_context=True)
    async def checkgp(self,ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        message = ctx.message
        await self.client.send_message(message.channel, "You have " + str(users[message.author.id]['gp']) + "gp in your account.")
    
        with open('users.json', 'w') as f:
            json.dump(users, f)
            
    @commands.command(pass_context=True)
    async def poordice(self,ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        compRoll = random.randint(1,6)
        myRoll = random.randint(1,6)
        if myRoll > compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've won 1gp.")
            await self.addgp(users, message.author, 1)
        elif myRoll < compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've lost 1gp")
            await self.subtractgp(users, message.author, 1)
        else:
            await self.client.send_message(message.channel, "Draw, no gp was given or taken")
            
        with open('users.json', 'w') as f:
            json.dump(users, f)
            
    @commands.command(pass_context=True)
    async def lowdice(self,ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        compRoll = random.randint(1,6)
        myRoll = random.randint(1,6)
        if myRoll > compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've won 10gp.")
            await self.addgp(users, message.author, 10)
        elif myRoll < compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've lost 10gp")
            await self.subtractgp(users, message.author, 10)
        else:
            await self.client.send_message(message.channel, "Draw, no gp was given or taken")
            
        with open('users.json', 'w') as f:
            json.dump(users, f)
            
    @commands.command(pass_context=True)
    async def dice(self,ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        compRoll = random.randint(1,6)
        myRoll = random.randint(1,6)
        if myRoll > compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've won 100gp.")
            await self.addgp(users, message.author, 100)
        elif myRoll < compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've lost 100gp")
            await self.subtractgp(users, message.author, 100)
        else:
            await self.client.send_message(message.channel, "Draw, no gp was given or taken")
            
        with open('users.json', 'w') as f:
            json.dump(users, f)
        
    @commands.command(pass_context=True)
    async def highdice(self,ctx):
        message = ctx.message
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        await self.update_data(users, message.author)
        
        compRoll = random.randint(1,6)
        myRoll = random.randint(1,6)
        if myRoll > compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've won 1000gp.")
            await self.addgp(users, message.author, 1000)
        elif myRoll < compRoll:
            await self.client.send_message(message.channel, "You rolled a " + str(myRoll))
            await self.client.send_message(message.channel, "The dicer rolled a " + str(compRoll) + ". You've lost 1000gp")
            await self.subtractgp(users, message.author, 1000)
        else:
            await self.client.send_message(message.channel, "Draw, no gp was given or taken")
            
        with open('users.json', 'w') as f:
            json.dump(users, f)
            
    
        
def setup(client):
    client.add_cog(Dicing(client))