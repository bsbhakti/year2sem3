library(readr)
library(scales)
library(ggplot2)
library(dplyr)
library("depmixS4")
library("lubridate")
library(ggbiplot)
library(robustbase)

######PART 1############################
dataset <- read_csv("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/Project/TermProjectData.txt",
  col_types = cols(
    Date = col_date("%d/%m/%Y"),
    Time = col_character(),
    Global_active_power = col_double(),
    Global_reactive_power = col_double(),
    Voltage = col_double(),
    Global_intensity = col_double(),
    Sub_metering_1 = col_double(),
    Sub_metering_2 = col_double(),
    Sub_metering_3 = col_double()
  )
)

randomFriday <- dataset[dataset$Date == "2006-12-22",]
randomFriday = replace(randomFriday, is.na(randomFriday), 0)
display <- rep(c(F),each= 180)
display <- append(display,T)

ggplot()+
  geom_line(aes(x = randomFriday$Time, y = randomFriday$Global_active_power,color = "steelblue", group = 1))+
  geom_line(aes(x = randomFriday$Time, y = randomFriday$Global_intensity,color = "#52854C", group = 1))+
  scale_x_discrete(breaks = randomFriday$Time[display])+
  scale_colour_manual (labels = c("Global active power", "Global Intensity"),values = c("steelblue", "#52854C"))+
  geom_point(color = "black")+
  labs(title="Random Friday",y = "Unit values", x  = "Time")


dataset_removed_time <-subset(dataset, select = -c(Date,Time) )
dataset_removed_time <- dataset_removed_time %>% mutate_all(~(scale(.) %>% as.vector))
dataset_removed_time <-na.omit(dataset_removed_time)
dataset_removed_time[is.infinite(dataset_removed_time$Global_active_power), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Global_reactive_power), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Voltage), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Global_intensity), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Sub_metering_1), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Sub_metering_2), ] <- NA
dataset_removed_time[is.infinite(dataset_removed_time$Sub_metering_3), ] <- NA

pca <- prcomp(dataset_removed_time, scale=TRUE)
ggbiplot(pca,alpha=0)

pca.var <- pca$sdev^2
pca.var.per <- round(pca.var/sum(pca.var)*100, 1)
pca.var.per
rotation <- data.frame(pca[['rotation']])

index = c(1:100)
barplot(pca.var.per, main="Scree Plot", xlab="Principal Component", ylab="Percent Variation", col = "steelblue")
pca.data <- data.frame(label = index,
                       X=pca$x[(1:181),1],
                       Y=pca$x[(1:181),2])
corr <- data.frame(pca["rotation"])
pca.data
ggbiplot(pca.data)
ggplot(data=pca.data, aes(x=X, y=Y,label =index )) +
  geom_point() +
  xlab(paste("PC1 - ", pca.var.per[(1:100),1], "%", sep="")) +
  ylab(paste("PC2 - ", pca.var.per[(1:100),2], "%", sep="")) +
  theme_bw() +
  ggtitle("My PCA Graph")


#chosen response variables are: Global active power and Global reactive power


###################PART 2####################
#Picked fridays from 6:00 PM to 10:00 PM
dataset$weekday <- wday(dataset$Date,label = TRUE)
dataset_day <- dataset[dataset$weekday == "Fri",]


dataset_filtered <- dataset_day[dataset_day$Time >= "18:00:00" & dataset_day$Time <= "21:00:00",]
colNames <- c('Global_active_power','Global_intensity','Date',"Time")
row <- dataset_filtered[,colNames]
row <-subset(row, select = -c(Date,Time) )
row <- row%>% mutate_all(~(scale(.) %>% as.vector))
vec <- rep(c(181),each= 107)

train_set <- row[(1:19367),]
test_set <- row[(19368:27874),]

train_set = replace(train_set, is.na(train_set), 0)
test_set = replace(test_set, is.na(test_set), 0)

################################
#model training
set.seed(1)

states<-c(4,6,8,10,12,14,16,20,24)
models <- vector()
BIC <- vector()

logs <-vector()
for(j in states){
  
    mod1<- depmix(list(train_set$Global_active_power ~1,train_set $Global_intensity~1), data=train_set , nstates=j,
              family=list(gaussian(),gaussian()), ntimes=vec)
    fm1 <- fit(mod1)
    print(j)
    print(fm1)
    models <- append(models, fm1);
    BIC <- append(BIC, BIC(fm1))
    logs <- append(logs, logLik(fm1))
}

####################################

ggplot2()+
  geom_line(aes(x = states, y = BIC,color = "darkred"))+
  geom_line(aes(x = states, y = logs,color = "steelblue")) +
  scale_colour_manual (labels = c("BIC","Log likelihood"),values = c("darkred","steelblue"))+
  labs(title = "BIC and log likelyhood", y = "Unit values")

