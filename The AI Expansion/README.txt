THE AI EXPANSION
October 2026

The AI Expansion.docx / .pdf   The finished article (also in 01 Report)

01 Report
   The AI Expansion.docx / .pdf

02 Python Models   (run "python3 run_all.py" from inside this folder; needs pandas, numpy, matplotlib)
   common.py                          Shared paths, data loaders and chart style
   model_01_who_is_falling.py         Fall from record close: Oracle, CoreWeave, Nvidia, hyperscalers, S&P 500 (Figure 1)
   model_02_revenue_gap.py            2026 hyperscaler capex and its yearly depreciation vs OpenAI and Anthropic revenue (Figure 2)
   model_14_can_giants_pay.py         Capex as a share of operating cash flow, and net new debt, for the hyperscalers and Oracle (Figure 3)
   model_15_history.py                The build out against past booms as % of GDP, and its contribution to US growth (Figure 4)
   model_03_openai_bill.py            OpenAI commitments vs revenue plan and cash burn (Figure 5)
   model_11_openai_monte_carlo.py     20,000 simulated OpenAI revenue paths vs Oracle and its commitments (Figure 6)
   model_04_anthropic.py              Anthropic quarterly revenue, valuation multiple, revenue mix (Figure 7)
   model_12_price_deflation.py        Falling AI prices, Chinese models' share, the price treadmill (Figure 8)
   model_05_bubble_test.py            Nasdaq 100 now vs the dot com boom; Nvidia since ChatGPT (Figure 9)
   model_13_your_pension.py           S&P 500 concentration now vs 2000 and a simple stress test (Figure 10)
   model_06_power_metal.py            Copper prices; data centre electricity; OpenAI's 30 GW (Figure 11)
   model_10_picks_and_shovels.py      Power, copper and chip suppliers vs the borrowers (Figure 12)
   model_07_productivity_jobs.py      US labour productivity; young workers in AI exposed jobs (Figure 13)
   model_09_imbalances.py             Current accounts: Taiwan, Korea, US and others (Figure 14)
   model_08_money_politics.py         AI money in the 2026 midterms; scale of the bet (Figure 15)
   run_all.py                         Runs every model
   (models are numbered in the order they were built; figure numbers follow the order in the article)

03 Data
   daily_close.csv                    Nasdaq daily closes via OpenBB (shares, ETFs, Nasdaq 100 from 1996)
   hyperscaler_cash_flows.csv         Nasdaq cash flow statements for Microsoft, Alphabet, Amazon, Meta and Oracle (USD bn)
   imf_weo_us_gdp.csv                 IMF World Economic Outlook US nominal GDP, 2022 to 2027
   imf_pcps_metals_monthly.csv        IMF copper and aluminium prices
   imf_weo_current_account_*.csv      IMF current account balances
   bls_productivity_nonfarm.csv       BLS labour productivity
   fed_h15_us10y_oct2026.csv          Federal Reserve H.15 ten year Treasury yield, October 2026
   hand_collected_sources.csv         Every figure taken from an article, report or film, with source and URL
   bloomberg_circular_deals_captions.txt  Key captions from the third Bloomberg film [BBG3]
   raw/                               Original downloads as JSON

04 Outputs
   charts/   fig01 to fig15 (file numbers follow the models; figure numbers follow the article)
   comics/   cartoon_submarine.png and cartoon_iou.png, the two cartoons used in the article
   tables/   csv and text summaries for every model

05 Report Build Files
   report_text.md, references.txt, build_report.py   Rebuilds the Word document
