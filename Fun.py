import random
import discord
from discord.ext import commands

class Fun():
    def __init__(self, client):
        self.client = client
    
    def calculatePet(self, dropRate):
        petChance = 0
        petLoop = 0
        while petChance != dropRate:
            petChance = random.randint(0,dropRate)
            petLoop += 1
        else:
            return petLoop        
    
    @commands.command(passcontext=True)
    async def pet(self, ctx):
        try: 
            if ctx == "bandos":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "sire" or ctx == "abyss":
                await self.client.say("It took " + str(self.calculatePet(2560)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "mole" or ctx == "giantmole":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "callisto":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "cerberus" or ctx == "hellpuppy":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "inferno" or ctx == "zuk":
                await self.client.say("It took " + str(self.calculatePet(100)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "kq" or ctx == "kalphitequeen":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "tob" or ctx == "theatreofblood":
                await self.client.say("It took " + str(self.calculatePet(650)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "guardians":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "olm":
                await self.client.say("It took " + str(self.calculatePet(65)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "chaosele" or ctx == "ele" or ctx == "chaoselemental":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "prime":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "supreme":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "rex":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "corp":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "zammy":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "kraken":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "arma" or ctx == "armadyl":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "thermi" or ctx == "smokedevil":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "zulrah":
                await self.client.say("It took " + str(self.calculatePet(4000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "zil" or ctx == "zilyana" or ctx == "sara" or ctx == "saradomin":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "kbd":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "scorpia":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "skotizo":
                await self.client.say("It took " + str(self.calculatePet(65)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "jad":
                await self.client.say("It took " + str(self.calculatePet(200)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "venenatis" or ctx == "spider":
                await self.client.say("It took " + str(self.calculatePet(2000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "vetion" or ctx == "vet'ion":
                await self.client.say("It took " + str(self.calculatePet(2000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "vorkath" or ctx == "vorki":
                await self.client.say("It took " + str(self.calculatePet(3000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "master" or ctx == "bloodhound":
                await self.client.say("It took " + str(self.calculatePet(1000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "chick" or ctx == "chompychick":
                await self.client.say("It took " + str(self.calculatePet(500)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "herbi":
                await self.client.say("It took " + str(self.calculatePet(6500)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "penance" or ctx == "pq" or ctx == "penancequeen":
                await self.client.say("It took " + str(self.calculatePet(1000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
            elif ctx == "phoenix" or ctx == "wintertodt" or ctx == "wt":
                await self.client.say("It took " + str(self.calculatePet(5000)) + " kills to get the pet! <:gnomechild:498673024099287053>")
        except Exception as e:
            print(e)
            await self.client.say("That is not a valid boss name. Please Try Again.")

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        channel = ctx.message.channel
        fiftyfifty = random.randint(0,1)
        if fiftyfifty == 0:
            await self.client.send_file(channel, 'heads.png')
        elif fiftyfifty == 1:
            await self.client.send_file(channel, 'tails.png')    
        
    @commands.command()
    async def ping(self):
        await self.client.say(':ping_pong: Pong!')
    
    @commands.command()
    async def didpopgetmoleyet(self):
        await self.client.say('NOPE! <:mole:498673418829561856> <:mole:498673418829561856> <:mole:498673418829561856>')
    
    @commands.command()
    async def barrows(self):
        bLoop = 0
        
        while True:
            getItem = random.randint(1,16)
            if getItem == 16:
                bLoop += 1
                await self.client.say("It took you " + str(bLoop) + " chests to get a Barrows item.")
                break
            else:
                bLoop += 1
    
    @commands.command()
    async def rangerboots(self):
        #Counts Number of times the loop has ran
        rangerLoop = 0
        pickLoop = 0
        
        try:
            while True:
                pickLoop = random.randint(0,2)
                if pickLoop == 0:
                    threeSlots = 0
                    rangerLoop += 1
                    threeSlots = random.randint(0,333)
                    if threeSlots == 333:
                        await self.client.say("It took " + str(rangerLoop) + " Medium Clues until you got ranger boots.")
                        break
                    
                if pickLoop == 1:
                    fourSlots = 0
                    rangerLoop += 1
                    fourSlots = random.randint(0,250)
                    if fourSlots == 250:
                        await self.client.say("It took " + str(rangerLoop) + " Medium Clues until you got ranger boots.")
                        break
                    
                if pickLoop == 2:
                    fiveSlots = 0
                    rangerLoop += 1
                    fiveSlots = random.randint(0,200)
                    if fiveSlots == 200:
                        await self.client.say("It took " + str(rangerLoop) + " Medium Clues until you got ranger boots.")
                        break
        except Exception as e:
            print(e)
    
    @commands.command()
    async def dds(self):
        val = random.randint(0,46)
        val1 = random.randint(0,46)
        x = str(val)
        y = str(val1)
        await self.client.say('<:dds:498673023998754816> You hit a ' + x + ", " + y)
        
    @commands.command()
    async def ags(self):
        val = random.randint(0,94)
        x = str(val)
        if val < 90:
            await self.client.say("<:ags:498673023575130125> You spec'd a " + x)
        else:
            await self.client.say("<:ags:498673023575130125> You spec'd a " + x + " and the target tele'd out")
            
    @commands.command()
    async def dclaws(self):
        val = random.randint(0,46)
        val1 = random.randint(0,23)
        val2 = random.randint(0,11)
        val3 = random.randint(0,12)
        w = str(val)
        x = str(val1)
        y = str(val2)
        z = str(val3)
        await self.client.say("<:dclaws:498673024002949120> You spec'd a " + w + "," + x + "," + y + "," + z)   
        
    @commands.command()
    async def gmaul(self):
        val = random.randint(0,46)
        val1 = random.randint(0,46)
        x = str(val)
        y = str(val1)
        await self.client.say("<:gmaul:498673023763742733> You spec'd a " + x + ", " + y)    
            
    @commands.command()
    async def whichskillnext(self):
        skills = ['Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints', 'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing', 'Cooking', 'Firemaking', 'Woodcutting', 'Farming']        
        medChoice = random.choice(skills)
        await self.client.say("<:gnomechild:498673024099287053>  I think you should train " + medChoice + " next.")

def setup(client):
    client.add_cog(Fun(client))