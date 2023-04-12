import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 710820274 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    conv1 = x_success / x_cnt
    conv2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z = (conv1 - conv2) / np.sqrt(p * (1-p) * (1/x_cnt + 1/y_cnt))

    return abs(z) > stats.norm.ppf(0.06)
