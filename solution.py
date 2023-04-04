import pandas as pd
import numpy as np


chat_id = 436801091 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = 32
    x_sum = np.sum(x)
    lambd = x_sum /(n * t)

    return lambd # Ваш ответ

