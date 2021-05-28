from random import *
import datetime
import locale
import discord
from discord.ext import commands

locale.setlocale(locale.LC_TIME, "fr_FR")

token = ""

bot = commands.Bot(command_prefix='!', help_command=None)


@bot.event
async def on_ready():
    print(bot.user.name, "est connect")
    print(bot.user.id)
    print('------')
    print(" ")
    print(" ")
    print(bot.user.name + ".py")
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("Hey !"))


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    vip_role = discord.utils.get(bot.get_guild(payload.guild_id).roles, name="VIP")

    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 831273331999113266 and message == 831273381969133568 and emoji == "👍":
        print("grade ajouté")
        await member.add_roles(vip_role)
        await member.send("tu obtient le grade VIP ")


@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    vip_role = discord.utils.get(bot.get_guild(payload.guild_id).roles, name="VIP")
    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 708681605321064529 and message == 708681709822148750 and emoji == "👍":
        print("garde suprimé")
        await member.remove_roles(vip_role)
        await member.send("tu pers le grade VIP")


@bot.command()
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, reason=None):
    if reason is None:
        await ctx.send(f"Woah {ctx.author.mention},donner une raison")
    else:
        messageok = f"tu as été banni par {ctx.author.mention} pour {reason}"
        messagein = f"{ctx.author.mention} a banni {member}"
        await ctx.channel.send(messagein)
        await member.send(messageok)
        await member.ban(reason=reason)


@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, member_name: discord.Member):
    message = f"{ctx.author.mention} a kick {member_name.mention}"
    messagein = f"tu as été kick du serveur par {ctx.author.mention}"
    await member_name.kick()
    await ctx.channel.send(message)
    await member_name.send(messagein)


@bot.command()
async def clear(ctx, n_msg):
    n_msg = int(n_msg)
    await ctx.channel.purge(limit=n_msg + 1)


@bot.command()
async def heure(ctx):
    await ctx.channel.send(str(datetime.datetime.now().strftime("%H" "h" "%M" "m" "%S" "s")))


@bot.command()
async def date(ctx):
    await ctx.channel.send(str(datetime.datetime.now().strftime("On est le %A %d %B %Y")))


@bot.command()
async def code(ctx):
    await ctx.channel.send("```""coucou""```")


@bot.command()
async def help(ctx):
    await ctx.channel.send(embed=discord.Embed(title="!Help", color=discord.Color.dark_blue(), description="""```
-heure affichage de l'heure 
-date: affichage de la date 
-code envoie d'un message textuel
-clear supression d'un ou plusieurs message
-ping afficher son ping
-invite affiche une invitation du serveur
-dev affichage d'un site de developpment
-python affichage d'un site pour télécharger python
-ban_all commande pour bannir tous les membres du serveurs discord
-mute_eddedy commande permetant de mute le roi
-jeux pour lancer un jeu du plus ou du moins (pas encore opérationnel)```"""))


@bot.command()
async def ping(ctx):
    await ctx.send(str(round(bot.latency, 3) * 1000) + "ms")


@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age=300, max_uses=0)
    await ctx.send(link)


@bot.command()
async def dev(ctx):
    await ctx.channel.send("https://www.learndev.info/fr")


@bot.command()
async def python(ctx):
    await ctx.channel.send("https://docs.python.org/fr/3/")


@bot.command()
async def ban_all(ctx):
    await ctx.channel.send("vasi vous zète tous ban")


@bot.command()
async def mute_eddedy(ctx):
    await ctx.channel.send("non, tu ne peux pas mute le maître 'xD comme il dit' ")


@bot.command(pass_context=True)
@commands.has_role("Admin")
async def mute(ctx, member: discord.Member = None):
    if member is None:
        await ctx.channel.send('rentrez un pseudo valide')
        return
    member = ctx.message.author
    role = discord.client.create_role(member.roles, name="muted")
    await ctx.channel.send(f"{str(member)} a était muté")
    await bot.add_roles(member, role)


@bot.command()
async def jeux(ctx):
    mystere3 = randrange(0, 1000)
    mystere2 = randrange(0, 100)
    mystere1 = randrange(0, 20)

    running = True

    await ctx.channel.send("niveau 1: 0 à 20")
    await ctx.channel.send("niveau 2: 0 à 100")
    await ctx.channel.send("niveau 3: 0 à 1000")

    saisie = int(input("Entrez le niveau de difficulté"))

    if saisie == 1:
        await ctx.channel.send("Le plus simple bien sûr !")
        input("Appuyer sur entrer pour continuer...")
        while running:
            saisie1 = int(input("Entrez un nombre entre 0 et 20"))
            if saisie1 < mystere1:
                await ctx.channel.send("C'est plus")
            elif saisie1 > mystere1:
                await ctx.channel.send("C'est moins")
            else:
                await ctx.channel.send("Bravo tu as gagné !")
                running = False

    if saisie == 2:
        await ctx.channel.send("ça commence à être pas mal !")
        input("Appuyer sur entrer pour continuer...")
        while running:
            saisie2 = int(input("Entrez un nombre entre 0 et 100"))
            if saisie2 < mystere2:
                await ctx.channel.send("C'est plus")
            elif saisie2 > mystere2:
                await ctx.channel.send("C'est moins")
            else:
                await ctx.channel.send("Bravo tu as gagné !")
                running = False

    if saisie == 3:
        await ctx.channel.send("Bonne chance pour celui là !")
        input("Appuyer sur entrer pour continuer...")
        while running:
            saisie3 = int(input("Entrez un nombre entre 0 et 1000"))
            if saisie3 < mystere3:
                await ctx.channel.send("C'est plus")
            elif saisie3 > mystere3:
                await ctx.channel.send("C'est moins")
            else:
                await ctx.channel.send("Bravo tu as gagné !")
                running = False

    input("Appuyer sur entrer pour fermer...")

bot.run(token)

