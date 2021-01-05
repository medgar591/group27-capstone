# Making the Patient Database

# I will create a dataframe with all of the requisit columns, then convert that to a .csv and then insert that into the database
set.seed(35)
#patients ID
id <- c(10001:10090)

# create a sample of ages
age <- round(rnorm(90,mean=32,sd=3),0)

# sample gender
sam = c("M", "F")
gender <- sample(sam, 90, replace = TRUE)

# sample weight (lbs)
weight <- round(rnorm(90, mean= 8, sd = 2), 1)

# sample height (inches)
height <- round(rnorm(90, mean= 12, sd = 3), 1)

#combine the vectors into a dataframe
df <- data.frame(id, age, gender, weight, height)
head(df)

### WRITES TO MY DESKTOP.  WILL NOT WORK ON OTHER MACHINES WITHOUT MODIFIYING THIS ###
write.csv(df,"C:\\Users\\Nathan\\Desktop\\PatientData.csv", row.names = FALSE)
