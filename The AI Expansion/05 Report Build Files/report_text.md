# Introduction

It feels like all anyone talks about now is AI. It comes up in lectures, at dinner and in every investment pitch I sit through, and somewhere along the way the conversation split into two camps. One says this is the biggest technology shift since electricity, and the other says it is the biggest bubble since 1999. What made me want to write this report is that both camps sound completely sure of themselves while rarely looking at the same numbers.

The trigger was Oracle. On Friday 16 October 2026 its shares closed at $128.23, which is 61% below the record of $328.33 they reached on 10 September 2025 (Model 01). Oracle is not a speculative start up but one of the oldest names in software, and it fell because it borrowed heavily to build computing capacity for OpenAI, which has promised to pay it about $300 billion over five years [SF1]. In the same fortnight the bonds of CoreWeave, which rents out Nvidia chips, traded at a 15% yield [WALLST1], and the Financial Times reported that OpenAI's revenue was about $20 billion lower than investors had been led to believe [TC1]. The obvious question was whether the whole thing was starting to crack.

A family story kept coming back to me while I read about all of this. My dad's PhD supervisor, who is now at Oxford, likes to say that asking whether AI can really think is like asking whether a submarine can swim. The line goes back to the Dutch computer scientist Edsger Dijkstra, who wrote in 1984 that "the question of whether Machines Can Think … is about as relevant as the question of whether Submarines Can Swim" [DIJKSTRA1]. A submarine cannot swim, and it crosses the Atlantic anyway. I think the bubble debate works the same way, because whether AI "really" thinks matters far less than whether anyone can pay for it, power it and build it fast enough.

[COMIC cartoon_submarine.png]

So this report asks one question, which is **whether AI is a bubble or a real boom being held back by money, power and metal.** I have tried to answer it the way I answered the France question, with fifteen Python models built on public data. They use share prices and company cash flow statements from Nasdaq, the IMF's World Economic Outlook and commodity prices, the US Bureau of Labor Statistics, the Federal Reserve, the IEA and the US Department of Energy, together with reported figures that each carry a source. I also watched three recent Bloomberg Originals films on where the AI money is going [BBG1, BBG2, BBG3], because they raise points that market data on its own does not. Where I give my own opinion I say so, because it is my report after all.

# Key terms

**Capex** is capital expenditure, the money spent on things that last for years, such as data centres, chips and power equipment.

**Hyperscalers** are the four giant cloud companies, Amazon, Microsoft, Alphabet (Google) and Meta, which build most of the world's AI data centres.

**Operating cash flow** is the cash a company's business actually brings in during a year, before it spends anything on new buildings or equipment.

**Run rate** is a company's latest monthly or quarterly revenue scaled up to a full year, which makes it a snapshot rather than a year of actual sales.

**Depreciation and useful life** describe how the cost of equipment is spread out. A company that buys a server for $6 does not book a $6 cost on day one but spreads it over the years it expects the server to work, so a six year life means $1 a year. The longer the life, the smaller the yearly cost and the higher the reported profit.

**Backlog**, or remaining performance obligations, is revenue that customers have signed up to pay but which has not been earned yet.

**Bond yield and CDS** both measure how nervous lenders are. The yield is the return a lender demands for lending to a company, and a credit default swap is insurance against that company not paying. Both rise when lenders start to worry.

**Private credit and SPVs** are loans made by investment funds rather than banks, often through a special purpose vehicle, which is a separate company set up so that the debt does not sit on the main company's balance sheet.

**Gigawatts and terawatt hours** measure power and energy. A gigawatt is roughly what a large nuclear reactor produces, and a terawatt hour is about what 90,000 American homes use in a year.

**Current account** is the balance between what a country earns from the rest of the world and what it spends there. A country with a surplus has savings to invest abroad.

# Chapter 1  The selloff is a credit story, not a technology story

## Who is actually falling?

If AI were collapsing you would expect everything with AI attached to it to be falling at once, so that was the first thing I checked. Figure 1 shows how far each of the main AI stocks sits below its own record close, using daily Nasdaq prices up to 16 October 2026 (Model 01).

[FIG fig01_who_is_falling.png]

They are not falling together. CoreWeave is down 67% and Oracle 61%, but Microsoft is only 3% below its record, Nvidia 10%, Meta 10%, Amazon 12% and Alphabet 15%, while the S&P 500 is 2% off its peak and the Nasdaq 100 7%. What separates the two groups is not how much AI they do but how they pay for it. The hyperscalers have funded most of their data centres from the cash their existing businesses throw off, whereas Oracle and CoreWeave are borrowing to build capacity for customers who will only pay them later.

Oracle shows how stretched that second model has become. In its results for the quarter to August, published on 10 September, it reported $664 billion of contracted future revenue, up $209 billion in a year, but free cash flow of minus $5 billion, and it had sold $20 billion of new shares to help pay for the build out [ORCL1]. Its total debt is approaching $167 billion and it has guided to $90 billion to $95 billion of capital spending this financial year [SF1]. S&P rates it BBB minus, one notch above junk, and has named OpenAI as a key credit risk, while the cost of insuring Oracle's debt against default has reached about 203 basis points, the highest since 2008 [SF1]. CoreWeave has a $104 billion backlog, yet on 14 October its unsecured bonds touched a 15% yield, which is the kind of return lenders ask of a company they think might not pay them back [WALLST1].

> Q: So is the AI bubble bursting?
> A: Not in the way people usually mean it. The companies that make the chips and own the clouds are close to their highs, and what is cracking is the borrowed middle layer, meaning the companies that took on debt to build capacity for somebody else. That is a credit problem inside a real boom, and I think it is the single most important distinction in this whole debate.

## What actually set it off

