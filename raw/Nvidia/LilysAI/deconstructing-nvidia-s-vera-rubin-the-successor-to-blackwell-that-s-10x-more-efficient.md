# Deconstructing Nvidia’s Vera Rubin — The Successor To Blackwell That’s 10x More Efficient

## Content

고급모델

## Deconstructing Nvidia’s Vera Rubin — The Successor To Blackwell That’s 10x More Efficient

00:00:02This is what Nvidia's Grace Blackwell looks like on the inside, the 72 GPU system that's seen soaring sales from the likes of Microsoft, Google, Amazon, and Meta

00:00:12But what we're really at Nvidia for is an exclusive first look at this Vera Rubin

00:00:16Nvidia's next rack-scale system for AI data centers has the AI world buzzing because NVIDIA says it'll help solve the biggest bottleneck threatening AI buildouts today, energy

00:00:28It's actually going to be about 10 times more performant in terms of performance per watt compared to Blackwell

00:00:34So, how did Nvidia pull this off? We're taking you on a deep dive inside Vera Rubin to find out because this AI powerhouse takes a lot more companies than Nvidia and a lot more parts than These GPUs

00:00:42It's not comprised of just chips

00:00:50It also has the compute trays, the chassis, the side rails, the bus bars, and 1.3 million components, over 80 different suppliers, and across more than 20 countries

00:00:58VR Rubin's in volume production today with plans to ship later this year

00:01:01But from a memory shortage to a supply chain ridden with tariffs, what are the risks Nvidia faces to getting these two-ton systems out the door? There is that risk that with all this AI capex, you, you basically have pulled forward or have a little bit too much than you need

00:01:17But I don't see that as being a risk this year, and I think that's why Nvidia is so confident that their customers are saying, we need more, and if we had it, we could deploy

00:01:26It right now

00:01:28From compute to connectivity to power, we take a look at the astounding ecosystem behind this single system and asked Nvidia how it built this complex web, and whether competitors like AMD could ever catch up

00:01:50When Nvidia released its current Blackwell rack design in 2024, demand was insane

00:01:54Nvidia stock is up more than 100% since before it was announced because it completely changed the game

00:02:01Because it was the first full rack-scale design that took this approach of disaggregating compute, the scale of networking, as well as all the memory infrastructure, but all of it was done to make it behave as a single GPU

00:02:12The first generation of compute knew, you'd buy a server, you'd buy a switch, you know, you would You, you would, uh, maybe buy a rack to cool if you got to a point where it needed that

00:02:23Got all these systems pulled together into a single rack built for absolute greatest efficiency and greatest performance

00:02:29And that's just not how servers were historically built

00:02:34Grace Blackwell has 72 GPUs, nearly 800 other chips, 1.2 million total components made at some 350 factories

00:02:44TSMC is developing the the silicon and the core chips

00:02:46We're working with Foxconn on a lot of the other rack assembly components, Delta Electronics for a lot of the liquid cooling elements

00:02:53The nozzles that connect on the end of the hoses are made by a number of different providers, whether it's Amphenol and getting the connectors and the

00:02:59copper, whether that's Vertiv and getting the cooling distribution systems

00:03:02With so many components, not every rack is touched by the exact same global suppliers

00:03:08From China to Israel to Mexico to the US, Vietnam, Thailand

00:03:14So Nvidia created a standard reference design

00:03:17So the whole idea by creating a standard is it opens it up to the entire ecosystem

00:03:22There's power shelves by MegMeet, Lighton or Flex

00:03:24Power components by Infineon, Analog Devices or ST Micro Electronics

00:03:29Chassis by Foxconn or Interplex

00:03:31Bizlink for bus bars, Pindac for rack manifolds, cold plates by Auras, ABC, Boyd, Cooler Master, JPC to Rico deal for power whips, the list goes on

00:03:44This supply chain has really become this core group of Companies that are building this all together

00:03:48And of course, they're all leaning in on the success of Nvidia

00:03:51Is Blackwell still sold out? Blackwell is in full production still

00:03:57We're still, you know, producing thousands of racks per week

00:03:58And so what I'll say is they're spoken for

00:04:10So now Nvidia is making the next big leap to Vera Rubin with full production announced at CES in January

00:04:17This is a Rubin pod, 1152 GPUs in 16 racks, with about 100,000 more components than Grace Blackwell

00:04:27Vera Rubin uses about double the energy, but can deliver way more compute

00:04:32The number of tokens it's generating is exponentially higher than last generation, and so they become very efficient for these, you know, these heavy workloads

