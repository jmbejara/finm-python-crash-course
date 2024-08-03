# {py:mod}`misc_tools`

```{py:module} misc_tools
```

```{autodoc2-docstring} misc_tools
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`merge_stats <misc_tools.merge_stats>`
  - ```{autodoc2-docstring} misc_tools.merge_stats
    :summary:
    ```
* - {py:obj}`dataframe_set_difference <misc_tools.dataframe_set_difference>`
  - ```{autodoc2-docstring} misc_tools.dataframe_set_difference
    :summary:
    ```
* - {py:obj}`freq_counts <misc_tools.freq_counts>`
  - ```{autodoc2-docstring} misc_tools.freq_counts
    :summary:
    ```
* - {py:obj}`move_column_inplace <misc_tools.move_column_inplace>`
  - ```{autodoc2-docstring} misc_tools.move_column_inplace
    :summary:
    ```
* - {py:obj}`move_columns_to_front <misc_tools.move_columns_to_front>`
  - ```{autodoc2-docstring} misc_tools.move_columns_to_front
    :summary:
    ```
* - {py:obj}`weighted_average <misc_tools.weighted_average>`
  - ```{autodoc2-docstring} misc_tools.weighted_average
    :summary:
    ```
* - {py:obj}`groupby_weighted_average <misc_tools.groupby_weighted_average>`
  - ```{autodoc2-docstring} misc_tools.groupby_weighted_average
    :summary:
    ```
* - {py:obj}`groupby_weighted_std <misc_tools.groupby_weighted_std>`
  - ```{autodoc2-docstring} misc_tools.groupby_weighted_std
    :summary:
    ```
* - {py:obj}`weighted_quantile <misc_tools.weighted_quantile>`
  - ```{autodoc2-docstring} misc_tools.weighted_quantile
    :summary:
    ```
* - {py:obj}`groupby_weighted_quantile <misc_tools.groupby_weighted_quantile>`
  - ```{autodoc2-docstring} misc_tools.groupby_weighted_quantile
    :summary:
    ```
* - {py:obj}`load_date_mapping <misc_tools.load_date_mapping>`
  - ```{autodoc2-docstring} misc_tools.load_date_mapping
    :summary:
    ```
* - {py:obj}`calc_check_digit <misc_tools.calc_check_digit>`
  - ```{autodoc2-docstring} misc_tools.calc_check_digit
    :summary:
    ```
* - {py:obj}`convert_cusips_from_8_to_9_digit <misc_tools.convert_cusips_from_8_to_9_digit>`
  - ```{autodoc2-docstring} misc_tools.convert_cusips_from_8_to_9_digit
    :summary:
    ```
* - {py:obj}`_with_lagged_column_no_resample <misc_tools._with_lagged_column_no_resample>`
  - ```{autodoc2-docstring} misc_tools._with_lagged_column_no_resample
    :summary:
    ```
* - {py:obj}`with_lagged_columns <misc_tools.with_lagged_columns>`
  - ```{autodoc2-docstring} misc_tools.with_lagged_columns
    :summary:
    ```
* - {py:obj}`leave_one_out_sums <misc_tools.leave_one_out_sums>`
  - ```{autodoc2-docstring} misc_tools.leave_one_out_sums
    :summary:
    ```
* - {py:obj}`get_most_recent_quarter_end <misc_tools.get_most_recent_quarter_end>`
  - ```{autodoc2-docstring} misc_tools.get_most_recent_quarter_end
    :summary:
    ```
* - {py:obj}`get_next_quarter_start <misc_tools.get_next_quarter_start>`
  - ```{autodoc2-docstring} misc_tools.get_next_quarter_start
    :summary:
    ```
* - {py:obj}`get_end_of_current_month <misc_tools.get_end_of_current_month>`
  - ```{autodoc2-docstring} misc_tools.get_end_of_current_month
    :summary:
    ```
* - {py:obj}`get_end_of_current_quarter <misc_tools.get_end_of_current_quarter>`
  - ```{autodoc2-docstring} misc_tools.get_end_of_current_quarter
    :summary:
    ```
* - {py:obj}`add_vertical_lines_to_plot <misc_tools.add_vertical_lines_to_plot>`
  - ```{autodoc2-docstring} misc_tools.add_vertical_lines_to_plot
    :summary:
    ```
* - {py:obj}`plot_weighted_median_with_distribution_bars <misc_tools.plot_weighted_median_with_distribution_bars>`
  - ```{autodoc2-docstring} misc_tools.plot_weighted_median_with_distribution_bars
    :summary:
    ```
* - {py:obj}`_demo <misc_tools._demo>`
  - ```{autodoc2-docstring} misc_tools._demo
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`_alphabet <misc_tools._alphabet>`
  - ```{autodoc2-docstring} misc_tools._alphabet
    :summary:
    ```
````

### API

````{py:function} merge_stats(df_left, df_right, on=[])
:canonical: misc_tools.merge_stats

```{autodoc2-docstring} misc_tools.merge_stats
```
````

````{py:function} dataframe_set_difference(dff, df, library='pandas', show='rows_and_numbers')
:canonical: misc_tools.dataframe_set_difference

```{autodoc2-docstring} misc_tools.dataframe_set_difference
```
````

