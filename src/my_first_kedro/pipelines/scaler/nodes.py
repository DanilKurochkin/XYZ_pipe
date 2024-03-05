import numpy as np
import pandas as pd

#параметр scaler - есть простой множитель, например x в дюймах, y в футах
#добавил как такую возможность из разных систем измерения точки сводить
def scale(X : pd.DataFrame, parameters):
    X *= parameters['scale']
    
    return X