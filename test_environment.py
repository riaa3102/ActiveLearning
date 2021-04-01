import sys
import os
from src.data.DatasetManager import DatasetManager
from src.data.constants import *
from src.models.constants import *
from src.models.TrainValidTestManager import train_model, get_transforms



REQUIRED_PYTHON = "python3"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()

    dataset_manager = DatasetManager(CIFAR10, 0.1)


    train_model(epochs=100, data_loader=data_loader_train, file_name='model',
                model_name=SQUEEZE_NET_1_1, pretrained=True, learning_rate=0.0001)