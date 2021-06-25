# IMPORTS
import discord
from discord.ext import commands
import random
import json
import os
import asyncio
from keep_alive import keep_alive
from commands_general import *
from commands_coinbot import *

bot = commands.Bot(command_prefix=('coin ', 'Coin ', 'coin.', 'Coin.'), case_insensitive=True)

#COMMANDS - Test command

shop_icon = 'https://i.pinimg.com/736x/f1/ec/be/f1ecbe2fa9f2be67baa42812f070f3a6.jpg'
bank_icon = 'https://i.pinimg.com/originals/f1/7e/77/f17e77823de96021c63f8bc58f4e1356.jpg'

# COMMANDS - GeneralBot (Bot)

@bot.event
async def ready():
    print('The bot is online!')


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send('You are on cooldown. Wait for **{:.2f} seconds and try again.**'.format(error.retry_after))


@bot.command()
async def invite(ctx):
  await invite.invite(ctx)


@bot.command()
async def rickroll(ctx):
  await commands_general.rickroll_message(ctx)


@bot.command()
async def facepalm(ctx, username):
  if username == None:
    user = ctx.author.name 
    await commands_general.facepalm_message(ctx, user)
  else:
    await commands_general.facepalm_message(ctx, username)

@bot.command()
async def meme(ctx):
    await commands_general.meme_message(ctx)

@bot.command()
async def joke(ctx):
    await commands_general.joke_message(ctx)

@bot.command()
@commands.has_any_role(836230938827554857)
async def giveaway(ctx):
    await ctx.send(
        f'{ctx.author.name}, You have started the giveaway. Before I can start, **let me ask 3 questions.**'
    )
    asyncio.sleep(1)
    await ctx.send('Respond quickly in 15 seconds!')

    questions = [
        '**Which channel** should I post it in?',
        'What should be **the duration** of this giveaway? (in s/m/h/d)',
        'What is the **prize of the giveaway?**'
    ]

    answers = []

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    for question in questions:
        embed = discord.Embed(title=f'Questions',
                              description=f'{question}',
                              color=0x006AFF)

        await ctx.send(embed=embed)
        try:
            msg = await bot.wait_for('message', timeout=15, check=check)

        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time!')
            return

        else:
            answers.append(msg.content)

    try:
        channel_id = int(answers[0][2:-1])
    except:
        await ctx.send(
            f'You did not mention the channel properly! do it like this: {ctx.channel.mention}'
        )
        return

    channel = bot.get_channel(channel_id)

    giveaway_time = commands_general.convert_the_time(answers[1])
    if giveaway_time == -1:
        await ctx.send(
            f'You did not answer it properly! use s/m/h/d for the task.')
        return

    elif giveaway_time == -2:
        await ctx.send('Time must be an integer!')

    prize = answers[2]
    await ctx.send(
        f'The giveaway has started in {channel.mention} and will last for {answers[1]} seconds!'
    )

    embed = discord.Embed(title='A wild Giveaway has started!',
                          description=f'Prize: \n{prize}',
                          color=0x006AFF)

    embed.add_field(name='Event ends:',
                    value=f'{answers[1]} seconds from now.')
    embed.set_footer(text=f'Hosted by {ctx.author.name}')

    giveaway_msg = await channel.send(embed=embed)
    await giveaway_msg.add_reaction('🎉')
    await asyncio.sleep(giveaway_time)

    new_msg = await channel.fetch_message(giveaway_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)

    embed = discord.Embed(
        title='Winner of the giveaway',
        description=f'The winner of this giveaway is {winner.name}!',
        color=0x006AFF)
    embed.add_field(name='Prize', value=f'{prize}', inline=False)

    await channel.send(embed=embed)


#COMMANDS - CoinBot
@bot.command()
async def bank(ctx):
    await commands_coinbot.open_account(ctx.author)
    user = ctx.author
    users = await commands_coinbot.get_bank_data()

    wallet_amt = users[str(user.id)]['Wallet']
    bank_amt = users[str(user.id)]['Bank']

    await ctx.send(embed = commands_coinbot.bank_message(ctx.author, wallet_amt, bank_amt, bank_icon))


@bot.command()
async def work(ctx):
    await commands_coinbot.work_message(ctx)


@bot.command()
@commands.has_any_role(817746669977993246, 814157402701037619,
                       817746566919225355, 793733745336516629,
                       817746474188013588, 817746389202108416)
async def add(ctx, coins, user: discord.Member, amount=None):
    if coins != 'coins':
        await ctx.send(
            f'The command "add {coins}" does not exist. the only one in existence is sdr add coins <user name> <amount of coins>. \n(P.S. Make sure to remove the <> signs.)'
        )
        return

    else:
        await commands_coinbot.open_account(user)
        users = await commands_coinbot.get_bank_data()

        amount = int(amount)
        wallet_amt = users[str(user.id)]['Wallet']

        if amount == None:
            await ctx.send(
                f'**Please give a valid amount of money to add to {user}\'s bank account.**'
            )
            return

        if amount < 0:
            await ctx.send(
                'You cannot add negative amounts of money to an account.')
            return

        bank_amt = users[str(user.id)]['Bank']
        bank_amt += amount
        await ctx.send(
            f'{amount} <:SDRCoin:850353434061307924> have been added to {user}\'s bank account. (More specifically, his bank.)'
        )

        await commands_coinbot.addcoins(user, amount)
        
        asyncio.sleep(1)
        await ctx.send('Preview: ')
        embed = discord.Embed(title=f'{user}\'s Bank account', color=0x006AFF)
        embed.add_field(
            name='Wallet',
            value=
            f'You currently have {wallet_amt} <:SDRCoin:850353434061307924>, {user}!',
            inline=False)
        embed.add_field(name='Bank',
                        value=f'{bank_amt} <:SDRCoin:850353434061307924>',
                        inline=False)
        embed.set_thumbnail(url=bank_icon)
        await ctx.send(embed=embed)


