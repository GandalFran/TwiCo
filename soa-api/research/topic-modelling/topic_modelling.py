#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto) and Francisco Pinto-Santos (@gandalfran)
# See LICENSE for details.

import re
import numpy as np

# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA
from typing import List, Dict, Any

NUM_TOPICS = 5 # Number of topics to extract from text
NUM_WORDS = 10

class TopicModellingExtraction:

    def __init__(self, num_topics: int = NUM_TOPICS):

        # Create model component handler
        self._lda = LDA(n_components=num_topics)

        # Initialise the count vectorizer with the English stop words
        self._count_vectorizer = CountVectorizer(stop_words='english')

    def __clean_data(self, text: str):

        # Remove punctuation
        text_processed = re.sub('[,\.!?]', '', text)

        # Convert the titles to lowercase
        text_processed = text_processed.lower()

        return text_processed

    def __vectorize_data(self, text: str):

        # Fit and transform the processed titles
        vec_data = self._count_vectorizer.fit_transform([text])

        return vec_data

    def get_topics(self, text: str, words_per_topic: int = NUM_WORDS):

        # 1. Clean data
        text_processed = self.__clean_data(text)

        # 2. Text transformation with BOW (bag of words) into vector representation
        #    as the format that will serve as input for training LDA model
        vectorized_data = self.__vectorize_data(text_processed)

        # 3. Model training
        # Create and fit the LDA model
        self._lda.fit(vectorized_data)

        # 4. Print topics
        topics = self.__summary_topics(model=self._lda, 
                                       vectorizer=self._count_vectorizer, 
                                       n_top_words=words_per_topic)

        return {'topics': topics}

    def __summary_topics(self, model, vectorizer, n_top_words):
        words = vectorizer.get_feature_names()
        list_topics = []
        for topic_idx, topic in enumerate(model.components_):
            print("\nTopic #%d:" % topic_idx)
            topics_str = " ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
            list_topics.extend(topics_str.split())

        return list_topics

if __name__ == '__main__':
    tme = TopicModellingExtraction(num_topics=1)
    results = tme.get_topics(text='a rapid coronavirus test at the heart of boris johnson’s mass-testing strategy missed more than 50% of positive cases in an operation moonshot pilot in greater manchester the guardian can revealthe 20-minute tests on which the government has spent £323m for use with hospital and care home staff with no symptoms identified only 467% of infections during a crucial trial in manchester and salford last monththis means that many of those carrying covid-19 were wrongly told they were free of the virus potentially allowing them to infect otherscovid testing: does operation moonshot have a shot at successthe tests were due to be used in the uk’s first city-wide mass-testing initiative which starts in liverpool on friday there was confusion on thursday night when the council suggested they would no longer be deployed as part of the trial but the government later insisted that small numbers of nhs staff would be using them in hospitalsadvertisementscientists with greater manchester’s mass testing expert group (mteg) raised significant concerns about the accuracy of the optigene direct rt-lamp tests this week and said the technology should not be widely used as intended in hospitals or care homesthe findings pose significant questions about one of the main tests in the government’s mass-screening strategy which johnson heralded this week as the uk’s main route back to normality the prime minister told mps on monday that the government was “rolling out testing of all nhs staff as fast as we possibly can” and that it wanted to introduce rapid regular testing for hospitals care homes schools and universitiesthe salford trial was billed as the first step in the operation moonshot mass-testing scheme but was drastically scaled back after just six weeks in part due to concerns about the accuracy of the optigene test the guardian understandslocal leaders had asked the government for the clinical validity data behind the technology but it is understood this data has not been providedthe department of health and social care said the test had been validated in three other trials which differed from manchester’s findings however it has not made this data public')
    print(results)
