# Introduction

On Tuesday 20 October 2026 Elon Musk said that SpaceX and Tesla had each set up special committees to study a merger, a deal that would join his two public companies into something worth more than $3 trillion and would be the largest combination of all time [FT1]. His reason was that "we are pretty much in the superintelligence singularity" [FT1]. Five days earlier Tesla had launched a Roadster off a ramp at a SpaceX test site, flipped it in mid air with jets of compressed air and landed it on its wheels [FORT1]. In February SpaceX quietly dropped its plan to send ships to Mars this year and said it would build a city on the Moon first [NBC1].

Reading all of that in one week, my first reaction was the obvious one. Mars looks out of reach, a flying car will never be allowed on the road, and a man who keeps promising the impossible somehow keeps persuading investors to hand him more money. So I set out to test those reactions against the numbers, the way I did with France and with the AI build out, using five Python models on share prices, company accounts and some basic physics.

The answer turned out to be more interesting than I expected, and in a few places my first reaction was simply wrong. The short version is that investors are not really paying for Mars or flying cars at all. They are paying for a person whose promises almost always arrive late but have a habit of arriving, and for two businesses, Starlink and an AI cloud, that are making real money today.

# Key terms

**Market value** is the share price multiplied by the number of shares, which is what the whole company is worth on the stock market.

**Price to earnings ratio** is market value divided by a year of profit. A ratio of 10 means investors pay ten years of today's profit for the company, and a ratio of 300 means they are paying for profits that do not exist yet.

**Free cash flow** is the cash a business brings in minus what it spends on factories and equipment.

**IPO** is an initial public offering, the moment a private company first sells shares on the stock market.

**g** is the acceleration of gravity, 9.81 metres per second squared. Pulling 1 g forward feels like your own body weight pressing you into the seat.

**COPV** is a carbon overwrapped pressure vessel, a lightweight tank wrapped in carbon fibre that stores gas at very high pressure.

# Chapter 1  Did the flying car sink Tesla?

## What actually happened to the shares

The neat story would be that the Roadster reveal was so ridiculous that investors gave up. The data does not support it. Tesla closed at $362.44 on the day of the reveal, fell 2.1% to $354.72 the next day, and then rose 3.8% to $368.06 on the following Monday [DATA1]. One analyst called the whole event an "engineering flex", and most of the market treated it as a sideshow ahead of the third quarter results due on 21 October [YAHOO1, TIKR1].

[FIG fig01_tesla_shares.png]

The real fall is much bigger and has been going on for most of the year. Tesla's record close was $489.88 on 16 December 2025, and at $368.06 it is 25% below that and 18% down since the start of 2026 (Model 01). Over the same period its profits have been draining away. Operating profit was $1.6 billion in the third quarter of 2025 and only $0.4 billion in the second quarter of 2026, and free cash flow went from $4.0 billion to minus $1.1 billion as capital spending more than doubled to $5.8 billion in a single quarter [DATA2]. Annual net income has fallen every year since 2023, from $15.0 billion to $3.8 billion in 2025, while revenue has barely moved at about $95 billion [DATA2]. Tesla expects to spend more than $25 billion on capex this year [TIKR1], much of it on AI training computers, robotaxis and its Optimus robot rather than on cars.

> Q: So is the Roadster why Tesla's stock dropped?
> A: No. The reveal cost the shares about 2% for one day and they had more than recovered by the next trading day. They have fallen because the car business is earning far less than it did and Tesla is spending heavily on things that do not earn anything yet. The Roadster was a distraction from that, not the cause of it.

# Chapter 2  What are investors paying for?

## Five times Toyota, a seventh of the profit

The most striking number in this whole story is the valuation. At $368 a share Tesla is worth about $1.38 trillion (Model 02). Over the last four quarters it earned $3.8 billion of net income [DATA2], which puts it on a price to earnings ratio of about 363. Toyota earned $25.45 billion in the year to March 2026 and trades on a ratio of about 10 [WALL1], so Tesla is worth roughly five times as much as Toyota while earning about a seventh of its profit. In July Tesla was worth more than the next 37 vehicle and parts makers in the world put together [WALL1].

[FIG fig02_valuation.png]

The right hand side of Figure 2 turns that price into the profit it assumes. If Tesla one day traded on a ratio of 25, which would still be generous for a huge mature company, it would need to earn about $55 billion a year to justify today's value, 14.5 times what it earns now. On Toyota's ratio it would need $138 billion, more than five times Toyota's own profit. Nobody buying Tesla shares at this price thinks they are buying a car company. They are buying robotaxis, humanoid robots and AI, which together earn almost nothing today.

