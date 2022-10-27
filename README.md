# udp-hole-punching
My attempt on udp hole punching

This project demonstrates a simple p2p chat application that exploits udp hole punching.
There are 2 types of entity. Host is the public entity behind a public ip. It reveals the host and ports number of any peer to other peers. 
The other entity, peer, first needs to register to the host. Host assigns them peer id after registration. Later, other peers can connect to this peer using peer id.
