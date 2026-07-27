

<내가 관심 갖는 주제>
- human empowerment; human will; 인간의 무한정한 의지와 영향. 르네상스 맨.
- 자연 법칙
- 인간의 역사. 사회의 역사. 





summary of sungycho/sungcho-life/07-21-26-intuition-on-KL-divergence.md

The KL term in a VAE is not an arbitrary penalty added after the fact; it follows naturally from requiring the encoder’s latent distribution q_ϕ(z∣x) to be compatible with the prior p(z) used during generation. The reconstruction term ensures that z contains enough information to recover x, while the KL term prevents the encoder from inventing a private latent coding system that cannot be reached by sampling from the prior. It therefore behaves like a regularizer, but its deeper meaning is the cost of making inference and generation agree.






you need to measure something to start analyzing!
often times, coming up with how to measure is a real change (Hubble Telescope, Shannon's Information Theory)


analysis vs. build
- 소설의 주제를 분석하고 정리한다고 해서 그 소설을 쓸 수 있는 것은 아니다
- 언제 분석만이 충분하고 언제는 직접 쓸 수 있어야 하는가?
- technical vs non technical founder


polymath
renaissance man


strategic, top-down view on business 
vs.
product-oriented, bottom-up view on business

is like Newton vs. Quantum mechanics



<Books I read>
- Elon Musk
- 니체: 도덕의 계
- The Goal
- 일을 잘한다는 것
생각하는 힘은 유일한 무기가 된다
초격차
Hard Things on Hard Thing
숫자로 경영하라
Principles
당신은 사업가입니까?
Credit Investing Handbook
Why I left Goldman Sachs

Quant
Dark Pool
군주론
사피엔스
총균쇠
나는 습관을 조금 바꾸기로 했다
Grit
Originals
평균의 종말 - 토드로
톨스토이 고백록 



<Books I'm reading>
반항하는 인간
로마사 논고
The beginning of Infinity
Poor Charlie's Almanack
The Art of Doing Science and Engineering
선과 모터사이클 관리술
플루타르크 영웅전
Feynman Physics

<읽고싶은 책>
- Alibaba
- The Dream Machine
- Material World (물질의 세계) - 에드 콘웨이
- Swimming Across
- The Power Broker: Robert Moses and the Fall of New York
- The Polymath: Unlocking the Power of Human Versatility
- The Information: A History, a Theory, a Flood
- The Sovereign Individual: Mastering the Transition to the Information Age
- A Mind at Play: How Claude Shannon Invented the Information Age — Jimmy Soni & Rob Goodman
- 문명의 충돌 - 새뮤얼 헌팅
- The End of History and the Last Man - Francis Fukuyama
- The Battle of Bretton Woods - Benn Steil
- The Bretton Woods International Monetary System: A Historical Overview - Michael D. Bordo
- Chums: How A Tiny Caste of Oxford Tories Took Over The UK (옥스포드 초엘리트 - 밀) 
- 도덕경 - 노자 

- https://www.oreilly.com/library/view/deep-learning-for/9781492039822/
- https://readwriteown.com/
- https://a16z.com/books/the-cold-start-problem/
- https://a16z.com/books/secrets-of-sand-hill-road/


<Books I don't like>
- 부의 추월차선
- Man's Search for meaning
- 데일 카네


<Write-ups>
https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf


<Stripe Press books to Buy>
Tier 1
- the origins of efficiency
- the scaling era: an oral history of ai
- boom
- 
Tier 2
- the dream machine
- Scientific Freedom: The Elixir of Civilization
    - funding model에 대한 얘기 다룬다는데 재밌을듯? 
- Pieces of the Action
    - management 관련 책 같은 느낌 
- The Big Score: The Billion Dollar Story of Silicon Valley
- An Elegant Puzzle: Systems of Engineering Management
- Stubborn Attachments: A Vision for a Society of Free, Prosperous, and Responsible Individuals
- Where Is My Flying Car?

Tier 3
- The Making of Prince of Persia: Journals 1985-1993
- Get Together: How to Build a Community With Your People
- The Revolt of the Public and the Crisis of Authority in the New Millennium
- High Growth Handbook: Scaling Startups from 10 to 10,000 People
- Working in Public: The Making and Maintenance of Open Source Software
- Scaling People: Tactics for Management and Company Building
- Maintenance: Of Everything, Part One


<Things I want/have to learn>

Leetcode
DSA
How to write a good code
OS / Systems
Rust
kernel engineering
Lyapunov function & Linear Systems/Control Theory
Measure Theory
Functional Analysis
Functional Differential Geometry
Algorithmic Game Theory (NETS4120)
Abstract Algebra

<이상적인 동업자/파트너의 자질>
- long term mindset
    - minimal tweaking / emotional maturity /
- audacity
    - ambition / willingness to excel (which is different from excellence itself)
- learning machine
    - which necessarily comes with humbleness
    - read a lot / interact with human knowledge a lot (not necessarily talking to ppl tho)
- multidisciplinary ? (is this necessary?)
- 야수성, 반항정신, 홍대병... nonconformist

<글감>
좋은 조언의 조건
- specific (ex. red flag - how to get a job)

돈이 몰리는 곳에 high-growth opps가 있다
돈은 어디에 몰리나? bottleneck에
etched가 짧은 기간에 그렇게 많은 revenue를 내고 많이 raise한 것도 그래서임.
자본의 흐름을 파악해야 한다
안그러면 sales도 어려워짐

your thought is so cool only until you write it down
it's so easy to fool yourself. 

technology always is slowed down by law, economics, psychology, regulation -> huge, huge force
이건 근데 모든 게 항상 그렇다.
본질적으론 인간이 이성적 존재이면서 동시에 비이성적 존재이기 때문. 즉 유기체이기 때문? (동물도 이성과 감정을 동시에 가지나?)
그리고 여러 인간이 모여서 집단을 형성하는 사회적 동물로 남아있는 한, 인간은 항상 그 두가지 모습을 동시에 가진 사회를 이룰 것.
나는 역시나 그 사이 어딘가에 위치한 '중간자'이지만, 그래도 지금 내게 더 필요한 것은 과학적 사고

corporate은 기본적으로 이성과 비이성의 결합이고, 인간과 가까워질 수록 (세일즈 등) 비이성적이어지고 인간과 멀어질 수록 (무언가를 만드는, 엔지니어링 등) 이성적이어진다.
investment banking은 advice를 준다는 점에서 이성적이어 보일 수 있지만, 사실 



와튼이 아닌 다른 학교를 갔었어야 했을까? 답은 

 

it's so funny that i, once got so fed up with pure studies (math) that ended up pursuing a secular area (finance), now am so done with secular stuff (finance, startup,...) that is pursuing a research phd. history does repeat its rhythm. (both in individual and macroscopic sense - prolly because there are only a handful of structure that can be folded out if you look from a high enough view)


ppl only do what they think is cool. I thought of banking initially cuz i thought it was cool. then, I pivoted to startup cuz i thought it was cool. now i think research is cool. why do one think of something as cool? multiple factors: could be a surroundings you grew up, someone you look up to, something you just randomly ran into and found fascinating...


am i too obsessed with my career in top-down, high-level view? am i not giving enough focus to details, bottom-up stuff? (e.g., actually learning bunch of stuff)


소년 같다의 정의? 호기심을 유지하는 것.
나이 먹어도 소년 같은 사람의 비결? 호기심이 짓밟히지 않고 적당히 보상해주며 그것의 즐거움을 향유할 수 있는 여유 혹은 필요를 가진 인생을 살아온 사람
corporate 환경은 사람을 늙게 만든다! 단순히 physically가 아니라 정신적으로. 왜냐면 호기심을 꺾기 때문

2015년부터 2025년까지 10년 동안 나는 세상을 더욱 higher resolution으로 보려고했다. 그러나 마침내 가까이서 본 세상의 모습은 더없이 추악하고 지루하기 그지 없었다. 그래서 나는 다시 순수의 세계로 돌아간다. clear thinking만이 지배하는.


mathematics is a language for clear thinking.
- 핑계가 없다


뇌터의 법칙: https://youtu.be/Em-cqknAFKw?si=RJJ3MkX61txHmAmM
- 에너지 보존은 대칭성에서 나온다. 대칭성이 깨지면 보존법칙도 깨진다. 너무나 아름다운 아이디어 
https://en.wikipedia.org/wiki/Noether%27s_theorem



우리는 우리 자신의 인생을 매순간 현실인 것처럼 살아가야 하지만, 또한 동시에 제3자의 시선으로 마치 남의 인생인 것처럼 바라볼 수 있어야 한다.
마치 과학 탐구에서, 내가 해당 순간에 탐구하고 있는 주제에 최선을 다해야 하지만, 동시에 한발짝 물러서서 이걸 계속 탐구하는 게 맞는지 끊임없이 loop 검증해야 하는 것처럼 (스타트업도 마찬가지)



---

<Quote>
“Progress in science depends on new techniques, new discoveries and new ideas, probably in that order.” - Sydney Brenner
"What I cannot create, I do not understand" - Richard Feynman

<Good Essays/Reads - Business>

- https://www.nfx.com/post/technology-windows
- https://x.com/NFX/status/2075253076152263069
- https://www.nfx.com/post/ai-games


<Good Essays/Reads - Philosophy/Humanities/History>
- https://www.econlib.org/library/Essays/hykKnw.html

- https://www.cs.unc.edu/techreports/86-020.pdf

- https://samoburja.com/borrowed-versus-owned-power/
- https://samoburja.com/gft/

- https://www.nosetgauge.com/p/growth-and-civilisation

- https://www.nosetgauge.com/p/review-foragers-farmers-and-fossil-fuels
- https://www.benlandautaylor.com/p/looking-beyond-the-veil
- https://medium.com/entrepreneurs-first/tech-entrepreneurship-and-the-disruption-of-ambition-4e6854121992
- https://rudolf.website/short-reviews-nonfiction-1/#section-3


- https://danfaggella.com/essays/

- https://www.almendron.com/tribuna/wp-content/uploads/2018/03/the-dynamo-and-the-computer-an-historical-perspective-on-the-modern-productivity-paradox.pdf

<Good Essays/Reads - AI & Society>
- https://intelligence-curse.ai/
    - pretty comprehensive outlook & analysis of how AI will play out and what should be done as a society. also a lot of great reference/citations
- https://gradual-disempowerment.ai/
- Dario Amodei Essays
    - https://darioamodei.com/essay/the-adolescence-of-technology
    - https://darioamodei.com/essay/machines-of-loving-grace
        - Both has a lot of great reference/citations
- The History of Future series
    - https://www.nosetgauge.com/p/a-history-of-the-future-2025-2027
    - 

- https://www.forethought.org/research/ai-enabled-coups-how-a-small-group-could-use-ai-to-seize-power

- https://vitalik.eth.limo/general/2023/11/27/techno_optimism.html
- https://www.asimov.press/p/gentle-romance
- https://www.beren.io/2023-04-23-Composable-latent-spaces-BCIs-modular-minds/
- https://lukedrago.substack.com/p/the-future-of-taste
- https://lukedrago.substack.com/p/the-use-of-knowledge-in-agi-society
- https://epoch.ai/gradient-updates/moravec-s-paradox
- https://epoch.ai/gradient-updates/most-ai-value-will-come-from-broad-automation-not-from-r-d
- https://www.astralcodexten.com/p/your-book-review-the-dawn-of-everything?hide_intro_popup=true


- https://ai-2027.com/
- https://inferencemagazine.substack.com/p/how-much-economic-growth-from-ai

- https://strangecities.substack.com/p/the-choice-transition
- https://www.lesswrong.com/posts/Kobbt3nQgv3yn29pr/my-motivation-and-theory-of-change-for-working-in-ai#Extinction_by_industrial_dehumanization


- https://www.nosetgauge.com/p/a-history-of-the-future-2025-2027

- https://www.beren.io/2023-04-10-the-singularity-as-cognitive-decoupling/
- https://www.nosetgauge.com/p/a-disneyland-without-children
- https://danfaggella.com/flex/


<Good Essays/Reads - AI Technology>

- https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf
- https://groups.csail.mit.edu/medg/people/psz/Licklider.html

- https://devinterp.com/
- https://aligned.substack.com/p/alignment-mvp
- https://www.alignmentforum.org/posts/tmuFmHuyb4eWmPXz8/rant-on-problem-factorization-for-alignment
- https://arxiv.org/pdf/2406.14546
- https://aiguide.substack.com/p/the-llm-reasoning-debate-heats-up
- https://www.lesswrong.com/posts/HQyWGE2BummDCc2Cx/the-case-for-cot-unfaithfulness-is-overstated
- https://darioamodei.com/post/the-urgency-of-interpretability#fnref:1




https://www.pi.website/blog/pi0

<Good Essays/Reads - non-AI Technology>
- https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf


<<Good Essays/Reads - Science/Mathematics>

- https://arxiv.org/pdf/1802.05968


<Good Essays/Reads - Miscellaneous Interesting Concepts/Stuff>
- https://en.wikipedia.org/wiki/Ephemeralization
- https://en.wikipedia.org/wiki/Lyapunov_exponent
- https://en.wikipedia.org/wiki/Jevons_paradox
- https://en.wikipedia.org/wiki/Lump_of_labour_fallacy
- https://en.wikipedia.org/wiki/No_Silver_Bullet
- https://en.wikipedia.org/wiki/Elite_overproduction
- https://en.wikipedia.org/wiki/PARC_(company)


<Important AI Papers>
- https://arxiv.org/abs/2001.08361
- https://arxiv.org/pdf/2504.01849

<Peopl/Newsletter/Blog I follow/read>
- https://thegregyang.com/
- https://a16z.com/news-content/




<AI Research Ideas>
- What we know about AI
- AI models are vastly more psychologically complex: introspection (https://www.anthropic.com/research/introspection) & persona (https://www.anthropic.com/research/persona-vectors)
    - source: https://darioamodei.com/essay/the-adolescence-of-technology#1-i-m-sorry-dave
- https://www.anthropic.com/research/emergent-misalignment-reward-hacking
- https://www.anthropic.com/research/auditing-hidden-objectives

<AI Reads>
- https://www.anthropic.com/research/next-generation-constitutional-classifiers
- https://arxiv.org/pdf/2504.01849
- https://www.anthropic.com/news/the-need-for-transparency-in-frontier-ai
- https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html#assessing-features-v-neurons
- https://www.anthropic.com/news/golden-gate-claude
- https://transformer-circuits.pub/2025/attribution-graphs/biology.html
- https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf
- https://alignment.anthropic.com/2025/inoculation-prompting/
- https://darioamodei.com/post/the-urgency-of-interpretability
- https://www.anthropic.com/news/collective-constitutional-ai-aligning-a-language-model-with-public-input

- https://www.anthropic.com/research/mapping-mind-language-model
- https://www.anthropic.com/research/auditing-hidden-objectives


<AI-relevant Reads>
- https://worksinprogress.co/issue/the-golden-age-of-vaccine-development/
- https://distill.pub/2020/circuits/frequency-edges/
- https://sites.cc.gatech.edu/computing/nano/documents/Joy%20-%20Why%20the%20Future%20Doesn%27t%20Need%20Us.pdf
- https://www.science.org/doi/10.1126/science.ads9158#elettersSection
- https://www.anthropic.com/constitution
- https://slatestarcodex.com/2015/08/17/the-goddess-of-everything-else-2/
- https://en.wikipedia.org/wiki/Socialist_calculation_debate#:~:text=The%20socialist%20calculation%20debate%2C%20sometimes,of%20the%20means%20of%20production.





<Cool Stuff I'm following>
- https://ai.objectives.institute/talk-to-the-city
- https://www.arena.education/
- https://alpha.school/the-program/
- https://www.primeintellect.ai/blog/intellect-2

In fact, there are many examples, in both the natural and artificial worlds, of systems we understand (and sometimes control) at the level of principles but not in detail: economies, snowflakes, cellular automata, human evolution, human brain development, and so on. (source: https://darioamodei.com/post/the-urgency-of-interpretability#fn:1)
+ Bingbin Liu (7/17/26): "Although 2-layer MLPs are not the same as the actual Transformers we're using nowadays, the former give useful insights on the latter's behavior" 
-> My Q: then can we approach AI interpretability as we approach Economics?
 