Shareholders made that explicit last November, when 75% of the votes cast approved a pay award that could give Musk more than 423 million extra shares over a decade [CBT1]. To get all of it Tesla must reach a market value of $8.5 trillion, more than six times today's, along with 20 million vehicle deliveries a year, a million robotaxis and a million Optimus robots in commercial use, and up to $400 billion a year of adjusted profit [CBT1]. Even the first step, a $2 trillion market value, is 45% above where the shares are now (Model 02). In my view the vote tells you what Tesla's owners believe the company is for, which is everything except selling cars.

> Q: Why would anyone pay 363 times earnings?
> A: Because they are not valuing the earnings, they are valuing the chance that one of Musk's bets becomes enormous. If robotaxis or robots turn into a business the size of the car industry, today's price will look cheap, and if they do not, it is far too high. It is closer to buying an option than buying a share, and the price of that option depends almost entirely on whether you trust the man selling it.

# Chapter 3  SpaceX is the part that makes money

## Rockets, satellites and, mostly, AI

If Tesla is the dream, SpaceX is increasingly the cash. It raised about $86 billion in the largest IPO ever in June, selling shares at $135 that valued it at about $1.77 trillion [ALPHA1, FT1]. On 20 October it reported third quarter revenue of $14.6 billion, up 161% on a year earlier and well ahead of the $12.9 billion analysts expected, and a net profit of $4.4 billion against a loss of $1.1 billion a year before [FT1].

[FIG fig03_spacex.png]

The most interesting thing in Figure 3 is where that money now comes from. Starlink, the network of about 11,000 broadband satellites, earned $5.2 billion of revenue and $2.4 billion of net income in the quarter, which makes it a genuinely good business. Launches brought in $1.8 billion and made a small loss. But the biggest line by far was AI, where revenue from renting out computing power rose ninefold in a year to $7.6 billion, more than half of the total [FT1]. SpaceX now owns xAI and X, and Musk said he is "hounded relentlessly" by other AI companies wanting to rent his data centres, with Anthropic and Google among those paying premium prices [FT1]. Its 1.7 gigawatts of installed computing is already bigger than CoreWeave's 1.5 gigawatts, and Musk said he would be surprised not to have 13 gigawatts by the end of next year [FT1].

That growth comes with the same problem I wrote about in my report on the AI build out. SpaceX spent $19.6 billion on capex in the third quarter, 34% more than all of its revenue, and guided to between $35 billion and $40 billion in the fourth quarter alone [FT1]. The share price shows investors weighing exactly that trade off. It closed its first day at $160.95, peaked at $201.80 four days later and is now $147.96, 27% off the peak and only 10% above the IPO price (Model 03).

## So is Mars unattainable?

This is where I think my first reaction was wrong. Mars is not physically out of reach. Last month Starship, the 400 foot rocket that is supposed to get there, reached orbit for the first time and deployed 26 Starlink satellites, and SpaceX will try to catch both stages with mechanical arms on the next flight in November [FT1]. What has slipped is the timetable. In January 2025 Musk said the Moon was "a distraction" and SpaceX was going straight to Mars, and through 2025 he talked about sending uncrewed ships there by the end of 2026 [NBC1, PEB1]. By February 2026 that had reversed, with SpaceX telling investors it would land an uncrewed ship on the Moon in March 2027 and build a self growing city there first, while Musk said a Mars city could still start in five to seven years [NBC1]. Because Earth and Mars only line up every 26 months or so, missing the window that opens in November 2026 means the next chance does not come until around 2029 [WIN1].

> Q: Why do investors keep funding Mars if it keeps slipping?
> A: Mostly they do not. Nobody valuing SpaceX at nearly $2 trillion is paying for a Mars colony that makes no money. They are paying for Starlink and the AI cloud, which together earned the large majority of last quarter's revenue. Mars is the story that recruits engineers and keeps Musk motivated, and Starship is the tool, but the tool also happens to be the cheapest way to launch thousands of Starlink satellites and, Musk hopes, data centres in orbit.

# Chapter 4  The flying Roadster

## What was actually shown

The Roadster was first revealed in 2017 with a promise of deliveries in 2020, and customers paid $50,000 deposits, or $250,000 for one of 1,000 Founders Series cars [TC1]. It was pushed back in 2020, 2021, 2023 and 2024, and the reveal itself slipped from the end of 2025 to April 2026 and then to October [TC1]. When it finally appeared on 15 October it came in three versions. The Performance version is meant to be road ready, the Thrust version adds rear facing cold gas thrusters for a claimed 0 to 60 mph in under one second, and the single seat Rocket version has ten thrusters fed by 600 litres of compressed air stored in carbon overwrapped tanks that fill "every usable void" in the car [TC1]. Production is planned for 2028, eight years later than first promised, and reservations are $50,000 for the Performance and $250,000 for the Thrust [FORT1].

