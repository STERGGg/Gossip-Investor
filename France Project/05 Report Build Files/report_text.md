# Introduction

When I wrote my EPQ on Greece, the question was whether a country could survive a debt crisis without outside help, and the answer depended less on the size of the debt than on whether markets still trusted the government that owed it. Watching France this autumn, with lycées on fire in Créteil and Marseille and the French ten year bond yield touching 4.94% on 1 October 2026 [EURONEWS1], I wanted to apply the same lens to a country that is far richer, far larger and, until recently, was treated by markets as part of the core of the euro area.

My starting view is that the riots are not the problem. The French government has known for years how weak its public finances were, and on 17 September 2026 Prime Minister Sébastien Lecornu said openly that without new measures the deficit would approach 6.5% of GDP in 2027 and that debt service alone would need an extra €10 billion [EURONEWS1]. What the riots have done is make that weakness visible, add costs to a state that cannot afford them, and push away the private capital France needs to refinance itself. This matters because in Greece private bondholders carried the biggest single piece of debt relief, through the Private Sector Involvement (PSI) of March 2012 rather than 2015, the year of the referendum [ESM11].

This report therefore asks one question: **to what extent are the 2026 riots a cause of France's fiscal crisis, rather than an amplifier of a problem the state already knew it had?** Because France is the second largest economy in the euro area, I also ask what its crisis means for the euro and for European politics, and I compare France with its neighbours throughout. Chapter 8 then takes seven questions that people most often ask about France, from whether the street usually wins to what the crisis means for a mortgage. I combine public research from INSEE, the IMF, the ECB, Eurostat, the OECD and the Agence France Trésor (AFT) with fourteen Python models of my own, and every figure is either taken from a named source or calculated in one of those models, as the appendix explains. A short list of key terms follows for readers who do not work with bond markets.

# Key terms

**Basis point (bp):** one hundredth of a percentage point, so 100 basis points equal 1%.

**OAT and Bund:** the ten year government bonds of France and Germany. The **spread** is the gap between their yields, the extra interest France pays to borrow compared with Germany, and is the market's clearest measure of French risk.

**Primary balance:** the budget balance before interest payments. A primary deficit means the state borrows even to pay for its current services, before it has paid anything to its creditors.

**r minus g:** the interest rate on the debt (r) minus the growth rate of nominal GDP (g). When r is below g, debt shrinks relative to the economy on its own; when r is above g, the state needs a primary surplus just to stand still. The **debt stabilising primary balance** is the surplus needed to keep debt flat as a share of GDP.

**Refinancing:** replacing debt that falls due with new borrowing at today's rates, which is how higher rates slowly feed into the interest bill.

**Gross financing need:** the deficit plus all the debt that matures in a year, in other words everything the state must borrow that year.

**Haircut and PSI:** a haircut is a cut in the amount a bondholder is repaid. The Greek PSI of 2012 was a negotiated haircut imposed on private investors.

**CDS (credit default swap):** an insurance contract that pays out if a country defaults. Its price shows how likely markets think a default is.

**ECB, TPI and ESM:** the European Central Bank; its Transmission Protection Instrument, which allows it to buy a country's bonds if spreads move without good reason, but only if the country follows EU fiscal rules; and the European Stability Mechanism, the euro area's rescue fund.

**Article 49.3 and censure motion:** 49.3 lets a French government pass a budget without a vote, but the Assembly can then bring down the government with a censure motion.

**Monte Carlo simulation:** running a model thousands of times with random but realistic shocks to see the range of outcomes rather than one forecast.

**Event study and abnormal return:** a way of measuring how much a share price moved because of an event, by comparing the move with what the market as a whole would normally have caused.

**Assurance vie:** the main French savings product, a life insurance contract that households use as a savings account and which invests heavily in French government bonds.

**RN:** the Rassemblement National, Marine Le Pen's party.

# Chapter 1  How did France get here?

## Fifty years without a balanced budget

France last balanced its budget in 1974 [IFRAP1], and in the IMF database, which runs from 1995, there is not a single year in which the French general government ran a surplus (Model 01). Debt rose from 65.5% of GDP in 2007 to 98.2% in 2019 and then to 115.6% at the end of 2025 [INSEE2], and by the end of the second quarter of 2026 it had reached €3,595.5 billion, or 119.0% of GDP [INSEE3]. As Figure 1 shows, France started this period alongside Germany and has finished it much closer to Italy, and on IMF projections it will overtake a falling Greek ratio in 2029.

[FIG fig01_debt_paths.png]

[FIG figA1_model01_decomposition.png]

The simplest explanation is the size of the French state. In 2025 general government spending was 57.2% of GDP, compared with 50.1% in Germany, 51.2% in Italy and 45.3% in Spain (IMF WEO, Model 01). Revenue is also high at 52.2% of GDP, so the issue is not that France does not tax but that it has never taxed enough to cover what it spends (Figure 3).

[FIG fig02_revenue_spending.png]

## Tax cuts in the good years

The more interesting question is when the gap widened, so I split each change in the deficit into a revenue part and a spending part (Model 01). Between 2017 and 2024 the deficit widened from 3.4% to 5.8% of GDP. Over the same period spending actually fell by 0.7 points of GDP, while revenue fell by 3.1 points, which at 2024 GDP is about €91 billion a year of income the state gave up. Over the longer run from 2007 to 2025 the picture is different, with spending up 3.6 points and revenue up 1.5 points, so France has both a spending problem built up over two decades and a revenue problem created more recently.

This matters for my argument because the tax cuts of the first Macron term, which included the replacement of the wealth tax and the flat tax on capital income, were made in years when borrowing was almost free. In 2019 the effective interest rate on French debt was only 1.54% while nominal GDP grew by 3.26% (Model 01). That was the moment to build a buffer, and instead the state used it to lower revenue, and so when Covid ("whatever it costs") and the energy shield of 2022 arrived, they were added to a deficit that was never closed in the first place.

## The end of cheap money

