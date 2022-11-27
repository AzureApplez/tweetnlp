# basic loader
from .loader import load_model, load_dataset
# model class
from .text_classification.model import Classifier, Sentiment, Offensive, Emoji, Emotion, Irony, Hate,\
    TopicClassification, StanceAtheism, StanceAbortion, StanceClimate, StanceHillary, StanceFeminist
from .ner.model import NER

# dataset class
from .text_classification.dataset import load_dataset_text_classification