The timing tells you what the market is really worried about. On 8 October the Financial Times reported that OpenAI had told investors its annualised revenue was "approaching $50 billion" rather than the roughly $70 billion that had been reported a week earlier, and that the higher figure had come from investors trying to compare OpenAI with Anthropic [TC1]. A week later CoreWeave's bonds hit 15%, and when the investor Chamath Palihapitiya posted that AI might be creating a private credit bubble, Elon Musk replied with the single word "Yikes" [WALLST1]. By 16 October Oracle had fallen about 9% in a week, US consumer prices were 3.7% higher than a year earlier [REUTERS1], and the ten year Treasury yield was still above 5% at 5.09%, having touched 5.31% earlier in the month [DATA4]. The trigger, in other words, was not that AI stopped working. It was that one very important customer turned out to be smaller than people thought at exactly the moment that borrowing became more expensive.

> Q: Why did Nvidia not fall like Oracle?
> A: Because Nvidia gets paid up front. It sells chips for cash to customers who are still buying, so its risk is that orders slow down in future. Oracle and CoreWeave have already spent the money and are waiting to be paid over five years by a customer that is losing money. In a gold rush the people selling shovels are paid on the day, while the people who borrowed to dig only get paid if they find gold.

## The money merry go round

The second reason people talk about a bubble is that so much of the money seems to go round in circles. A chip maker invests in an AI lab, the lab uses the money to rent computing from a cloud company, and the cloud company borrows to buy chips from the chip maker, so that everyone reports higher revenue and a bigger backlog. Bloomberg's film on circular deals draws the clearest map of it. Nvidia has said it will invest up to $100 billion in OpenAI, OpenAI is one of Nvidia's biggest customers, and Oracle sits in the middle as a buyer of Nvidia's chips that rents computing to OpenAI [BBG3]. One of the people interviewed makes the fair point that there is nothing wrong with this in principle, but that once these deals are stacked on top of each other the companies become so dependent on one another that if one stumbles the whole structure is at risk [BBG3]. That is the part that worries me, because it means the risk is not spread across thousands of independent customers but concentrated in a handful of companies that are all each other's customers.

The best hard number on the circle comes from the Bank for International Settlements, the central bank for central banks. In a bulletin published on 1 October 2026 it found that 55.2% of all the money invested in AI firms between 2021 and 2025 came from other AI firms, and that 46.4% of the value of those AI to AI deals also involved a supply relationship, so the investor was also selling to, or buying from, the company it had invested in [BIS1]. The BIS does not call this fraud, and it accepts that companies do it partly to secure scarce chips, but it warns that it carries risks for the wider economy and makes the industry much harder to see into [BIS1]. The circle is still getting bigger. In July Bloomberg reported that Nvidia had deals worth more than $750 billion in the works, including a partnership with South Korea's SK Group that Nvidia says will bring more than $500 billion of business and talks to guarantee up to $250 billion of leases so that OpenAI can rent computing power [BGOV1].

The financing behind the buildings has become just as creative. In October 2025 Meta put its Hyperion data centre in Louisiana into a $27 billion joint venture that is 80% owned by funds managed by Blue Owl and paid for largely with bonds, so the debt sits outside Meta's own balance sheet while Meta leases the buildings back and guarantees their value for the first sixteen years [BISNOW1]. It is a sensible deal for Meta, but it means the real amount of debt behind the build out is larger than any single company's accounts show.

> Q: Is it a problem that the money goes round in circles?
> A: Only if the final customer never pays. Critics compare it to the late 1990s, when telecom companies sold capacity to each other and both sides booked it as revenue. The circle works as long as ordinary businesses and consumers eventually spend enough on AI to cover the chips, the buildings and the interest, so the real danger is not the circle itself but how much of the industry's revenue it hides.

# Chapter 2  How big is the bet?

## One year of building against the whole industry's sales

To see whether the spending makes sense I compared one year of building with the money AI actually earns. On their latest guidance Amazon plans about $220 billion of capital spending in 2026, Alphabet about $200 billion, Microsoft about $175 billion and Meta about $137.5 billion, which comes to $732.5 billion in a single year. On their July earnings calls Amazon said that even this would not give it enough capacity to meet demand, and Alphabet said it expects its spending to rise significantly again in 2027 [PLATFORM1]. Against that, the two leading model makers together bring in about $117 billion a year, made up of OpenAI's run rate of about $50 billion [TC1] and Anthropic's third quarter revenue of $16.8 billion multiplied by four [FOOL1].

[FIG fig02_revenue_gap.png]

One year of hyperscaler capex is therefore 6.2 times the yearly revenue of the two labs (Model 02). That comparison flatters the problem slightly, because a data centre lasts for years, so the fairer test is the yearly cost of the spending. If the servers and buildings last six years, the longest life any of the companies uses, one year of capex costs $122 billion a year in depreciation, which is roughly all of OpenAI's and Anthropic's revenue combined. If AI chips wear out or go out of date in three years, as critics argue, the yearly cost doubles to $244 billion, and that is before the spending of 2024, 2025 and 2027 is added on top.

This is where the accounting argument comes in. Meta lengthened the assumed life of its servers to 5.5 years from January 2025, and the other hyperscalers have lengthened theirs too [FORTUNE1]. Michael Burry, the investor made famous by The Big Short, argues that as a result Big Tech will understate depreciation by about $176 billion between 2026 and 2028 [FORTUNE1]. I would not go as far as calling it a trick, because nobody yet knows how long an AI chip stays useful, but it does mean today's profits rest on an assumption that has never been tested.

## Can even the giants pay for it from cash?

The comfortable answer to all of this is that the hyperscalers can afford it, because they are among the most profitable companies in history. I wanted to check whether that is still true, so I downloaded their cash flow statements and compared what they spend on capex with the cash their businesses bring in (Model 14).

[FIG fig14_can_giants_pay.png]

It is becoming much less true. In 2023 the four hyperscalers spent 41% of their operating cash flow on capex, which left plenty over for dividends, buybacks and a cushion. Over the four quarters to June 2026 that share had risen to 77%. Amazon spent 107% of its operating cash flow, which means its building programme now costs more than its entire business brings in, and Oracle spent 161% [DATA5]. Microsoft is the only one of the five that has not needed to borrow. The others have gone to the bond market, and over the same twelve months Amazon took on $75 billion of net new debt, Alphabet $70 billion and Meta $52 billion, which adds up to $194 billion for the four hyperscalers in a single year [DATA5]. The 2026 guidance of $732.5 billion is 111% of the $660 billion of operating cash flow the four produced over those twelve months, so unless their cash flow grows very fast, more borrowing is guaranteed.

