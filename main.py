import wikipediaapi


def read_wiki_titles(filename: str):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title,lang="en"):
    w_api = wikipediaapi.Wikipedia(lang)
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""


def get_art_content(filename):
    wik = read_wiki_titles(filename)
    for t in wik:
        article = get_article(t)
        yield article.strip()


def count(filename, all_letters):
    articles = get_art_content(filename)
    num_of_articles = 0
    all_counted = []
    for art in articles:
        letters_for_article = {}
        art = art.lower()
        if len(art) > 0:
            num_of_articles += 1
            for let in all_letters:
                letters_for_article[let] = art.count(let)
        all_counted.append(letters_for_article)
    all_averages = []
    for letter in all_letters:
        sum = 0
        for d in all_counted:
            if letter in d:
                sum += d[letter]
        all_averages.append(sum/num_of_articles)
    return all_averages


all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ave = count("small.txt", all_letters)

for i in range(len(all_letters)):
    print(all_letters[i] + ": " + str(ave[i]))
