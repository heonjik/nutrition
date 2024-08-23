import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize

ABB = {'JJ': 'a', 'JJR': 'a', 'JJS': 'a',
       'NN': 'n', 'NNS': 'n', 'NNP': 'n', 'NNPS': 'n',
       'VB': 'v', 'VBG': 'v', 'VBD': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v',
       'RB': 'r', 'RBR': 'r', 'RBS': 'r', 'WRB': 'r',
       'IN': 'p', 'PRP': 'p', 'PRP$': 'p', 'WP': 'p', 'WP$': 'p', 'POS': 'p', 'RP': 'p',
       'DT': 'd', 'PDT': 'd', 'WDT': 'd',
       'CC': 'c', 'UH': 'i', 'MD': 'm', 'TO': 't', 'EX': 'e', 'SYM': 's'
    }

class Syns:

    def get_synonyms(sentence, word):
        syn_list = []
        pos = ''
        tokens = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(tokens)
        for pos_tag in pos_tags:
            if pos_tag[0] == word:
                pos = ABB[pos_tag[1]]
                break
        try:
            synsets = wn.synsets(word, pos=pos)
            for syn in synsets:
                for lemma in syn.lemmas():
                    if lemma.name() not in syn_list:
                        syn_list.append(lemma.name())
        except Exception as e:
            print(f"An error occurred: {e}.")
        return syn_list


if __name__=='__main__':
    sentence1 = 'She always wins, it is not fair.'
    word1 = 'wins'
    print(Syns.get_synonyms(sentence1, word1))

    sentence2 = '''In fact, however, though now much farther off than before, the Rostóvs
                all saw Pierre—or someone extraordinarily like him—in a coachman’s coat,
                going down the street with head bent and a serious face beside a small,
                beardless old man who looked like a footman.'''
    word2 = 'serious'
    syns = Syns.get_synonyms(sentence2, word2)
    print(syns)