None of this means the giants are in trouble. Alphabet and Meta still have some of the strongest credit ratings of any company and enormous profits behind them. What it does mean is that the line I drew in Chapter 1 between the cash rich giants and the borrowed middle layer is getting thinner. Morgan Stanley estimated last year that about $2.9 trillion would be spent on data centres and their hardware between 2025 and 2028, that roughly $1.5 trillion of it would have to come from outside the companies doing the building, and that about $800 billion of that gap would be filled by private credit [MS1]. The AI build out started as a story about cash and is turning into a story about debt.

> Q: If the numbers look this bad, why do the hyperscalers keep spending?
> A: Because for them the cost of falling behind looks bigger than the cost of overbuilding. Each one is betting that AI becomes as central as the cloud did and that whoever has the capacity wins the customers. They can afford to be wrong for a few years, which is exactly what Oracle and CoreWeave cannot, but as their own cash flow statements show, even they are now borrowing to keep up.

## Has anything this big happened before?

People often describe this as the largest investment boom in history, so I checked that against the numbers (Model 15). The four hyperscalers' 2026 guidance comes to about 2.2% of US GDP on the IMF's estimate [DATA2], which is an upper bound, because some of the spending happens abroad and not all of it is for AI. Exante Data estimated AI data centre spending at 0.3% of GDP in 2023, 0.8% in 2024 and 1.3% in 2025 [FOX1].

[FIG fig15_history.png]

That is large, but it is not unprecedented. American railroad investment averaged about 2.4% of GDP through the 1870s and 1880s and reached around 6% at its peak, and spending on all information technology equipment and software hit 4.6% of GDP at the end of 2000 [FOX1]. The telecom build out on its own peaked at about 1% [FOX1], so AI has already overtaken the fibre boom and is now in the same range as the railways. That comparison cuts both ways, because the railway boom did transform the American economy, but it also ended in a string of financial crises in which many of the companies that laid the track went bust.

The right hand side of Figure 4 shows something I found more surprising. The US economy grew 2.1% in the year to the second quarter of 2026, and the Flossbach von Storch Research Institute estimates that AI related investment added between 0.45 and 0.94 percentage points of that before imports are taken into account [FVS1]. Most of the chips and servers are built abroad, though, and hardware imports have risen from 0.5% of GDP in 2024 to 1.6% now, so once they are subtracted AI's contribution falls to between 0.14 and 0.38 points [FVS1]. A large part of what looks like American growth is really money flowing to factories in Taiwan and South Korea, which is a theme I come back to in Chapter 7.

## Can OpenAI pay its bills?

Most of this bet rests on one customer. In November 2025 Sam Altman said OpenAI had about $1.4 trillion of data centre commitments over eight years [TC2], covering 30 gigawatts of computing at more than $40 billion of capital cost per gigawatt [KT1]. Spread evenly, that is $175 billion a year against a run rate of about $50 billion, so OpenAI's yearly bill is 3.5 times its revenue (Model 03), and the Oracle contract alone, at about $60 billion a year from 2027, is worth 120% of everything OpenAI currently earns.

[FIG fig03_openai_bill.png]

OpenAI does have a plan. According to internal forecasts reported by The Information, it expects revenue of $62 billion in 2027 and $282.5 billion in 2030, and it expects to burn $25 billion of cash in 2026, $57 billion in 2027, $85 billion in 2028 and $51 billion in 2029 before turning positive in 2030 [DECODER1]. That adds up to $228 billion of cash burned by the end of 2029, almost twice the $122 billion it raised in March 2026 [TC1]. To get from $50 billion to $175 billion within three years it needs to grow by 52% every single year, which is possible for a company that has grown as fast as OpenAI but leaves no room for a bad year, and October has already shown that its revenue was $20 billion lower than investors had been told [TC1].

The other problem is that most of its users pay nothing. In February OpenAI's head of ChatGPT, Nick Turley, put the number of paying subscribers at around 50 million out of more than 900 million weekly users, roughly one in eighteen [ROIC1]. Turning the other seventeen into revenue, through advertising, shopping or cheaper plans, is the part of the plan that has not been proven yet.

[COMIC cartoon_iou.png]

## Running the probabilities

A single plan hides how likely it is, so I did for OpenAI what I did for French debt and simulated it (Model 11). The model runs 20,000 versions of OpenAI's revenue from 2026 to 2030. Each starts from the company's own plan, and every year a random surprise pushes revenue above or below it, with the surprises building on each other so that a bad 2027 also drags down 2028. I sized those surprises from OpenAI's own record this year, which includes both the October gap between the $70 billion run rate investors had heard about and the $50 billion it confirmed, and the February upgrade of its forecasts by about 27% [TC1, DECODER1]. Costs are held at the levels in its own plan, because most of them are computing contracts it has already signed.

[FIG fig11_openai_monte_carlo.png]

Even taking OpenAI's plan at face value, the odds look more like a coin toss than a sure thing. Revenue covers the $60 billion Oracle contract in 2027 in 55% of paths, reaches the $175 billion average of its yearly commitments by 2029 in 48% and by 2030 in 79%, and OpenAI is cash positive in 2030 in 60% of paths. The median path needs about $224 billion of cash before it turns, and 45% of paths need more than twice the $122 billion it raised in March. If the plan drifts down by the size of the October gap, the chance of covering Oracle in 2027 falls to 39% and the chance of being cash positive in 2030 to 30%, and prices falling ten points a year faster than planned, which is what the next chapter is about, does almost the same damage.

> Q: So what are the chances OpenAI can pay?
> A: On its own plan, a little better than even for most of the milestones, and a lot worse if the plan is even slightly too optimistic. The exact percentage matters less than how sensitive it is, because a company that has to beat its plan in most years is a company that will need to keep raising money, and every one of Oracle's and CoreWeave's lenders is effectively betting that it can.

