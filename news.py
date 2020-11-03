from requests_html import HTMLSession
from flask import flask, jsonify,request
app= flask(__name__)
@app.route('/', methods=['GET'])
def test():
    session = HTMLSession()


    r = session.get('https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en')

    r.html.render(sleep=1, scrolldown=5)


    articles = r.html.find('article')
    newslist = []

    for item in articles:
        try:
            newsitem = item.find('h3', first=True)
            title = newsitem.text
            link = newsitem.absolute_links
            newsarticle = {
                'title': title,
                'link': link 
            }
            newslist.append(newsarticle)
        except:
           pass


    return jsonify(newslist)
if __name__ == '__main__':
    app.run(debug=True, port=8000)
    