table <- data.frame(states,BIC,logs)
####################testing data###############
vec2 <- rep(c(181),each= 47)

testBIC <- vector()
testLogs <- vector()
testLogs2 <- vector()
selectedModel <- models[c(7,8)]
states2 <-c(16,20)


for(i in selectedModel){
  
  test <- depmix(response = list(Global_active_power~1, Global_intensity~1),
                      data = test_set,
                      nstates = i@nstates,
                      ntimes = vec2,
                      family = list(gaussian(),gaussian() ));
  test <- setpars(test, getpars(i));
  testlogs2()<- append(testLogs2,logLik(forwardbackward(test)))
  

  testLogs <- append(testLogs, logLik(test));
  testBIC <- append(testBIC, BIC(test));

}
table2 <- data.frame(states2,testBIC,testLogs)

testLogs <- testLogs/47
logs <- logs/107
logs <- logs[c(7,8)]
normalisedLogs <- data.frame(logs,testLogs)

normalisedLogs <- data.frame()
##pick state 20


##########################PART 3#####################3
anamoly_logs <- vector()
anamoly_BIC <- vector()

anomaly1 <- read_csv("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/Project/DataWithAnomalies1.txt",
                    col_types = cols(
                      Date = col_date("%d/%m/%Y"),
                      Time = col_character(),
                      Global_active_power = col_double(),
                      Global_reactive_power = col_double(),
                      Voltage = col_double(),
                      Global_intensity = col_double(),
                      Sub_metering_1 = col_double(),
                      Sub_metering_2 = col_double(),
                      Sub_metering_3 = col_double()
                    )
)


anomaly1 = replace(anomaly1, is.na(anomaly1), 0)
date <- anomaly1$Date
time <- anomaly1$Time
anomaly1$weekday <- wday(anomaly1$Date,label = TRUE)
anomaly1 <- anomaly1[anomaly1$weekday == "Fri",]

anomaly1 <- anomaly1[anomaly1$Time >= "18:00:00" & anomaly1$Time <= "21:00:00",]
colNames <- c('Global_active_power','Global_intensity','Date',"Time")
anomaly1 <- anomaly1[,colNames]

detection2_GlobalActivePower <- AnomalyDetectionVec(x = anomaly1$Global_active_power,period = 181, direction = "both",plot = T)
detection2_GlobalIntensity <- AnomalyDetectionVec(x = anomaly1$Global_intensity,period = 181, direction = "both",plot = T)

anomaly1 <-subset(anomaly1, select = -c(Date,Time) )
anomaly1 <- anomaly1%>% mutate_all(~(scale(.) %>% as.vector))


cutoff <- qchisq(p = 0.99 , df = 2)
detection1 <- mahalanobis(anomaly1[,c(1,2)], colMeans(anomaly1[,c(1,2)]),cov(anomaly1[,c(1,2)]))
anomaly1$MD <- round(detection1,3)
anomaly1$outlier <- FALSE
anomaly1$outlier[anomaly1$MD > cutoff] = TRUE
anomaly1$color = "black"
anomaly1$color[anomaly1$outlier== TRUE]="blue"
number1 = sum(anomaly1$outlier==TRUE)

ggplot(data = anomaly1,aes( x = Global_intensity, y = Global_active_power, color = color))+
  geom_point(size = 3,alpha = 0.6)+
  labs(title = "Dataset 1")+
  scale_colour_manual (labels = c("Normal points","Anomalies"),values = c("blue","orange"))
plot(anomaly1$Global_intensity, anomaly1$Global_active_power, col =  anomaly1$color )
vec <- rep(c(181),each= 52)

set.seed(5)
mod_A<- depmix(list(anomaly1$Global_active_power ~1,anomaly1 $Global_intensity~1), data=anomaly1 , nstates=20,
              family=list(gaussian(),gaussian()), ntimes=vec)
fm_A <- fit(mod_A)
print(fm_A)
anamoly_BIC <- append(anamoly_BIC, BIC(fm_A))
anamoly_logs <- append(anamoly_logs, logLik(fm_A))


anomaly2 <- read_csv("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/Project/DataWithAnomalies2.txt",
                    col_types = cols(
                      Date = col_date("%d/%m/%Y"),
                      Time = col_character(),
                      Global_active_power = col_double(),
                      Global_reactive_power = col_double(),
                      Voltage = col_double(),
                      Global_intensity = col_double(),
                      Sub_metering_1 = col_double(),
                      Sub_metering_2 = col_double(),
                      Sub_metering_3 = col_double()
                    )
)
anomaly2 = replace(anomaly2, is.na(anomaly2), 0)
anomaly2$weekday <- wday(anomaly2$Date,label = TRUE)
anomaly2 <- anomaly2[anomaly2$weekday == "Fri",]

