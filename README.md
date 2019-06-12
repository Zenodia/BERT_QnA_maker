step1-
pip install bert-serving-server
pip install -U bert-serving-client

Step2-
download pre-trained multi-lingo BERT model 
https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip
other available models ( chinese for example ) are listed here 
https://github.com/google-research/bert/blob/master/multilingual.md


Step3- go to the folder where the pre-trained model was downloaded and start the server
bert-server-start -model_dir ./multi_cased_L-12_H-768_A-12/ -num_worker=1

Step4- open a terminal in python ( in the same directory where you qna_example.py script is located)
python qna_example.py 
Key in your query ( in Swedish )

Note: the qna.txt is extracted from this link-
https://support.office.com/sv-se/article/chatta-i-microsoft-teams-f3a917cb-1a83-42b2-a097-0678298703bb?ui=sv-SE&rs=sv-SE&ad=SE

citing original git repo
@misc{xiao2018bertservice,
  title={bert-as-service},
  author={Xiao, Han},
  howpublished={\url{https://github.com/hanxiao/bert-as-service}},
  year={2018}
}