# Automatic-Relation-Extraction-from-Scientific-Wet-lab-Protocols

This repository is being prepared for relation extraction between the entities that appear in Wet-lab Protocols. Wet-lab Protocols are the instruction that researchers follow while conducting an experiment in biological or chemical laboratory. This work is intended to enable the researchers to get structured knowledge on the relationships between taken actions and scientific objects present in text of scientific protocols. As a result, they can get insights and make valuable decisions. The dataset being used for this task is free-sourced developed by (Chaitanya Kulkarni, Wei Xu, Alan Ritter, Raghu Machiraju) and available at: https://github.com/chaitanya2334/WLP-Dataset

<h2>Requirements</h2>
Linux OS bash Terminal (Tested on Debian 10)

**Anaconda Environment:**

**1- For Graph Convolutional Neural Network:**

- Python (Tested on 3.6.8)
- PyTorch (Tested on 1.8.0)

**2- For Contextualized Graph Convolutional Neural Network**

- Python (tested on 3.7.10)
- PyTorch (tested on 1.4.0)
- Cudatoolkit (tested on 9.2)

<h2>Implementation:</h2>


1. Open Linux OS terminal and go to project directory ../gcn-over-pruned-trees-wetlab/..
2. unzip dataset.zip file (Dataset after preprocessing)
3. First download and unzip GloVe vectors with:

`chmod +x download.sh; ./download.sh`

Then prepare vocabulary and initial word vectors with:  

`python prepare_vocab.py dataset/wetlab dataset/vocab --glove_dir dataset/glove`

3. GCN Training and Evaluation
After creating the conda enviroment for GCN as above mentioned, run the command;

`bash train_gcn.sh 0 `

Model checkpoints and logs will be saved to ./saved_models/00.

For evaluation on test set, run;

`python eval.py saved_models/00 --dataset test`

4. C-GCN Training and Evaluation
After creating the conda enviroment for C-GCN as above mentioned, run the command  

`bash train_cgcn.sh 1`

Model checkpoints and logs will be saved to ./saved_models/01.
For evaluation on test set, run;

`python eval.py saved_models/01 --dataset test`








