from .oneletteronly import OneLetterOnly

def setup(bot):
    bot.add_cog(OneLetterOnly(bot))