> Q: Didn't Oracle's own boss think OpenAI would not be able to pay?
> A: It was the other way round. Clay Magouyrk, Oracle's co chief executive, said OpenAI can "of course" pay, pointing to ChatGPT's 800 million weekly users [SF1]. The doubts come from outside the company, from S&P, which has Oracle one step above junk, from the credit market, which is charging the most to insure Oracle's debt since 2008, and from the shareholders who have taken 61% off its value.

## How is Anthropic meant to make money if anyone can cancel?

This was the question I most wanted answered, because a subscription you can cancel tomorrow does not sound like a solid base for a company valued in the trillions. It turns out that cancellable subscriptions are a much smaller part of the story than I assumed. The Financial Times reported that Anthropic made $16.8 billion of revenue in the third quarter of 2026, up 50% on the quarter after 140% growth the quarter before, and that it was cash flow positive and profitable on an adjusted basis, with a gross margin of 85% [FOOL1]. Working backwards from those growth rates gives about $4.7 billion in the first quarter and $11.2 billion in the second (Model 04).

[FIG fig04_anthropic.png]

Most of that money comes from businesses rather than individuals. The estimates I found are unofficial, so I treat them only as a guide, but they put about 80% of Anthropic's revenue with business and API customers and about 60% of OpenAI's with consumer subscriptions [ARCADE1]. A company that has built its customer service or its software development on a particular model does not cancel on a whim, because switching means rebuilding its own systems, and that is why I think Anthropic's business is sturdier than OpenAI's even though OpenAI is far better known.

The harder question is the price. A reported valuation of about $2 trillion at the IPO would be about 30 times Anthropic's annualised revenue of $67 billion [FOOL1]. If investors eventually valued it at ten times sales, which would still be a rich multiple for a software company, revenue would need to reach $200 billion to justify today's price, which takes 2.7 years at 50% annual growth or 4.9 years at 25% (Model 04). Anthropic also expects to spend over half a trillion dollars on infrastructure over the next decade [FOOL1], so the business looks real but the valuation already assumes years of growth.

One more caveat only showed up when I read the small print. Anthropic counts sales of its models made through cloud partners such as Amazon and Google as its own revenue, whereas OpenAI does not count the equivalent sales through Microsoft in the same way [TC1]. The two run rates are therefore not measured on the same basis, and the headline that Anthropic has overtaken OpenAI should be read with that in mind.

> Q: So could Anthropic really be profitable by the fourth quarter?
> A: On the reported numbers it already claims to be profitable on an adjusted basis and cash flow positive in the third quarter, well ahead of the 2028 breakeven it was aiming for [DECODER1]. Adjusted profit is not the same as accounting profit and none of these figures has been audited in public, so I would wait for the IPO filing before treating them as fact. The idea that it lives or dies on people cancelling their subscriptions, though, is wrong.

# Chapter 3  The price treadmill

## Falling prices

There is one force in this story that I think gets far less attention than the debt, which is that the price of AI keeps collapsing. Epoch AI, which tracks the economics of the industry, found that the price of reaching a given level of performance has been falling by between 9 and 900 times a year depending on the task, and that matching GPT-4 on a set of PhD level science questions got about 40 times cheaper every year [EPOCH1]. Andreessen Horowitz called this "LLMflation" and estimated that the cost of the same performance falls about tenfold a year. Its example is striking, because GPT-3 cost $60 per million tokens in November 2021 and three years later a small open model matched it for $0.06, a thousand times less [A16Z1].

For users that is great news, but for companies that need $175 billion a year of revenue it is a treadmill. Revenue is usage multiplied by price, and OpenAI's plan needs revenue to grow 9.4 times between 2026 and 2030 (Model 12). If prices stayed flat, usage would only need to grow 9.4 times, but if prices halved every year it would need to grow 151 times, and if they fell fourfold a year more than 2,400 times. The frontier labs escape part of this because each new model is better and can be sold at a higher price, so their prices fall much more slowly than the cost of a given level of performance, but it means they have to keep spending on new models just to stand still.

[FIG fig12_price_deflation.png]

## China and the open models

China is making the treadmill run faster. In June 2026 DeepSeek's V4 Flash model cost $0.14 per million input tokens against $5.00 for OpenAI's GPT-5.5, about 36 times less [YAHOO1]. On OpenRouter, a service that lets companies switch between models, Chinese models went from 4.5% of business usage in the first half of 2025 to a weekly peak of 46% by the middle of 2026, and they now handle 46.4% of all the tokens routed through it against 35.7% for American models [YAHOO1]. OpenRouter is not the whole market, because big companies mostly buy directly from OpenAI, Anthropic and Google, but it is where cost conscious developers go, and it shows how quickly they move once something cheaper is good enough.

> Q: Is China winning the AI race?
> A: Not at the frontier, where the American labs still lead, but it is winning the price war. Chinese open models are good enough for a large share of everyday tasks at a fraction of the price, which caps what anyone can charge for those tasks. I think this is the biggest threat to the revenue forecasts in this report, bigger than any bubble, because it means the money has to come from the most advanced work, where only a handful of companies compete.

> Q: If AI keeps getting cheaper, isn't that a good thing?
> A: For the economy it is, and it is probably how the productivity gains in Chapter 6 will eventually arrive. For the people who financed the data centres it is a problem, because cheaper AI means more computing is needed to earn the same dollar. Cheap AI and expensive data centres can both be true at once, and that is exactly the squeeze Oracle is in.

# Chapter 4  Is it 1999 again?

## The Nasdaq then and now

The comparison everyone makes is with the dot com bubble, so I tested it directly. Figure 9 lines up the Nasdaq 100 from June 1996, the first date in my data, with the Nasdaq 100 from the launch of ChatGPT on 30 November 2022, both rebased to 100 (Model 05).

[FIG fig05_bubble_test.png]

