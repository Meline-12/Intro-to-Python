import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="text", type=str)
parser.add_argument("word1", help="word", type=str)
parser.add_argument("word2", help="word", type=str)
args = parser.parse_args()

if args.str.find(args.word_1)==-1:
    print("There is no such word in the text")
else:
    print("The given text:", args.text)
    print("First word:", args.word1)
    print("Second word:", args.word2)
    print("Output string:", args.text.replace("word1", "word2"))