What it did at the demonstration was drive up a curved ramp, launch, roll over in the air with bursts of compressed air and land on its wheels, then jump over a line of other Teslas with a mannequin in a spacesuit at the wheel [FORT1]. Tesla has not said how long or how far it can stay in the air [FORT1]. That is a car that jumps, not a car that flies.

## The physics of one second

I wanted to know whether the claims even make sense, so I worked through the physics with a few simple assumptions (Model 04). Going from 0 to 60 mph in one second means an average acceleration of 2.73 g. A road tyre can only push a car forward at roughly 1.1 g before it spins, which is why the fastest road cars, such as Tesla's own Model S Plaid, top out at around two seconds. Everything above that has to come from the thrusters, and for a car weighing about 1,900 kilograms with a driver that means roughly 30 kilonewtons of thrust for one second.

[FIG fig04_roadster_physics.png]

Cold gas thrusters are not very efficient, so that one second burns roughly 41 to 62 kilograms of air depending on the design, about 48 kilograms on my central guess. Six hundred litres of air at 100 bar weighs about 71 kilograms, which is barely enough for one launch, while at 300 bar, a normal pressure for this kind of tank, it holds about 214 kilograms, enough for four or so. So the claim is physically possible, and the trick is simply carrying enough very high pressure air. The catch is what that air contains. At 300 bar those 600 litres store about 100 megajoules of energy, roughly the same as 25 kilograms of TNT if a tank ruptures all at once. TechCrunch points out that COPVs of this type have been implicated in several SpaceX rocket explosions [TC1].

> Q: Can a human even survive 3 g in a car?
> A: Easily, which surprised me. 2.7 g for one second, pushed back into your seat, is in the range of a big rollercoaster and well below what fighter pilots train for. The acceleration is not the danger. The danger is sitting in front of tanks that hold the energy of a small bomb, and Musk himself said during the reveal that "this is not necessarily a safety optimized car" [FORT1].

## Will it ever be approved?

My assumption was that no regulator would ever approve a car like this, and the truth is stranger. The Federal Aviation Administration has said the Roadster does not meet its definition of an aircraft, so it does not need to be certified as one [FORT1]. On the road, the National Highway Traffic Safety Administration mostly relies on carmakers to certify for themselves that their vehicles meet federal safety standards, and the Department of Transportation has only said it "will continue to monitor the situation" [FORT1]. Tesla's own website says the Rocket version is "not approved for public road use" [FORT1]. So the honest answer is not that it will never be approved, but that nobody is clearly in charge of approving it, which in my view is the more worrying position.

> Q: Then why build it at all?
> A: Because it is marketing for everything else. Musk has said himself that the Roadster will not be a big contributor to revenue [FORT1], and one analyst put it more bluntly, saying it "will not move the volume or revenue needle" [FORT1]. It was launched at a SpaceX site using SpaceX thrusters five days before a merger announcement, and prediction markets nearly doubled their odds of a Tesla and SpaceX deal the day after [YAHOO1]. I think the car was as much an advert for the merger as it was a product.

# Chapter 5  Why do investors keep following him?

## The promise tracker

To understand why people keep believing him, I lined up five of his best documented promises against what actually happened (Model 05).

[FIG fig05_promise_tracker.png]

The pattern is consistent. Almost nothing arrives on time, but a surprising amount arrives eventually. In 2019 Musk said Tesla would have robotaxis on the road "next year" [CNN1], and by 2026 its robotaxis were running without a safety supervisor in parts of Texas and Florida, about six years late [TIKR1]. The Cybertruck was promised for late 2021 and deliveries began at the end of 2023 [DRIVE1]. The Roadster is now planned for 2028, eight years late, and the Mars timelines have slipped by years and are still slipping. In 2018 he said humans would reach Mars in seven to ten years, which would be 2025 to 2028 [CNN1], and today the earliest plausible date is the next decade.

Seen that way, the investors are not as irrational as they look. Musk's track record is not a list of impossible things that never happened. It is a list of things experts said were impossible that happened three to eight years after he said they would, from rockets that land themselves to Starlink and an electric car company worth more than the rest of the industry. If you believe that pattern holds, buying at a price that assumes the future arrives late but arrives is a bet with some logic to it.

> Q: Is he a genius or a salesman?
> A: Both, and I do not think you can separate them. The deadlines are not really forecasts, they are a way of pushing engineers and pulling in capital, and they work because he has delivered enough times for people to forgive the misses. The danger for investors is that the forgiveness gets priced in. When the shares already assume robotaxis, robots and an AI empire, a delay stops being a story and starts being a loss.

