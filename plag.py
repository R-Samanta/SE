import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from siz_check import *

def plag_rate(file1,file2):
    #if not file1.endswith('.txt') or not file2.endswith('.txt'): return -1
    files = [file1,file2]
    if 0 in [siz_chk(i) for i in files]:return -1
    sample_contents = [open(File).read() for File in files]
    vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
    similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])
    vectors = vectorize(sample_contents)
    s_vectors = list(zip(files, vectors))
    return([i[2] for i in check_plagiarism(similarity,s_vectors)][0])

def check_plagiarism(similarity,s_vectors):
    results = set()
    for sample_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
        for sample_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            sample_pair = sorted((sample_a, sample_b))
            score = sample_pair[0], sample_pair[1], sim_score
            results.add(score)
    return results


#print(plag_rate('sample1.txt','sample2.txt'))