anomaly2 <- anomaly2[anomaly2$Time >= "18:00:00" & anomaly2$Time <= "21:00:00",]
colNames <- c('Global_active_power','Global_intensity','Date',"Time")
anomaly2 <- anomaly2[,colNames]


detection1_GlobalActivePower <- AnomalyDetectionVec(x = anomaly2$Global_active_power,period = 181, direction = "both",plot = T)
detection1_GlobalIntensity <- AnomalyDetectionVec(x = anomaly2$Global_intensity,period = 181, direction = "both",plot = T)


anomaly2 <-subset(anomaly2, select = -c(Date,Time) )
anomaly2 <- anomaly2%>% mutate_all(~(scale(.) %>% as.vector))

detection2 <- mahalanobis(anomaly2[,c(1,2)], colMeans(anomaly2[,c(1,2)]),cov(anomaly2[,c(1,2)]))
anomaly2$MD <- round(detection2,3)
anomaly2$outlier <- FALSE
anomaly2$outlier[anomaly2$MD > cutoff] = TRUE
anomaly2$color = "black"
anomaly2$color[anomaly2$outlier== TRUE]="blue"
number2 = sum(anomaly2$outlier == TRUE)

ggplot(data = anomaly2,aes( x = Global_intensity, y = Global_active_power, color = color))+
  geom_point(size = 3,alpha = 0.6)+
  labs(title = "Dataset 2")+
  scale_colour_manual (labels = c("Normal points","Anomalies"),values = c("blue","orange"))

vec <- rep(c(181),each= 52)

set.seed(5)
mod_B<- depmix(list(anomaly2$Global_active_power ~1,anomaly2 $Global_intensity~1), data=anomaly1 , nstates= 20,
               family=list(gaussian(),gaussian()), ntimes=vec)
fm_B <- fit(mod_B)
print(fm_B)
anamoly_BIC <- append(anamoly_BIC, BIC(fm_B))
anamoly_logs <- append(anamoly_logs, logLik(fm_B))

anomaly3 <- read_csv("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/Project/DataWithAnomalies3.txt",
                    col_types = cols(
                      Date = col_date("%d/%m/%Y"),
                      Time = col_character(),
                      Global_active_power = col_double(),
                      Global_reactive_power = col_double(),
                      Voltage = col_double(),
                      Global_intensity = col_double(),
                      Sub_metering_1 = col_double(),
                      Sub_metering_2 = col_double(),
                      Sub_metering_3 = col_double()
                    )
)

anomaly3 = replace(anomaly3, is.na(anomaly3), 0)
anomaly3$weekday <- wday(anomaly3$Date,label = TRUE)
anomaly3 <- anomaly3[anomaly3$weekday == "Fri",]

anomaly3 <- anomaly3[anomaly3$Time >= "18:00:00" & anomaly3$Time <= "21:00:00",]
colNames <- c('Global_active_power','Global_intensity','Date',"Time")
anomaly3 <- anomaly3[,colNames]


detection3_GlobalActivePower <- AnomalyDetectionVec(x = anomaly3$Global_active_power,period = 181, direction = "both",plot = T)
detection3_GlobalIntensity <- AnomalyDetectionVec(x = anomaly3$Global_intensity,period = 181, direction = "both",plot = T)

anomaly3 <-subset(anomaly3, select = -c(Date,Time) )
anomaly3 <- anomaly3%>% mutate_all(~(scale(.) %>% as.vector))
vec <- rep(c(181),each= 52)

detection3 <- mahalanobis(anomaly3[,c(1,2)], colMeans(anomaly3[,c(1,2)]),cov(anomaly3[,c(1,2)]))
anomaly3$MD <- round(detection3,3)
anomaly3$outlier <- FALSE
anomaly3$outlier[anomaly3$MD > cutoff] = TRUE
anomaly3$color = "black"
anomaly3$color[anomaly3$outlier== TRUE]="green"
number3 = sum(anomaly3$outlier == TRUE)

ggplot(data = anomaly3,aes( x = Global_intensity, y = Global_active_power, color = color))+
  geom_point(size = 3,alpha = 0.6)+
  labs(title = "Dataset 3")+
  scale_colour_manual (labels = c("Normal points","Anomalies"),values = c("blue","orange"))


set.seed(2)
mod_C<- depmix(list(anomaly3$Global_active_power ~1,anomaly3 $Global_intensity~1), data=anomaly1 , nstates=20,
               family=list(gaussian(),gaussian()), ntimes=vec)
fm_C <- fit(mod_C)
print(fm_C)
anamoly_BIC <- append(anamoly_BIC, BIC(fm_C))
anamoly_logs <- append(anamoly_logs, logLik(fm_C))

 table3 <- data.frame(anamoly_BIC,anamoly_logs)
table4 <- data.frame(number1,number2,number3)
