# Deep learning, RNNs, and Time-series prediction
##### by Kenneth Li

A lot of us are familiar with the term 'deep learning' nowadays, especially since its recent explosion in industry popularity. Though the practice has yet to come under rigorous scrutiny in academia, companies are loving its far-reaching applications to a variety of problems. From image recognition and language processing, deep learning also has a future in the field of reinforcement learning. Problems in reinforcement learning are well-illustrated by the [OpenAIGym platform](https://gym.openai.com/). Reinforcement learning is centered on the idea of making optimal decisions in an environment, given state observations and rewards from previous actions. To better understand this relationship, we look into a type of deep learning model: Recurrent Neural Networks (RNNs). 

## RNNs: Just another neural net?

Neural networks are machine learning models structured after the neurons in our brains. Essentially, neural nets continually learn to define a mathematical function from a set of inputs and outputs. **Recurrent Neural Networks** build on this model by feeding neuron outputs as inputs in a sort of loop. This setup allows neurons to operate on past information like memory. 

RNNs have become particularly useful for natural language processing because of their ability to perceive context. For example, consider the sentence *"In France I loved to speak ___ ."* An ML model trained with some vocabulary could infer that the next word should be the name of a language. However, without the idea of context, the model doesn't consider the word *"French"* as a strong candidate for prediction. A more thorough introduction to RNNs can be found [here.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Additionally, a rather recent development in RNN architecture called LSTM, or *Long short-term memory*, allows RNNs to solve a breadth of problems that RNNs previously couldn't. In its basic form, the RNN can be subject to 'vanishing' or 'exploding' gradients during training and backpropagation due to its nature of feeding inputs recurrently. LSTM units allow information to be properly interpreted across layers. More detail about this property can be found [here](https://deeplearning4j.org/lstm.html). 

## RNNs and Deep Learning in Finance

We're no strangers to quantitative prop shops and management funds like Two Sigma and Renaissance Technologies who've spearheaded innovative technologies into lucrative trades. Similar groups have been earning 30% annually are on track to leverage further applications in deep learning like [artificial intelligence](https://www.bloomberg.com/news/articles/2017-07-11/bored-traders-on-tinder-are-a-symptom-of-wall-street-revenue-dip). Neural networks are gaining the attention of investment management firms in their abilities to learn from financial data in capacities greater than basic analysis. 

Particularly, RNNs have potential to accurately forecast the financial landscape by understanding context in time series data. For example, our project at Bayesquare deals with natural gas futures and how they fluctuate with respect to a variety of factors like storage, exports, and weather. In [another financial application of RNNs](http://www.naun.org/main/NAUN/mcs/2017/a042002-041.pdf), researchers achieve about 65-70% accuracy in predicting the forward price of Google stock up to 10 days. This is fairly remarkable in how the model closely follows a stock price with just historical signals. 

**Deep learning** is enabling firms to find new alphas and relationships among variables that would otherwise need far more computational resources to understand. Moreover, as stated in the Google stock prediction paper, neural networks are "not black box learning models with non interpretable inner structure" after some analysis on hidden dynamics in such models. Of course, there are countless other models (*search for ARMA, GARCH, and also just SVM and KNN trading strategies*) that also try to forecast securities in trading and are often less complex in implementation. Nonetheless, RNNs show promise to combine the far-reaching abilities of human-based learning and contextual understanding. 


### Cool links to check out
* LSTM introduction: https://colah.github.io/posts/2015-08-Understanding-LSTMs/ 
* RNN introduction: https://medium.com/@camrongodbout/recurrent-neural-networks-for-beginners-7aca4e933b82 
* Hedge funds and AI: https://www.bloomberg.com/news/articles/2017-03-27/hedge-fund-quants-close-in-on-designing-ultimate-trader-s-brain 
* Hedge funds and AI (more): https://www.wired.com/2016/01/the-rise-of-the-artificially-intelligent-hedge-fund/
* Machine learning and trading: https://link.springer.com/chapter/10.1007/978-3-642-36318-4_3 
* RNNs and Stock price predictions: http://www.naun.org/main/NAUN/mcs/2017/a042002-041.pdf 





