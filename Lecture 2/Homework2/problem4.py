import argparse
parser = argparse.ArgumentParser()
parser.add_argument("text", help="text", type=str)
text="Welcome to USA. usa is awesome, isn’t it?"
print("The given text:", text)
print("The USA count is:", text.upper().count("USA"))
print("The new text:", text.replace("USA", "Armenia").replace("usa", "Armenia"))
args = parser.parse_args()