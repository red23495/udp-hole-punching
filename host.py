import socket
import json

class Host:

  def __init__(self, ip: str, port: int):
    self._peers = []
    self._ip = ip
    self._port = port
    self.connection = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
    self.connection.bind((self._ip, self._port,))

  
  def run(self):
    print(f"Listening at {self._ip}:{self._port}")
    while True:
      data, addr = self.connection.recvfrom((1<<16)-1)
      self.execute(addr, *data.decode('utf-8').split(' '))
      

  def execute(self, address, command, *args):
    try:
      getattr(self, f"exec_{command.lower()}")(address, *args)
    except:
      print(f"failed to execute command {command}")

  def exec_add(self, address, *args):
    self._peers.append(address)
    print(f"registered {address} as {len(self._peers)}")
    self.connection.sendto(json.dumps(len(self._peers)).encode('ascii'), address)

  def exec_get(self, address, peer_id, *args):
    print(f"peers, {peer_id}, {self._peers}")
    peer = self._peers[int(peer_id)-1]
    self.connection.sendto(f"{peer[0]} {peer[1]}".encode('ascii'), address)

