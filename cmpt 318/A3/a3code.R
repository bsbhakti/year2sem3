library("depmixS4")
library("lubridate")
library(chron)

library(dplyr)
library(ggplot2)

dataset <- read.table("/Users/bhakti/Desktop/year 2 sem 3/cmpt 318/A2/Group_Assignment_2_Dataset.txt", header=TRUE,sep=",",)

#picking fridays from 6pm to 10pm

dataset$Date <-as.Date(dataset$Date,format = "%d/%m/%Y")
dataset$weekday <- wday(dataset$Date,label = TRUE)
dataset_day <- dataset[dataset$weekday == "Fri",]
dataset_filtered <- dataset_day[dataset_day$Time >= "18:00:00" & dataset_day$Time <= "22:00:00" ,]

colNames <- c('Global_active_power','Date',"Time")
row <- dataset_filtered[,colNames]
row$Global_active_power = scale(row$Global_active_power)
row[is.na(row)] <- 0

#181 entries in each Friday 52 mondays in all
first_friday = row[0:241,]
second_friday = row[242:482,]
third_friday = row[483:723,]
fourth_friday = row[724:964,]
fifth_firday = row[965:1205,]


data_points <- c(1:241)
ggplot()+
  geom_line(aes(x = data_points, y = first_friday$Global_active_power,color = "darkred"))+
  geom_line(aes(x = data_points, y = second_friday$Global_active_power,color = "steelblue"),linetype="twodash")+
  geom_line(aes(x = data_points, y = third_friday$Global_active_power,color = "darkgreen"),linetype="twodash")+
  geom_line(aes(x = data_points, y = fourth_friday$Global_active_power,color = "#C3D7A4"))+ 
  geom_line(aes(x = data_points, y = fifth_firday$Global_active_power,color = "#52854C"))+
  scale_colour_manual (labels = c("First friday","Second friday","Third friday","Fourth friday","Fifth friday"),values = c("darkred","steelblue","darkgreen","#C3D7A4","#52854C"))+

  labs(title="Fridays",y = "Unit Values")
vec <- rep(c(241),each= 52)


#DIFFERENT HMM MODELS
set.seed(2)

mod1 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 3, ntimes = vec)
fm1 <- fit(mod1)

summary(fm1)
print(fm1)


####################################################################################

mod2 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 5, ntimes = vec)
fm2 <- fit(mod2)

summary(fm2)
print(fm2)

####################################################################################

mod3 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 6, ntimes = vec)
fm3 <- fit(mod3)

summary(fm3)
print(fm3)

####################################################################################

mod4 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 8, ntimes = vec)
fm4 <- fit(mod4)

summary(fm4)
print(fm4)

####################################################################################

mod5 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 12, ntimes = vec)
fm5 <- fit(mod5)

summary(fm5)
print(fm5)
####################################################################################

mod6 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 16, ntimes = vec)
fm6 <- fit(mod6)

summary(fm6)
print(fm6)
####################################################################################

mod7 <- depmix(response = row$Global_active_power ~ 1, data = row, nstates = 4, ntimes = vec)
fm7 <- fit(mod7)

summary(fm7)
print(fm7)
####################################################################################

#PLOTTING
states = c(3,4,5,6,8,12,16)
BIC = c(BIC(fm1),BIC(fm7),BIC(fm2),BIC(fm3),BIC(fm4),BIC(fm5),BIC(fm6))

logs = c(logLik(fm1),logLik(fm7),logLik(fm2),logLik(fm3),logLik(fm4),logLik(fm5),logLik(fm6))

matplot(states, cbind(BIC,logs),type="l",col=c("red","green"),lty=c(1,1))

ggplot()+
  geom_line(aes(x = states, y = BIC,color = "darkred"))+
  geom_line(aes(x = states, y = logs,color = "steelblue")) +
  scale_colour_manual (labels = c("BIC","Log likelihood"),values = c("darkred","steelblue"))+
  labs(title = "BIC and log likelyhood", y = "Unit values")

table <- data.frame(states,BIC,logs)

