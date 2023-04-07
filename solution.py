import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 412238846 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  n = len(x)
  y = x - 0.083
  return max(y)/(pow((1+p)/2,1/n))+0.083, max(y)/(pow((1-p)/2,1/n))+0.083

