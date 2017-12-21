# openAIGym
This folder holds different approaches to some OpenAI environments to primarily introduce me to reinforcement and deep learning algorithm design. The `cart_tensorflow.py` program borrows heavily from a tutorial series by [sentdex on YouTube.](https://www.youtube.com/user/sentdex) In the future I hope to experiment with using recurrent neural nets as effective reinforcement learning models. 

# General ML
Folder containing general ML stuff- like EDA's or model comparisons on various datasets. 

### Framingham Heart Study feature extraction/engineering
My final project for a data science class at school- This primarily compares accuracy of SVM and Random Forest on the dataset in R. Also, some data imputation and feature extraction with Random Forest is explored using MICE and randomForest. The models ended up being nothing too special, with ~80% cross-validated accuracies. 

## Deep Learning

### RNN Time Series Modeling 
A notebook that runs setting up a RNN with LSTM units with Keras to model and forecast time series data. For now, this is just for a single-variable time series. Play around with factors like look-back, structure of the model, and forecast periods. 

### Bus Ticket EDA
A work-in-progress EDA notebook on the patterns of daily bus ticket colors. Bus Tickets are from a local service that utilizes online tickets and a unique set of colors to display the ticket. I fear that the data I've collected over a 1-month period, which is basically about 28 daily bus tickets, is not sufficient for a training procedure using either CNNs or RNNs to try to predict tomorrow's bus ticket colors. 

### SimpleFNN
Small feed-forward neural net implementations using just `numpy`. Just my demos of [Andrew Trask's tutorial.](https://iamtrask.github.io/) 
