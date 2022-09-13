# BERT-Fine-Tuning-on-Quora-Question-Pairs

Over 100 million people visit Quora every month, so it's no surprise that many people ask similarly worded questions. Multiple questions with the same intent can cause seekers to spend more time finding the best answer to their question, and make writers feel they need to answer multiple versions of the same question. Quora values canonical questions because they provide a better experience to active seekers and writers, and offer more value to both of these groups in the long term.

In this case study, I identify which questions asked on Quora are duplicates of questions that have already been asked.
This could be useful to instantly provide answers to questions that have already been answered. I used streamlit app for predicting whether a pair of questions are duplicates or not.

I run BERT pre-trained model on the Quora Question Pair Similarity detection dataset to experience the bi-directionality of BERT. This colab notebook is a step-by-step guide to the implementation of the same using pytorch-transformers by hugging face. i fine tuned BERT model on 100k question pairs and got Accuracy on Train data 88.9

<img src="https://github.com/monika2910/BERT-Fine-Tuning-on-Quora-Question-Pairs
/blob/main/downloadHello.png">
