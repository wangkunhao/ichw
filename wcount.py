#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wangkunhao"
__pkuid__  = "1800011715"
__email__  = "1800011715@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def count(lines):
    words = []
    word = []
    state = 0
    nums = dict()
    for letter in lines:
        a = ord(letter)
        if 65 <= a <=90 or 97 <= a <= 122 or a == 39:
            word.append(letter)
            state = 1
        elif state == 1:
            words.append("".join(word))
            word[:] = []
            state = 0
    for w in words:
        w = w.lower()
        if w in nums:
            nums[w] += 1
        else:
            nums[w] = 1
    return nums


def wcount(lines, topn = 10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    alist = sorted([(a, b) for (b, a) in count(lines).items()])
    k = -1
    anss_alist = []
    if topn <= len(alist):
        while k>= -topn:
            anss_alist.append((alist[k][1], alist[k][0]))
            k -= 1
        anss_dict = dict(anss_alist)
    else:
        alist.reverse()
        anss_dict = dict([(b, a) for (a, b) in alist])
    return anss_dict


def main():
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

if __name__ == '__main__':
     main()