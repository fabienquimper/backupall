"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client

# Configuration
CONFIG_NETWORK_PORT_FOR_SEQUENCE = 8002

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="docker",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=CONFIG_NETWORK_PORT_FOR_SEQUENCE,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  print("Before message")
  client.send_message("/audio/shape", "786 1000 0 0 120")
  print("After message")