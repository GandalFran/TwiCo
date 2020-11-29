#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from soa.models.news_model import NewsExtraction
from soa.models.topic_modelling_model import TopicModellingExtraction
from soa.models.twitter_model import TwitterExtraction
from soa.models.sentiment_model import SentimentAnalyzer

class NewsAndTwitterExtraction:

    def extract(self, 
                query:str, 
                count_news:int=DEFAULT_NUM_NEWS_EXTRACTED, 
                count_tweets:int=DEFAULT_NUM_TWEETS_EXTRACTED, 
                lang:str=DEFAULT_TWEETS_LANGUAGE, 
                from_date:str=(datetime.datetime.now() - datetime.timedelta(days=365)).strftime('%Y-%m-%d'), 
                to_date:str=datetime.date.today().strftime('%Y-%m-%d')) -> dict:
        """
        Extracts news about a theme given, extracting the main topics of those news and getting tweets talking about that theme and each topic extracted
        to know the sentiment and opinion of the people on Twitter talking about those themes.

        Arguments:
            query (:obj:`str`): Keyword or theme to search news and tweets from.
            count_news (:obj:`int`, optional): Number of news to extract.
            count_tweets (:obj:`int`, optional): Number of tweets to extract.
            lang (:obj:`str`, optional): Language of the tweets and news to retrieve. The language must be ISO coded. For example, English code would be 'en'.
            from_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will start.
            to_date (:obj:`str`, optional): Date in ISO 8601 format (YYYY-mm-dd) where data retrieval time interval will stop.

        Returns:
            :obj:`list` of :obj:`dict` formatted Twitter Sentiment and Topic Modelling data.

        Examples:
            >>> print(self.extract())
            [{'news': ['This a news about covid-19'. '...', ...], 
              'topics': {
                    't1': {
                            'name': 'covid-19, health',
                            'tweets': [
                                {
                                    'url': 'https://www.twitter.com/statuses/...',
                                    'text': 'This is a tweet about covid-19 and health',
                                    'sentiment' 'neutral'
                                },
                                ...
                            ]
                    }
              }
            }, ...]
        """
        final_results = []

        ## 1. Extract news from NEWS API
        news_hdlr = NewsExtraction()
        print("Extracting news...")
        list_news = news_hdlr.get_news_everything(q=query,
                                                  count=count_news,
                                                  lang=lang)

        ## 2. Analyze and get topics from list of news
        topics_hdlr = TopicModellingExtraction()
        print("Extracting topics...")
        text_query = ''.join([ news['content'] for news in list_news if news['content'] is not None])
        printable = set(string.printable)
        text_query = ''.join(filter(lambda x: x in printable, text_query))
        topics = topics_hdlr.get_topics(text=text_query)
        topics['topics'] = list(set(topics['topics']))

        ## 3. Search tweets containing 'covid' keywords and topics extracted
        topic_result = {}
        twitter_hdlr = TwitterExtraction()
        sentiment_hdlr = SentimentAnalyzer()
        print("Extracting tweets...")
        for topic in topics['topics']:

            twitter_search_query_list = [query, topic]

            # Extract from twitter api
            print("····· FROM API")
            print(twitter_search_query_list)
            list_tweets = twitter_hdlr.get_tweets_multiple_query(query=twitter_search_query_list, 
                                                                 count=count_tweets,
                                                                 lang=lang,
                                                                 start_date = from_date,
                                                                 end_date = to_date,
                                                                 include_both=True)
            topic_result['name'] = twitter_search_query_list

            ## 4. Sentiment analysis on text
            twitter_results = []
            print("····· CALCULATING SENTIMENT")
            for tweet in list_tweets:
                twitter_results.append({'url': tweet['url'], 
                                        'text': tweet['text'], 
                                        'sentiment': sentiment_hdlr.analyze(tweet['text'])['sentiment']})

            topic_result['tweets'] = twitter_results
            final_results.append(topic_result)

        results = {
            'news': list_news,
            'topics':{
                't1': final_results
            }
        }

        return results
