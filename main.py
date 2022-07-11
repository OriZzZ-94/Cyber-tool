import sys
import threading
import socket
from faker import Faker
import tkinter as tk
import hashlib
from cryptography.fernet import Fernet
import requests



# start faker
def chooseyourfakedata(choose):
    if choose == "1":
        fake = Faker(['it_IT'])
        print(fake.profile())
    elif choose == "2":
        fake = Faker(['he_IL'])
        print(fake.profile())
    elif choose == "3":
        fake = Faker(['ja_JP'])
        print(fake.profile())
    else:
        fake = Faker(['en_US'])
        print(fake.profile())

def fakergenerator():
    flag = True
    while (flag):
        choice = input("Welcome to Faker data program please choose your language:\n for italian insert 1\n for hebrew insert 2\n for japanese insert 3\n for english just press enter\n for finish insert exit\n")
        if choice != "exit":
         chooseyourfakedata(choice)
        else:
            print("bye bye\n")
            break
# end faker
# start caser
def encrypt():
    plainText = input("What is your plaintext? ")
    shift = int(input("What is your shift? "))
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter

    print ("Your ciphertext is: ", cipherText,"with a shift of",shift)


def decrypte():
    encryption=input("enter in your encrypted code")
    encryption_shift=int(input("enter in your encryption shift"))

    cipherText1 = ""
    for c in encryption:
        if c.isalpha():
            stayInAlphabet1 = ord(c) - encryption_shift
        if stayInAlphabet1 > ord('z'):
            stayInAlphabet1 += 26
        finalLetter1 = chr(stayInAlphabet1)
        cipherText1 += finalLetter1

    print ("Your ciphertext is: ", cipherText1,"with negative shift of",encryption_shift)
def caser():

    flag = True
    while (flag):
        plainText = input(
            "welcom to caser encryption & decryption program:\n for encryption insert 1\n for decryption insert 2\n for exit press enter\n  ")
        if plainText == "1":
            encrypt()
        elif plainText == "2":
            decrypte()
        else:
            print("bye bye\n")
            break
# end caser
# start vigenere

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))



def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))



def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))


# Driver code
def vigenere():
    string = input("please insert your string in capital letter:\n")
    keyword = input("please insert your keyword in capital letter:\n")
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
          originalText(cipher_text, key))
    print("bye bye\n")
# end vigenere
# start sha&fernet



def fernetencrypt(hash_string):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(hash_string)
    temp= str(token)
    print("your FERNET encrypt string is: "+temp)



