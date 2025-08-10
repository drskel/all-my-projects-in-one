# made by skel67
from sherlockbyskel67 import user
from starinturtle import star
from coolerHelloWorld import helloworld
from passwordgen import generate_password
from randomasciidrawing import random_ascii_drawing
from ddos import ddos 
from randomsonginspotify import random_song_on_spotify
def prmain():
    print('welcome to my projects')
    print('here i will show every project ive made that hasnt been lost')
    print('1. sherlockbyskel67')
    print('2. star draeing in turtle(not very good)')
    print('3. hello world in a cooler way')
    print('4. password generator')
    print('5. random ascii drawing')
    print('6. DDoS script (use responsibly)')
    print('7. random song on spotify')
    ask = input('\n\nwhich project would you like to see? ')
    if ask == '1':
        user(username=input('Made By skel67\nenter user: ').strip())
    elif ask == '2':
        star()
    elif ask == '3':
        helloworld()
    elif ask == '4':
        password_length = int(input("Enter the desired password length (MUST BE OVER 10): "))
        if password_length < 10:
            print("Warning: Password length is less than 10 characters, which may not be secure.")
        else:
            print("Your password is secure.")
        print("Generated Password:", generate_password(password_length))
    elif ask == '5':
    
        print(random_ascii_drawing())
    elif ask == '6':
        url = input("Enter the URL to DDoS (e.g., http://example.com): ").strip()
        num_requests = int(input("Enter the number of requests to send: "))
        ddos(url, num_requests)
        print("DDoS attack initiated. Use responsibly!")
    elif ask == '7':
        print("Opening a random song on Spotify...")
        song = random_song_on_spotify()
        print(f"Now playing: {song}")
    else:
        print('project not found')
        return

if __name__ == '__main__':
    prmain()