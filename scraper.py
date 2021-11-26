from googlesearch import search
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('punkt')

query = "omicron cases rises in india"
 
max_a=0.
max_b=0.
link='none'

for url in search(query, num=15, tbs="qdr:w", stop= 15, pause=3): 
#tbs (str) – Time limits (i.e “qdr:h” => last hour, “qdr:d” => last 24 hours, “qdr:m” => last month)
	print(url)
	
	try:
		toi_article = Article(url, language="en")
		toi_article.download()
		toi_article.parse()
		toi_article.nlp()
	except:
		print('***********Error while parsing the url*****************')
		continue
	
	summary = toi_article.summary
	corpus = [summary, query]
	vect = TfidfVectorizer(min_df=1, stop_words="english")
	tfidf = vect.fit_transform(corpus)
	pairwise_similarity = tfidf * tfidf.T
	a = pairwise_similarity.toarray()
	
	title = toi_article.title
	corpus = [title, query]
	vect = TfidfVectorizer(min_df=1, stop_words="english")
	tfidf = vect.fit_transform(corpus)
	pairwise_similarity = tfidf * tfidf.T
	b = pairwise_similarity.toarray()
	
	max_num = max(max_a,max_b)
	if (a[0][1]>max_num) or (b[0][1]>max_num):
		max_a=a[0][1]
		max_b=b[0][1]
		link=url

res=int(round(max(max_a,max_b),2)*100)
if res>70:
	print(f"Most Relevant News: {link}")
	print(f"Genuinity: {res}%")
elif res>20:
	print(f"Most Relevant News: {link}")
	print(f"Genuinity: {res+30}%")
else:
	print(f"It Might be a Fake News")
	print(f"Genuinity: {res+5}%")