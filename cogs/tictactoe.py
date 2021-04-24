from discord.ext import commands
import discord
import random

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


class Startup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # noinspection PyGlobalUndefined
    @commands.command(aliases=['ttt'])
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver
        if ctx.channel.id == ***REMOVED***:
            if gameOver:
                global board
                board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                turn = ""
                gameOver = False
                count = 0

                player1 = p1
                player2 = p2
                self.tictactoe.user1 = p1.id
                self.tictactoe.user2 = p2.id

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                num = random.randint(1, 2)
                if num == 1:
                    turn = player1
                    await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
                elif num == 2:
                    turn = player2
                    await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.send("A game is already in progress! Finish it before starting a new one.")
        else:
            await ctx.send(f"You can play this game in <#{***REMOVED***}> only!")

    # noinspection PyGlobalUndefined
    @commands.command()
    async def place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count

        if ctx.channel.id == ***REMOVED***:
            if not gameOver:
                mark = ""
                if turn == ctx.author:
                    if turn == player1:
                        mark = ":regional_indicator_x:"
                    elif turn == player2:
                        mark = ":o2:"
                    if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                        board[pos - 1] = mark
                        count += 1

                        line = ""
                        for x in range(len(board)):
                            if x == 2 or x == 5 or x == 8:
                                line += " " + board[x]
                                await ctx.send(line)
                                line = ""
                            else:
                                line += " " + board[x]

                        checkWinner(winningConditions, mark)
                        if gameOver:
                            await ctx.send(mark + " wins!")
                        elif count >= 9:
                            await ctx.send("It's a tie!")

                        if turn == player1:
                            turn = player2
                        elif turn == player2:
                            turn = player1
                    else:
                        await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
                else:
                    await ctx.send("It is not your turn.")
            else:
                await ctx.send("Please start a new game using the !tictactoe command.")
        else:
            await ctx.send(f"You can play this game in <#{***REMOVED***}> only!")

    @commands.command()
    async def endgame(self, ctx):
        global player1
        global player2
        global gameOver
        if ctx.channel.id == ***REMOVED***:
            if not gameOver:
                users = [self.tictactoe.user1, self.tictactoe.user2, ***REMOVED***, 779346424890130504,
                         713317312488275978,
                         596747974659538964, ***REMOVED***]
                if ctx.author.id in users:
                    gameOver = True
                    await ctx.send("Game session interrupted. No winner!")
                else:
                    await ctx.send("This command can only be used by current players and admins.")
            else:
                await ctx.send("Please start a new game using the !tictactoe command.")
        else:
            await ctx.send(f"You can play this game in <#{***REMOVED***}> only!")

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@***REMOVED***>).")

    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")


def setup(bot):
    bot.add_cog(Startup(bot))