00:04:41To get there, Nvidia redesigned all six of the core chips

00:04:44So this is our Vera CPU

00:04:47It delivers about 2x the performance per watt compared to our previous gen Grace CPU

00:04:50Then, of course, there's the Rubin GPU

00:04:52This can actually deliver about 50 petaflops of AI performance, so about 2.5x performance

00:04:58So let's take a deeper look at one rack

00:05:00It has 18 compute trays

00:05:03Each one starring two Vera Rubin superchips, the computing hearts of the system

00:05:05Each has one Vera CPU, two Rubin GPUs, and much more

00:05:11So this particular superchip has 17,000 components

00:05:14And as you look at all these elements that have to connect to each other, a lot of these are just to help make sure that the power is being modulated

00:05:17correctly

00:05:19These are actually the SOCAM memory

00:05:22So we've actually have memory units that can be applied and and removed on the new Vera Rubin processor

00:05:30Compared to Grace Blackwell, they were all sort of soldered in

00:05:34But the real memory star lines the top and bottom of the Rubin GPU itself

00:05:38Eight stacks of the latest high bandwidth memory, HBM4, by the likes of SK Hynix and Samsung

00:05:42Is there any risk because it is in such short supply right now? The one thing that we've been very laser-focused on is making sure our entire supply chain is aware and aware of not just sort of the design itself, but we're actually giving them very detailed forecasts

00:05:57We're aligning to make sure that everything we're shipping will be met

00:06:00by our supply chain

00:06:03So, I think we're in good shape

00:06:06Another risk factor, those 1.3 million components running workloads 24/7 generate a lot of heat

00:06:11Some customers reported overheating issues in the early days of Blackwell deployments at the end of 2024

00:06:19Every component has to fit together perfectly

00:06:21Um, and I think when we were doing some of those initial deployments, there were things like you didn't get proper seating with the um, liquid cooling valve

00:06:28It was just actual implementation, user error

00:06:30And for the most part, all the systems are fully deployed today, running hundreds of thousands of scales and and without an issue

00:06:39VR Rubin compute trays have no hoses, cables, or fans

00:06:41It's NVIDIA's first

00:06:43system that's 100% liquid-cooled

00:06:47Will this mean that data centers have to have a really robust liquid cooling loop ready and in place before they can move from Blackwell to Vera Rubin? Yes

00:06:56Essentially, we are requiring as we build out the AI factories of the future that the vast majority will be leveraging this liquid-cooled base architecture

00:07:06The superchip is covered with cold plates piping in water that keeps the components cool

00:07:09These are the cold plates on the Vera CPU

00:07:11You also have the Rubin GPUs that are also underneath there

00:07:16Data centers currently consume a lot of water

00:07:18Will Vera Rubin help with that? One of the counterintuitive savings is actually you use less water using liquid

00:07:23cooled systems

00:07:28The main reason is because you don't use the evaporative cooling technologies as much, and that allows you to consume much less water through a closed-loop system

00:07:33A lot of the needs for cooling come because of just how much power is running through the system

00:07:38It's about twice the amount of overall power, um, roughly about 220 kilowatts per rack

00:07:44And so we had to redesign, obviously, the power delivery system

00:07:47But most of all, efficiency is tied to how quickly each GPU can access the memory and processing on every other GPU simultaneously, which Nvidia solves with its own networking product, NVLink

00:07:58This is the NVLink switch chip responsible for connecting all of these GPUs and CPUs together to have them behave as one

00:08:04So this actually doubled the line rate from, from again, 1.88 terabytes per second to 3.6 terabytes per second

00:08:11Nine NVLink switch trays sit between the compute trays, connecting all 72 GPUs together and pushing data at an incredible 260 terabytes per second

00:08:21And they connect through this NVLink spine on the back side

00:08:23And this is really the magic of this full rack scale system

00:08:28One of these spines stands vertically, glowing through the back of each rack, connecting everything together with 5,000 copper cables, 2 meters worth

00:08:33Each wire specifically placed in a line to where it needs to go to connect to another connection point on the spine itself

00:08:42Finally, there's Bluefield DPUs for storage and security, and Outwardbound Connect X9 networking controllers originally built by Melanox, which Nvidia bought for nearly $7 billion in 2020

00:08:53That was one of the most, you know, incredible acquisitions as you're starting to scale AI factories from single systems to full-on data center scale workloads

00:09:00The networking is incredibly important

00:09:03Thousands of racks make up what CEO Jensen Wong calls an AI factory

