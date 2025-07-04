# rail_sec_sim
simulator of attacks and security in the train-control system

The system demonstrates how encrypted and signed messages can be sent from a train to a control center and how attacks such as message tampering or spoofing can be detected.
It focuses on basic concepts: encryption, integrity checks, spoofing detection, and basic secure protocols.


Trains send signed and encrypted messages (ID, location, speed) via sockets.
![Form Screenshot](train.png)
![Form Screenshot](train_1.png)

The control center decrypts and verifies each message.
![Form Screenshot](control_center_1.png)

A simulated attacker sends tampered or spoofed messages.
![Form Screenshot](attacker.png)
![Form Screenshot](attacker1.png)

The system detects and logs successful messages and cyber attacks.
![Form Screenshot](control_center_1.png)
![Form Screenshot](control_center_4.png)

Includes a Tkinter dashboard for real-time monitoring (status, counters, last train).
![Form Screenshot](secure_train_monitoring.png)








