# Transform data type
Data = transform(Data,Overpayment_Amount=as.numeric(Data$Overpayment_Amount))
str(Data)

# sum, mean
with(Data,mean(Overpayment_Amount,na.rm=T))
with(Data,sum(Overpayment_Amount,na.rm=T))
summary(Data$Overpayment_Amount)

# group by
Data=as.data.table(Data)
Data[,.(mean(Benefit_Amt,na.rm=T)),by=.(ZipCodes)]
Data[,.(length(unique(ID))),by=Citizenship] # count unique value
# group by multiple variables
Data[,.(sum(Benefit_Amt,na.rm=T),sum(Income,na.rm=T)),by=.(ZipCodes,Previous_Felony)]
Data[,.(sum(Benefit_Amt,na.rm=T),mean(Benefit_Amt,na.rm=T),.N),by=.(ZipCodes)]

round(cor(subset(Data,select=c("Number_Children","Benefit_Amt")),use="pairwise.complete.obs"),2)
