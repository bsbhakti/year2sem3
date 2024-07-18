#Assignment 2
#Karim Khoja and Bhakti Bhanushali


library(dplyr)
library(xts)
library(ggplot2)
# Install zoo package
library("zoo") 
library("stargazer")


dataset <- read.table("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/A2/Group_Assignment_2_Dataset.txt", header=TRUE,
                      sep=",")

class(dataset$Date)
dataset$Date <-as.Date(dataset$Date,format = "%d/%m/%Y")
class(dataset$Date)
dataset %>% filter(Date < "2007-12-31")
new_dataset <- subset(dataset, dataset$Date != '2007-12-31')
new_dataset$week_num <- strftime(new_dataset$Date, format = "%V")
new_dataset[is.na(new_dataset)] <- 0
#week_group = dataset %>% group_by(week_num)
#dataset2 <- week_group %>% as.data.frame()

grouped <- (split(new_dataset, f = new_dataset$week_num))
#grouped_frame <- as.data.frame(grouped)
numbers <- 1:10071


average_smoothened_week <- data.frame(numbers )
for (i in 1:52){
  
  dataset4 <- do.call(rbind.data.frame,grouped[i])
  class(dataset4)
  columnName <- paste("smoothened_week", i, sep= "_")
  nameA <-  (rollmean(dataset4$Global_intensity,k = 10))
  average_smoothened_week[paste0("smoothened_week",i,sep = "_")] = nameA
  assign(paste("smoothened_week", i, sep= "_"),nameA)
  
}
average_smoothened_week <- select(average_smoothened_week,-numbers)
average_smoothened_week$Mean = rowMeans(average_smoothened_week, na.rm = TRUE)

scores <- data.frame(1:1)
#print(scores)
for(j in 1:52) {
  #print(average_smoothened_week[i])
  average_smoothened_week[paste0("difference",j,sep ="")] = abs(average_smoothened_week[j]-average_smoothened_week$Mean)
  colName = paste("difference",j,sep ="")
  #print(colName)
 # print(average_smoothened_week[colName])
  a = sum(average_smoothened_week[colName],na.rm = TRUE)

  scores[paste0("score_of_week_",j,sep = "")] = a
 
}
average_smoothened_week$numbers <-(numbers)

time <- new_dataset$Time[1:10071]
average_smoothened_week$Time <-(time)

ggplot() +
  geom_line(data = average_smoothened_week, mapping = aes(x = time,y = smoothened_week_52, colour = "red")) +
  geom_line(data = average_smoothened_week, mapping = aes(x =time,y =Mean,colour = "blue"))+
  geom_line(data = average_smoothened_week, mapping = aes(x =time,y = smoothened_week_37,colour = "pink"))+
  
  labs(title = "Anomaly", y = "Global Intensity")+ scale_color_manual(labels = c("Most anamolous week","Normal week","Least anamolous week"),values = c("red","blue","pink"))


minimum = apply(scores[,-1], 1, min)
maximum = apply(scores[,-1], 1, max)
#print(scores)
#append(scores,3)
#print(scores)





