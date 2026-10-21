THE MUSK PREMIUM
October 2026

The Musk Premium.docx / .pdf   The finished article (also in 01 Report)

02 Python Models   (run "python3 run_all.py" from inside this folder; needs pandas, numpy, matplotlib)
   common.py                        Shared paths, data loaders and chart style
   model_01_tesla_shares.py         Tesla's shares since 2024, the Roadster week, quarterly profit and free cash flow (Figure 1)
   model_02_valuation.py            Tesla against Toyota, and the profit today's price assumes (Figure 2)
   model_03_spacex.py               SpaceX revenue by business and its shares since the IPO (Figure 3)
   model_04_roadster_physics.py     0 to 60 in one second, thrust, air needed and stored energy (Figure 4)
   model_05_promise_tracker.py      Five Musk promises against what happened (Figure 5)
   run_all.py                       Runs every model

03 Data
   daily_close.csv                  Nasdaq daily closes for TSLA and SPCX via OpenBB
   tesla_financials.csv             Tesla quarterly and annual income and cash flow figures (USD bn)
   hand_collected_sources.csv       Every figure taken from an article, with source and URL
   promise_tracker.csv              The five promises with sources
   raw/                             Original downloads as JSON

04 Outputs
   charts/   fig01 to fig05
   tables/   csv results for every model

05 Report Build Files
   report_text.md, references.txt, build_report.py   Rebuilds the Word document
