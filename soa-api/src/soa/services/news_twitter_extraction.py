#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from soa.models.news_model import NewsExtraction
from soa.models.topic_modelling_model import TopicModellingExtraction
from soa.models.twitter_model import TwitterExtraction
from soa.models.sentiment_model import SentimentAnalyzer


class NewsAndTwitterExtraction:

    def extract(self, query:str=None, from_date:str=None, to_date:str=None) -> dict:

        if query is not None:
            ## 1. Extract news from NEWS API
            news_hdlr = NewsExtraction()
            list_news = news_hdlr.get_news_everything(q=query)

            ## 2. Analyze and get topics from list of news
            topics_hdlr = TopicModellingExtraction()
            list_content_news = [news['content'] for news in list_news]
            text_query = '.'.join(list_content_news)
            topics = topics_hdlr.get_topics(text=text_query)

            ## 3. Search tweets containing 'covid' keywords and topics extracted
            twitter_hdlr = TwitterExtraction()
            twitter_search_query_list = [query]
            twitter_search_query_list = twitter_search_query_list.append(topics['topics'])
            if from_date is None or to_date is None:
                list_tweets = twitter_hdlr.get_tweets_multiple_query(query=twitter_search_query_list, 
                                                                     start_date = from_date,
                                                                     end_date = to_date,
                                                                     include_both=True)
            else:
                list_tweets = twitter_hdlr.get_tweets_multiple_query(query=twitter_search_query_list,
                                                                     include_both=True)

            ## 4. Sentiment analysis on text
            sentiment_hdlr = SentimentAnalyzer()
            sentiment_results = [sentiment_hdlr.analyze(tweet['text']) for tweet in list_tweets]

            results = {
                'sentiment': sentiment_results
            }
        else:
            results = {} 

        return results