The final ingredient is the interest bill. Measured as the primary balance minus the overall balance, France paid €62 billion of interest in 2025, or 2.1% of GDP, and the IMF expects €75 billion in 2026 and €119 billion by 2030 (Model 01). The reason the bill keeps growing even if rates stopped rising today is that only about one seventh of the state's debt is repriced each year, the €175.8 billion of bonds maturing in 2026 plus the €220 billion of short term bills that are rolled over [SENAT1, AFT1], so old cheap bonds are still being replaced by new expensive ones.

The comparison with Italy shows why markets have turned. Italy carries more debt, but it runs a primary surplus of 0.5% of GDP in 2025 and 1.0% in 2026, whereas France runs a primary deficit of 3.0% and 2.9% (IMF WEO, Model 01). With the interest rate and nominal growth now almost equal (Figure 2), the primary balance that would hold debt flat is close to zero, so the 2.9 point gap to the actual primary balance is the true size of the problem, and it existed before a single school was blockaded. Put simply, France is borrowing to pay for today's services, not only to pay interest on the past.

# Chapter 2  Timeline: where it went wrong

Figure 4 places the main political and fiscal events of the last twenty years against the spread between French and German ten year yields, which is the clearest measure of how much extra France pays because it is France.

[FIG fig03_timeline.png]

Three things stand out. The first is that the euro crisis hit France hard, with the spread peaking at 154 basis points in November 2011 (Model 08), but this was contagion from Greece and Italy and it faded once the ECB committed to defending the euro. The second is that every spike after 2012 was political rather than fiscal: the Le Pen surge in early 2017, the dissolution of the Assembly in June 2024, the censure of the Barnier government in December 2024 and the fall of the Bayrou government on 8 September 2025, which was followed four days later by Fitch cutting France to A+. The third is that the floor has moved. Between January and May 2024 the spread averaged 52 basis points, by September 2026 the monthly average was 97, and around 2 October 2026 it reached about 150 basis points, the widest since the euro crisis [REUTERS1].

## Where it went wrong

Looking back over this timeline, I would point to three decisions rather than one event. The first was cutting taxes in 2017 to 2019 without matching spending cuts, which wasted the one period in which consolidation would have been cheap. The second was the repeated slippage after Covid, when missed deficit targets were quietly revised. The third, and the one with the clearest market impact, was President Macron's decision to dissolve the National Assembly in June 2024, which produced a parliament with no majority at exactly the moment France needed to pass several years of difficult budgets. Since then two prime ministers have fallen over the budget and the 2026 budget was only adopted on 2 February 2026 through Article 49.3 after two censure motions failed [ALJAZEERA1].

The external environment has also turned against France in 2026. An energy shock linked to the conflict involving Iran pushed euro area inflation back up, and the ECB raised its deposit rate to 2.25% from 17 June and to 2.50% from 16 September, its first increases since 2023 [DATA4]. Higher rates hurt most the country with the largest primary deficit to refinance.

## The 2026 riots

Against this background the lycée protests began in the week of 21 September 2026 in Île de France [ACTU17] and by 4 October had touched 735 schools, 24 of which had been burned or ransacked according to the Education Minister [EURONEWS4]. The students' grievances were concrete, from unreplaced teachers and classes of 32 to 36 pupils to crumbling buildings, and the movement coincided with a public sector strike over the budget. By 5 October the Justice Ministry counted 5,060 people held in police custody, 87% of them minors [ACTU17], and around 715 police officers and gendarmes had been injured, along with 215 pupils [FRANCEINFO1]. On 17 October around 550,000 people marched nationally against the budget according to the Interior Ministry, and 800,000 according to the unions [CLEPUBLIQUE1].

The students were not rioting against France's debt; they were rioting against the consequences of a state that spends 57% of GDP and still cannot staff its classrooms, and the €54 billion of savings in the 2027 budget, which includes a freeze on public sector pay and limits on pension indexation [EURONEWS1, TOUTELEUROPE1], will make that tension worse rather than better. The comparison with Greece is telling. There the riots of 2010 to 2012 came after the Troika had imposed austerity, whereas in France they have arrived before any real austerity has begun, which is why I read them as an early warning rather than a reaction.

> Q: Why did a snap election cost France more than a riot?
> A: Because markets price the ability to pass a budget, not the number of burned cars. The dissolution removed the government's majority for years, which affects every future budget, whereas a riot is a short shock unless it changes what parliament can vote for. My event study in Chapter 5 finds that the dissolution produced a large and statistically significant fall in French shares relative to their European peers, while the riot weeks did not.

# Chapter 3  The price of disorder in the bond market

## France now borrows like Italy

For most of the history of the euro, France borrowed at a large discount to Italy. In 2012 the French ten year yield averaged 296 basis points below the Italian one, in 2019 the gap was 182 basis points and in 2023 it was still 129 basis points (Model 08). In September 2026, according to the ECB's monthly data, France paid 4.44% against Italy's 4.36% and Greece's 4.22% (Figure 5). The country whose crisis I studied for my EPQ now borrows more cheaply than France. The stress has not stayed at home either: in the week to 2 October Italy's spread neared 110 basis points as KBC reported clear contagion to Belgium and Italy, and on 5 October the euro fell to $1.1161, its lowest since May 2025 [EURONEWS3].

[FIG fig04_yields_peers.png]

## How much of the spread is politics?

To separate politics from fundamentals I built a panel model of nine euro area countries (Model 03), which explains each country's spread over Germany from 2017 to 2023 by its debt, its budget balance and its normal standing, and fits 85% of the variation (Figure 6). In plain terms, the model learns from how markets treated all nine countries what spread a given level of debt and deficit "should" cost, and whatever France pays above that is the part I attribute to politics.

[FIG figA3_model03_fit.png]

The result is shown in Figure 7. Over 2017 to 2023 the model gives France a country constant of minus 34 basis points, the lowest of the nine countries, which is the discount markets used to give a core issuer. That discount has gone. In 2024 France paid 13 basis points more than the model predicts, in 2025 43 basis points more, and in the first nine months of 2026 50 basis points more. In September 2026 the unexplained premium was 71 basis points, and at the early October peak it was roughly 125 basis points.

