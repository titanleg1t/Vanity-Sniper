import requests
import time
import os
from datetime import datetime
from pystyle import Colors, Colorate, Center

# ds: titanlegit

class VanitySniper:
    def __init__(self):
        self.vanity = input(Colorate.Vertical(Colors.purple_to_blue, "what vanity u want? (no discord.gg/): "))
        self.webhook = input(Colorate.Vertical(Colors.purple_to_blue, "enter webhook url: "))
        self.check_time = 15
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        banner = """
 ██▒   █▓ ▄▄▄       ███▄    █  ██▓▄▄▄█████▓▓██   ██▓     ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███
▓██░   █▒▒████▄     ██ ▀█   █ ▓██▒▓  ██▒ ▓▒ ▒██  ██▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░  ▒██ ██░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░ ▓██▓ ░   ░ ▐██▓░     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ �ew██▀▀█▄
   ▒▀█░   ▓█   ▓██▒▒██░   ▓██░░██░  ▒██▒ ░   ░ ██▒▓░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
   ░ ▐░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓    ▒ ░░      ██▒▒▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░    ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░    ░     ▓██ ░▒░    ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
     ░░    ░   ▒      ░   ░ ░  ▒ ░  ░       ▒ ▒ ░░     ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░
      ░        ░  ░         ░  ░            ░ ░              ░           ░  ░              ░  ░   ░
     ░                                      ░ ░                    ds @titanlegit     gh @titanleg1t  V1
       """
        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, banner)))

        info = f"""
╔════════════════════════════════════════════════════════════════╗
║ watching: discord.gg/{self.vanity:<44} ║
║ status: checking...                                            ║
║ check every: {self.check_time} sec{' ' * 43} ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, info)))

    def get_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        return Colorate.Vertical(Colors.purple_to_blue, current_time)

    def checkvan(self):
        url = f"https://discord.com/api/v9/invites/{self.vanity}"

        try:
            r = self.session.get(url)

            if r.status_code == 404:
                return True, "free"
            elif r.status_code == 200:
                return False, "taken"
            else:
                return None, f"weird status: {r.status_code}"

        except Exception as e:
            return None, f"error: {str(e)}"

    def log(self, status, msg):
        time_str = self.get_time()

        if status == "checking":
            print(f"{time_str} {Colorate.Vertical(Colors.yellow, '[CHECKING]')} {msg}")
        elif status == "taken":
            print(f"{time_str} {Colorate.Vertical(Colors.red, '[TAKEN]')} {msg}")
        elif status == "free":
            print(f"{time_str} {Colorate.Vertical(Colors.green, '[AVAILABLE]')} {msg}")
        elif status == "error":
            print(f"{time_str} {Colorate.Vertical(Colors.red, '[ERROR]')} {msg}")
        elif status == "info":
            print(f"{time_str} {Colorate.Vertical(Colors.blue, '[INFO]')} {msg}")

    def send_webhook(self):
        embed = {
            "title": "Vanity Available!",
            "description": f"The vanity `discord.gg/{self.vanity}` is now available!",
            "color": 0x00ff00,
            "fields": [
                {
                    "name": "Vanity",
                    "value": f"discord.gg/{self.vanity}",
                    "inline": True
                },
                {
                    "name": "Timestamp",
                    "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "inline": True
                }
            ],
            "footer": {
                "text": "Vanity Sniper by titanlegit"
            }
        }
        data = {
            "embeds": [embed]
        }
        try:
            response = requests.post(self.webhook, json=data)
            if response.status_code == 204:
                self.log("info", "webhook sent!")
            else:
                self.log("error", f"webhook failed: {response.status_code}")
        except Exception as e:
            self.log("error", f"webhook error: {str(e)}")

    def wait(self, seconds):
        for i in range(seconds, 0, -1):
            wait_text = Colorate.Vertical(Colors.purple_to_blue, f"checking again in {i} sec...")
            print(f"{self.get_time()} {Colorate.Vertical(Colors.yellow, '[WAITING]')} {wait_text}", end='\r')
            time.sleep(1)
        print(' ' * 80, end='\r')

    def start(self):
        self.clear_screen()
        self.banner()

        self.log("info", "starting to watch vanity...")
        self.log("info", f"watching: discord.gg/{self.vanity}")
        print(Colorate.Vertical(Colors.purple_to_blue, "━" * 60))

        check_count = 0

        try:
            while True:
                check_count += 1

                self.log("checking", f"check #{check_count}")

                is_free, msg = self.checkvan()

                if is_free is True:
                    self.log("free", f"discord.gg/{self.vanity} is free now!")
                    self.send_webhook()
                    break

                elif is_free is False:
                    self.log("taken", f"discord.gg/{self.vanity} is taken")
                else:
                    self.log("error", f"check failed: {msg}")

                if check_count % 5 == 0:
                    self.wait(5)
                else:
                    self.wait(self.check_time)

        except KeyboardInterrupt:
            self.log("info", "stopped watching")
        except Exception as e:
            self.log("error", f"something broke: {str(e)}")

def main():
    try:
        vs = VanitySniper()
        vs.start()
    except Exception as e:
        print(Colorate.Vertical(Colors.purple_to_blue, f"big error: {str(e)}"))
        input("enter to close..")

if __name__ == "__main__":
    main()
