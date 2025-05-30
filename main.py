import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image

st.set_page_config(layout="wide")
st.title("Influencers")

img = Image.open("A Good Christian.png")

coords = streamlit_image_coordinates(img, key="click-img")

regions = {
    "Coffee or Tea?": {"center": (71, 573), "radius": 121},
    "Discipline": {"center": (322, 716), "radius": 114},
    "Perfection": {"center": (1132, 570), "radius": 155},
    "Erasure": {"center": (1194, 281), "radius": 113},
    "A Good Christian": {"center": (529, 259), "radius": 159},
    "Shanghai": {"center": (889, 245), "radius": 187},
    "Integrity": {"center": (218, 200), "radius": 131}
}

texts = {
    "Coffee or Tea?": '''"Biracial"

I grew up being fully White and fully Chinese—but never at the same time. At the country club pool, I was White. When my grandma handed me a bowl of red bean soup, I was Chinese. My identity felt modular, like pieces I could assemble or disassemble depending on the room I was in. I became skilled at reading a space and adjusting accordingly—speaking with or without an accent, downplaying certain foods, skipping over certain stories. It wasn’t shame—it was survival. And for a while, it worked.

But life isn’t that compartmentalized anymore. I no longer move through rooms where I can afford to split myself in two. Instead, I’ve had to learn how to carry both sides of me at once—how to be whole, even when others don’t know how to read me. I’ve come to understand that being biracial isn’t about fitting into two separate boxes. It’s about living in the tension between them and finding strength in the in-between.

Now, I don’t shift to make others comfortable. I bring my full self into the spaces I occupy, even when it means being misunderstood. I’ve learned that duality isn’t a flaw—it’s a form of richness. And claiming both my identities at once is not a contradiction.''',
    "Discipline": '''I hated ballet for years before I finally quit.

Discipline is defined as “training oneself to do something in a controlled and habitual way”—and I did exactly that. But in Chinese, 嚴以律己 means “to demand a lot of oneself,” and I realized ballet was not the path through which I wanted to make that demand. I walked away, not because I lacked discipline, but because I chose to invest it elsewhere. Even if others find it distasteful or disappointing, this is why I’ve poured so much of myself into academics—because I chose where my effort belongs.

For a long time, I thought quitting meant failure. I worried that walking away would confirm the judgments of those who saw me as someone who gives up when things get hard. But leaving ballet wasn’t about giving up—it was about choosing. I no longer wanted to be shaped by pain I didn’t believe in, or push myself for a version of excellence that didn’t feel like mine. I had the strength to stay, but I found the courage to walk away.

Now, when I sit with a dense research paper reworking a sentence until it feels just right, I feel that same discipline—but it's rooted in purpose. I still demand a lot of myself, just in a way that’s aligned with who I am and what I value. And that, I’ve come to believe, is what true discipline looks like: not endurance for endurance’s sake, but the clarity to know where your energy is best spent.''',
    "Perfection": '''Letting go of “perfect”

I’ve maintained a 4.0 GPA across 66 college credit hours and high school. At the same time, I’ve failed—scoring 60s and 70s on major exams. My failures push me further and are a source of motivation. Perfection isn’t just an unrealistic goal—it’s also not something worth striving for.

What I’ve come to understand is that perfection leaves no room for learning. It demands a polished exterior, not progress. When I chase perfection, I work out of fear—fear of being seen as less than, fear of disappointing others, fear of confirming my own doubts. But when I embrace imperfection, I work from curiosity. I ask questions, take risks, and stay open to being wrong. That’s where the growth happens.

Letting go of perfect has meant redefining success. It’s not just about grades or achievements—it’s about showing up, being resilient, and having the humility to try again after falling short. I still hold myself to high standards, but they’re mine now, not borrowed from anyone else's expectations. I’m not perfect, but I’m consistent. I’m not flawless, but I’m honest—with myself and with others.''',
    "Erasure": '''Who am I?

This wall holds more than just reminders—it holds pieces of me. Some are tasks I need to finish, others are memories I want to keep close. Together, they form a kind of map: not of where I’m going, but of who I am. Growing up, I was constantly told who I was. Teachers, family members, even strangers would offer labels and observations, often with confidence, as if they knew me better than I knew myself. At first, I believed them. I shaped myself around those assumptions—quiet, smart, obedient, driven—even when they clashed with how I felt inside.

But over time, I started to feel the strain of performing identities that didn’t belong to me. Each time I accepted someone else’s version of who I should be, I lost a little bit of my own. These notes on my wall—brief, chaotic, handwritten—serve as a quiet act of resistance. They remind me that conforming for the sake of approval can be a subtle form of erasure. And that fulfilling others’ expectations at the expense of your own truth isn’t selflessness—it’s self-abandonment.

To know who I am, I’ve had to strip away those outside narratives and start listening to the voice that’s been buried underneath. This wall is part of that process.''',
    "A Good Christian": '''What does it mean to be Christian?

To me, the cross hanging in my room is more than a religious symbol—it’s a reminder of all the Sundays I spent in the pews, listening, watching, absorbing. I grew up attending a church where most of the congregation didn’t look like me. At first, I didn’t think much of it. But as I got older, I began to notice the subtle ways that my family stood out—not just in appearance, but in the way we experienced and interpreted faith.

Church was supposed to be a place of unity, a place where love, humility, and selflessness were not only preached but lived. And yet, as I observed more closely, I began to sense a quiet contradiction. People spoke eloquently about compassion, about sacrifice and serving others. But when tensions rose or discomfort set in, those same values often gave way to judgment, defensiveness, or even indifference. I saw kindness withheld out of convenience, and truth softened to avoid conflict.

It made me ask harder questions: Is faith only real when it’s easy? What does it mean to truly live out one’s beliefs? I realized that many people—including myself—struggle to align what they believe with how they behave. Christianity, I began to understand, isn’t about perfection or performance. It’s about the constant, sometimes uncomfortable work of confronting your own flaws and choosing love anyway. Being Christian, then, is not just about knowing the right answers, but about wrestling with them—especially when it’s inconvenient or lonely.''',
    "Shanghai": '''Second Home

Shanghai has always existed in layers for me—a city of contradictions, where sleek glass malls tower over crumbling alleyways, and luxury cars idle just blocks from fruit stands and laundry lines. Growing up, I heard vivid stories from my mother and grandparents about their lives in this city. Their Shanghai was different: slower, humbler, filled with resilience and small joys. They spoke of cramped apartments, shared meals, and long walks under dim streetlights. When I finally walked those same streets years later, I struggled to reconcile their memories with what I saw.

The Shanghai I encountered was fast-paced and gleaming, ambitious in every direction. Yet beneath that surface shimmer, I began to notice the sharp edges—the inequality etched into the city itself. The difference between who gets to rise and who stays behind wasn’t just economic; it was structural. Malls weren’t just malls—they were symbols of access. Alleyways weren’t just alleyways—they were reminders of who had been left out of Shanghai’s transformation.

In this city that is both foreign and familiar, I started to see how class, opportunity, and access are distributed unevenly—not just in Shanghai, but everywhere. And I began to understand my own position more clearly: a visitor tied to both past and present, someone who benefits from access yet carries the stories of those who did not. Shanghai, in all its complexity, has become a second home''',
    "Integrity": '''Grandfather’s voice

“有一次，我的爸爸把钱放在最高的柜台上。当他回家时，钱不见了。他问了我是否偷了柜台上的钱。我诚实地回答说，没有。他打了我，反复质问我是不是我偷了他的钱。没过多久，我妈妈拿着他的钱进来了，解释说是他把钱放在桌子上了。我爸爸没有道歉。”

"One time, my dad put his money on the highest shelf. When he came home, the money was gone. He asked me if I had stolen it. I answered honestly and said no. He hit me and repeatedly questioned whether I had taken his money. Not long after, my mom came in holding the money and explained that he had left it on the table. My dad didn’t apologize."
'''
}


if coords is not None:
    x, y = coords["x"], coords["y"]
    for label, data in regions.items():
        cx, cy = data["center"]
        r = data["radius"]
        if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
            st.subheader(label)
            st.write(texts[label])
            break