````{py:function} freq_counts(df, col=None, with_count=True, with_cum_freq=True)
:canonical: misc_tools.freq_counts

```{autodoc2-docstring} misc_tools.freq_counts
```
````

````{py:function} move_column_inplace(df, col, pos=0)
:canonical: misc_tools.move_column_inplace

```{autodoc2-docstring} misc_tools.move_column_inplace
```
````

````{py:function} move_columns_to_front(df, cols=[])
:canonical: misc_tools.move_columns_to_front

```{autodoc2-docstring} misc_tools.move_columns_to_front
```
````

````{py:function} weighted_average(data_col=None, weight_col=None, data=None)
:canonical: misc_tools.weighted_average

```{autodoc2-docstring} misc_tools.weighted_average
```
````

````{py:function} groupby_weighted_average(data_col=None, weight_col=None, by_col=None, data=None, transform=False, new_column_name='')
:canonical: misc_tools.groupby_weighted_average

```{autodoc2-docstring} misc_tools.groupby_weighted_average
```
````

````{py:function} groupby_weighted_std(data_col=None, weight_col=None, by_col=None, data=None, ddof=1)
:canonical: misc_tools.groupby_weighted_std

```{autodoc2-docstring} misc_tools.groupby_weighted_std
```
````

````{py:function} weighted_quantile(values, quantiles, sample_weight=None, values_sorted=False, old_style=False)
:canonical: misc_tools.weighted_quantile

```{autodoc2-docstring} misc_tools.weighted_quantile
```
````

````{py:function} groupby_weighted_quantile(data_col=None, weight_col=None, by_col=None, data=None, transform=False, new_column_name='')
:canonical: misc_tools.groupby_weighted_quantile

```{autodoc2-docstring} misc_tools.groupby_weighted_quantile
```
````

````{py:function} load_date_mapping(data_dir=None, add_remaining_days_in_year=True, add_estimated_historical_days=True, historical_start='2016-01-01', add_estimated_future_dates=True, future_end='2092-01-01')
:canonical: misc_tools.load_date_mapping

```{autodoc2-docstring} misc_tools.load_date_mapping
```
````

````{py:data} _alphabet
:canonical: misc_tools._alphabet
:value: >
   '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*@#'

```{autodoc2-docstring} misc_tools._alphabet
```

````

````{py:function} calc_check_digit(number)
:canonical: misc_tools.calc_check_digit

```{autodoc2-docstring} misc_tools.calc_check_digit
```
````

````{py:function} convert_cusips_from_8_to_9_digit(cusip_8dig_series)
:canonical: misc_tools.convert_cusips_from_8_to_9_digit

```{autodoc2-docstring} misc_tools.convert_cusips_from_8_to_9_digit
```
````

````{py:function} _with_lagged_column_no_resample(df=None, columns_to_lag=None, id_columns=None, lags=1, date_col='date', prefix='L')
:canonical: misc_tools._with_lagged_column_no_resample

```{autodoc2-docstring} misc_tools._with_lagged_column_no_resample
```
````

````{py:function} with_lagged_columns(df=None, column_to_lag=None, id_column=None, lags=1, date_col='date', prefix='L', freq=None, resample=True)
:canonical: misc_tools.with_lagged_columns

```{autodoc2-docstring} misc_tools.with_lagged_columns
```
````

````{py:function} leave_one_out_sums(df, groupby=[], summed_col='')
:canonical: misc_tools.leave_one_out_sums

```{autodoc2-docstring} misc_tools.leave_one_out_sums
```
````

````{py:function} get_most_recent_quarter_end(d)
:canonical: misc_tools.get_most_recent_quarter_end

```{autodoc2-docstring} misc_tools.get_most_recent_quarter_end
```
````

````{py:function} get_next_quarter_start(d)
:canonical: misc_tools.get_next_quarter_start

```{autodoc2-docstring} misc_tools.get_next_quarter_start
```
````

````{py:function} get_end_of_current_month(d)
:canonical: misc_tools.get_end_of_current_month

```{autodoc2-docstring} misc_tools.get_end_of_current_month
```
````

````{py:function} get_end_of_current_quarter(d)
:canonical: misc_tools.get_end_of_current_quarter

```{autodoc2-docstring} misc_tools.get_end_of_current_quarter
```
````

````{py:function} add_vertical_lines_to_plot(start_date, end_date, ax=None, freq='Q', adjust_ticks=True, alpha=0.1, extend_to_nearest_quarter=True)
:canonical: misc_tools.add_vertical_lines_to_plot

```{autodoc2-docstring} misc_tools.add_vertical_lines_to_plot
```
````

````{py:function} plot_weighted_median_with_distribution_bars(data=None, variable_name=None, date_col='date', weight_col=None, percentile_bars=True, percentiles=[0.25, 0.75], rolling_window=1, rolling=False, rolling_min_periods=None, rescale_factor=1, ax=None, add_quarter_lines=True, ylabel=None, xlabel=None, label=None)
:canonical: misc_tools.plot_weighted_median_with_distribution_bars

```{autodoc2-docstring} misc_tools.plot_weighted_median_with_distribution_bars
```
````

````{py:function} _demo()
:canonical: misc_tools._demo

```{autodoc2-docstring} misc_tools._demo
```
````
