import math


def norm(vec):
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    n = 0.0
    for w, count in vec1.items():
        if w in vec2: n += vec1[w] * vec2[w]

    d = norm(vec1) * norm(vec2)
    return n / d

def build_semantic_descriptors(sentences):
    sem_desc = {}

    for s in sentences:
        for w  in s:
            if w not in sem_desc:
                sem_desc[w] = {}

            for other_word in s:
                if other_word != w:
                    if other_word not in sem_desc[w]:
                        sem_desc[w][other_word] = 1

                    else:
                        sem_desc[w][other_word] += 1

    return sem_desc



def build_semantic_descriptors_from_files(filenames):
    all_sen = []

    for filename in filenames:
        text = open(filename, "r", encoding="latin1").read()
        #change all sentences to lowercase
        text = text.lower()

        #strip out punctuation that isn't a sentence separator        
        text = text.replace(",", "").replace(":", "").replace(";", "").replace("-", "").replace("--", "")

        #replace any type of punuctation with .
        text = text.replace("!", ".").replace("?", ".")
    
        #split by dot to get sentences
        sen = text.split(".")

        #split each sentence by word
        for i in range(len(sen)):
            sen[i] = sen[i].split()

        #append the sentences to the list of all sentences
        all_sen += sen

    return build_semantic_descriptors(all_sen)



        


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    sims = []

    for c in choices:
        if (c in semantic_descriptors) and (word in semantic_descriptors):
            sims.append(similarity_fn(semantic_descriptors[word], semantic_descriptors[c]))
        else:
            sims.append(-1)

    #using .index of the max ensures that we get the lowest index with that value also
    return choices[sims.index(max(sims))]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    lines = open(filename, "r", encoding="latin1").read().split("\n")

    corr = 0
    n = 0
    
    for line in lines:
        if line != "":
            line = line.split()
            res = most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn)
            if res == line[1]:
                corr += 1
            n += 1

    return (corr / n) * 100

