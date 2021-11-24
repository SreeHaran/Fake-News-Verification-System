from googlesearch import search
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer
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
	
	print("Title Similarity: ", a[0][1])
	print("Summary Similarity: ", b[0][1])