import numpy as np

def calculate(list):
  if len(list) != 9 :
    raise ValueError("the digit must contain 9 digit")
    
  ls = np.array(list)
  print(ls)
  mean_col= [ls[[0,1,2]].mean(),ls[[3,4,5]].mean(),ls[[6,7,8]].mean()]
  mean_row= [ls[[0,3,6]].mean(),ls[[1,4,7]].mean(),ls[[2,5,8]].mean()]

  var_col = [ls[[0,1,2]].var,ls[[3,4,5]].var(),ls[[6,7,8]].var()]
  var_row = [ls[[0,3,6]].var(),ls[[1,4,7]].var(),ls[[2,5,8]].var()]

  std_col = [ls[[0,1,2]].std(),ls[[3,4,5]].std(),ls[[6,7,8]].std()]
  std_row = [ls[[0,3,6]].std(),ls[[1,4,7]].std(),ls[[2,5,8]].std()]
  
  max_col = [ls[[0,1,2]].max(),ls[[3,4,5]].max(),ls[[6,7,8]].max()]
  max_row = [ls[[0,3,6]].max(),ls[[1,4,7]].max(),ls[[2,5,8]].max()]

  min_col = [ls[[0,1,2]].min(),ls[[3,4,5]].min(),ls[[6,7,8]].min()]
  min_row = [ls[[0,3,6]].min(),ls[[1,4,7]].min(),ls[[2,5,8]].min()]

  sum_col = [ls[[0,1,2]].sum(),ls[[3,4,5]].sum(),ls[[6,7,8]].sum()]
  sum_row = [ls[[0,3,6]].sum(),ls[[1,4,7]].sum(),ls[[2,5,8]].sum()]

  return {
  'mean': [mean_row,mean_col,ls.mean()],
  'variance': [var_row,var_col,ls.var()],
  'standard deviation': [std_row,std_col,ls.std()],
  'max': [max_row,max_col,ls.max()],
  'min': [min_row,min_col,ls.min()],
  'sum': [sum_row,sum_col,ls.sum()],
}

list = [0,1,2,3,4,5,6,7,8]

project = calculate(list)
print(project)