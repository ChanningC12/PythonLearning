# Read in data
Part_dat=read.csv("Desktop/PythonLearning/Pythonlearning/PythonDataAnalysis/Dataset_Partial.csv")
Bamt_dat=read.csv("Desktop/PythonLearning/Pythonlearning/PythonDataAnalysis/Dataset_BenAmt.csv")
Nfam_dat=read.csv("Desktop/PythonLearning/Pythonlearning/PythonDataAnalysis/Dataset_NoFamily.csv")

# Check dimensions
dim(Part_dat)
dim(Bamt_dat)
dim(Nfam_dat)

# See column names
colnames(Part_dat)
colnames(Bamt_dat)
colnames(Nfam_dat)

# View first few observations
head(Part_dat,n = 4)

dat_temp = merge(Part_dat,Bamt_dat,by="ID",all.x=T)
dat_temp1 = merge(Part_dat,Bamt_dat,by=c("ID","Payment_Date"),all.x=T)
dat_temp2 = merge(Part_dat, Nfam_dat, by.x="ID",by.y="KEY",all.x=T)
dat_temp3 = merge(dat_temp1,Nfam_dat,by.x="ID",by.y="KEY",all.x=T)

write.csv(dat_temp3,"Desktop/PythonLearning/Pythonlearning/PythonDataAnalysis/R_Merged_Data.csv")
