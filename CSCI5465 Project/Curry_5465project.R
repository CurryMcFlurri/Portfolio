library(ggplot2)

# Read CSV into dataframe
data <- read.csv("C:/Users/cjinr/OneDrive/Documents/Grad School Documents/BICB/CSCI5465/Project/projectoutput.csv")

# This line below changes the is_peak info to a boolean logical which allows for the 
# information to be plotted. Currently commented out because it makes the plot
# messy and hard to read. find_peak function from python is either not useful here
# or over-sensitive and detecting far too many peaks still.
#data$is_peak <- as.logical(data$is_peak)



# ggplot with peak info
ggplot(data, aes(x = mz, y = smoothed_intensity)) +
  geom_line() +
  geom_point(data = subset(data, is_peak == TRUE), aes(x = mz, y = smoothed_intensity), color = "red", size = 0.25, alpha = 0.5) +
  labs(title = "Mass Spectrometry Data with Detected Peaks",
       x = "m/z ratio",
       y = "Smoothed Intensity")