[FIG fig05_spread_premium.png]

## The bill for disorder

If the riots were the cause of the crisis, their direct cost should be large relative to the fiscal hole. Model 04 puts the direct and indirect costs side by side in Figure 8.

[FIG fig06_bill_for_disorder.png]

[FIG figA4_model04_premium.png]

The direct damage from the 2026 protests is small. The regions, which own the lycées, have reported up to €30 million of damage in Auvergne Rhône Alpes, €7 million in Île de France and €1 million in Hauts de France [PUBLICSENAT1], plus €6 million in the Région Sud [SUDRADIO1], at most €44 million in total. Even the far more destructive urban riots of June 2023 produced €650 million of insured losses [FRANCEASSUREURS1] and about €1 billion of business damage according to MEDEF [JDE1]. These are real costs, but they are a rounding error against a €54 billion savings package.

The indirect channels are a different scale. To price the political premium I ran the unexplained spread through the debt model in Chapter 7 (Figure 9). At the September 2026 spread the premium costs €2.2 billion in its first year on the €310 billion annual issuance programme [AFT2], but because each year's expensive bonds stay on the books, the extra interest grows to €19 billion a year by 2031 and totals €56 billion over 2027 to 2031. If the October peak were to persist, the five year cost would be €99 billion. Separately, the OFCE estimates that political uncertainty has cut growth by a cumulative 0.8% by 2026 [OFCE1], which is €24.4 billion of lost output and €12.8 billion a year of lost tax, alongside €8.7 billion a year of business investment that did not happen out of the €364.8 billion companies invested in 2025 [INSEE5].

> Q: So are the riots the problem?
> A: Not directly. Their damage is measured in tens of millions and the fiscal gap in tens of billions. They matter because they make it harder for a minority government to pass consolidation, which keeps the risk premium high, and at the September 2026 spread that premium costs more over five years than the whole 2027 savings package. Chapter 8 shows the other way they matter: in France the real bill for unrest has usually been the concessions made to end it.

# Chapter 4  Private investment and the lesson from Greece

## Foreign capital is leaving the real economy

France still attracts more foreign investment projects than any other European country, 852 in 2025 against 730 in the UK and 548 in Germany, but the trend is clearly negative. EY counted 1,259 foreign investment projects in France in 2022, 1,025 in 2024 and 852 in 2025, a fall of 32% in three years (Figure 10) [EY1, EY2]. New R&D centres fell by 47% in 2025, American and German companies have halved their investment in France since 2022, and 33% of executives now cite political stability as a French disadvantage [EY1].

[FIG fig07_fdi_projects.png]

## Why France cannot do what Greece did

The link to my EPQ is in the bond market. In Greece, the PSI of 2012 forced private holders of €198 billion of Greek bonds to accept a 53.5% haircut, which wiped out €106 billion, about 54% of Greek GDP [ESM11]. The haircut worked because most of the debt was held abroad, and even so the Greek banks that held their own government's bonds had to be recapitalised afterwards, which added to the burden on the state.

France's position is far more exposed. Of its €2,882 billion of negotiable debt [AFT1], 57.5% was held by non residents in the first quarter of 2026 [AFT1], which is €1,657 billion (Model 05). A Greek style haircut on the foreign holders alone would be €887 billion, or 29% of 2026 GDP, more than eight times the entire Greek PSI (Figure 11). The remaining €1,225 billion is held largely by French banks, insurers and life insurance funds, the savings of French households, so a haircut there would simply move a loss of €655 billion, or 21% of GDP, from the state to its own citizens and banks. A French PSI would not be debt relief for France; it would be a crisis for the whole euro area.

[FIG fig08_psi_comparison.png]

[FIG figA5_model05_ownership.png]

The flow of private money therefore matters more to France than it did to Greece, because at the current non resident share foreign buyers must absorb about €195 billion of the record €340 billion programme for 2027 [IFRAP3, AFP2]. The ECB's Transmission Protection Instrument requires compliance with EU fiscal rules, which France in its excessive deficit procedure may not meet [EFG1], so the willingness of private investors to keep buying is the real backstop.

> Q: Could France use a Greek style PSI if things got worse?
> A: Practically, no. Even a haircut on foreigners alone would be eight times the Greek one, and over 40% of the debt is held at home. Greece was small relative to its creditors; France is one of its own largest creditors.

# Chapter 5  How public companies are trading

To see how listed French companies have reacted, I used daily prices of the MSCI country funds for France, Germany, Italy and Spain (Model 06). Because all four are quoted in dollars, the euro exchange rate cancels out when France is compared with another euro area country.

[FIG figA6_model06_event_study.png]

Since the last close before the dissolution, on 7 June 2024, French equities are up only 1.5% to 16 October 2026, while Germany is up 30.1%, Italy 46.5% and Spain 75.0% (Figure 14). Relative to an equal weighted basket of the other three, France has lost about a third of its value. This is not a market that has always lagged: from October 2016 to June 2024 the French fund rose 75%, far ahead of Germany at 24.5%. In 2026 alone France is down 6.4% while Italy and Spain are up, and French banks, heavy holders of government debt, have lagged most: by 2 October Société Générale was down nearly 4% on the year and Crédit Agricole 3.8%, while the index of European banks was up 14% [REUTERS1].

[FIG fig09_equities_relative.png]

The event study (Figure 13) gives the clearest support to my argument. It compares how French shares moved around each event with how they would normally have moved given what European markets did that day. Measured this way, the dissolution produced an abnormal fall of 3.2%, with a t statistic of minus 4.1, meaning a move that large would almost never happen by chance. None of the later events produced a significant abnormal move, and the riot and budget period from 17 September to 16 October 2026 shows an abnormal return of plus 0.5%, essentially zero: French shares fell 5.2% over the window, but European peers fell 5.3% at the same time. Equity investors are not reacting to the riots themselves; they repriced France once, when its political system lost the ability to govern, and they have been slowly marking it down since.

