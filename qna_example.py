import numpy as np
from bert_serving.client import BertClient
from termcolor import colored

prefix_q ='Q:' 
answer ='A:'
topk = 1

def whatisthis(s):
        if isinstance(s, str):
            #print("ordinary string")
            s=s.replace('Ã¥','å')
            s=s.replace('Ã¶','ö')
            s=s.replace('Ã¤','ä')
            #print(s)
            return s

        elif isinstance(s, unicode):
            print("unicode string")
            return s
        else:
            print("not a string")
            return s
def qna_dictionary(prefix_q='Q:',prefix_a='A:',file='qna.txt'):
    prefix_q =prefix_q
    prefix_a =prefix_a
    topk = 1
    indexer=0
    qna={}
    with open(file, encoding='utf-8-sig') as fp:
        lines = fp.readlines()
        lines=[line for line in lines if len(line)>1]
        cnt=0
        for l in lines:

            #print('{}'.format(str(cnt)),l)
            if l.startswith(prefix_q):
                #print(l)
                question=l.replace(prefix_q, '').strip()
                question=whatisthis(question)
                print("Q",question)
                answer=lines[cnt+1].replace(prefix_a, '').strip()
                answer=whatisthis(answer)
                print("A",answer)
                qna[question]=answer
                #print(cnt,l)
            cnt+=1
        return qna
qna=qna_dictionary()
with open('qna.txt', encoding='utf-8-sig') as fp:
    questions = [v.replace(prefix_q, '').strip() for v in fp if v.strip() and v.startswith(prefix_q)]
    print('%d questions loaded, avg. len of %d' % (len(questions), np.mean([len(d.split()) for d in questions])))

with BertClient() as bc:
    doc_vecs = bc.encode(questions)

    while True:
        query = input(colored('din fråga: ', 'green'))
        query_vec = bc.encode([query])[0]
        # compute normalized dot product as score
        score = np.sum(query_vec * doc_vecs, axis=1) / np.linalg.norm(doc_vecs, axis=1)
        topk_idx = np.argsort(score)[::-1][:topk]
        #print('top %d questions similar to your query \n"%s"' % (topk, colored(query, 'green')))
        #print('top %d answer to your question %s')%(topk,colored(qna[whatisthis(query)],'yellow'))

        for idx in topk_idx:
            print('most similar question in our QnA list is \n---> %s\t%s' % (colored('%.1f' % score[idx], 'cyan'), colored(questions[idx], 'yellow')))
            q=whatisthis(questions[idx])
            
            print('answer from QnA maker txt \n ---> %s' % (qna[q]))
