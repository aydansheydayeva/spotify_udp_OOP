# About app

This application is simple client-server CLI model that exchange information based on UDP protocol. It uses OOP based approach to create client and server objects.

## Scenario

The Spotify regional server warehouse provides music streaming services for the billions of clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason, the clients must wait for responding with regarding the next **time schedule**:

- **First interval:** Between 12:00 – 17:00 the maximum wait time must be 2 seconds

- **Second Interval:** After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds

- **Third Interval:** After the 23:59 till the 12:00 of the next day the waiting time must be 1 second


The **exponential backoff** of these intervals must be increased by the next factors: 

- For **the first and third** intervals: doubles each iteration
- For **the second interval**: triples on each iteration 

## Installation

To download app, you need to type following command:

```bash
git clone https://github.com/aydansheydayeva/spotify_udp_OOP
```
 Then install requirements to have all packets needed for this project:

```bash
pip install requirements.txt
```

## Usage

To use this app, 2 terminals should be opened. Next 2 commands should be run in terminals:

**First terminal:**
```
python3 spotify_OOP.py server "" -p 5555
```
Here "" represents the interface for server to accept incoming data and "-p" is for port number. In this example, port is 5555. If not mentioned, port selected by default is 4444.

**Second terminal:**
```
python3 spotify_OOP.py client hostname -p 5555
```
Here instead of "hostname", hostname of your local machine should be written. Default port to connect is 4444.