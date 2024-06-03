def precisionAt_k(relevant_docs, retrieved_docs, k):
    retrieved_at_k = retrieved_docs[:k]
    relevant_and_retrieved = set(relevant_docs) & set(retrieved_at_k)
    return len(relevant_and_retrieved) / k


def recall(relevant_docs, retrieved_docs):
    relevant_and_retrieved = set(relevant_docs) & set(retrieved_docs)
    return len(relevant_and_retrieved) / len(relevant_docs) if len(relevant_docs) != 0 else 0



def averagePrecision(relevant_docs, retrieved_docs):
    relevant_docs_set = set(relevant_docs)
    score = 0.0
    num_hits = 0.0
    for i, doc in enumerate(retrieved_docs):
        if doc in relevant_docs_set:
            num_hits += 1.0
            score += num_hits / (i + 1.0)
    return score / len(relevant_docs) if len(relevant_docs) != 0 else 0



def meanAveragePrecision(all_relevant_docs , all_retrieved_docs):
    avg_precisions = []
    for relevant_docs, retrieved_docs in zip(all_relevant_docs, all_retrieved_docs):
        avg_precisions.append(averagePrecision(relevant_docs, retrieved_docs))
    return sum(avg_precisions) / len(avg_precisions) if len(avg_precisions) != 0 else 0



def meanReciprocalRank(all_relevant_docs, all_retrieved_docs):
    reciprocal_ranks = []
    for relevant_docs, retrieved_docs in zip(all_relevant_docs, all_retrieved_docs):
        for rank, doc in enumerate(retrieved_docs):
            if doc in relevant_docs:
                reciprocal_ranks.append(1.0 / (rank + 1))
                break
        else:
            reciprocal_ranks.append(0.0)
    return sum(reciprocal_ranks) / len(reciprocal_ranks) if len(reciprocal_ranks) != 0 else 0



def fullEvaluation(all_relevant_docs , all_retrieved_docs ):
    precision_at_10 = [precisionAt_k(relevant, retrieved, 10) for relevant, retrieved in zip(all_relevant_docs, all_retrieved_docs)]
    recalls = [recall(relevant, retrieved) for relevant, retrieved in zip(all_relevant_docs, all_retrieved_docs)]
    map_score = meanAveragePrecision(all_relevant_docs, all_retrieved_docs)
    mrr_score = meanReciprocalRank(all_relevant_docs, all_retrieved_docs)
    print("\n\n\n---------<<  Full Evaluation >>----------\n")
    print(f"Precision@10: {precision_at_10}")
    print("\n")
    print(f"Recall: {recalls}")
    print("\n")
    print(f"MAP: {map_score}")
    print("\n")
    print(f"MRR: {mrr_score}")
    print("\n-------------------------------------------\n")

    
    
    
 

           
           

all_relevant_docs = [
    [1, 2, 3], 
    [1, 2],   
    [8] 
]

all_retrieved_docs = [
    [4, 1, 2, 3],  
    [2, 3, 1],  
    [1,2,7]
]

#fullEvaluation(all_relevant_docs , all_retrieved_docs )





