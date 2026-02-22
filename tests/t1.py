"""Define PATH"""

from pathlib import Path
import sys

#Presenx dir 
BASE_DIR = Path(__file__).resolve().parents[1]

#src dir
SRC_DIR = BASE_DIR / "src"

#adding src path to module
sys.path.append(str(SRC_DIR))

"""Clean before test """
import clean
clean.cl()

"""IMPORT and RUN test code"""
from main import testCode

testCode()

"""Clean after test """
clean.cl()

