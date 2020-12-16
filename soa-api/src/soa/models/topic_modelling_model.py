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
NUM_WORDS = 10 # Number of words to extract from each topic

class TopicModellingExtraction:

    def __init__(self, num_topics: int = NUM_TOPICS):
        """
        Extracts topics from a text using LDA (Latent Diriechit Allocation) to get themes from main kewyords in multiple documents
        
        Keyword Arguments:
            num_topics (:obj:`int`, optional): number of topics to extract from text (default: {NUM_TOPICS})
        """
        # Create model component handler
        self._lda = LDA(n_components=num_topics)

        # Initialise the count vectorizer with the English stop words
        self._count_vectorizer = CountVectorizer(stop_words='english')

    def __clean_data(self, text: str) -> str:
        """
        Processes data and cleans it as entry for the vectorizer
        
        Arguments:
            text (:obj:`str`): text preprocessed 
        
        Returns:
            :obj:`str`: cleaned and postprocessed text
        """
        # Remove punctuation
        text_processed = re.sub('[,\.!?]', '', text)

        # Convert the titles to lowercase
        text_processed = text_processed.lower()

        return text_processed

    def __vectorize_data(self, text: str):
        """
        Transforms text into a vector of 0s and 1s as entry of the LDA model.
        
        Arguments:
            text (:obj:`str`): text cleaned and postprocessed
        """
        # Fit and transform the processed titles
        vec_data = self._count_vectorizer.fit_transform([text])

        return vec_data

    def get_topics(self, text: str, words_per_topic: int = NUM_WORDS) -> dict:
        """
        Returns the number of topics predicted in the text given.
        
        Arguments:
            text (:obj:`str`): text to get topics from
            words_per_topic (:obj:`int`, optional): number of words to extract per topic (default: {NUM_WORDS})

        Return:
            :obj:`dict`: structure containing the list of topics extracted from a text given
        """

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

    def __summary_topics(self, model, vectorizer, n_top_words: int) -> list:
        """
        Gets number of topics predicted and stores them into a list
        
        Arguments:
            model: pretrained LDA model
            vectorizer: pretrained Count Vectorizer vectorizer
            n_top_words (:obj:`int`, optional): number of words to analyze from each topic
        
        Returns:
            :obj:`list` of :obj:`str`: list of topics extracted
        """
        words = vectorizer.get_feature_names()
        list_topics = []
        for topic_idx, topic in enumerate(model.components_):
            topics_str = " ".join([words[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
            list_topics.extend(topics_str.split())

        return list_topics[:NUM_TOPICS]