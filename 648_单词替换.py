"""
在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

示例 1：

输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 2：

输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
 

提示：

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写字母组成。
1 <= sentence.length <= 10^6
sentence 仅由小写字母和空格组成。
sentence 中单词的总量在范围 [1, 1000] 内。
sentence 中每个单词的长度在范围 [1, 1000] 内。
sentence 中单词之间由一个空格隔开。
sentence 没有前导或尾随空格。

解答：
将句子分割为数组，将词根列表按长度排序；
双重for循环遍历查找
"""

from typing import List


class Solution:
    """方案一：使用自带的startswith函数判断词根"""
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_list = sentence.split(" ")
        dictionary_sorted = sorted(dictionary, key=lambda word:len(word))
        for i, word in enumerate(sentence_list):
            for root in dictionary_sorted:
                # 找到词根，替换
                if word.startswith(root):
                    sentence_list[i] = root
                    break
        return " ".join(sentence_list)


class Solution2:
    """方案二：使用 hash 表判断"""
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        dictionary_set = set(dictionary)
        for i, word in enumerate(words):
            for j in range(1, len(words)+1):
                if word[:j] in dictionary_set:
                    # 找到词根，替换
                    words[i] = word[:j]
                    break
        return " ".join(words)


class Solution3:
    """方案三：字典树"""
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 使用词根构建字典树        
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = {}
        words = sentence.split(' ')
        for i, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if '#' in cur:
                    words[i] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return " ".join(words)