> Q: Do the riots move the CAC 40?
> A: Not measurably. Over the month of the lycée protests French shares moved in line with Germany, Italy and Spain once their usual relationship is accounted for. The damage is a slow discount that started with the dissolution and has continued through each government collapse, which fits the riots being a symptom of the deadlock rather than a new cause.

# Chapter 6  Immigration: what do the statistics say?

Immigration is often blamed for the state of the public finances, so I tested the claim against official data (Model 07). INSEE counted 7.0 million immigrants in France in 2022, or 10.3% of the population, and its provisional figure for 2024 is 7.7 million, 11.3%, although a change in census method means the latest numbers are not directly comparable [INSEE4].

[FIG figA7_model07_employment_gap.png]

## Immigrants were needed for the labour force

Between 2006 and 2022 the immigrant population grew by 1.89 million while the total population grew by 4.87 million, so immigration accounted for 39% of France's population growth. In 2024 immigrants made up 12.2% of the labour force aged 15 to 64, 3.74 million people out of 30.73 million [DGEF1]. Immigrant men are in fact more likely to be in the labour force than non immigrant men, which supports the first half of my view, that immigration added workers to an ageing economy.

## But they work less, and that has a fiscal cost

The second half is also supported, but less dramatically than the political debate suggests. The employment rate of immigrants aged 15 to 64 was 62.4% in 2024, compared with 69.8% for non immigrants, and their unemployment rate was 11.7% against 6.9% [DGEF1]. Most of the participation gap comes from women, with an activity rate of 62.7% for immigrant women against 72.8% for non immigrant women.

[FIG fig10_immigration.png]

The OECD estimated the net fiscal contribution of immigrants in France over 2006 to 2018. Counting only taxes paid and the health, education and social spending they receive, they were net contributors of 1.02% of GDP a year, but once each person is also given a share of pure public goods such as defence and debt interest, they become a net cost of 0.85% [OECD1]. Since every group looks like a net cost on that measure when the state runs deficits, the fair test is the share of the deficit. Over 2006 to 2018 the deficit averaged 4.4% of GDP, so the 0.85% was 19.4% of it, while immigrants were 8.9% of the population, about twice their share. CEPII, using a different method over 1979 to 2011, found a net effect between minus 0.5% and plus 0.05% of GDP [CEPII1].

The more useful finding is what the gap is worth. If immigrants aged 15 to 64 worked at the same rate as non immigrants, France would have about 392,000 more people in work (Model 07). Valuing their output at 60% to 100% of the average output per worker of €105,600, the one assumption in the calculation and therefore shown as a range (Figure 15), gives €25 billion to €41 billion of extra GDP and €13 billion to €22 billion of extra tax a year, or 0.4% to 0.7% of GDP. The gap is narrowing: immigrant unemployment fell from 17.7% to 11.7% between 2014 and 2024, and for immigrants from outside the EU from 21.2% to 12.7%.

## France against the rest of Europe

Set against the rest of Europe, France is not unusual in how many immigrants it has but in how few of them work. Eurostat counts 9.6 million foreign born residents in France at the start of 2025, a broader measure than INSEE's because it includes French citizens born abroad, which is 14.0% of the population against an EU average of 14.3%, and well below Germany at 20.5%, Spain at 19.3% or Austria at 22.5% [EUROSTAT1]. The difference is employment. In 2024 the employment rate of foreign born adults in France was 65.0% against 76.8% for the native born, a gap of 11.8 points that is close to the Netherlands, Germany and Sweden and almost twice the EU gap of 6.5 (Figure 17). In Italy, Spain, Ireland and Portugal the gap is close to zero or even reversed, because migrants there mostly arrive to work. The countries with large gaps are the generous northern welfare states, so the problem is how France integrates migrants into work rather than immigration itself.

[FIG fig11_immigration_europe.png]

> Q: Statistically, are immigrants responsible for France's deficit?
> A: They are a measurable but minor part of it. On the OECD's broadest measure they cost about 0.85% of GDP a year, roughly twice their population share of the deficit, mainly because of lower employment. But even removing that cost entirely would take the 2025 deficit only from 5.1% to about 4.2%, and it would not touch the €91 billion a year lost to tax cuts since 2017. The figure that matters most is the employment gap, which is one of the widest in Europe but is closing.

# Chapter 7  What happens next?

## The next seven months

Two events will decide which path France takes. The first is the 2027 budget, which will most likely be forced through with Article 49.3 again and then face a censure motion. The second is the presidential election on 18 April and 2 May 2027 [EURONEWS5], which will probably be followed by new legislative elections. Marine Le Pen, whose conviction was upheld on appeal in July 2026 but with a ban that no longer stops her standing [STRATFOR1], leads the first round with 35% in the latest OpinionWay poll [CONNEXION1], and on 19 October the Polymarket prediction market gave an RN candidate a 48% chance of winning, 47% for Le Pen and 1% for Jordan Bardella [POLYMARKET1]. Her counter budget promises €140 billion of savings but also cuts taxes by €30 billion, returns the retirement age to 62 and assumes 1.8% growth [EURONEWS2].

## Four fixed paths

The debt engine behind this chapter (Model 02, Figure 19) rolls the debt forward in euros from €3,460.5 billion at the end of 2025 [INSEE2], repricing about 13.7% of the state's debt each year [SENAT1, AFT1]. Each year the new debt equals the old debt plus interest minus the primary balance, and the interest rate on the debt drifts towards the market rate as old bonds are replaced.

[FIG fig12_debt_scenarios.png]

[FIG figA2_model02_refinancing.png]

