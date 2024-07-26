library(arrow)
library(fs)
library(ggplot2)
library(tidyverse)

## Prevent the creation of Rplots.pdf
pdf(NULL)
## Another solution is this:
# library(Cairo)
# CairoPNG(file = path(OUTPUT_DIR, "example_r_plot.png"))

library(dotenv)
load_dot_env()

DATA_DIR <- Sys.getenv("DATA_DIR")
OUTPUT_DIR <- Sys.getenv("OUTPUT_DIR")

# Print the value to stdout
# cat("DATA_DIR:", DATA_DIR, "\n")

# Use base R
# filepath <- file.path(DATA_DIR, "pulled", "fred.parquet")
# Use fs
filepath <- path(DATA_DIR, "pulled", "fred.parquet")

# Read the Parquet file into a tibble
fred_tibble <- read_parquet(filepath)

# Create plot of GDP
ggplot(fred_tibble %>% drop_na(GDP), 
    aes(x = DATE, y = GDP)) +
    geom_line() +
    labs(x = "DATE", y = "GDP") +
    theme_minimal()


filepath <- path(OUTPUT_DIR, "example_r_plot.png")
ggsave(filepath)
