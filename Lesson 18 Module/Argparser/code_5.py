# Default Argument
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", default="Guest")

args = parser.parse_args()

print("Hello", args.name)