# Chapter 6  Why merge Tesla and SpaceX?

## Two companies, one boss

The two companies are already tangled together. They are working on Terafab, a chip factory in Texas that could cost $119 billion, and SpaceX has already absorbed X and xAI [FT1]. Musk listed the benefits of a merger as cooperation on "superintelligence software, chip design, the Terafab, robotics" and connectivity through Starlink [FT1]. At Monday's prices Tesla is worth about $1.38 trillion and SpaceX about $1.94 trillion (Models 02 and 03), so the combined company would be worth around $3.3 trillion.

For Tesla shareholders the attraction is obvious. They would swap a car business whose profits are shrinking for a share of one of the fastest growing AI clouds anywhere and a satellite network that already earns billions of dollars a quarter. For SpaceX shareholders the case is weaker, because they would be taking on a company valued at 363 times earnings whose main business is losing ground. And because Musk runs both companies, he has said he cannot take part in the talks, and that the special committees have not agreed terms and may never do so [FT1].

> Q: What happens to all of this if something happens to Musk?
> A: That is the risk I think gets least attention. Both valuations rest heavily on one person's ability to raise money, recruit engineers and keep pushing impossible deadlines. A merger would make the combined company even more dependent on him, which is great while it works and very dangerous if it stops.

# Conclusion

I started with three reactions, that Mars is unattainable, that a flying car will never be approved and that Musk is somehow conning investors into following him. The data turned all three into something more interesting. Mars is not unattainable, it is late, and Starship reaching orbit last month makes it more plausible than it has ever been, even if a city on the Moon now comes first. The flying Roadster is a car that jumps on compressed air, the physics works, and the real problem is not that it will never be approved but that no regulator clearly has to approve it. And Tesla's shares did not fall because of the Roadster, they fell 18% this year because profits and cash flow have been sinking while spending rises.

What investors are really buying is a pattern. Musk promises the impossible, misses every deadline and then, three to eight years later, delivers a surprising amount of it, and SpaceX's latest results show the pattern paying off, with an AI cloud and a satellite network bringing in $12.8 billion in a single quarter. The price of Tesla, at 363 times earnings, assumes the pattern will keep holding for robotaxis, robots and AI. My view is that it probably will for some of them, but at a price that leaves very little room for the next delay, and a merger would tie both companies even more tightly to the one man who sets the deadlines.

# Appendix A  Methodology and models

All models are written in Python using pandas, numpy and matplotlib and sit in 02 Python Models, where run_all.py rebuilds every chart and table in 04 Outputs. Share prices and Tesla's income and cash flow statements were downloaded from Nasdaq through the OpenBB platform on 21 October 2026, and every figure taken from an article is stored in 03 Data/hand_collected_sources.csv with its source and URL.

Model 01, Tesla's shares. Daily closes since January 2024, the record close and the change in 2026 so far, the daily moves around the Roadster reveal, and quarterly operating profit and free cash flow (operating cash flow minus capex) for the four quarters to June 2026.

Model 02, Valuation. Tesla's share count is backed out from its $1,423 billion market value on 21 July 2026 and multiplied by the latest close. The price to earnings ratio uses net income over the latest four quarters. Toyota's value is its net income times its reported ratio of 10. The profit needed to justify Tesla's price is market value divided by an assumed ratio of 25 or 10.

Model 03, SpaceX. Revenue by business in the third quarter of 2026 against a year earlier, with the earlier launch figure backed out as total minus AI and Starlink, capex against revenue, and the share price since the IPO, with market value scaled from the $1,770 billion offer value.

Model 04, Roadster physics. 60 mph in one second gives 2.73 g. Tyre grip is assumed at 1.1 g, the car and driver at 1,900 kilograms and the thrusters' specific impulse at 65 seconds (range 50 to 75). Air needed equals thrust times time divided by specific impulse times 9.81. The air held in 600 litres uses the ideal gas law at 20 C, and stored energy uses isothermal expansion, pressure times volume times the natural log of the pressure ratio, at 4.184 megajoules per kilogram of TNT. These are illustrations with stated assumptions, not Tesla figures.

Model 05, Promise tracker. Five promises with the year made, the year promised and the year delivered or now expected, each with a source in 03 Data/promise_tracker.csv.

Limitations. SpaceX's segment figures come from press reporting of its results. Toyota's market value is approximate. The physics model ignores air resistance, the time taken to reach full thrust and the drop in pressure as the tank empties, which would all make the real air requirement higher. The promise tracker is a selection of well documented promises rather than a complete record, and it includes delivered and undelivered ones.
