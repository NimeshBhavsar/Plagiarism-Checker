from queue import PriorityQueue
class CalcSim:
    '''
     This class will calculate similarity between all the documents present in the dataset with the suspicious document
     doc_rank will contain number of trigram matches per unit length for a given document
     document with higher priority(in the front) will have more similarity with the suspicious document than a document with lower priority
    '''
    doc_rank = PriorityQueue()
    """ Priority queue with percentage plagiarism and doc name"""
    def __init__(self,corpus,inp):
        """
          Run a loop through all the documents
          For each document if there is a trigram match increment the count(s in this case)
          When all trigram is matched for a particular document add its value to the queue(count per unit length)
        """
        for doc_name in corpus:    
            s = 0
            orig = corpus[doc_name]
            for tri in inp:
                if tri in orig:
                    s+=1
            self.doc_rank.put((s/len(inp)*100,doc_name))
        
