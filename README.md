# WordCloud API
API to generate word/tag clouds.
_Blog post/tutorial coming soon._

## Why? It's 2019, tag clouds died with page hit counters...
Great question! Because I've always liked them. Yes, they've been done _really_ wrong. But I feel they can still give a good sense of weight to a body of text or terms. By giving a visable difference of _weighted_ words, you can, at a quick glance, understand the what a blob of information is trying to portray.

## Okay, point made, _kinda_...
You're right! Let's demonstrate an example. Let's use a book, "Little Big Man" by Thomas Berger. I googled obscure books, and this one popped up. I've never read it, but put the summery found [HERE](http://www.bookrags.com/studyguide-little-big-man/), through this API.

![Little Big Man Word Cloud](https://kbcarte.com/wp-content/uploads/little_big_man_summery.jpeg)

Now, from this word cloud alone, we can gather that:
- It's about a white guy and indians
- Somewhere in or close to Kansas, Denver, or Cheyenne
- Most likely dramatic. _kill_, _soldier_, _depressed_, _ambushed_

Not exactly my genre or type of book, but I can gather that by glancing over this image instead of reading a synopsis of the literature. This can go beyond books. Scrape a website and get a general sense of what it's about. Need to present a speach or lecture? Run your notes through the API and find what you might be talking too much on, or see the subjects that are neglected.

But mostly I just wanted to get into API dev, and this is great for learning. Handling images, multiple _variable_ end points, and of course Python =)

### End Points
- **GET** /colors/_<string: search_color>_
    - _optional_ `<string: search_color>`
- **POST** /cloud
    - **BODY** `{"terms": "A big string of text to make cloud", "color": "Greens"}`

### Examples
![Little Big Man Word Cloud Color List](https://kbcarte.com/wp-content/uploads/postman_full_color_list.jpg)

![Little Big Man Word Cloud Color Select List](https://kbcarte.com/wp-content/uploads/postman_select_color_list.jpg)

![Little Big Man Word Cloud Image](https://kbcarte.com/wp-content/uploads/postman_post_words.jpg)

### TO-DO
- **Image Masks** _(upload images to be masked against)_
- **Custom Colors** _(trasnparent background, inherited masked text colors, other image formats, stop word filter)_
- **Authentication** _(User profiles, OAuth support, voting?, mobile apps?)_

### Contact
- https://kbcarte.com
- contact@kbcarte.com
- Pull Request
- Twitter: https://twitter.com/KBCarte42