The two booms started in a similar way but look very different now. By March 2000, 46 months into my dot com series, the Nasdaq 100 had risen 7.1 times, whereas almost exactly the same number of months after ChatGPT it is up 2.4 times. After the March 2000 peak the index went on to fall 83%. The AI rally is large, but it is nowhere near the vertical climb of 1999, and much of it has been carried by one company, with Nvidia up 12.6 times since ChatGPT launched.

The other big difference is earnings. In 1999 many of the companies driving the index had little revenue and no profit, whereas today's biggest AI spenders are among the most profitable companies in history. That makes a 1999 style collapse of the whole index less likely, although Chapter 2 shows that even these companies are now borrowing, and Oracle and CoreWeave show what happens to the ones that borrowed most.

What happened after 2000 is the part people tend to forget. Bloomberg's film on circular deals points out that even the survivors took years to recover, with Amazon's shares taking around eight years to get back to their peak and Cisco, which sold the routers and switches the internet was built on, taking 25 years [BBG3]. My own data confirms the end of Cisco's wait, because it first closed above its March 2000 record on 10 December 2025, at $80.25 [DATA1]. Cisco stayed profitable and grew a great deal over those years, and it still took a quarter of a century for its shares to catch up with what investors had paid for them in 2000.

> Q: Is Nvidia the new Cisco?
> A: In one way it is. Both sold the equipment for a build out that everyone agreed was the future, and both saw their customers borrow heavily to buy it. Nvidia's profit margins are far higher than Cisco's ever were, though, and its shares trade on a much lower multiple of earnings than Cisco's did in 2000. I think Nvidia the company will be fine whatever happens, but Cisco is a warning that a great company bought at the wrong price can still be a bad investment for a very long time.

> Q: Then why do so many fund managers think it is a bubble?
> A: Because the spending is running far ahead of the revenue and because so much of the market now depends on a handful of AI companies. In Bank of America's October 2026 survey, fund managers ranked an AI bubble as the second biggest risk to markets, behind only a disorderly rise in bond yields [XTB1]. The two are connected, because higher yields make every debt funded data centre more expensive.

## Am I exposed without knowing it?

Most people do not own Oracle or CoreWeave directly, but almost everyone with a pension or an index fund owns the companies at the centre of this. In July 2026 the ten largest companies made up 38% of the S&P 500, worth $24.4 trillion together, and eight of them, Nvidia, Apple, Microsoft, Alphabet, Amazon, Broadcom, Meta and Micron, are tied directly to the AI build out [LANDMARK1]. At the peak of the dot com bubble in June 2000 the ten largest made up 33.2% of the MSCI USA index, which is a slightly different measure but a fair comparison [NASDAQ1]. The market is more concentrated now than it was then.

[FIG fig13_your_pension.png]

That makes an index fund less diversified than it sounds. Of every £100 in an S&P 500 tracker, £38 sits in ten companies. If those ten fell by half and the other 490 did not move at all, the whole index would fall 19%, and if they fell as far as the Nasdaq 100 did after 2000 it would fall 32% (Model 13). That is before any knock on effect on the rest of the market, which in a real crash would make it worse.

## Who loses if it pops?

If the boom does turn, the losses will not land evenly. First in line are the lenders to the borrowed middle layer, meaning Oracle's and CoreWeave's bondholders and the private credit funds behind deals like Hyperion. Next come the investors holding the most expensive shares, and after them the pension savers who own those shares without knowing it. Bloomberg makes a point I had not thought about, which is that Asian economies could be hit twice, first through the money they have invested in US technology shares and then through their exports of chips and memory, and that because so much of the world's savings is now tied to a few American companies nobody really knows how widely the exposure is spread [BBG2].

> Q: Am I exposed to AI even if I have never bought a tech share?
> A: Almost certainly, if you have a workplace pension or a global index fund, because they track markets in which a handful of AI companies now carry more weight than the biggest companies did in 2000. That is not a reason to panic, but it is worth knowing that "diversified" means something narrower today than it used to.

> Q: Should I sell my AI shares?
> A: I cannot tell you that, and I am not a financial adviser. What the data does say is that the risk is concentrated in companies that borrow to build for one or two customers, while the cash rich giants have so far held up, so knowing which kind of company you own matters more than whether it has AI in its name.

# Chapter 5  The real limit is physical

## Power, copper and the grid

Money can be raised in a week, but a power line takes years. This is the part of the story that I think gets too little attention, and Figure 11 puts numbers on it (Model 06).

[FIG fig06_power_metal.png]

Start with electricity. The IEA estimates that data centres used 415 TWh worldwide in 2024, about 1.5% of the world's electricity, and expects that to more than double to about 945 TWh by 2030 [IEA1]. In the US, data centres used 176 TWh in 2023, 4.4% of the country's electricity, and the Department of Energy's study projects 325 to 580 TWh by 2028, which would be between 6.7% and 12% [LBNL1]. Now put OpenAI's 30 gigawatts next to those numbers. Run flat out for a year, 30 GW would use 263 TWh, which is 1.5 times what every data centre in America used in 2023 and about 6.6% of all US electricity (Model 06), and that is one company's plan.

The grid cannot simply absorb that. The IEA notes that waits for transformers and cables have doubled in three years, that new transmission lines take four to eight years to build in advanced economies, and that about 20% of planned data centre projects could be delayed by grid constraints [IEA1]. Then there is metal. Copper is the wiring of the whole system, and the IMF's price data shows it at $14,473 a tonne in September 2026, up 48% since January 2022 and more than three times its 2015 low (Model 06). The IEA also warns about gallium, which is used in chips and of which China supplies about 99% of the world's refined output [IEA1].

> Q: So is AI held back by copper, minerals and the electrical grid?
> A: Yes, and I think this is the binding constraint, more than money. You can always find another investor, but you cannot find another transformer if the factories have a two year waiting list. It also changes the bubble question, because a physical bottleneck slows the build out and stretches it over more years, which may be exactly what stops it from overshooting.

## Who is selling the shovels?

If power and metal are the bottleneck, the companies that sell them should be doing well, so I compared the share prices of some of the physical suppliers with the chip makers and the borrowers (Model 10).

