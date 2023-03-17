from flask import Flask
import os, sys
app = Flask(__name__)
from app import home,manage