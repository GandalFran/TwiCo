#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from soa import config
from newsapi import NewsApiClient
from datetime import datetime
from typing import List, Dict, Any

class NewsExtraction:

    def __init__(self):
        """
        Create NewsAPI object to get news
        """

        self._api = NewsApiClient(config.NEWSAPI_TOKEN)

    def get_news_top_headlines(self,
                               query: str,
                               country_code: str = config.DEFAULT_NEWS_COUNTRY) -> List[Dict]:
        """Retrieve top news in a country specified and containing a keyword given in a query
        
        Arguments:
            query {str} -- keyword to find in top news
            country_code {str} -- two letter code to specify the country (default: {DEFAULT_NEWS_COUNTRY})

        Returns:
            :obj:`list` -- list of dictionaries containing information about the news retrieved
        """

        # Empty list to store parsed news
        news = []

        try:
            top_news = self._api.get_top_headlines(q = query,
                                                   country = country_code)

            # src: https://medium.com/daily-python/python-script-to-search-for-news-based-on-keywords-daily-python-5-509348bd190e
            num_news = top_news['totalResults']

            for a_new in top_news['articles']:
                # Format title
                title = self._format_title(a_new['title'])

                # Format date
                date = self._format_date(a_new['publishedAt'])

                # Extract information
                news_item = {}
                news_item['title'] = title
                news_item['description'] = a_new['description']
                news_item['publishedAt'] = date
                news_item['content'] = a_new['content']
                news_item['url'] = a_new['url']
                news.append(news_item)

        except Exception as e:
            print("Whoops! Something went wrong here. \
                    The error code is " + str(e))
            return []

        print('News retrieved: ', len(news))
        return news

    def get_news_everything(self,
                            q: str,
                            from_date: str = datetime.today().strftime('%Y-%m-%d'),
                            to_date: str = datetime.today().strftime('%Y-%m-%d'),
                            lang: str = config.DEFAULT_NEWS_LANGUAGE,
                            count: int = config.DEFAULT_NUM_NEWS_EXTRACTED) -> List[Dict]:
        """Retrieve every news in a range of time, in an specific language and containing in their title a keyword given
        
        Arguments:
            q {str} -- keyword to find in the title of news
            from_date {str} -- beginning date point to retrieve news (default: {datetime.today().strftime('%Y-%m-%d')})
            to_date {str} -- end date point to retrieve news (default: {datetime.today().strftime('%Y-%m-%d')})
            lang {str} -- language ot the news (default: {DEFAULT_NEWS_LANGUAGE})
            count {int} -- number of news to retrieve (default: {DEFAULT_NUM_NEWS_EXTRACTED})

        Returns:
            :obj:`list` -- list of dictionaries containing information about the news retrieved
        """

        # Empty list to store parsed news
        news = []

        try:
            every_news = self._api.get_everything(q = q,
                                                   from_param = from_date,
                                                   to = to_date,
                                                   language = lang,
                                                   page_size = count,
                                                   sort_by = 'popularity')

            num_news = every_news['totalResults']

            for a_new in every_news['articles']:
                # Format date
                date = self._format_date(a_new['publishedAt'])

                # Extract information
                news_item = {}
                news_item['title'] = a_new['title']
                news_item['description'] = a_new['description']
                news_item['publishedAt'] = date
                news_item['content'] = a_new['content']
                news_item['url'] = a_new['url']
                news.append(news_item)

        except Exception as e:
            print("Whoops! Something went wrong here. \
                    The error code is " + str(e))
            return []

        print('News retrieved: ', len(news))
        return news

    def _format_title(self, title: str) -> str:
        """Write title in the proper format
        
        Arguments:
            title {str} -- title to be formatted

        Returns:
            :obj:`str` title with the proper format
        """

        title_list = []

        title_split = title.split(' - ')

        for i in range(len(title_split)-1):
            title_list.append(title_split[i])

        final_title = ' - '.join(title_list)

        return final_title

    def _format_date(self, date_hour: str) -> str:
        """Write date in the proper format
        
        Arguments:
            date_hour {str} -- date to be formatted

        Returns:
            :obj:`str` date with the proper format
        """

        date_list = []

        date_split = date_hour.split('T')
        date = date_split[0]
        hour = date_split[1][:-1]
        date_hour = [date, hour]

        final_date = ', '.join(date_hour)

        return final_date