[FIG fig10_picks_and_shovels.png]

The picture is more mixed than I expected. Since the start of 2025 Freeport, one of the world's biggest copper miners, is up 84% and Vertiv, which makes the power and cooling equipment inside data centres, is up 75%, both ahead of Nvidia at 55% and the S&P 500 at 31%. AMD, which agreed to supply OpenAI with six gigawatts of chips [DCD1], is up 338%, and Nebius, a smaller AI cloud, is up 442%. The selloff has reached the suppliers too, though. Vertiv is 45% below its May 2026 peak, Nebius 42% below its June peak and Constellation, the largest US nuclear operator, 33% below its October 2025 high, so the market is not treating any part of the chain as safe. Oracle is the only one of these companies that is lower than it was at the start of 2025.

> Q: If power is the bottleneck, why have power stocks fallen too?
> A: Because their future orders depend on the same customers. A transformer maker or a nuclear operator signing long contracts with data centres faces the same question as Oracle, which is whether the AI labs will keep paying. The difference is that the suppliers sell something physical and scarce, which is why I think they will hold up better over a full cycle than the companies renting out computers.

## Why your electricity bill might be going up

This has already reached households. PJM, which runs the largest power grid in the US, including "Data Center Alley" in Virginia, held a capacity auction in July 2025 that cleared at a record $329.17 per megawatt day for June 2026 to May 2027, 22% above the previous record, which means $16.1 billion of payments to generators that will flow through to bills [OG1]. US electricity prices were already rising faster than overall inflation, up 5.6% in a year against 2.7% for consumer prices [OG1]. Bloomberg's film on the midterms shows residents in Virginia fighting data centres being built next to their homes, and a plan for more than 35 data centres near the Manassas battlefield being thrown out by the courts [BBG1].

> Q: Why should someone who never uses ChatGPT care?
> A: Because they may end up paying for it through their electricity bill. When data centres compete with homes for power, the price of power rises for everyone, which is why energy costs have become one of the biggest political issues around AI.

# Chapter 6  Is anyone actually more productive?

## The productivity numbers

The whole bet only works if AI makes the economy more productive, so I looked at the official US data. Figure 13 shows labour productivity in the nonfarm business sector, measured as the change in output per hour on a year earlier, from the Bureau of Labor Statistics (Model 07).

[FIG fig07_productivity_jobs.png]

There is something there. Productivity has grown by an average of 2.5% a year since the start of 2023, compared with 1.5% between 2016 and 2019, and it was still 2.2% up in the second quarter of 2026 [DATA3]. I would be careful about giving AI all the credit, because part of 2023 was a rebound from a weak 2022 and the jump in 2020 was not real productivity at all but the loss of low paid jobs during Covid. The academic estimates are all over the place. Apollo collected studies that put AI's total effect on productivity over a decade anywhere between 0.7% and 12%, and survey data shows workers saving only about 1.4% to 1.8% of their hours with generative AI [APOLLO1]. My reading is that the gains are real but small so far, and nowhere near large enough yet to justify $732.5 billion a year of building.

Part of the reason is that producing more is not the same as producing something the economy can measure. AI can write a strategy document in seconds, but somebody still has to read it, decide what to do and then do it, and most of the gain will only show up once companies reorganise how they work around the tools. It took factories decades to reorganise around electricity, and in 1987 the economist Robert Solow joked that you could see the computer age "everywhere but in the productivity statistics", roughly a decade before the computer finally did show up there in the late 1990s. Economists call this the lag between a technology arriving and the statistics catching up, and I think AI is still in it.

## Will AI take my job?

The most worrying chart in this report for someone my age is the one on the right of Figure 13. Erik Brynjolfsson and colleagues at Stanford used payroll data from ADP covering millions of workers and found that between November 2022 and June 2026 employment of 22 to 25 year olds fell about 11% in the jobs most exposed to AI while it grew about 10% in the least exposed jobs. In the most exposed jobs, young workers' employment is now 19% below where it would be if it had kept pace with their less exposed peers, and the gap has been widening since August 2025 [STANFORD1].

> Q: Will AI take my job?
> A: The early evidence says it is taking the entry level version of some jobs, the tasks that graduates used to learn on, rather than whole professions. The authors are careful to call these "canaries in the coal mine" rather than proof of cause, but the trend is going the wrong way. For graduates the practical lesson is to get good at the parts of a job that AI is worst at, such as judgement, and to learn the tools before the employer expects it.

> Q: What does this mean for someone starting a career in finance?
> A: This one is personal, because it is my generation. The tasks AI already does well, such as summarising filings, building first drafts of models and writing up notes, are exactly the tasks junior analysts used to be trained on. I do not think the job disappears, but I think its first two years change, and the people who do well will be those who can check the machine's work and still form a judgement of their own. Every number in this report had to be checked by hand, which is still the part AI cannot be trusted with.

# Chapter 7  Where the money goes

## The rest of the world

Bloomberg's film on AI and the world's wealth makes a point that is easy to miss when you only look at US share prices. The AI boom is pulling capital from all over the world into a small number of American companies, and the film argues that the gap between the countries that save and the countries that borrow is now as wide as it was in 2008 [BBG2]. I checked this with the IMF's data on current accounts (Model 09).

[FIG fig09_imbalances.png]

The pattern is striking. The IMF projects that Taiwan, which makes most of the world's advanced chips, will run a current account surplus of 22% of GDP in 2026, and South Korea, home of the big memory makers, 18.8%. Taiwan's surplus was already high at 10.7% in 2019 but has roughly doubled since, while the US is running a deficit of about 3.9% of GDP. This is the other side of the import figures in Chapter 2. Every server America installs is partly an export from Taiwan or Korea, and those countries' surpluses are savings, a lot of which flow straight back into US assets.

Bloomberg points out that in the 2000s this money went into US government bonds, whereas now it is going into shares, and that the pull of AI is starting to affect the US government's ability to sell its own debt at a time when it already pays about $1 trillion a year in interest [BBG2]. With the ten year yield at 5.09% [DATA4] and inflation at 3.7% [REUTERS1], that is not a theoretical worry. If AI keeps attracting the world's savings, Washington has to pay more to borrow, and higher yields in turn make every data centre financed with debt more expensive.