def sha256encrypt(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    temp = str(sha_signature)
    print("your SHA256 encrypt string is: "+temp)

def sha256_fernet_encryptor():
    plaintext=input("Welcome to SHA256 & FERNET encryptor:\n for encrypt SHA256 insert 1\n for encrypt FERNET insert 2\n  ")
    if plaintext=="1":
        user_string=input("please insert your string:\n")
        sha256encrypt(user_string)
    elif plaintext=="2":
        user_string=input("please insert your string:\n")
        fernetencrypt(user_string.encode())

    print("bye bye")
# end sha&fernet

# start D-dos
def attack(ip, port, msg, thread_id):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print(sys.stderr, 'connecting to %s port %s' % server_address)
    sock.connect(server_address)
    try:
        # Send data
        threadmsg = 'Thread-', thread_id, ':', msg;
        message = str.encode(str(threadmsg))
        print(sys.stderr, 'thread-', thread_id, 'sending "%s"' % message)
        sock.sendall(message)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(sys.stderr, 'received "%s"' % data)
    finally:
        print(sys.stderr, 'closing socket')
        sock.close()
class myThread(threading.Thread):

    def __init__(self, threadID, name, counter,ip,port,msg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.ip = ip
        self.port = port
        self.msg = msg

    def run(self):
        print("Starting " + self.name)
        attack(self.ip, self.port, self.msg, self.threadID)
        print("Exiting " + self.name)



def ddos_attack():
    print("Welcome to DDOS ATTACK:\n ")
    ip = input("Enter ip (for localhost write localhost):")
    port = int(input("Enter port:"))
    msg = input("Enter message:")
    i = 0
    # Create new threads
    thread1 = myThread(1, "Thread-1", 1,ip,port,msg)
    thread2 = myThread(2, "Thread-2", 2,ip,port,msg)
    thread3 = myThread(3, "Thread-3", 3,ip,port,msg)
    thread1.start()
    thread2.start()
    thread3.start()
    while i<10:
         # Start new Threads
         thread1.run()
         thread2.run()
         thread3.run()
         i=i+1
    print ("Exiting Main Thread")

    print("bye bye")
# end D-dos

#Start Print soure code
def findyoursourcecode():
    url=input("Please insert your Url:")
    word=input("Please insert your word:")
    # Search GitHub's repositories for requests
    response = requests.get(url)
    # get the response text. in this case it is HTML
    html = response.text
    # parse the HTML
    index= html.find(word)
    splithtml= html.split()
    # Inspect some attributes of the `requests` repository
    # print the HTML as text
    matches = []
    words_indexes=[]
    for match in splithtml:
        if word in match:
            matches.append(match)
            words_indexes.append(match.find(word)+1)

    print("-----------URL--------\n")
    print(html)
    print("-----------END-URL--------\n\n\n")
    print("List of All Words where your word Found:")
    print(matches)
    print("List of All indexes where your word found in List of Words:")
    print(words_indexes)
    if index==-1:
        print("not found your word")
    else:
        print("your word found in index number:")
        print(index)

    print("Bye Bye")

#End print source code
#Start mssp
def calcSubsetSum(nums, i, sum, strArr):
    res = False
    if (sum == 0):
        res = True

    elif i >= len(nums):
        res = False
    else:
        res = calcSubsetSum(nums, i + 1, sum - nums[i], strArr + str(nums[i]) + " ") or calcSubsetSum(nums, i + 1, sum,
                                                                                                      strArr)
    return res


def calcSubsetSumOver(nums, sum):
    return calcSubsetSum(nums, 0, sum, "")



def cyphertext_ssp(list):
    mins=[]
    sums=[]
    for i in range(0, len(list), 1):
        mins.append(min(list[i]))
        sums.append(sum(list[i]))
    smin=max(mins)
    smax=min(sums)
    s=0
    for i in range(smin, smax, 1):
        counter = 0
        for j in range(0, len(list), 1):
            if calcSubsetSumOver(list[j],i):
                counter+=1
        if counter == len(list):
            s=i
    return s


def mssp():
    # Parameters
    cyphertext = input("please insert your cypher-text:\n")
    n = int(len(cyphertext) / int((input("how many arrays did you want to split?\n"))))
    m = int(input("how many number did you want in each array?\n"))
    d = int(input("how many digits did you want to each number?\n"))
    # Bulding the groups of numbers loop
    a = [(cyphertext[i:i + n]) for i in range(0, len(cyphertext), n)]
    for i in range(0, len(a), 1):
        a[i] = [(a[i][j:j + d]) for j in range(0, len(a[i]), d)]
    # Make list of integers for SubsetSum
    b = [[int(float(j)) for j in i] for i in a]
    # Prints
    print("your Plain-text is:\n")
    print(cyphertext_ssp(b))
    print("bye bye")
#End mssp
window = tk.Tk()
window.title("Cyber-Tool")
greeting = tk.Label(text="Welcome to the advanced hacking tool \n designed for the novice hacker who wants to become a pro\n Please select the cyber operation you want to perform: ", font="italic")
greeting.pack()
tk.Button(window, text="faker fake data", borderwidth=3, relief="raised", padx=5, pady=10,
       command=fakergenerator).pack(padx=30, pady=30)
tk.Button(window, text="source cod", borderwidth=3, relief="raised", padx=5, pady=10,command=findyoursourcecode).pack(
 padx=30, pady=30)
tk.Button(window, text="encryption SHA256&FERNET", borderwidth=3, relief="raised", padx=5, pady=10,
       command=sha256_fernet_encryptor).pack(padx=30, pady=30)
tk.Button(window, text="Caesar cipher", borderwidth=3, relief="raised", padx=5, pady=10, command=caser).pack(
 padx=30, pady=30)

tk.Button(window, text="vigenere cipher", borderwidth=3, relief="raised", padx=5, pady=10, command=vigenere).pack(
 padx=30, pady=30)
tk.Button(window, text="mssp", borderwidth=3, relief="raised", padx=5, pady=10, command=mssp).pack(padx=30,
                                                                                                pady=30)
tk.Button(window, text="DDos Attack", borderwidth=3, relief="raised", padx=5, pady=10, command=ddos_attack).pack(
 padx=30, pady=30)

window.mainloop()
