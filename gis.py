"""
gis.py - Google Image Search Willie module
Ross Mulcare - rossmulcare.net
-
Modified version of search.py 
by Sean B. Palmer / Edward Powell
"""

from willie import module, web
import json

def google_ajax(query):
    uri = 'http://ajax.googleapis.com/ajax/services/search/images'
    args = '?v=1.0&safe=off&q=' + web.quote(query)
    bytes = web.get(uri + args)
    return json.loads(bytes)

def google_search(query):
    result = google_ajax(query)
    height = result['responseData']['results'][0]['height']
    width = result['responseData']['results'][0]['width']
    url = result['responseData']['results'][0]['url']
    size = height + 'x' + width
    try:
     return url + ' \x035[' + size + ']\x03'
    except IndexError:
        return None
    except TypeError:
        return False

@module.commands('gis', 'img')
@module.example('.gis french bulldog')
def gis(bot, trigger):
    query = trigger.group(2)
    if not query:
        return bot.reply('.gis what?')
    uri = google_search(query)
    if uri:
        bot.reply(uri)
    elif uri is False:
        bot.reply("Problem getting data from Google.")
    else:
        bot.reply("No results found for '%s'." % query)
