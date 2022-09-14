# Overview
A malicious network actor (e.g., malware or an intruder) on a local network will attempt to find open ports as a way to discover information about a system and gain entry into it. One of the ways to detect this activity is with a honey pot. This is a specialized open port disguised as a legitimate service for the purpose of catching and alerting malicious or undesired activity.

In this article, we use Python and its socket library to develop a honey pot. There are many different paths to take when developing a honey pot. One can go as far as fully emulating a particular service (i.e., ftp) and allowing the bad actor to download false or potentially dangerous files (e.g., launch malware on your neighbor's network in retribution for him or her jumping onto yours).

In this article, we're going to meet the following goals:

Create a Python listener on an IPv4 known port address (telnet) using sockets
Show that nmap discovers our honey pot
Alert us when our honey pot is accessed: occurrence of a TCP (SYN/ACK) handshake
With just this basic, simple Python script, we can be alerted to malicious activity on our network.

![Alt text](images/network-honeypot.png?raw=true "Title")