> Q: Why should anyone outside America care about the AI boom?
> A: Because the whole world is lending into it. Asian savings are funding US technology shares, emerging markets that need money for roads and power networks are struggling to attract it, and if AI valuations fall, Asia loses twice, on its investments and on its exports. Cross border investment grew from 27% of world GDP in 1980 to 141% in 2008 and has largely levelled off since, so the money that does move is going to fewer places [BBG2].

## Politics

The other place the money is going is Washington. Bloomberg's film on the midterms calls 2026 the most expensive US election ever, with well over $11 billion spent on advertising, and says AI aligned political groups have raised close to $300 million [BBG1]. The biggest is Leading the Future, backed by Andreessen Horowitz and OpenAI's president Greg Brockman, which wants light touch federal rules and has raised over $125 million, or $140 million by its own count. On the other side is Public First Action, set up partly in response, which Anthropic seeded with $20 million and which is estimated at $75 million to $83 million [TT1, BBG1]. Meta has spent around $65 million more [TT1].

[FIG fig08_money_politics.png]

The film compares the strategy to the crypto industry's in 2024 and even to Big Tobacco, but it also makes the point that AI is a harder sell than crypto because it touches every voter, through their job, their power bill and the data centre going up behind their house [BBG1]. I read this spending as a sign of how much is at stake rather than as a sign of a bubble. An industry spending over $700 billion a year on buildings can easily afford $300 million on politics, and if that money shapes the rules in its favour, it is one of the best returns the industry will get [BBG1].

> Q: Why are AI companies spending so much on elections?
> A: Because whoever writes the rules decides how much the industry can build, where and how fast, and who pays for the power. The fight is not really between AI and no AI but between companies that want almost no federal rules and companies that want some, with voters caught in the middle.

# Chapter 8  What happens next?

## What would make it pop?

Pulling the chapters together, I can see four things that would turn a boom with a credit problem into a real bust. The first is OpenAI missing its plan a second time, because so much of Oracle's and CoreWeave's backlog depends on it. The second is bond yields, which fund managers already rank as the biggest risk and which raise the cost of every borrowed data centre, now including the hyperscalers' own. The third is evidence that chips wear out faster than six years, which would force the hyperscalers to book bigger costs and report lower profits. The fourth is power, because if the grid cannot connect new data centres, capacity that has already been financed sits idle while the interest keeps running.

## What I will be watching

Rather than guess a date for the top, I would rather list the numbers that would tell me the story is changing. The first is OpenAI's next revenue update, because the Oracle contract is worth 120% of its current run rate. The second is the yield on CoreWeave's bonds and the price of insurance on Oracle's debt, which are the best live measure of whether lenders still trust the borrowed middle layer. The third is how much of their operating cash flow the hyperscalers are spending, because if that share keeps rising past 100% the line between the giants and the middle layer disappears. The fourth is the US ten year yield, since investors in Bank of America's survey said a yield of 5.9% would make them move money from shares into bonds [XTB1]. The fifth is the next PJM capacity auction, and the last is the Anthropic IPO filing, which will be the first time anyone outside the company sees audited accounts for one of the frontier labs.

> Q: Is this like the railway mania or the fibre bubble?
> A: In one important way it is. In both the British railway mania of the 1840s and the telecom boom of the late 1990s, investors lost a lot of money but the railways and the fibre stayed in the ground and were used for decades. If AI follows that pattern, the people who financed the build out lose, the people who use it later win, and the infrastructure outlives the companies that built it. The difference is that chips go out of date in a few years whereas a railway line or a fibre cable lasts for decades, so less of this overbuilding will still be useful in twenty years.

> Q: Is there anything that could prove the bubble fears wrong?
> A: Growth could. If OpenAI really reaches $282.5 billion of revenue in 2030 and Anthropic keeps compounding at anything like its current pace, today's spending will look sensible in hindsight, just as Amazon's losses in the early 2000s did. The bear case is not that AI fails but that the revenue arrives two or three years after the debt falls due.

## My view

My answer is that AI is a real boom with a bubble inside it. The technology is not a fad, the productivity gains are starting to show, and companies like Anthropic seem to have found customers who pay and keep paying. The financing, though, has run ahead of the revenue, and the weakest part of the chain is the companies that borrowed to build for customers who are still losing money. I expect more casualties like Oracle and CoreWeave, and I expect the giants to survive them and perhaps buy what is left cheaply, which is roughly what happened to the fibre networks laid in 1999 that went on to carry the internet for the next twenty years. What has changed my mind while writing this is the cash flow data, because the giants are no longer simply paying for the build out from profits, and the longer that continues the more the whole boom depends on credit markets staying open.

The thing I would watch most closely is not a share price but the grid. Power, copper and transformers will decide the pace of AI more than investors will, and that might turn out to be a good thing, because it forces the build out to happen over a decade rather than in three frantic years.

# Conclusion

I set out to answer whether AI is a bubble or a real boom held back by money, power and metal, and the evidence points to both at once. The market is not collapsing. Microsoft is 3% off its record and the Nasdaq 100 7%, and the AI rally is about a third of the size of the dot com run at the same stage. What is falling is the borrowed middle layer. Oracle is down 61% and CoreWeave 67% because they took on debt to serve OpenAI, whose $175 billion a year of commitments are 3.5 times its revenue and which by its own forecast will burn $228 billion of cash before it turns a profit. My simulation gives it roughly even odds of hitting its main milestones on its own plan, and much worse odds if the plan proves even slightly too optimistic.