Figure 18 shows four paths, each tied to an observed spread. If the spread fell back to its pre dissolution average of 52 basis points, debt would still reach 124% of GDP by 2031 with interest of €136 billion a year. At the September 2026 spread it ends at 125%, with €35 billion more interest over five years. If the unrest persisted, with a 150 basis point spread, slower growth and half the planned consolidation, debt reaches 133% and interest €168 billion. Only a plan that cuts the deficit to 3% by 2029 stabilises debt, at around 119%, and it needs a primary improvement of about €111 billion a year, twice the 2027 package.

> Q: Can France simply grow its way out of the debt?
> A: Not on current numbers. In 2025 the effective interest rate on French debt was 1.88% and nominal growth 1.99%, and when the two are equal growth stops eroding the debt, which is why even the IMF projects debt rising every year to 2031.

## Running the probabilities

Fixed paths hide how likely each one is, so Model 09 simulates 20,000 paths to 2031 with two layers of uncertainty. Think of it as replaying the next five years 20,000 times, each time drawing an election result and then the kind of luck France has had in a real past year. The first layer is political, with the probability of an RN president set at the 48% market price and the probability of a presidential majority at 40%, which gives four outcomes: a centrist president with a majority (21%) who delivers the IMF path, a centrist president without one (31%) who delivers half of it, an RN president with a majority (19%) who delivers the same half but repeals the 2023 pension reform at a cost rising to €14.1 billion a year [MONEYVOX2], and an RN president without one (29%). The second is economic, with each simulated year borrowing the growth, Bund, spread and primary balance shocks of a real year between 2008 and 2025, so the 2009 recession and the 2011 euro crisis are both in the sample. The appendix explains both layers in full.

[FIG fig13_debt_fan.png]

[FIG figA8_model09_distress.png]

The median path takes debt to 129% of GDP in 2031, and nine paths in ten end between 118% and 148% (Figure 20). Debt is above 130% in 45% of paths and still rising in 2031 in 76% of them. The gross financing need has a median of 18% of GDP, above the IMF's 15% high scrutiny line for advanced economies [IMF2] in 98% of paths, and in 2027 alone it is about €573 billion for the state and social security on my measure, more than the €433 billion the ESM can still lend [ESM1]. The IMF's broader measure for all public administrations is €740 billion, 23.6% of GDP [IFRAP3].

[FIG fig14_debt_2031_by_regime.png]

Figure 22 splits the outcomes by political result, and the most important finding is that the name of the president matters less than whether anyone has a majority. A centrist president with a majority gives a median of 124%, while the other three outcomes cluster around 130%. Moving the political inputs across wide ranges changes the chance of debt above 130% only between 42% and 48% (Figure 21).

## What it means for the euro area and European politics

France differs from Greece in one decisive way, which is size. In 2025 it produced 19% of euro area GDP but owed 24% of its public debt, more than Italy at 22% or Germany at 20%, which makes it the largest public debtor in the euro area (Model 10, Figure 23). Its stress also travels. Before the dissolution, French spread moves were mostly echoes of crises elsewhere, with Italy moving 2.2 basis points for each French one. Since June 2024 the shocks have started in France and the others absorb part of each move, with Italy taking 0.8 basis points, Greece 0.6 and Belgium 0.4, while the Netherlands and Ireland barely move.

[FIG fig15_eurozone_spillovers.png]

That leaves the euro area with three problems. The first is the ECB, which raised rates twice this year because inflation reached 3.8% in September, and which would be asked to cap French spreads at the same time as it is trying to tighten. Its Transmission Protection Instrument has never been used, and Bundesbank president Joachim Nagel has said the focus is price stability rather than spread levels [EURONEWS3]. The second is that the ESM's €433 billion would not cover one year of French refinancing, so any real rescue would need either conditional ECB buying or a new common instrument on the scale of NextGenerationEU. The third is that both need German consent at a time when the AfD leads German polls with 30% against 18% for the CDU and CSU [HURRIYET1], while Spain holds a snap election on 29 November and Italy votes by 2027. The euro area may therefore face its next test with weaker governments everywhere.

> Q: Could France's crisis break the euro?
> A: Not directly, because no major French party now proposes leaving it, and the RN dropped its plan for euro exit years ago. The real risk is slower: a weaker euro, higher borrowing costs for Italy, Belgium and Spain, and an ECB forced to choose between fighting inflation and protecting its second largest member.

## Would France need a haircut?

I flagged a path as in distress if by 2031 France would need a permanent primary surplus above 3% of GDP just to stop its debt rising, since Eichengreen and Panizza found only three episodes in which any country held 5% for ten years [EP1]. That happens in 14% of my paths, 9% under a centrist majority and 17% under an RN presidency. Markets price something similar. The five year CDS reached about 87 basis points around 2 October, the highest since early 2013 and nearly three times its level a month earlier [REUTERS1]. With the standard 40% recovery convention that implies a 7.0% probability of a credit event within five years, which is an upper bound because CDS prices also contain a risk premium.

> Q: Would France need a haircut?
> A: Not in the central case, and probably not even in distress. In most paths debt rises slowly, which calls for higher taxes and lower spending rather than default. In the one in seven paths where the numbers become unsustainable, the order of defence would be tightening under EU rules, then the ECB's TPI or OMT, then pressure on French banks and insurers to keep buying OATs. A Greek style haircut comes last because €655 billion of the loss would land on French savers and banks (Model 05), and any restructuring would more likely extend maturities than cut face value.

The model has one important blind spot. It contains no self fulfilling run in which buyers refuse to roll the debt, because since 2008 French spreads have always reverted under the ECB's backstops, so the true tail is fatter than Figure 20 shows.

# Chapter 8  Seven questions people ask

## Does the street win in France?

