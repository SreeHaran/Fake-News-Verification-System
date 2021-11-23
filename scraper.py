from googlesearch import search
from newspaper import Article
import nltk
nltk.download('punkt')

query = "omicron cases rises in india"
 
for url in search(query, num=1, tbs="qdr:d", stop= 1, pause=3): 
#tbs (str) – Time limits (i.e “qdr:h” => last hour, “qdr:d” => last 24 hours, “qdr:m” => last month)
	print(url)
	
	toi_article = Article(url, language="en")
	toi_article.download()
	toi_article.parse()
	toi_article.nlp()
	
	
	print("Article's Title:")
	print(toi_article.title)
	print("\n")
	
	
	print("Article's Summary:")
	print(toi_article.summary)
	print("\n")


	print("Article's Keywords:")
	print(toi_article.keywords)