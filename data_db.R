# data records for the database

# this will create 9 csv files corresponding to patient ID's 1-10, 11-20, etc.
# each new dataframe
# the length of each dataframe will be one entry every 10 seconds over the course of 3 days
set.seed(35)
length = 6*60*24*3

#create timestamp
x <- c(1:length)
time = 1609873460 + 10 * x

#keep records on the statistics
records <- data.frame(id = integer(),
                      mu = double(),
                      mean = double(),
                      sigma = double(),
                      sd = double())

for (i in c(0:8))
{
  #initialize an empty dataframe
  df <- data.frame(patient_id=integer(),
                   bed_id=integer(),
                   heart_rate =integer(),
                   O2=integer(),
                   blood_pressure=character(),
                   time = integer(),
                   stringsAsFactors=FALSE)

  #records inside of dataframe
  for (j in c(1:10))
  {
    #bed ID and patient ID are created
    id = i * 10 + j
    bed_id = rep(id, length)
    patient_id = 10000 + bed_id

    # sample heart rate
    heart_rate = round(rnorm(length, mean=80, sd = 10), 0)

    #sample O2
    O2 <- round(rnorm(length, mean = 84 + 2*i, sd = j), 0)
    O2 <- replace(O2, O2 > 100, 100)

    #sample Blood Pressure
    upper =  round(rnorm(length, mean=120, sd = 10), 0)
    lower =  round(rnorm(length, mean=60, sd = 5), 0)
    blood_pressure = paste(upper, "/", lower)

    #combine dataframes
    temp = data.frame(patient_id, bed_id, heart_rate, O2, blood_pressure, time)
    df = rbind(df, temp)
    head(df)

    stats <- c(id, (84+2*i), mean(O2), j, sd(O2))
    records = rbind(records, stats)
  }

  filename = paste("C:\\Users\\Nathan\\Desktop\\Data", i, ".csv")
  write.csv(df,filename, row.names = FALSE)

}

write.csv(records, "C:\\Users\\Nathan\\Desktop\\Statistics.csv", row.names = FALSE)