France has a long record of governments giving way to the street, and this is where the riots could become expensive. In December 1995 the Juppé government dropped the pension part of its social security plan after three weeks of strikes, and in April 2006 the first employment contract (CPE) was withdrawn after student protests even though it had already become law. The gilets jaunes are the clearest case with a price attached. The fuel tax rise that started them was cancelled, and by April 2019 the finance minister put the cost of the concessions at €17 billion a year [AFP1]: €10 billion of tax cuts and income top ups announced in December 2018, €5 billion of income tax cuts in April 2019 and €1.4 billion for lifting the freeze on low pensions. Model 11 puts that at 0.70% of 2019 GDP, 29% of that year's deficit and almost a third of the entire 2027 savings package. The exception is the 2023 pension reform, which passed with Article 49.3 after months of strikes, but even that was suspended in October 2025, at a cost of €0.4 billion in 2026 and €1.8 billion in 2027, so that the Lecornu government could survive a censure vote [IFRAP2].

[FIG fig16_protest_concessions.png]

Figure 24 puts these side by side on a scale that grows tenfold at each step. The reported damage from the 2026 protests, at most €44 million, is so small that the gilets jaunes bill was 386 times larger. So far the government has offered the lycée students five working groups on absent teachers, buildings, the school timetable, Parcoursup and pupils' representation, with first decisions due at the end of October [ECOMATIN1], and the 2027 education budget is already €1.2 billion higher than in 2026. Every billion conceded must be found elsewhere in the €54 billion package, and bond investors know the history.

> Q: If the riots cost so little, why should investors care?
> A: Because in France the bill for unrest has never been the broken windows; it has been the concessions made to end it. A repeat of the gilets jaunes would undo almost a third of the 2027 savings, and investors price that risk before any concession is made.

## Why France and not Japan, the United States or the United Kingdom?

The most common objection to all of this is that Japan owes over 200% of GDP and the United States runs a deficit of 7%, yet neither pays a French style premium. Figure 25 compares them using IMF data. On the burden of interest France is not the worst: in 2025 interest took 4.0% of French government revenue against 10.4% in the United States and 6.8% in the United Kingdom (Model 12).

[FIG fig17_france_japan_us_uk.png]

What sets France apart is not the size of the bill but who it owes and what stands behind it. First, France borrows in a currency it does not control. Japan, the United States and the United Kingdom each have a central bank that can buy its own government's bonds without asking anyone else, and the Bank of Japan holds 46.7% of all Japanese government bonds [MOF1]. The ECB can buy French bonds only under rules agreed by twenty one countries. Second, France owes most of its debt abroad: 57.5% of its negotiable debt is held by non residents [AFT1], against 7.9% of Japanese government bonds [MOF1]. Foreign investors can sell and leave, whereas Japanese banks and pension funds mostly cannot. Third, the United States issues the world's reserve currency, which gives it a tolerance no other borrower has, and the IMF expects the United Kingdom to reach a primary surplus by 2029 while France is still in primary deficit at the end of its forecast.

> Q: So is France in a worse position than America?
> A: On the arithmetic, no: the United States has a bigger deficit and pays a larger share of its revenue in interest. On the plumbing, yes: France cannot print the currency it borrows in, most of its creditors are foreign, and its lender of last resort answers to twenty one governments rather than one.

## Could France have a Truss moment?

In September 2022 the British government announced unfunded tax cuts and the thirty year gilt yield rose by about 130 basis points in three trading days, three times more than any previous move of that length [BOE1]. The fall in gilt prices was amplified by pension funds using liability driven investment, which had borrowed against their gilts and had to sell them to meet collateral calls, so the Bank of England offered to buy up to £65 billion of gilts and in the end bought £19.3 billion [BOE1]. The prime minister was gone within weeks.

The trigger exists in France. A new government after May 2027 could announce unfunded tax cuts, such as the €30 billion in the RN counter budget [EURONEWS2]. Running a 130 basis point jump through my debt model (Model 12) adds €5.9 billion of interest in 2027 and €105 billion over 2027 to 2031, and raises debt in 2031 by 2.9 points of GDP. The amplifier would be different, however. France has no British style leveraged pension industry; its large domestic holder is assurance vie, where most money sits in guaranteed euro funds and where, under the Sapin 2 law, the financial stability council can limit or suspend withdrawals for up to six months [MONEYVOX4]. That makes a fire sale less likely but moves the pain onto savers. And unlike the Bank of England, the Banque de France cannot act alone: the ECB's TPI is conditional on the very fiscal discipline that a Truss style budget would break.

> Q: Would a French Truss moment end the same way?
> A: Probably not as quickly. In London the central bank stepped in within days and the government fell within weeks. In France the sellers are slower, but the rescuer is also slower, so the crisis would last longer and would end in Frankfurt and Brussels rather than in Paris.

## What happens if France is downgraded again?

As of 19 October 2026 S&P and Fitch rate France A+ with stable outlooks, Moody's rates it Aa3 with a negative outlook and DBRS rates it AA with a negative outlook [AFT4]. Moody's has a scheduled review on 23 October, four days after this report, and S&P on 27 November [AFT4]. A cut by Moody's to A1 would put France in the single A band at all three large agencies for the first time.

Mechanically, a downgrade does less than people fear. For collateral the Eurosystem uses the best rating among its accepted agencies [ECB1], and the best French rating, AA at DBRS, sits seven notches above the investment grade floor, so French banks can keep using OATs to borrow from the ECB. The effect is through who is allowed or willing to hold French debt. Some reserve managers and funds are restricted to the highest ratings, and a lower rating raises the capital some investors must hold against the bonds. In practice markets usually move before the agencies: the French yield already trades above Italy's, which is rated lower, so a downgrade would mostly confirm what prices already say. The danger is a cut that coincides with a failed budget, when confirmation turns into a reason to sell.

> Q: Would a downgrade stop the ECB accepting French bonds?
> A: No. The ECB uses the best of four ratings and France is far above the floor at all of them. The real cost of a downgrade is a slightly smaller pool of buyers and a higher price for each new bond.

## What would a credible fix look like?

Model 02 showed that reaching the EU's 3% deficit limit by 2029 needs the primary balance to rise from minus 2.9% of GDP in 2026 to plus 0.4% in 2029, an improvement of 3.3 points, or about €111 billion a year by 2029 (Model 13). To see whether that has ever been done, I took the IMF primary balance of all twenty euro area members since 1995 and found each country's largest improvement over three years, leaving out the rebound after Covid and one off bank rescues (Figure 26).

