__author__ = 'Irrevocable Cascade'

"""
This is used to mess around
"""
import os

SETTINGS_DIR = os.path.dirname(__file__)

print(SETTINGS_DIR)

PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
print(PROJECT_PATH)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
print(PROJECT_PATH)

print(os.pardir)