The bet itself is enormous but not unprecedented. The four hyperscalers will spend $732.5 billion in 2026, about 2.2% of US GDP, which is more than the fibre boom and in the same range as the railways, and they now spend 77% of their operating cash flow on capex against 41% in 2023, borrowing $194 billion in a year to keep going. Anthropic's answer to my question about cancellations is that it sells mostly to businesses and on reported numbers has already reached cash flow breakeven, although its rumoured valuation already prices in years of growth. Meanwhile the price of AI keeps falling, Chinese models are taking share, and the real limits are physical. One company's 30 gigawatt plan would use 1.5 times as much electricity as every American data centre did in 2023, copper is up 48% since 2022, and households are starting to see it in their bills.

So I come back to the submarine. Arguing over whether the machine can really think is a distraction, because AI can already do useful work and does more of it every quarter. Whether it turns out to be a bubble depends on whether its revenue can catch up with its debt before its power supply runs out, and on current numbers that race is closer than either camp admits.

# Appendix A  Methodology and models

All models are written in Python using pandas, numpy and matplotlib and sit in 02 Python Models, where run_all.py rebuilds every chart and table in 04 Outputs. Each script starts with a description of its method. Market data and company cash flow statements were downloaded through the OpenBB platform on 19 October 2026 and are stored in 03 Data, and every figure taken from an article or report is stored in 03 Data/hand_collected_sources.csv with its source and URL. Figures are numbered in the order they appear, while the file and model numbers follow the order in which the models were built.

Model 01, Who is falling. Nasdaq daily closes for Oracle, CoreWeave, Nvidia, Microsoft, Alphabet, Amazon, Meta and the S&P 500 and Nasdaq 100 funds, with the fall from each record close to 16 October 2026 and the price paths rebased to the first close of 2025.

Model 02, Revenue gap. The sum of the four hyperscalers' 2026 capex guidance midpoints, with straight line depreciation of that one year of spending over six years, 5.5 years and three years, compared with OpenAI's reported run rate plus Anthropic's third quarter revenue times four.

Model 03, OpenAI's bill. $1.4 trillion of commitments spread evenly over eight years, OpenAI's revenue and its internal plan with 2028 and 2029 interpolated geometrically between 2027 and 2030, its own cash flow forecast and cumulative burn, and the growth rate needed to reach the yearly bill, which is 175 divided by 50 raised to the power of one over the number of years, minus one.

Model 04, Anthropic. Quarterly revenue rebuilt from the reported third quarter figure and growth rates, the run rate and valuation multiple, the years needed to reach a ten times sales valuation as an illustration, and an estimated revenue mix flagged as unofficial.

Model 05, Bubble test. The Nasdaq 100 from June 1996 and from 30 November 2022, both rebased to 100 and measured in months from the start, with the peak multiple, months to peak and fall after the March 2000 peak, and Nvidia rebased to the launch of ChatGPT.

Model 06, Power and metal. Monthly copper prices from the IMF's Primary Commodity Prices, data centre electricity from the IEA and from LBNL for the US Department of Energy, total US electricity backed out from LBNL's 176 TWh and 4.4% share, and OpenAI's 30 GW at full use for 8,760 hours as an upper bound.

Model 07, Productivity and jobs. BLS nonfarm business labour productivity as the change on a year earlier, averaged over 2016 to 2019 and over 2023 to the latest quarter, and employment changes for 22 to 25 year olds from Brynjolfsson, Chandar and Chen.

Model 08, Money and politics. Reported AI political spending by group, and the hyperscalers' capex against the US federal interest bill and OpenAI's commitments.

Model 09, Imbalances. IMF current account balances as a share of GDP from 2000 to 2031 for the US, Taiwan, South Korea, China, Japan and Germany.

Model 10, Picks and shovels. The share price change from 2 January 2025, or the first 2025 price, to 16 October 2026 for Vertiv, Constellation Energy, Freeport McMoRan, AMD, Nvidia, Nebius, Oracle, CoreWeave and the S&P 500, and each stock's fall from its record close.

Model 11, OpenAI Monte Carlo. 20,000 paths of OpenAI's revenue from 2026 to 2030 around its own plan. Each year's deviation from the plan, measured in logs, is a normal shock with a standard deviation of 0.29, the average size of the two 2026 revisions (the log of 50 over 70 and the log of 1.27), and the shocks accumulate. The 2026 shock is a quarter of that size because most of the year is already known. Costs are planned revenue minus planned cash flow and are held fixed. A pessimistic case adds a yearly drift equal to the October gap spread over three years, and a deflation case cuts growth by ten points a year from 2027.

Model 12, Price treadmill. The price per million input tokens for GPT-5.5 and DeepSeek V4 Flash, Chinese models' share of business tokens on OpenRouter, and the usage growth needed for OpenAI's 9.4 times revenue plan, which equals 9.4 times the cumulative price fall over four years.

Model 13, Your pension. The top 10 share of the S&P 500 in July 2026 against the top 10 share of MSCI USA in June 2000, and the index fall if only the top 10 fell, equal to their weight times their fall.

Model 14, Can the giants pay. Quarterly and annual cash flow statements from Nasdaq for Microsoft, Alphabet, Amazon, Meta and Oracle, with capex as a share of operating cash flow in the 2023 financial year and over the latest four quarters, net debt issuance over the latest four quarters, and 2026 capex guidance against the four hyperscalers' combined operating cash flow.

Model 15, History and growth. Investment booms as a share of US GDP from estimates collected by Justin Fox for Bloomberg, the four hyperscalers' 2026 capex guidance divided by the IMF's estimate of 2026 US GDP as an upper bound, and Flossbach von Storch's estimates of AI investment's contribution to US growth before and after imports.

Cartoons. The two cartoons are illustrations added by the author and carry no data.

Limitations. Private company figures for OpenAI and Anthropic come from press reports of investor documents rather than audited accounts, and the revenue mix figures are unofficial estimates. The three year chip life and the ten times sales multiple are illustrations rather than forecasts. The 30 GW energy figure is a maximum, because no data centre runs at full power all year. The historical booms are measured in slightly different ways by different authors, so Figure 4 compares orders of magnitude rather than exact figures. Nasdaq 100 data only starts in June 1996, so the dot com comparison begins part way through that boom, and the Bloomberg films were captured from their captions, so I quote them only where the wording was clear.
