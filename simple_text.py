import nltk
from nltk.corpus import wordnet as wn
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

ABB = {'JJ': 'a', 'JJR': 'a', 'JJS': 'a',
       'NN': 'n', 'NNS': 'n', 'NNP': 'n', 'NNPS': 'n',
       'VB': 'v', 'VBG': 'v', 'VBD': 'v', 'VBN': 'v', 'VBP': 'v', 'VBZ': 'v',
       'RB': 'r', 'RBR': 'r', 'RBS': 'r', 'WRB': 'r',
       'IN': 'p', 'PRP': 'p', 'PRP$': 'p', 'WP': 'p', 'WP$': 'p', 'POS': 'p', 'RP': 'p',
       'DT': 'd', 'PDT': 'd', 'WDT': 'd',
       'CC': 'c', 'UH': 'i', 'MD': 'm', 'TO': 't', 'EX': 'e', 'SYM': 's'
    }

model = SentenceTransformer('bert-base-nli-mean-tokens')

class Syns:

    def extract_lines(paragraph: str, word_list: list) -> dict:
        word_dict = dict()
        sents = paragraph.split('.')
        for word in word_list:
            word_dict[word] = {}    # initiazlize
            index = [idx for idx, sent in enumerate(sents) if word in sent][0]
            word_dict[word]['sentence'] = sents[index]
        return word_dict

    def get_synonyms(word_dict: dict) -> dict:
        pos = ''
        for word in word_dict:
            sentence = word_dict[word]['sentence']
            tokens = nltk.word_tokenize(sentence)   # tokenize
            pos_tags = nltk.pos_tag(tokens)
            pos = [pos_tag for pos_tag in pos_tags if pos_tag[0] == word][0]    # part-of-speech tagging
            word_dict[word]['pos'] = ABB[pos[1]]
            try:
                synsets = wn.synsets(word, pos=word_dict[word]['pos'])   # synonyms
                word_dict[word]['synonyms'] = {} # initialize
                for syn in synsets:
                    for lemma in syn.lemmas():  # lemmas
                        if lemma.name() not in word_dict[word]['synonyms']:
                            word_dict[word]['synonyms'][lemma.name()] = float(0)
            except Exception as e:
                print(f"An error occurred: {e}.")
        return word_dict
    
class Readability:

    def cos_sim(word_dict: dict) -> dict:
        for word in word_list:
            origin_sent_emb = model.encode(word_dict[word]['sentence'])
            for syn in word_dict[word]['synonyms']:
                new_sent = word_dict[word]['sentence'].replace(word, syn)
                new_embed = model.encode(new_sent)
                similarity_score = cosine_similarity([origin_sent_emb], [new_embed])
                word_dict[word]['synonyms'][syn] = similarity_score
        return word_dict
    
    def freq(word_dict: dict) -> dict:
        nltk.FreqDist
        return {}
    

if __name__=='__main__':
    paragraph = '''Automatic readability assessment (ARA) is the task of evaluating the level of ease or
                difficulty of text documents for a target audience. For researchers, one of the many
                open problems in the field is to make such models trained for the task show efficacy
                even for low-resource languages. In this study, we propose an alternative way of utilizing
                the information-rich embeddings of BERT models with handcrafted linguistic features through a
                combined method for readability assessment. Results show that the proposed method outperforms
                classical approaches in readability assessment.'''
    word_list = ['evaluating', 'linguistic']
    
    word_dict = Syns.extract_lines(paragraph, word_list)
    word_dict = Syns.get_synonyms(word_dict)
    word_dict = Readability.cos_sim(word_dict)
    for word in word_dict:
        for syn in word_dict[word]['synonyms']:
            print(f"Word: '{word}'\nPOS: {word_dict[word]['pos']}\nsynonyms: '{syn}'\nCosine Similarity Score: {word_dict[word]['synonyms'][syn]}\n")