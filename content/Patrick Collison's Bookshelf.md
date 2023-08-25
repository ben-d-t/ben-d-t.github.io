### 0. The bookshelf

[Patrick Collison](https://en.wikipedia.org/wiki/Patrick_Collison) (co-founder, CEO of Stripe) has a bookshelf page with a long list of books and a few recommendations: [Bookshelf · Patrick Collison](https://patrickcollison.com/bookshelf). And it’s not just a wishful to-read list. [He reads a lot](https://www.justgogrind.com/p/patrick-collison). The bookshelf lists most of the physical books Patrick owns, of which he’s read about half. 

The bookshelf’s in no particular order. Not even alphabetical. Patrick writes “Since the stacks and shelves lack any particular order, so does this list.” There’s something fun about and whimsical about that and I like it. But it makes it hard to use the list for anything other than just browsing or a quick “ctrl+f” to see if he has or likes a particular book. 

So I had GPT-4 help me compile and then categorize the list.

### 1. The results

Here's a Google Sheet of the bookshelf: [CollisonBookshelf - Google Sheets](https://docs.google.com/spreadsheets/d/1olzx87nTVH3qmy_QL2zwuwDi_gTPklhjqgwzc9_AkTU/edit?usp=sharing)

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTNMv1fRaJTH5A6w_yFbU9VFgsuJHeAOUSVl6p9tEL9lK_N1VIeN5teonglrcL8B1syaIkJsOJLeZOS/pubhtml?widget=true&amp;headers=false"></iframe>

Some summary stats:
- There are close to 800 books (778 with a few duplicates)
- The titles plus subtitles make up more than 6,000 words (titles only are less than 3,000)
- That's almost 40,000 characters -- meaning gpt-4-32k could take a shot at the whole list at once, if only I had access
- 17 books are on the shelf more than once; just one book, [Popper Selections](https://www.goodreads.com/en/book/show/61552) is on there x3, leaving 760 unique books

### 2. Some observations about the categories

**Clusters with many books:**
There are, not surprisingly, a lot of books that broadly fall under “Science & Technology.” I’m also surprised at how many books there are about Aviation! But it turns out [both](https://twitter.com/patrickc/status/711226514960945153) [Collison brothers](https://www.altfi.com/article/8178_private-jets-are-so-last-year-fintech-entrepreneur-john-collison-is-buying-an-airport)are pilots. There’s also an interesting cluster around Design, including books about Urban Planning, Typography, Visual Arts, and Creativity. 

After “Science & Technology” two of the next biggest mega-categories are “Literature & Fiction” and “Biography & Memoir.” That might be what stands out the most — it’s not like Collison’s bookshelf is mostly Science, Business, Economics, and Politics with not much else in between. 

”Biography & Memoir” also makes up a disproportionate 30% (6 of 20) share of the green books — which Collison says are “particularly great.”

**Clusters with only a few books:** 
There are only a handful of “self-help” or “pop business” books (GPT-4 categorized twice as many books as “Business & Economics” as opposed to “Business & Management”). 

It didn’t make the final cut but in all the testing I saw just one book specific enough to Stripe’s business model to get tagged as “Payment Systems.”

Yes, some of the categories overlap (are “Science and Technology” vs ”Technology and Science” really that different?) 

### 3. Some learnings for programming with GPT

I started out with a prompt something like “Please sort, order, and categorize the following list of books. Each book should be in only one category. Please return the list in this format: **Category**: book1, book2, book3, etc…” and the final prompt wasn’t that different. 

Using the chat.OpenAI.com interface was going to take way too long so I ended up building a script that looped through the .CSV file of books and sent a chunk at a time through the API. 

The downside here is the request token limit — you can only do so many books at once. The current token limit for gpt-3.5-turbo is circa 4,000 tokens. For gpt-4 it’s just over 8,000 tokens. 

But in practice I had to keep these prompts well under the token limit. The more books at once, the more that would be “missed” and not returned in the output. gpt-3.5-turbo seemed to drop more books than gpt-4. In the end even with gpt-4 I changed the script to go back through a second time and re-do any uncategorized books. 

gpt-3.5-turbo also seemed to create *more* categories, and would more often have a single book in a really niche category. That sort of ”creativity” might have been fun except that it was leading to something like 150 categories off 600 books. And it was less “creative connections between books” and more “made-up specificity.” 

I also tried Claude with the 100k context window but it didn’t perform nearly as well at this task with the same prompt. Maybe a different task or a smaller set at a time would have been better. 

I think with practice a more complex prompt to gpt-4 would’ve also been more reliable. 

Lastly I only did a bit of spot-checking around what books ended up in what categories. I’m sure there are some that are way off. 

TL;DR
1. Programming w/ gpt-4’s help is so great
2. Simple prompts get 80% of the way there but not 100%
3. Cleaning and checking output is hard but necessary if you need reliability

### 4. The green books
The 20 books that Patrick Collison thought were “particularly great” as summarized by chat-gpt-4 (limited fact checking). I made a Goodreads shelf out of these; would reading them make someone ready to build a tech unicorn?

1. **A Pattern Language: Towns, Buildings, Construction (Center for Environmental Structure)** by Christopher Alexander. This book offers a practical language for building and planning based on natural and human behavior, creating a guide for architects and urban planners.
    
2. **Age of Ambition: Chasing Fortune, Truth, and Faith in the New China** by Evan Osnos. Osnos narrates the rise of the individual in China, reflecting the country's shift towards personal ambition and faith in a rapidly changing society.
    
3. **Anthropic Bias: Observation Selection Effects in Science and Philosophy** by Nick Bostrom. The book explores how to reason when you suspect that your evidence is biased by "observation selection effects"—an issue that arises in many areas in science and philosophy.
    
4. **Dancing in the Glory of Monsters: The Collapse of the Congo and the Great War of Africa Kindle Edition** by Jason Stearns. This book offers a comprehensive history and analysis of the war in the Congo, highlighting its complex roots and devastating impact.
    
5. **Democracy in America: Abridged Edition (Mentor Series)** by Alexis de Tocqueville. A seminal work that examines the strengths and weaknesses of democracy as observed in 19th-century America.
    
6. **Hard Landing: The Epic Contest for Power and Profits That Plunged the Airlines into Chaos** by Thomas Petzinger Jr. It provides a detailed history of the airline industry's transformation following deregulation, focusing on the power struggles and chaotic market shifts.
    
7. **If the Universe Is Teeming with Aliens ... WHERE IS EVERYBODY?: Fifty Solutions to the Fermi Paradox and the Problem of Extraterrestrial Life** by Stephen Webb. Webb presents potential explanations to the paradox of why we have not yet encountered extraterrestrial life, despite the vastness of the universe.
    
8. **Metamagical Themas** by Douglas Hofstadter. A collection of essays on topics such as artificial intelligence, self-reference, and other philosophical issues related to mind and language.
    
9. **Mind-Body Problem** by Rebecca Goldstein. This novel explores the philosophical mind-body problem through the lens of a love story between a philosophy student and a renowned mathematician.
    
10. **Mindstorms** by Seymour Papert. Papert presents his innovative ideas on how children can use computers to learn, focusing on his development of the Logo programming language.
    
11. **Nixon Agonistes: The Crisis of the Self-Made Man** by Garry Wills. This book provides an introspective examination of Richard Nixon and his position in American history and culture.
    
12. **Out of Mao's Shadow: The Struggle for the Soul of a New China** by Philip P. Pan. A collection of stories about the individuals resisting the legacy of Mao's regime, illuminating China's struggle to reform.
    
13. **Paradigms of Artificial Intelligence Programming: Case Studies in Common Lisp** by Peter Norvig. This book presents classical problems, techniques, and algorithms in AI using Common Lisp, providing an in-depth understanding of AI programming.
    
14. **Poor Charlie's Almanack: The Wit and Wisdom of Charles T. Munger** by Charles T. Munger, Peter E. Kaufman (Editor). A compendium of Charlie Munger's best advice on a wide range of topics, offering insights into his investment strategies and worldview.
    
15. **Something Incredibly Wonderful Happens: Frank Oppenheimer and the world he made up** by K.C. Cole. This biography of Frank Oppenheimer, the physicist and educator who founded the Exploratorium in San Francisco, focuses on his groundbreaking approach to science education.

16. **The Art of Doing Science and Engineering** by Richard Hamming. Hamming shares his insights on how to do good science and engineering, emphasizing the importance of learning from past experiences and cultivating a mindset of continuous learning.
    
17. **The Beginning of Infinity: Explanations That Transform the World** by David Deutsch. This book presents the idea that all significant human progress and prosperity are the result of a single fundamental principle: the capacity of human beings to create explanatory knowledge.
    
18. **The Dream Machine: J.C.R. Licklider and the Revolution That Made Computing Personal** by M. Mitchell Waldrop. A detailed biography of J.C.R. Licklider, the visionary behind the development of personal computing and the internet.
    
19. **The Paris Review Interviews, I** edited by Philip Gourevitch. A compilation of in-depth, candid interviews with some of the greatest writers of our time, originally published in The Paris Review.
    
20. **The Rise and Fall of American Growth: The U.S. Standard of Living since the Civil War (The Princeton Economic History of the Western World)** by Robert J. Gordon. Gordon provides an in-depth exploration of the growth and development of the U.S. economy since the Civil War, arguing that the explosive growth seen during the 20th century may be an anomaly rather than a trend.