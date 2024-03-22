num_word = int(input())
list_word = []
for i in range(num_word):
    list_word.append(input())

connected_words = []
for i in range(len(list_word)):
    if not len(list_word[i]) < 2:
        end_two_letters = list_word[i][-2:]
        for x in range(len(list_word)):
            if not list_word[i] == list_word[x] and not len(list_word[i]) < 2:
                first_two_letters = list_word[x][:2]
                if end_two_letters == first_two_letters:
                    piece1 = list_word[i][:-2]
                    piece2 = list_word[x]
                    connected_word = piece1 + piece2
                    connected_words.append(connected_word)

if not len(connected_words):
    print(-1)
else:
    longest_connected_word = max(connected_words, key=len)
    print(len(longest_connected_word))



import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
