from src.scraper import get_citations_needed_count, get_citations_needed_report


def test_get_citations_needed_count_guam_wikipedia():
    url = 'https://en.wikipedia.org/wiki/Guam'
    actual = get_citations_needed_count(url)
    expected = 11
    assert actual == expected

def test_get_citations_needed_count_history_of_mexico_wikipedia():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(url)
    expected = 5
    assert actual == expected

def test_get_citations_needed_report_guam():
    paragraph = 'The removal of Guam\'s security clearance by President John F. Kennedy in 1963 allowed for the development of a tourism industry. When the United States closed U.S. Naval Base Subic Bay and Clark Air Base bases in the Philippines after the expiration of their leases in the early 1990s, many of the forces stationed there were relocated to Guam.[citation needed]'
    url = 'https://en.wikipedia.org/wiki/Guam'
    report = get_citations_needed_report(url)
    assert(paragraph in report)

def test_get_citations_needed_report_guam_paragraph2():
    paragraph = 'The 1997 Asian financial crisis, which hit Japan particularly hard, severely affected Guam\'s tourism industry. Military cutbacks in the 1990s also disrupted the island\'s economy. Economic recovery was further hampered by devastation from Supertyphoons Paka in 1997 and Pongsona in 2002, as well as the effects of the September 11 terrorist attacks on tourism.[citation needed]'
    url = 'https://en.wikipedia.org/wiki/Guam'
    report = get_citations_needed_report(url)
    assert(paragraph in report)

def test_get_citations_needed_report_guam_paragraph3():
    paragraph = 'The official languages of the island are English and Chamoru. Filipino is also a common language across the island. Other Pacific island languages and many Asian languages are spoken in Guam as well. Spanish, the language of administration for 300 years, is no longer commonly spoken on the island, although vestiges of the language remain in proper names, loanwords, and place names and it is studied at university and high schools.[citation needed]'
    url = 'https://en.wikipedia.org/wiki/Guam'
    report = get_citations_needed_report(url)
    assert(paragraph in report)
    