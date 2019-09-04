import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="text", type=str)
parser.add_argument("Meline", help="word", type=str)
parser.add_argument("Astine", help="word", type=str)
text="I am Meline Ayvazyan"
print("The given text:", text)
print("Output string:", text.replace("Meline", "Astine"))
args = parser.parse_args()