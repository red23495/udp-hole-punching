import socket
import json
import asyncio
import aioconsole
import threading

class Peer:

  def __init__(self, host_ip, host_port):
    self._host_ip = host_ip
    self._host_port = host_port
    self.id = None
    self.connection = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
  
  def register(self):
    self.connection.sendto(b"add", (self._host_ip, self._host_port))
    # warning: ignoring the possibility of receiving data from connection other than host
    data, addr = self.connection.recvfrom((1<<16)-1)
    self.id = data
    return data

  def connect(self, peer_id):
    self.connection.sendto(f"get {peer_id}".encode("ascii"), (self._host_ip, self._host_port))
    peer, addr = self.connection.recvfrom((1<<16)-1)
    ip, port = peer.decode("utf-8").split(" ")
    port = int(port)
    print(f"resolved {peer_id} to {ip}:{port}")
    async def task():
      await self.ainput((ip, port))
    t1 = threading.Thread(target=asyncio.run, args=(task(),))
    t2 = threading.Thread(target=self.listen)
    t1.start()
    t2.start()
    t2.join()

  async def ainput(self, peer):
    while True:
      message = await aioconsole.ainput()
      self.connection.sendto(message.encode("ascii"), peer)

  def listen(self):
    while True:
      data, addr = self.connection.recvfrom((1<<16)-1)
      print(f"{addr[0]}:{addr[1]}: ", data.decode("utf-8"))

  def close(self):
    self.connection.close()

  

