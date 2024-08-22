import wn
from wn.morphy import Morphy
from nltk.corpus import wordnet as wnet

def test_wn(word):
    syns = {}
    en = wn.Wordnet('oewn:2023', lemmatizer=Morphy())    # Create Wordnet object to query
    try:
        w = en.words(word)[0]
        pos = w.pos
        synsets = en.synsets(word, pos=pos)
        for synset in synsets:
            lemma_names = synset.lemmas()
            if lemma_names:
                lemma_name = lemma_names[0]
                definition = synset.definition() # Get the synset's definition
                syns[lemma_name] = definition
    except Exception as e:
        print(f"An error occurred: {e}")
    return syns

def test_wnet(word):
    syn_dict = {}
    synsets = wnet.synsets(word)
    pos = synsets[0].pos()
    for syn in synsets:
        definition = syn.definition()
        syn_dict[syn.name()] = definition
    return syn_dict


if __name__=='__main__':
    word = 'wins'

    syns = test_wn(word)
    #print(syns)

    syns2 = test_wnet(word)
    for syn in syns2:
        print(f"{syn}: {syns2[syn]}")