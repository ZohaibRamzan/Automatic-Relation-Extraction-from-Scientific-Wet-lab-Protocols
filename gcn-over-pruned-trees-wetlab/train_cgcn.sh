#!/bin/bash

SAVE_ID=$1
python train.py --id $SAVE_ID --seed 0 --prune_k 1 --lr 0.3 --rnn_hidden 200 --num_epoch 20 --pooling max --mlp_layers 2 --pooling_l2 0.003
