import bot as b
import os 
TOKEN = os.getenv('TOKEN')

def main():
    b.bot.run(TOKEN)

if __name__ == "__main__":
    main()