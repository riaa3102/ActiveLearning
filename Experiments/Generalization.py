"""
File:
    Experiments/Generalization.py

Authors:
    - Abir Riahi
    - Nicolas Raymond
    - Simon Giard-Leroux

Description:
    Generalization experiments.
"""

import os
import sys
sys.path.insert(0, os.getcwd())
from src.models.constants import SQUEEZE_NET_1_1, RESNET18
from src.data.constants import CIFAR10, EMNIST
from Helpers import send_experiment_cmds
EXPERIMENT_NAME = 'generalization'

FIXED_SQUEEZENET_CMDS = ['-en', EXPERIMENT_NAME, '--model', SQUEEZE_NET_1_1, '--dataset', CIFAR10, '--n_start', '100',
                         '--n_new', '100', '--epochs', '10', '--query_strategy', 'least_confident',
                         '--batch_size', '50', '--learning_rate', '0.0001', '--n_rounds', '20', '--patience', '3']

FIXED_RESNET_CMDS = ['-en', EXPERIMENT_NAME, '--model', RESNET18, '--dataset', EMNIST, '--n_start', '50',
                     '--n_new', '1000', '--epochs', '10', '--query_strategy', 'least_confident',
                     '--batch_size', '50', '--learning_rate', '0.0001', '--n_rounds', '10', '--patience', '3']


def combination_generator(fixed_model_cmds):
    return [fixed_model_cmds + ['--weight_decay', '0'],
            fixed_model_cmds + ['--data_aug'],
            fixed_model_cmds + ['--data_aug', '--weight_decay', '0.001'],
            fixed_model_cmds + ['--data_aug', '--weight_decay', '0.005'],
            fixed_model_cmds + ['--data_aug', '--weight_decay', '0.008']]


if __name__ == '__main__':
    send_experiment_cmds(combination_generator, FIXED_SQUEEZENET_CMDS, FIXED_RESNET_CMDS)




