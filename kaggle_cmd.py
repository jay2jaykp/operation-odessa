#!/usr/bin/env python3
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Kaggle_Cmd:
    """
    Kaggle Command Object that contains a lot of data fetching and unzipping.
    """
    def __init__(self, path, competition):
        """
        :param path(str): Contains our secret path to store our downloaded data.
        :param competition(str): Contains our secret kaggle command.
        """
        self.path = os.environ.get(path)
        self.compete = os.environ.get(competition)

    def get_cmd(self):
        """ Generate a path that does not exist and run kaggle command to store.
        :return:
        """
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            os.system(self.compete)
        else:
            pass

