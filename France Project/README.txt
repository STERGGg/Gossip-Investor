FRANCE REPORT PROJECT
October 2026

01 Report
   France Report.docx / .pdf   The finished report (main text with every model chart placed where the model is first used, glossary, methodology appendix and references). Copies also sit at the top of this folder.

02 Python Models   (run "python3 run_all.py" from inside this folder; needs pandas, numpy, matplotlib; model 09 takes about 15 seconds)
   common.py                              Shared paths, data loaders and chart style
   model_01_how_france_got_here.py        Deficit decomposition, interest bill, r minus g, debt stabilising primary balance
   model_02_debt_dynamics.py              Debt engine to 2031 with refinancing, four scenarios
   model_03_spread_fundamentals.py        Panel regression: how much of the OAT spread is politics
   model_04_cost_of_unrest.py             Direct riot damage vs risk premium vs lost growth and investment
   model_05_private_capital_and_psi.py    Foreign holdings of French debt and a Greek style PSI comparison
   model_06_equities.py                   French equities vs peers since the dissolution, event study
   model_07_immigration.py                Immigration, labour force and fiscal contribution
   model_08_timeline_charts.py            Timeline chart (Figure 3) and peer yields (Figure 4)
   model_09_monte_carlo_outlook.py        20,000 path simulation to 2031: election outcomes x historical shocks, haircut test
   model_10_eurozone_spillovers.py        France's weight in the euro area and how its spread stress spills into other countries
   model_11_protest_concessions.py        Protest movements since 1995: damage against the cost of concessions
   model_12_why_france_not_japan.py       France against Japan, the US and the UK; a Truss size shock run through the debt engine
   model_13_credible_fix.py               Size of a credible consolidation, largest euro area consolidations since 1995, menu of measures
   model_14_households.py                 Mortgage rates against Germany, Italy and Spain; monthly payments; Livret A and assurance vie
   run_all.py                             Runs everything in order

03 Data
   hand_collected_sources.csv   Every figure taken from a report or article, with source and URL on each row
   imf_weo_*.csv                IMF World Economic Outlook (retrieved 19 Oct 2026), including imf_weo_international.csv (US, UK, Japan) and imf_weo_primary_balance_euro.csv (20 euro members, 1995 to 2025)
   ecb_10y_yields_monthly.csv   ECB 10 year convergence yields, 11 countries, 2007 to Sep 2026
   ecb_key_interest_rates_daily.csv  ECB deposit, main refinancing and marginal lending rates, 2019 to 19 Oct 2026
   ecb_mir_mort_monthly.csv     ECB MIR mortgage rates on new loans, France, Germany, Italy, Spain, 2015 to Aug 2026
   ecb_mir_dep_monthly.csv      ECB MIR overnight deposit rate, France
   etf_daily_close.csv          Nasdaq daily closes EWQ, EWG, EWI, EWP, EZU, Oct 2016 to 16 Oct 2026
   adr_daily_close.csv          Nasdaq daily closes of TotalEnergies and Sanofi US listings (only French names with Nasdaq data)
   insee_*.csv                  INSEE immigration stock and labour market series
   eurostat_migration_europe.csv Eurostat employment rates by country of birth and foreign born shares, 12 countries plus EU
   imf_weo_euro_area_2025.csv   GDP and debt for all 21 euro area members
   raw/                         Original downloads as JSON

04 Outputs
   charts/   All 27 figures in the report, numbered in order of appearance (file names keep the original model numbering: fig01 to fig19 and figA1 to figA8)
   tables/   Every model result as csv, plus a plain text summary per model

05 Report Build Files
   report_text.md, references.txt, build_report.py   Rebuilds the Word document from the text and charts
