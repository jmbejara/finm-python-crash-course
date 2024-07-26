* Load environment variables
doenv using ".env"

* Define file paths
local data_dir = "`r(DATA_DIR)'"
local output_dir = "`r(OUTPUT_DIR)'"

local filepath = "`data_dir'/pulled/fred.csv"
local output_filepath = "`output_dir'/example_stata_plot.png"

* Display the paths to verify
display "`filepath'"
display "`output_filepath'"

* Read the CSV file into memory
import delimited `filepath', clear

* Drop rows where GDP is missing
drop if missing(gdp)

* Convert DATE column from string to Stata date format
gen date_numeric = date(date, "YMD")
format date_numeric %td

* Set the time variable
tsset date_numeric

* Generate the plot
twoway (tsline gdp), title("GDP over Time") xtitle("Date") ytitle("GDP")
graph export "`output_filepath'", replace

* * Save the plot
* graph export `output_filepath', replace