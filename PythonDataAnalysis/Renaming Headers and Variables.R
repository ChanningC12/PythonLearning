# add variables when import data
NH_dat = read.csv("Desktop/Github/PythonLearning/PythonDataAnalysis/Dataset_NoHead.csv")
colnames(NH_dat)=c('ID','Payment','Benefit_Amt')
head(NH_dat)

PH_dat = read.csv("Desktop/Github/PythonLearning/PythonDataAnalysis/Dataset_PartHead.csv")
names(PH_dat)[2]='Payment_Date'
# or
colnames(NH_dat)[2]='Payment_Date'
head(PH_dat)