00:09:08So, how do they all connect together? With entirely separate networking racks filled with Nvidia's latest Spectrum X switches

00:09:14Overall, a Vera Rubin rack weighs nearly 2 tons and has about 1,300 chips with some 220 trillion transistors

00:09:22Still, it's simpler than the current Grace

00:09:26Blackwell system

00:09:27You can now disassemble this full compute tray in seconds

00:09:32So, just what I just did there, to do this with Blackwell, this would actually be soldered to the board

00:09:38You would need screwdrivers, you would need all sorts of equipment to take that out

00:09:41And that's why when you look at this complete compute assembly, instead of two hours on Blackwell, it can be done in five minutes

00:09:47Just push it down there and now it's inside

00:09:50Right

00:09:52While Vera Rubin is less complex, it'll cost customers more upfront

00:09:55Nvidia doesn't share rack pricing, but analysts estimate the price will increase about 25% from Grace Blackwell

00:10:03So, from somewhere around three to three point two to three and a half to four million a rack

00:10:06The cost per token is about 10x

00:10:09lower for Rubin compared to Blackwell

00:10:12I mean, that's what I hear on my end

00:10:14It matters the most is the equation of how many tokens per watt or per, you know, power consumed can you get

00:10:24And the more you can tweak that or move up the curve, the higher the return would be on the dollar you spend

00:10:32Are there parts coming from China that are constrained because of tariffs? Have you seen prices of certain parts go up, for instance? So, what I'll say is, when you look at this supply chain, this complex, it's a game of whack-a-mole

00:10:42And in terms of pricing, certainly given the demand, different components have definitely been impacted

00:10:47But luckily, given demand, there's also incredible value in in making sure that we can secure that

00:10:49Nvidia

00:10:52has also been part of the big reshoring push

00:10:55It's vowed to manufacture up to $500 billion of AI infrastructure in the US through 2029, including making Blackwell at TSMC's new Arizona fabs

00:11:04Assembly, where all the components are pieced together, often by robots, also happens in the US and elsewhere, including Taiwan and at a big new Foxconn plant in Mexico

00:11:12As VR Rubin starts shipping in the second half of 2026, customers won't need to phase out Blackwell

00:11:19>> This is one of the few times that you'll hear a CEO tell its customers, buy less, right? So, we really want our customers to buy with our annual cadence because each architecture is going to continue to leapfrog itself

00:11:30We assume that there will be customers who will be parking Reubins right next to these Blackwell systems as well to power different workloads

00:11:38Later this year, Nvidia will see some big competition when AMD ships Helios, its first rack-scale system

00:11:44You're going to see, uh, a lot of uptake because customers want, you know, more capacity, but they also want a viable second source to kind of keep Nvidia honest, so to speak

00:11:53I, I don't know if we're the only company that can do it, but I can definitely say that there's a lot of, you know, sort of growing pains that went into understanding the complexity of delivering this type of system that has never been designed before at this scale

00:12:07Major NVIDIA customers are also making AI servers with their own in-house silicon

00:12:11We visited an AWS data center in October filled with Ultra servers made up of 64 AWS Tranium 2 chips, and Google's filled its data centers with racks of its own tensor processing units, too

00:12:22Amazon is developing their own AI chip

00:12:24So is Google

00:12:27So is Microsoft

00:12:29So is Meta

00:12:31And still, they're choosing to continue to work with Nvidia generation after generation

00:12:33And I think that's a testament to the fact that these platforms that they're developing are very powerful

00:12:41NVIDIA showed us a prototype of its next big rack architecture leap after Reuben Kyber with 288 GPUs

00:12:48If you think about the math, we went from 72 to 288

00:12:49That's four times, but the weight only went up by about 50%

00:12:55And the way we were able to do that, we actually removed a lot of the cabling

00:12:58What the actual production version will look like may be a little different, but it's just an example of how we're looking to kind of push the bounds in terms of compute density and overall performance efficiency

00:13:07Nvidia's next system, Vera Rubin Ultra, will be available with the Kyber rack design, expected to ship in 2027

00:13:13Ultimately, that's where they're headed is to have fewer connection points, fewer points of failure, more integration

00:13:22Not only does it make the system faster, but total cost of ownership should go down

00:13:28Really, if you're able to pack a large number of components within the same rack, that means that more GPUs can have super low latency

00:13:35If the user The experience of using AI is amazing, then more and more people will use it, and they'll use it more

00:13:43And then, at that point, the demand for GPUs is going to be even more.
