from foxdie.agents import Agent
from foxdie.servers import Server
from ipaddress import IPv4Address
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", type = str, choices = ["server", "agent"])
    parser.add_argument("-a", "--address", type = IPv4Address, required = True)
    parser.add_argument("-p", "--port", type = int, required = True)
    args = parser.parse_args()
    if args.mode == "server":
        server = Server(address = args.address, port = args.port)
        server.start()
    elif args.mode == "agent":
        agent = Agent()
        agent.connect(address = args.address, port = args.port)
    else:
        parser.print_help()