[FIG fig18_credible_fix.png]

Twelve countries have managed a three year improvement larger than the 3.3 points France needs, so it is not impossible. The list needs reading carefully, however. Cyprus, Portugal and Spain did it under EU or IMF programmes, with the Troika in the room. Latvia and Lithuania did it after 2009 through a collapse in wages and spending that no French government could survive. Slovenia, Slovakia and Germany start from years swollen by one off costs, bank rescues in the first two and the absorption of East German privatisation debts in the third, so part of their improvement came automatically. The cleanest precedents are Finland and the Netherlands between 1995 and 1998, when the reward for consolidation was a place in the euro. France's own best effort came in the same years, 2.7 points between 1995 and 1998, which is still short of what it needs now and was achieved with a majority and a deadline. In other words, the fix has been done before, but almost always with an outside anchor, either a programme or the euro itself.

The menu of measures is not short of money. The 2027 budget already contains €43 billion of new measures [TOUTELEUROPE1]. Keeping the 2023 pension reform rather than suspending or repealing it is worth €14.1 billion a year by 2030 [MONEYVOX2]. France's 465 tax expenditures cost €88.3 billion in 2026, led by the research tax credit at €8.1 billion, the credit for employing people at home at €7.0 billion and the 10% income tax allowance for pensioners at €5.3 billion [MONEYVOX3]; trimming them by a quarter would raise about €22 billion. Bringing spending one point of GDP closer to Italy's would save about €31 billion. Together these roughly match what is needed, and raising employment, including the immigrant employment gap worth €13 billion to €22 billion of tax in Chapter 6, is the least painful lever of all. The obstacle is not arithmetic but a parliament in which no majority has voted for any of it.

> Q: Is austerity the only way out?
> A: No, but some consolidation is unavoidable. Growth helps only if it is faster than the interest rate, which it no longer is. The least painful mix is to keep the pension reform, trim tax breaks that mostly help the better off, and get more people into work, but each of these needs a majority that France has not had since 2022.

## What does it mean for people living in France?

For most households the crisis arrives slowly, through borrowing costs, savings and taxes rather than through a bank run. French mortgage rates on new loans fell to 1.11% in December 2021 and were 3.20% in August 2026 (Figure 27). On a €200,000 loan over twenty years, used here as an illustration, that raises the monthly payment from €930 to €1,129 (Model 14). That is an extra €200 a month, or 21% more. So far French borrowers are no worse off than their neighbours, because the rise has come mostly from the ECB and the Bund rather than from the French premium: in August 2026 new mortgages cost 3.20% in France against 3.55% in Italy and 4.01% in Germany [DATA5]. If the political premium spreads from government bonds into bank funding costs, that advantage is the first thing households would lose.

[FIG fig19_households.png]

Savers are more directly tied to the state than most realise. Assurance vie held €2,171 billion at the end of August 2026 [OPTIONFIN1], about 71% of GDP, and much of it is invested in French government bonds, which is why a French haircut would hit French families first (Chapter 4). The Livret A pays 1.7% from 1 August 2026 [QUECHOISIR1], below the IMF's forecast of 2.4% French inflation for 2026, so money in the most popular savings account is losing about 0.7% a year in real terms (Model 14). And the 2027 budget asks for its savings partly from households: pensions above €2,000 a month would not be raised with inflation, the pensioners' tax allowance would be capped at €3,000, family allowances would be frozen and the civil service pay index would stay where it is [TOUTELEUROPE1].

> Q: Is my money safe in a French bank?
> A: Yes. Deposits are guaranteed up to €100,000 per person per bank [FGDR1], and France is very far from the kind of crisis in which that guarantee would be tested. The realistic risks are slower: lower real returns, higher taxes, and in an extreme crisis a temporary freeze of up to six months on assurance vie withdrawals.

## Which French companies are most exposed?

The CAC 40 is less French than it looks: in 2023 its companies made 77.3% of their revenue outside France [EY3]. For a luxury group, an aerospace company or an oil major, French politics matters less than Chinese demand, aircraft orders or the dollar. The exposed companies are the ones whose profits depend on French demand, French regulation or French taxes. Banks come first, because they hold OATs, lend to French households and companies, and pay more for their own funding when the state does. By 2 October Société Générale was down nearly 4% on the year and Crédit Agricole 3.8%, while the index of European banks had risen 14%, an underperformance of roughly 18 points; BNP Paribas, with more of its business abroad, was up 13.3% [REUTERS1]. After the banks come companies whose prices or contracts are set by the state, such as utilities and motorway concessions, then those tied to French household spending, such as telecoms, retailers and builders, and finally any large company caught by the exceptional surtax on profits, which the 2027 budget renews at a rate 30% lower [TOUTELEUROPE1].

> Q: Is it worth avoiding French shares altogether?
> A: Not necessarily. The French index has fallen behind its neighbours since the dissolution, but most of its value sits in global companies whose earnings barely depend on France. The risk is concentrated in domestic banks and in companies that depend on French consumers or on the French state.

# Conclusion

My research question asked to what extent the 2026 riots are a cause of France's fiscal crisis rather than an amplifier of a problem the state already knew it had. The evidence points strongly towards amplifier. France has not balanced a budget since 1974, it cut revenue by around €91 billion a year in a period of cheap money, and it entered 2026 with a primary deficit of almost 3% of GDP while Italy ran a surplus. All of this was known before the first lycée was blockaded.

What the riots add is real but indirect. Their direct damage is measured in tens of millions of euros, and my event study finds no measurable effect on French equities during the protest weeks. Their importance lies in the political arithmetic, because by making consolidation harder to vote through they keep alive a political premium of 71 basis points in September 2026, worth about €56 billion of extra interest over five years. French history adds a second channel: the expensive part of unrest has always been the concessions, and the gilets jaunes alone cost €17 billion a year. Immigration accounts for a small share of the deficit, and what sets France apart from Spain or Italy is not the number of migrants but how few of them work.

