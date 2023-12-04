#!/bin/bash
#SBATCH -c 10                                       # Number of cores (-c)
#SBATCH --gres=gpu:1                                # Number of GPUs
#SBATCH -t 0-24:00                                  # Runtime in D-HH:MM, minimum of 10 minutes
#SBATCH -p seas_gpu  # Partition to submit to
#SBATCH --mem=32000                                 # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -o myoutput_%j.out                          # File to which STDOUT will be written, %j inserts jobid
#SBATCH -e myerrors_%j.err                          # File to which STDERR will be written, %j inserts jobid
#SBATCH --constraint=a100|v100
module load Anaconda2/2019.10-fasrc01 cuda/12.2.0-fasrc01 cudnn
export LIBRARY_PATH=/n/sw/eb/apps/centos7/Anaconda2/2019.10-fasrc01/lib/:$LIBRARY_PATH
export LD_LIBRARY_PATH=/n/sw/eb/apps/centos7/Anaconda2/2019.10-fasrc01/lib/:$LD_LIBRARY_PATH
source activate nnet_calculator
# python3 transfer_learning.py

# Optionally set the cache for transformers
# export TRANSFORMERS_CACHE='YOUR_PATH/huggingface'

export model=$1 # llama2 or vicuna
export setup=$2 # behaviors or strings

# Create results folder if it doesn't exist
if [ ! -d "../results" ]; then
    mkdir "../results"
    echo "Folder '../results' created."
else
    echo "Folder '../results' already exists."
fi

for data_offset in 1 11 21 31 41 51 61 71 81 91
do

    python3 -u ../main.py \
        --config="../configs/individual_${model}.py" \
        --config.attack=gcg \
        --config.train_data="../../data/advbench/harmful_${setup}.csv" \
        --config.result_prefix="../results/individual_${setup}_${model}_gcg_offset${data_offset}" \
        --config.n_train_data=50 \
        --config.data_offset=$data_offset \
        --config.n_steps=50 \
        --config.test_steps=50 \
        --config.batch_size=512

done