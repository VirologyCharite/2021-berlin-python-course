#! /usr/bin/env python

import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic.replace({'Sex': {'female': 'f', 'male': 'm'}}, inplace=True)

titanic.to_csv('titanic.csv')