@bot.command()
@commands.has_any_role(817746669977993246, 814157402701037619,
                       817746566919225355, 793733745336516629,
                       817746474188013588, 817746389202108416)
async def remove(ctx, coins, user: discord.Member, amount=None):
    if coins != 'coins':
        await ctx.send(
            f'The command "add {coins}" does not exist. the only on ein existence is sdr add coins <user name> <amount of coins>. \n(P.S. Make sure to remove the <> signs.)'
        )
        return

    else:
        await commands_coinbot.open_account(user)
        users = await commands_coinbot.get_bank_data()

        amount = int(amount)
        wallet_amt = users[str(user.id)]['Wallet']

        if amount == None:
            await ctx.send(
                f'**Please give a valid amount of money to add to {user}\'s bank account.**'
            )
            return

        if amount < 0:
            await ctx.send(
                'You can remove negative amounts of money, but not here to an account.'
            )
            return

        bank_amt = users[str(user.id)]['Bank']
        bank_amt -= amount
        await ctx.send(
            f'{amount} <:SDRCoin:850353434061307924> have been added to {user}\'s bank account. (More specifically, his bank.)'
        )
        asyncio.sleep(1)
        await ctx.send('Preview: ')
        embed = discord.Embed(title=f'{user}\'s Bank account', color=0x006AFF)
        embed.add_field(
            name='Wallet',
            value=
            f'You currently have {wallet_amt} <:SDRCoin:850353434061307924>, {user}!',
            inline=False)
        embed.add_field(name='Bank',
                        value=f'{bank_amt} <:SDRCoin:850353434061307924>',
                        inline=False)
        embed.set_thumbnail(url=bank_icon)
        await ctx.send(embed=embed)

        await commands_coinbot.addcoins(user, amount, 'Bank')
        with open('bank.json', 'w') as f:
            json.dump(users, f)


@bot.command()
async def withdraw(ctx, amount=None):
    await commands_coinbot.open_account(ctx.author)
    user = ctx.author
    users = await commands_coinbot.get_bank_data()

    if amount == None:
        await ctx.send('**Please enter an amount of currency to withdraw.**')
        return

    if amount == 'all' or 'All' == True:
        amount = users[str(user.id)]['Bank']

    bal = await commands_coinbot.addcoins(ctx.author)
    amount = int(amount)

    if amount > bal[1]:
        await ctx.send(
            'You don\'t have enough money stored to withdraw. The ability to take a loan will be added later!'
        )
        return

    if amount < 0:
        await ctx.send('Did you expect to withdraw negative money dude')
        return

    await commands_coinbot.addcoins(ctx.author, amount)
    await commands_coinbot.removecoins(ctx.author, amount, 'bank')
    await ctx.send(
        f'**{ctx.author.name}**, you withdrew {amount} <:SDRCoin:850353434061307924> from your bank account.'
    )


@bot.command()
async def deposit(ctx, amount=None):
    await commands_coinbot.open_account(ctx.author)
    users = await commands_coinbot.get_bank_data()
    user = ctx.author

    if amount == None:
        await ctx.send('**Please enter an amount of currency to withdraw.**')
        return

    if amount == 'all' or 'All' == True:
        amount = users[str(user.id)]['Wallet']

    bal = await commands_coinbot.addcoins(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You don\'t have enough money stored to deposit.')
        return

    if amount < 0:
        await ctx.send('Did you expect to deposit negative money dude')
        return

    await commands_coinbot.removecoins(ctx.author, amount)
    await commands_coinbot.addcoins(ctx.author, amount, 'bank')
    await ctx.send(
        f'**{ctx.author.name}**, you deposited {amount} <:SDRCoin:850353434061307924> to your bank account.'
    )


@bot.command()
async def transfer(ctx, member: discord.Member, amount=None):
    await commands_coinbot.open_account(ctx.author)
    await commands_coinbot.open_account(member)

    if amount == None:
        await ctx.send('**Please enter an amount of currency to withdraw.**')
        return

    bal = await commands_coinbot.addcoins(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send(
            'You don\'t have enough money stored to withdraw. The ability to take a loan will be added later!'
        )
        return

    if amount < 0:
        await ctx.send('Did you expect to have negative money dude')
        return

    await commands_coinbot.removecoins(ctx.author, amount, 'bank')
    await commands_coinbot.addcoins(member, amount, 'bank')
    await ctx.send(
        f'**{ctx.author.name}**, you tranferred {amount} <:SDRCoin:850353434061307924> to {member}\'s bank account.'
    )


@bot.command()
async def donate(ctx, member: discord.Member, amount=None):
  pass



# SETUP
keep_alive()
my_secret = os.environ['TOKEN']
bot.run(my_secret)