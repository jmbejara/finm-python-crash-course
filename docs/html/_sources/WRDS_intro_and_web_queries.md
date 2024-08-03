# 3.6 Introduction to WRDS

## A Platform For Financial Data

Wharton Research Data Services (WRDS) is a data research platform and business intelligence tool widely used in academic, government, and corporate sectors. It provides access to a vast repository of financial, economic, and marketing data, which is pivotal for conducting rigorous research in various fields, especially in finance and economics. The platform is known for its comprehensive and high-quality datasets.

[![WRDS Logo](./assets/wrds_logo.png)](https://wrds-www.wharton.upenn.edu/)

WRDS offers a variety of datasets from numerous sources, including leading data providers like Compustat, CRSP, IBES, and Bloomberg. It covers a wide range of data types, including:

- Stock prices and trading volumes
- Financial statement data
- Analyst forecasts
- Corporate governance data
- Mutual fund and bond data
- Macroeconomic data

![WRDS Datasets](./assets/wrds_subscriptions.png)

One of the key strengths of WRDS is its user-friendly interface, which allows for easy data extraction and manipulation. It provides powerful tools for data analysis, including the ability to execute custom queries and perform complex statistical analyses. In academic settings, WRDS is particularly valued for its role in facilitating empirical research in finance and economics. It allows researchers, professors, and students to access a wealth of data necessary for testing financial theories, exploring economic trends, and developing new insights in the field of quantitative finance.

## The Core Data Sets

WRDS provides some usage statistics on their website in an introduction presentation [here](https://wrds-www.wharton.upenn.edu/documents/1400/wrds_research_data_overview.pdf). This chart shows 
the percentage of usage across all WRDS data sets.

![WRDS Database Usage](./assets/wrds_database_usage.png)

The two most popular data sets are CRSP and Compustat.

WRDS did an analysis finance papers published in the top 3 finance journals---the Journal of Finance, the Journal of Financial Economics, and the Review of Financial Studies---from the years 2004-2016. Out of all of these papers, the following chart shows how many times each data set was cited.

![Top 10 Databases](./assets/wrds_top_10_databases.png)


All of the listed data sets, except for those colored in red, are available in WRDS.

## Compustat

![Compustat Logo](./assets/Compustat_Logo.png)

[Compustat Financials, S&P Global Market Intelligence](https://www.marketplace.spglobal.com/en/datasets/compustat-financials-(8))

Compustat is a comprehensive database of financial, statistical, and market information, primarily focused on publicly traded companies. It is widely used in academic research, particularly in the fields of finance and economics, for conducting in-depth analysis of company performance and market trends. The dataset includes information from various countries and markets, making it a valuable resource for both domestic and international financial research.

Key features of the Compustat dataset include:

1. **Financial Statements:** Detailed income statements, balance sheets, and cash flow statements for a wide range of companies.

2. **Historical Data:** Longitudinal data that allows for historical trend analysis and time-series studies.

3. **Global Coverage:** Data on companies from various global markets, including North America, Europe, Asia, and more.

4. **Segment Data:** Information on business segments and geographical segments of companies.

5. **Market Data:** Includes stock prices, trading volume, and other market-related information.

6. **Corporate Actions:** Data on dividends, stock splits, mergers and acquisitions, and other corporate events.

7. **Ratios and Metrics:** Key financial ratios and metrics that are pre-calculated for ease of analysis, such as ROE, ROA, and EBITDA.

Compustat is highly regarded for its accuracy, depth, and consistency, making it a fundamental resource for both theoretical and empirical research in finance. It's extensively used for tasks like asset pricing models, risk management, portfolio construction, and corporate finance studies. For students and researchers in quantitative finance, Compustat provides a rich dataset for modeling, back-testing theories, and conducting robust financial analyses.

The following two videos provide a short introduction to Compustat on WRDS.

[![Compustat on WRDS Part 1](./assets/compustat_on_WRDS_p1.png)](https://wrds-www.wharton.upenn.edu/pages/grid-items/introduction-compustat-part-1/)
[![Compustat on WRDS Part 2](./assets/compustat_on_WRDS_p2.png)](https://wrds-www.wharton.upenn.edu/pages/grid-items/introduction-compustat-part-2/)


## CRSP

![CRSP Logo](./assets/crsp-llc-logo-web-01_3.png)

[Center for Research in Security Prices](https://www.crsp.org/)

The Center for Research in Security Prices (CRSP) is a renowned financial research database, primarily recognized for its comprehensive historical data on securities traded in the United States. Established at the University of Chicago's Booth School of Business, CRSP is a crucial resource for academic, commercial, and governmental research in finance.

Key characteristics of the CRSP database include:

1. **Extensive Historical Data:** CRSP is particularly noted for its long historical time series, which in some cases go back as far as 1925. This historical depth is invaluable for long-term financial studies and analyses.

2. **Stock Data:** The database provides detailed information on stocks listed on NYSE, AMEX, and NASDAQ, including prices, returns, trading volumes, and other market indicators.

3. **Indices:** CRSP develops and maintains a series of stock indices that serve as benchmarks for the investment industry, including value- and equal-weighted indices.

4. **Corporate Actions:** Information on dividends, stock splits, and other corporate events that impact stock valuation is extensively covered.

5. **Treasury and Mutual Fund Data:** Beyond stocks, CRSP also includes data on US Treasury bills, bonds, and mutual funds, expanding its utility for various types of financial research.

6. **Survivorship Bias-Free Data:** CRSP’s dataset is known for being free of survivorship bias, as it includes data on companies that have ceased to exist, which is crucial for accurate historical analysis.

7. **Research Quality:** The accuracy, completeness, and cleanliness of the data make CRSP a gold standard for financial research, particularly in academic settings.

For students and researchers in quantitative finance, CRSP provides essential data for analyzing stock performance, conducting empirical tests of asset pricing models, and studying market anomalies and behaviors. Its extensive historical data and robustness make it a fundamental tool for both historical analysis and contemporary market studies.

The following [video](https://wrds-www.wharton.upenn.edu/pages/grid-items/crsp-basics/) provides a nice introduction to the basics of CRSP.

[![CRSP in WRDS Basics](./assets/crsp_in_wrds_thumbnail.png)](https://wrds-www.wharton.upenn.edu/pages/grid-items/crsp-basics/)


## How do these compare with Bloomberg or Datastream?

Choosing between financial databases like CRSP, Bloomberg, or Datastream depends on the specific requirements of the research or analysis being conducted. Each of these platforms has unique strengths and features that make them suitable for different purposes. Here are some reasons why someone might opt for CRSP over Bloomberg or Datastream:

- **Historical Depth:** CRSP is renowned for its extensive historical data, particularly for U.S. securities. It offers data going back as far as 1925, which is invaluable for long-term historical research and analysis. This level of historical depth might not be matched by Bloomberg or Datastream.
- **Survivorship Bias-Free Data:** CRSP's data includes companies that have ceased to exist, which is crucial for accurate historical analyses. This feature helps in avoiding survivorship bias, making it a robust choice for academic studies that require comprehensive historical perspectives.
- **Data Consistency and Quality:** CRSP is known for its high standards in data accuracy, consistency, and cleanliness, which are critical for reliable academic research.

On the other hand, there are some drawbacks of CRSP relative to Bloomberg or Datastream.

- **Limited Scope**: CRSP has a limited scope relative to Bloomberg or Datastream. It primarily focuses on US markets and lacks the global coverage found in Bloomberg.
- **Real-Time Data**: Does not offer real-time data, which is essential for current market analysis.
- **Less Comprehensive**: Fewer types of financial data compared to Bloomberg (e.g., lacks extensive international data, commodities, real-time news).

Broadly speaking, CRSP is more suited for academic research focused on historical analysis of the U.S. stock market, offering in-depth and high-quality data with a bias-free historical perspective. Bloomberg, on the other hand, excels in providing a wide range of real-time global financial data and tools, catering more to finance professionals and analysts who require real-time data and sophisticated analysis tools. The choice between them largely depends on the specific needs, goals, and resources of the user.

## WRDS Web Queries

To familiarize yourselves to using WRDS, please [watch the following video](https://vimeo.com/436447434) about WRDS Web Queries. While we will be automating the query process using the WRDS Python package [`wrds`](https://pypi.org/project/wrds/), using the web query system is a good way for initial exploration of the data.

[![WRDS Web Queries](./assets/wrds_web_queries.png)](https://wrds-www.wharton.upenn.edu/pages/grid-items/introduction-web-queries-wrds/)


