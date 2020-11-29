#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

from soa import config
import datetime
import time
import random
import json
from typing import List, Dict, Any

class NewsExtraction:

    def get_news_top_headlines(self,
                               query: str,
                               country_code: str = config.DEFAULT_NEWS_COUNTRY) -> List[Dict]:
        """
        Retrieve top news in a country specified and containing a keyword given in a query
        
        Arguments:
            query (:obj:`str`) -- keyword to find in top news
            country_code (:obj:`str`) -- two letter code to specify the country (default: {DEFAULT_NEWS_COUNTRY})

        Returns:
            :obj:`list` -- list of dictionaries containing information about the news retrieved
        """

        # Empty list to store parsed news
        news = []

        # Extract info and wait between requests
        time.sleep(random.randint(config.REQUEST_MIN_TIME_WAIT, config.REQUEST_MAX_TIME_WAIT))

        # Build url to request
        url = config.ENDPOINT_RECENT_HEADLINES.replace('{query}', query).replace('{code}', country_code).replace('{api_key}', config.NEWSAPI_TOKEN)

        # Choose a random user agent
        user_agent = random.choice(config.USER_AGENT_LIST)

        # Send HTTP Request to website url with chosen user agent
        try:
            response = requests.get(url, headers={'User-Agent': user_agent})
        except Exception as e:
            print("Whoops! Something went wrong here. \
                    The error code is " + str(e))
            return []

        if response.status_code != requests.codes.ok:
            print("HTTP RESPONSE FAILED: " + str(response.status_code))
            print(response.content)
            return []

        # src: https://medium.com/daily-python/python-script-to-search-for-news-based-on-keywords-daily-python-5-509348bd190e
        results = json.loads(response.content)
        num_news = results['totalResults']

        for news_item in results['articles']:
            # Format title and date
            news_item['title'] = self._format_title(news_item['title'])
            news_item['publishedAt'] = self._format_date(news_item['publishedAt'])
            news.append(news_item)


        print('News retrieved: ', len(news))
        return news

    def get_news_everything(self,
                            q: str,
                            from_date: str = datetime.date.today().strftime('%Y-%m-%d'),
                            to_date: str = datetime.date.today().strftime('%Y-%m-%d'),
                            lang: str = config.DEFAULT_NEWS_LANGUAGE,
                            count: int = config.DEFAULT_NUM_NEWS_EXTRACTED) -> List[Dict]:
        """
        Retrieve every news in a range of time, in an specific language and containing in their title a keyword given
        
        Arguments:
            q (:obj:`str`) -- keyword to find in the title of news
            from_date (:obj:`str`, optional) -- beginning date point to retrieve news (default: {datetime.date.today().strftime('%Y-%m-%d')})
            to_date (:obj:`str`, optional) -- end date point to retrieve news (default: {datetime.date.today().strftime('%Y-%m-%d')})
            lang (:obj:`str`, optional) -- language ot the news (default: {DEFAULT_NEWS_LANGUAGE})
            count (:obj:`int`, optional) -- number of news to retrieve (default: {DEFAULT_NUM_NEWS_EXTRACTED})

        Returns:
            :obj:`list` -- list of dictionaries containing information about the news retrieved
        """

        # Empty list to store parsed news
        news = []

        # Extract info and wait between requests
        time.sleep(random.randint(config.REQUEST_MIN_TIME_WAIT, config.REQUEST_MAX_TIME_WAIT))

        # Build url to request
        url = config.ENDPOINT_NEWS_EVERYTHING.replace('{query}', q).replace('{from_date}', from_date).replace('{to_date}', to_date).replace('{api_key}', config.NEWSAPI_TOKEN)

        # Choose a random user agent
        user_agent = random.choice(config.USER_AGENT_LIST)

        # Send HTTP Request to website url with chosen user agent
        try:
            response = requests.get(url, headers={'User-Agent': user_agent})
        except Exception as e:
            print("Whoops! Something went wrong here. \
                    The error code is " + str(e))
            return []

        if response.status_code != requests.codes.ok:
            print("HTTP RESPONSE FAILED: " + str(response.status_code))
            print(response.content)
            return []

        results = json.loads(response.content)
        num_news = results['totalResults']

        for news_item in results['articles']:
            # Format date
            news_item['publishedAt'] = self._format_date(news_item['publishedAt'])
            news_item['content'] = self.__clean_data(news_item['content'])
            news.append(news_item)

        print('News retrieved: ', len(news))
        return news

    def _format_title(self, title: str) -> str:
        """
        Write title in the proper format
        
        Arguments:
            title (:obj:`str`) -- title to be formatted

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
        """
        Write date in the proper format
        
        Arguments:
            date_hour (:obj:`str`) -- date to be formatted

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

    def __clean_data(self, text: str) -> str:
        """
        Processes data and cleans it as entry for the vectorizer
        
        Arguments:
            text (:obj:`str`) -- text preprocessed 
        
        Returns:
            (:obj:`str`) -- cleaned and postprocessed text
        """
        if text is not None:
            # Remove punctuation
            text_processed = re.sub('[\(\[].*?[\)\]]', '', text)

            # Convert the titles to lowercase
            text_processed = text_processed.lower()
        else:
            text_processed = ''

        return text_processed