The lesson from Greece is the one I find most worrying. Greece was rescued because its debt was small enough for official lenders to replace private investors, and France has no such option because its debt is too large and so much of it is owned at home. Unlike Japan, the United States or the United Kingdom, it also cannot fall back on its own central bank. In my EPQ I concluded that the fundamental problem in Greece was a lack of trust between Greece and its partners that led to a negative spiral. For France the trust that matters is that of the private investors who must buy around €195 billion of its bonds next year, and each week of disorder gives them another reason to ask for a higher price. My simulations suggest France does not need a haircut, because in most paths its debt rises slowly rather than exploding, and the fix it needs has been achieved by other euro area countries before, although mostly under outside programmes. The outcome depends less on who wins in May 2027 than on whether anyone wins a majority. Because France is now the largest debtor in the euro area, that question also belongs to Berlin, Rome and Frankfurt. It is no longer whether France knew how bad its finances were, but whether any government, in Paris or elsewhere, will have the votes to act on what it knows.

# Appendix A  Methodology and models

All models are written in Python using only pandas, numpy and matplotlib, and run from the folder 02 Python Models with run_all.py (fourteen models), which rebuilds every chart and table in 04 Outputs. Each script begins with a description of its method, and every hand collected figure is stored in 03 Data/hand_collected_sources.csv with its source and URL.

Model 01, How France got here: IMF WEO fiscal series; deficit decomposition; interest as primary balance minus overall balance; effective interest rate as interest divided by the previous year's debt; debt stabilising primary balance equal to the previous debt ratio multiplied by (r minus g) and divided by (1 plus g).

Model 02, Debt dynamics: debt in euros rolled forward from the INSEE end 2025 stock; refinancing share of 13.7% a year from the 2026 medium and long term redemptions in the state financing table and the stock of short term bills; curve factor solved so the model reproduces the IMF's 2026 interest bill, after which its 2027 bill of €89 to €91 billion sits between the IMF's €86 billion and the more than €91 billion quoted by EFG; marginal rate equal to a calibrated curve factor times the Bund yield plus spread; four scenarios anchored to observed spread levels.

Model 03, Spread fundamentals: annual ECB ten year spreads over Germany for nine countries regressed on IMF debt and balance with country and year effects (2017 to 2023, 63 observations, R squared 0.85); France's residual from 2024 onwards is the unexplained premium.

Model 04, Cost of unrest: reported damage figures, the premium from Model 03 priced through Model 02, and OFCE uncertainty effects converted to euros with IMF GDP and revenue and INSEE business investment.

Model 05, Private capital and PSI: AFT negotiable debt and Banque de France non resident share applied to the 53.5% Greek haircut.

Model 06, Equities: Nasdaq daily closes of the iShares MSCI France, Germany, Italy and Spain funds; relative performance since 7 June 2024; market model event study with a 250 day estimation window.

Model 07, Immigration: INSEE stock and labour market data, OECD and CEPII fiscal estimates, and an employment gap scenario using IMF GDP, unemployment and revenue.

Model 08, Charts: the timeline in Figure 4 and the yield comparison in Figure 5 from ECB monthly long term interest rates.

Model 09, Monte Carlo outlook: 20,000 paths to 2031 with two layers of uncertainty. The political layer sets the probability of an RN president at the Polymarket price of 48% on 19 October 2026 and the probability that the new president wins an Assembly majority at 40%, the average of the long record (four of the five legislative elections that followed a presidential vote between 2002 and 2022 produced one) and the recent record (neither 2022 nor 2024 did). The economic layer borrows the growth, Bund, spread and primary balance shocks of real years between 2008 and 2025 in two year blocks, with persistence estimated by an AR(1) for each series; 2020 and 2021 are left out because with only sixteen years to draw from the pandemic would otherwise appear in about half of all paths. Distress is a 2031 debt stabilising primary balance above 3% of GDP, and the CDS implied default probability uses the standard 40% recovery convention: the annual default intensity is the CDS spread divided by one minus the recovery rate.

Model 10, Euro area: France's share of euro area GDP and public debt from IMF WEO data for all 21 members, and regressions of each country's monthly spread change on the French spread change before and after June 2024. Eurostat employment rates by country of birth and foreign born population shares feed the European comparison in Chapter 6.

Model 11, Protest concessions: reported annual costs of concessions since 1995 converted to shares of GDP and of the deficit with IMF data, set against reported damage and the Model 04 premium.

Model 12, International comparison: IMF WEO debt, balances and revenue for France, Italy, Germany, the United States, the United Kingdom and Japan in 2025 and 2031, with interest as primary minus overall balance; a 130 basis point jump, the size of the 2022 gilt move, added to the French spread from 2027 in the Model 02 engine.

Model 13, Credible fix: the primary improvement in Model 02 scenario D; the largest three year rise in the primary balance for each of the twenty euro area members over 1995 to 2025 from IMF data, excluding windows starting in 2020 or 2021 and windows starting from a primary deficit worse than 10% of GDP, with each window tagged if it overlaps an EU or IMF programme; and a menu of reported or illustrative measures.

Model 14, Households: ECB MFI interest rate statistics for new house purchase loans in France, Germany, Italy and Spain; the annuity formula for a €200,000 loan over twenty years; the Livret A rate against the IMF 2026 inflation forecast.

Limitations: the ECB yields are monthly averages, so daily peaks come from cited market reports; the panel model's debt coefficient is imprecise; the OFCE effects are model estimates rather than observed outcomes; the ETF prices exclude dividends; the immigration scenario depends on the productivity range shown; Model 09 has no self fulfilling bond run, so its tail is too thin, and its political probabilities are anchored to markets and history rather than measured; individual French share prices were not available from my data source, so the company exposure in Chapter 8 relies on reported moves rather than my own calculation; and the €200,000 loan and the trims in Model 13 are illustrations, labelled as such.
