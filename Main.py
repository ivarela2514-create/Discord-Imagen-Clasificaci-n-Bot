import discord
from discord.ext import commands
from Model import model


# Crear el bot con intención de miembros
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ha iniciado sesión correctamente')

@bot.command()
async def revisar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./images/{file_name}") 
            await ctx.send("Estamos Guardando tu archivo y lo estamos analizando...") 
            class_name, confidence_score = model("model.h5", "labels.txt", f"./images/{file_name}")
            await ctx.send(f"El resultado de tu imagen es: {class_name} con una confianza de {confidence_score:.2f}")
            
    else:
        await ctx.send("Envie una imagen para poder revisarla :P.") 

bot.run('MTQzMjUwNDkwMDUxNTkyNjA2Ng.GyDaUo.bCACWrsoRw0OpOWGlOwb74WXS5lOOOLqTF3FHI')

#               ____         ____
#              /    \       /    \
#
#
#           \\   \            /   \\
#                 \____/\____/
#                    



