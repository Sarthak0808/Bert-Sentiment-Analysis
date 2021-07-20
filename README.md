
# Sentiment Analysis Model

## Index
1. Overview
2. Jupyter Code Explaination
3. Integration Using Django within Pycharm
4. Result

## Overview:
Working on pre-trained BERT model to Analyse the Sentiments of the movie watchers based on their comments and phrases.

## Jupyter Code Explaination:
1. The data is fetched and read using the pandas library.
2. The unwanted columns are cleaned and removed.
3. Tokenisation is done over the Phrase column of the dataset in order to obtain input_ids and attention_mask.
    
    3.1 Max length of word is defined which is equal to the dataset length.
   
    3.2 If any phrase tends to be greater than the Max length it will truncate then and there.
    
    3.3 Else if any phrase tends to be shorted, padding with special Tokenisation will be done.
4. The Sentiment column works as the labels to the model which states five differnt emotions starting from negative to positive with neutral in the middle.
    
    4.1 Making tuples label file with sentiments and number samples.
5. Mapping the tuples together to make a whole datasets of tuples with batch size of your own choice.
6. Splitting the dataset into training and validation data set of 90:10 respectively.
7. Applying the model as per the requirements , compiling and fitting to find the best accuracy on GPU.
8. Save the model and can check by loading in same notebook to predict the sentimental output.


## Integration Using Django within Pycharm:
1. Create a Django-admin project and start the runserver.
2. Link the urls,templates and views files as per the need.
3. Create the neccesary html files and link them with url and views files.
4. Load the model and fetch the value from html tags to be predicted and displayd back on result html.


## Result:
As per the input the user will be getting an ouput ranging from 0 to 4:
* 0: negative
* 1: Average
* 2: neutral
* 3: Good
* 4: Positive 


