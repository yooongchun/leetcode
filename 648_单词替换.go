/*
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
*/
package leetcode

import (
	"sort"
	"strings"
)

// 方案一：使用自带的startswith函数判断词根
func replaceWords(dictionary []string, sentence string) string {
	sentenceWords := strings.Split(sentence, " ")
	sort.Slice(dictionary, func(i, j int) bool {
		return len(dictionary[i]) < len(dictionary[j])
	})
	for i, word := range sentenceWords {
		for _, root := range dictionary {
			if strings.HasPrefix(word, root) {
				sentenceWords[i] = root
				break
			}
		}
	}
	return strings.Join(sentenceWords, " ")
}

// 方案二：使用 hash 表判断
func replaceWords2(dictionary []string, sentence string) string {
	dictionarySet := map[string]bool{}
	for _, root := range dictionary {
		dictionarySet[root] = true
	}
	words := strings.Split(sentence, " ")
	for i, word := range words {
		for j := 1; j <= len(word); j++ {
			if dictionarySet[word[:j]] {
				words[i] = word[:j]
				break
			}
		}
	}
	return strings.Join(words, " ")
}

// 方案三：字典树
func replaceWords3(dictionary []string, sentence string) string {
	type trie map[rune]trie

	root := trie{}
	for _, s := range dictionary {
		cur := root
		for _, c := range s {
			if cur[c] == nil {
				cur[c] = trie{}
			}
			cur = cur[c]
		}
		cur['#'] = trie{}
	}

	words := strings.Split(sentence, " ")
	for i, word := range words {
		cur := root
		for j, c := range word {
			if cur['#'] != nil {
				words[i] = word[:j]
				break
			}
			if cur[c] == nil {
				break
			}
			cur = cur[c]
		}
	}
	return strings.Join(words, " ")
}
