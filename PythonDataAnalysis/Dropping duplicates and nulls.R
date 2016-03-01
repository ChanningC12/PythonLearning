# remove duplicates
duplicated(Data[,c("ID")])
Data_drop_duplicated = Data[!duplicated(Data[c("ID")]),]
Data_drop_duplicated2 = Data[!duplicated(Data[c("ID")],fromLast=T),]
dim(Data_drop_duplicated)
dim(Data_drop_duplicated2)

# dropping NAs
sum(is.na(Data$Overpayment_Amount)
sum(!is.na(Data$Overpayment_Amount))
Data_drop_NAs = Data[!is.na(Data[c("Overpayment_Amount")]),]
Data_drop_NAs2 = Data[with(Data,!is.na(Overpayment_Amount) & !is.na(Dollar_Error1)),]



