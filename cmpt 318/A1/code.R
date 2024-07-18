# 318 Assignment 1
#Karim Khoja and Bhakti Bhanushali
# 


library(dplyr)
library(ggplot2)
library(readr)

class(dataset$Date)
dataset$Date <-as.Date(dataset$Date,format = "%d/%m/%y")
class(dataset$Date)
row = dataset[dataset$Date > as.Date('2020-04-08') & dataset$Date < as.Date('2020-04-17'),]
class(row$Time)
row$Time <- as.Time(row$Time)
class(row$Time)

A = row$Global_active_power
B = row$Global_reactive_power
C = row$Voltage

mean(A)
mean(B,na.rm = TRUE)
mean(C,na.rm = TRUE)

exp(mean(log(A)))
exp(mean(log(B)))
exp(mean(log(C)))

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}
getmode(A)
getmode(B)
getmode(C)

sd(A)
sd(B)
sd(C)

weekend <- row[row$Date == as.Date("2020/04/14")|row$Date == as.Date("2020/04/15"),]
weekday <- row[row$Date != as.Date("2020/04/14")&row$Date != as.Date("2020/04/15"),]
class(weekday$Time)
weekday_day <- weekday[weekday$Time > "6:00:00" & weekday$Time<strptime("17:59:00", "%H:%M:%S"),]
weekday_night <- weekday[weekday$Time > strptime("18:00:00",format="%H:%M:%S") | weekday$Time < strptime("5:59:00", "%H:%M:%S"),]
weekend_day <- weekend[weekend$Time > strptime("6:00:00",format="%H:%M:%S") & weekend$Time<strptime("17:59:00", "%H:%M:%S"),]
weekend_night <- weekend[weekend$Time > strptime("18:00:00",format="%H:%M:%S") | weekend$Time < strptime("5:59:00", "%H:%M:%S"),]

min(weekday_day$Global_active_power)
max(weekday_day$Global_active_power)

min(weekday_day$Global_reactive_power)
max(weekday_day$Global_reactive_power)

min(weekday_night$Global_active_power)
max(weekday_night$Global_active_power)

min(weekday_night$Global_reactive_power)
max(weekday_night$Global_reactive_power)

min(weekend_day$Global_active_power)
max(weekend_day$Global_active_power)

min(weekend_day$Global_reactive_power)
max(weekend_day$Global_reactive_power)

min(weekend_night$Global_active_power)
max(weekend_night$Global_active_power)

min(weekend_night$Global_reactive_power)
max(weekend_night$Global_reactive_power)


corr_row <- row
class(corr_row)
corr_row$Date <- NULL
corr_row$Time <- NULL
cor(corr_row,method="pearson")

group_weekend_day = weekend_day %>% group_by(Time)  %>%
  summarise(Avg_Global_intensity = mean(Global_intensity))

group_weekend_night = weekend_night %>% group_by(Time)  %>%
  summarise(Avg_Global_intensity = mean(Global_intensity))

group_weekday_day = weekday_day %>% group_by(Time)  %>%
  summarise(Avg_Global_intensity = mean(Global_intensity))

group_weekday_night = weekday_night %>% group_by(Time)  %>%
  summarise(Avg_Global_intensity = mean(Global_intensity))

group_weekday_day = na.omit(group_weekday_day)

##fit_linear_weekday_day <- lm(group_weekday_day$Avg_Global_intensity~unlist(group_weekday_day$Time),na.rm = TRUE)
#fit_linear_weekday_day <- lm(Avg_Global_intensity~unlist(Time),data=group_weekday_day)

#group_weekday_night = na.omit(group_weekday_night)
#fit_linear_weekday_night <- lm(group_weekday_night$Avg_Global_intensity~unlist(group_weekday_night$Time))##

p <- c(row$Time)
pct <- as.POSIXct(p)
q <- c(group_weekday_night$Time)
pct <- as.POSIXct(q)

group_weekday_day <- group_weekday_day %>% rename(
  Avg_Global_intensity_wd = Avg_Global_intensity
)
group_weekend_day <- group_weekend_day %>% rename(
  Avg_Global_intensity_we = Avg_Global_intensity
)
graph1 <- group_weekday_day[,2]
graph2 <- group_weekend_day[,2]


graph1 <- c(group_weekend_day$Time,group_weekend_day$Avg_Global_intensity,group_weekday_day$Avg_Global_intensity)
ggplot() +
  geom_line( mapping = aes(x =pct,y=group_weekday_day$Avg_Global_intensity_wd)) + 
  geom_smooth(se = FALSE, colour = "red", method = "lm") +
  stat_smooth(se = FALSE, method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  
  geom_line( mapping = aes(x= pct, y = group_weekend_day$Avg_Global_intensity_we)) +
  geom_smooth(se = FALSE, colour = "green", method = "lm") +
  stat_smooth(se = FALSE, method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  labs(title = "Weekend/Weekday day", y = "Global Intensity",x = "Time") 
  
?plot
lm(data = group_weekend_day, x = group_weekend_day$Time, y = group_weekend_day$Avg_Global_intensity_we, na.action = T)
