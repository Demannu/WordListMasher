import sys, argparse, os

# Configure Application Arguments
parser = argparse.ArgumentParser(description='Combines wordlists to form more complex ones')
parser.add_argument("wordlist1", help="First wordlist input path")
parser.add_argument("wordlist2", help="Second wordlist input path")
parser.add_argument("destination", help="Output file destination")
parser.add_argument("-n", "--number", help="Enable number generation after mutation", type=int)
args = parser.parse_args()

# Set Variables
word1 = args.wordlist1
word2 = args.wordlist2 
dest = args.destination

# Banner Setup
print ("##################################")
print ("#      Python WordList Masher    #")
print ("#         Author: Demannu        #")
print ("# Github: Demannu/WordListMasher #")
print ("##################################")

# Perform File Actions
wordList1 = open(word1, 'r')
wordList2 = open(word2, 'r')
wordListMerge = open("tmp", 'w')
wordListMerge.close()
wordListMerge = open("tmp", 'a')
wordListFinal = open(dest, 'w')
wordListFinal.close()
wordListFinal = open(dest, 'a')

print ("[INFO] Input: " + word1)
print ("[INFO] Input: " + word2)
print ("[INFO] Output: " + dest)
print ("[INFO] Num Range: 0-" + str(args.number))

print ("[INFO] Starting List1 + List2 Merge")
for line in wordList1:
	line = line.rstrip()
	for line2 in wordList2:
		line2 = line2.rstrip() 
		wordListMerge.write(line + line2 + "\n")
		wordList2 = open("wordList2")
	wordList1 = open("wordList1")
print("[INFO] Completed L1 + L2 Merge")

print("[INFO] Starting List2 + List1 Merge")
for line in wordList2:
	line = line.rstrip()
	for line2 in wordList1:
		line2 = line2.rstrip() 
		wordListMerge.write(line + line2 + "\n")
		wordList1 = open("wordList1")
	wordList2 = open("wordList2")
print("[INFO] Completed L2 + L1 Merge")

if args.number:
	print("[INFO] Starting Number Addition")
	wordListMerge = open("tmp", 'r')
	for line in wordListMerge:
		line = line.rstrip()
		for number in range(0, args.number):
			wordListFinal.write(line + str(number) + "\n")
		wordListMerge = open("tmp", 'r')
	print("[INFO] Finished number addition")
	wordListMerge.close()
	os.remove("tmp")
else:
	wordListMerge = open("tmp", 'r')
	for line in wordListMerge:
		line = line.rstrip()
		wordListFinal.write(line)
	wordListMerge.close()
	os.remove("tmp")
print("[INFO] Completed Merge: View " + dest + " for complete wordlist")