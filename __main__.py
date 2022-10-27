import argparse
import host
import peer

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('mode', choices=['host', 'peer'])
  parser.add_argument('ip', type=str)
  parser.add_argument('port', type=int)
  parsed = parser.parse_args()
  if parsed.mode == 'host':
    host.Host(parsed.ip, parsed.port).run()
  else:
    p = peer.Peer(parsed.ip, parsed.port)
    peer_id = p.register()
    print(f"peer id is {peer_id}")
    dial = input("connect to:")
    p.connect(dial)
    p.close()
