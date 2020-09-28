# UDP server-client application
Simple server-client CLI application that allows sending and receiving messages using UDP protocol.
### Scenario 
The Spotify regional server warehouse provides music streaming services for the billions of
clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason,the clients must wait for responding with regarding the next time schedule:

- First interval: Between 12:00 – 17:00 the maximum wait time must be 2 seconds
- Second Interval: After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds
- Third Interval: After the 23:59 till the 12:00 of the next day the waiting time must be 1 second

The exponential backoff of these intervals must be increased by the next factors:
- For the first and third intervals: doubles each iteration
- For the second interval: triples on each iteration

### Installation
Clone this repository into your directory
``` bash
git clone https://github.com/Shakar-Gadirli/UDP_Unreliability.git
```
Install requirements for this application
``` bash
pip3 install -r requirements.txt
```
### Usage
For server and client, open 2 terminal tabs.
In the first tab, run the following command to create server.
``` bash
python3 udp_unreliability.py server ""
```
Here "" shows interface that the server accepts data coming from the client. By default, port 1060 is used, but you can specify the port by adding   **-p port_number** at the end of the command. 

In the second tab, run the following command to create client.
``` bash
python3 udp_unreliability.py client hostname
```
Here, in the place of *hostname*, you should write the hostname of your local machine. Again, default port is 1060, but you can change it by adding **-p port_number** at the end.

>To kill the process, run Ctrl + C.
