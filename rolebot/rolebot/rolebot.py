import discord
import logging

client = discord.Client()

@client.event
async def on_ready():
    print('My name is ' + client.user.name)
    print()
    print('Servers im in:')
    for guild in client.guilds:
        print("Name: " + guild.name)
        print("ID: " + str(guild.id))
        print('')
    print('')

@client.event
async def on_message(message):
    
    if message.content.startswith('!pingMessage') and message.author.guild_permissions.administrator:
        await message.delete()
        msg = await message.channel.history().get()
        emojiList = client.emojis
        s = 'Click on the emoji below to be notified when anyone wants to form a group for a given boss.'
        s+="\n"
        for emoji in emojiList:
            rolename = 'ping'+emoji.name
            role = discord.utils.get(client.get_guild(emoji.guild_id).roles, name=rolename)
            if role != None:
                s+="\n"+str(emoji)+" for "+ str(role.mention)
        if msg!=None:
            await msg.edit(content=s)
        if msg==None:
            msg = await message.channel.send(s)
        for emoji in emojiList:
            rolename = 'ping'+emoji.name
            role = discord.utils.get(client.get_guild(emoji.guild_id).roles, name=rolename)
            if role != None:
                await msg.add_reaction(emoji)

@client.event
async def on_raw_reaction_add(rawReaction):
    if str(await client.get_channel(rawReaction.channel_id).get_message(rawReaction.message_id)).find("468411047259406366"):
        try:
            rolename = 'ping'+rawReaction.emoji.name
            role = discord.utils.get(client.get_guild(rawReaction.guild_id).roles, name=rolename)
            await client.get_guild(rawReaction.guild_id).get_member(rawReaction.user_id).add_roles(role)
        except:
            pass
    
@client.event
async def on_raw_reaction_remove(rawReaction):
    if str(await client.get_channel(rawReaction.channel_id).get_message(rawReaction.message_id)).find("468411047259406366"):
        try:
            rolename = 'ping'+rawReaction.emoji.name
            role = discord.utils.get(client.get_guild(rawReaction.guild_id).roles, name=rolename)
            await client.get_guild(rawReaction.guild_id).get_member(rawReaction.user_id).remove_roles(role)
        except:
            pass

client.run('NDY4NDExMDQ3MjU5NDA2MzY2.DjdqYw.7aisjM8L6IJv-qdgTX44CO-JNps')
