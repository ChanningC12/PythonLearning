List_null = data.frame(one=c(1,3,NA,6,8,NA,9),two=c(8,0,1,NA,2,6,NA))
# replace na with column means
List_null[which(!complete.cases(List_null$one)),"one"]=mean(List_null$one,na.rm=T)
List_null[which(is.na(List_null$two)),"two"]=mean(List_null$two,na.rm=T)
# replace na with row means
ind = which(is.na(List_null),arr.ind=T)
List_null[ind]=rowMeans(List_null,na.rm=T)[ind[,1]]
# replace na with zero
List_null[which(!complete.cases(List_null)),]=0


