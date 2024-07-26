#!/usr/bin/env Rscript
# current_dir <- getwd()
# cat("Current working directory:", current_dir, "\n")

# Read the requirements file
packages <- readLines("r_requirements.txt")

# Function to install packages if not already installed
install_if_missing <- function(package) {
  if (!requireNamespace(package, quietly = TRUE)) {
    cat("Installing package:", package, "\n")
    install.packages(package, repos = "https://cran.rstudio.com/")
  }
}

# Apply the function to each package
sapply(packages, install_if_missing)

print("All packages installed successfully!")
