
data <- read_csv(
  'Group_Assignment_1_Dataset.txt',
  col_types = cols(
    Date = col_date("%d/%m/%Y"),
    Time = col_time(format = "%H:%M:%S"),
    Global_active_power = col_double(),
    Global_reactive_power = col_double(),
    Voltage = col_double(),
    Global_intensity = col_double(),
    Sub_metering_1 = col_double(),
    Sub_metering_2 = col_double(),
    Sub_metering_3 = col_double()
  )
)

row = data[data$Date > ('2007-04-08') & data$Date< ('2007-04-17'),]

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

weekend <- row[row$Date == ("2007/04/14")|row$Date == ("2007/04/15"),]
weekday <- row[row$Date != ("2007/04/14")&row$Date != ("2007/04/15"),]
class(weekday$Time)
weekday_night <- weekday[weekday$Time >  hours(18)+minutes(00)+seconds(00)| weekday$Time <  hours(5)+minutes(59)+seconds(00),]
weekend_day <- weekend[weekend$Time >  hours(6)+minutes(00)+seconds(00) & weekend$Time< hours(17)+minutes(59)+seconds(00),]
weekend_night <- weekend[weekend$Time >  hours(18)+minutes(00)+seconds(00)| weekend$Time <  hours(5)+minutes(59)+seconds(00),]

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

ggplot( )+
  geom_line(data = group_weekday_day, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#C3D7A4"))+
  geom_smooth(data = group_weekday_day, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "red"),se = FALSE, method = "lm")+
  stat_smooth(data = group_weekday_day, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#C4961A"),se = FALSE,method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  geom_line(data = group_weekend_day, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#52854C"))+
  geom_smooth(data = group_weekend_day, mapping = aes(x=Time, y = Avg_Global_intensity, colour = "blue"),se = FALSE, method = "lm")+
  stat_smooth(data = group_weekend_day, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#00AFBB"), se = FALSE,method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  labs(title = "Weekday/Weekend Day", y = "Global Intensity")+ scale_color_manual(labels = c("Polynomial weekday day", "Weekday_day","Weekend day","Polynomial Weekend day","Linear weekend day","Linear weekday day"), values = c("#C3D7A4", "red","#C4961A","52854C","blue","#00AFBB"))


ggplot( )+
  geom_line(data = group_weekday_night, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#C3D7A4"))+
  geom_smooth(data = group_weekday_night, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "red"),se = FALSE, method = "lm")+
  stat_smooth(data = group_weekday_night, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#C4961A"),se = FALSE,method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  geom_line(data = group_weekend_night, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#52854C"))+
  geom_smooth(data = group_weekend_night, mapping = aes(x=Time, y = Avg_Global_intensity, colour = "blue"),se = FALSE, method = "lm")+
  stat_smooth(data = group_weekend_night, mapping = aes(x=Time, y = Avg_Global_intensity,colour = "#00AFBB"), se = FALSE,method = lm, formula = y ~ poly(x, 5, raw = TRUE)) +
  labs(title = "Weekday/Weekend Night", y = "Global Intensity")+ scale_color_manual(labels = c("Polynomial weekday night", "Weekday_night","Weekend night","Polynomial Weekend night","Linear weekend night","Linear weekday night"), values = c("#C3D7A4", "red","#C4961A","52854C","blue","#00AFBB"))



