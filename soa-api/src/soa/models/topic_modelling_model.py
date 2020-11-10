#!flask/bin/python

# Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
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
