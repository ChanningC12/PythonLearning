Data = read.csv("Desktop/Github/PythonLearning/PythonDataAnalysis/Dataset.csv")
Data$Copy_of_Benefit = Data$Benefit_Amt
Data$Benefit_Amt_gt_200 = ifelse(Data$Benefit_Amt >= 200, 1, 0)
