# NLP - Procesamiento de Lenguaje Natural

Este repositorio contiene todos los trabajos realizados durante el cursado de la materia NLP, dentro de la [Especializacion en IA de la UBA](http://laboratorios.fi.uba.ar/lse/especializacion.html) (Universidad Nacional de Buenos Aires). 

A continuación se detalla el contenido de estos trabajos:

## Desafío 1: Word2Vec
#### [desafio1-word2vec.ipynb](./desafio1-word2vec.ipynb) 
<a href="https://colab.research.google.com/drive/1vLbtUPeSVoLMpwWQwYMy-0iYdVh_gBmJ?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

El objetivo de este trabajo fue tener un primer acercamiento con algunos conceptos y herramientas de NLP. Se realizan vectorizaciones de documentos como OneHotEncoding o Vectores de fecuencia (TF-IDF). Luego, utilizando estos vectores, se calcula la similitud de docoumentos la a través de la [similitud coseno](https://es.wikipedia.org/wiki/Similitud_coseno).

## Desafío 2: Q&A Chatbot (DNN + Spacy)
#### [desafio2-bot_dnn_spacy_esp.ipynb](./desafio2-bot_dnn_spacy_esp.ipynb)
<a href="https://colab.research.google.com/drive/1v7OwH4Fdnz1ajUgEZyid0AL2NFEqQkuf?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>
En este trabajo se utilizaron redes neuronales densas (DNN) y la librería [spaCy](https://spacy.io/universe/project/spacy-stanza) para generar un Q&A Chatbot con respuestas predeterminadas. El ejercicio se plantea como un problema de clasificación multiclase en donde se toma un texto como entrada, y el modelo de DNN lo clasifica dentro de una categoría (ej. bienvenida, problemas, saludos, datos de contacto, etc.). Luego el bot devuelve una respuesta pre-programada dependiendo de la categoría seleccionada. Para el entrenamiento se utilizó un pequeño dataset que se encuentra incluido dentro del notebook (en la sección "3 - Diccionario de entrada"), y que emula la etención al cliente de un sistema para reservar turnos.

## Desafío 3: Embedding con Gesim
#### [desafio3-embedding_Gensim.ipynb](./desafio3-embedding_Gensim.ipynb)
<a href="https://colab.research.google.com/drive/1N8gW7jPi9aldviAtlKgLqLU70eSdKMjK?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

En este trabajo se generan embeddings de palabras basados un contexto específico, utilizando [Gensim](https://radimrehurek.com/gensim/). Como dataset, se utilizaron los libros de Harry Potter. Este dataset puede ser descargado a través de este [link](https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter).

## Desafío 4: Text Prediction
#### [desafio4-text_prediction.ipynb](./desafio4-text_prediction.ipynb)
<a href="https://colab.research.google.com/drive/1UZNSHtkd3H_PDCrFbYWlr8NLBa5eLjRr?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

El objetivo de este trabajo es utilizar documentos para crear embeddings de palabras utilizando la layer Embedding de Keras. Luego, se utilizan estos embeddings junto con layers LSTM para predeccir la próxima palabra de un texto ingresado como input. Se utilizó como dataset un conjunto de canciones de Ed Sheeran, que puede ser descargado a través de este [link](https://github.com/r1fad/edSheeran/tree/master/JSONs).

## Desafío 5: Sentiment analysis (Embeddings + LSTM)
#### [desafio5-clothing_ecommerce_reviews.ipynb](./desafio5-clothing_ecommerce_reviews.ipynb)
<a href="https://colab.research.google.com/drive/11eYzehM2idq30AvpFnDji3KVjYTAZWey?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

El objetivo de este trabajo es utilizar un dataset de críticas de compradores de ropa (eCommerce), para entreanr un modelo que sea capaz de determinar la evaluación del comprador (cuantas estrellas le asigna al producto) a través de su crítica. El dataset puede ser descargado en este [link](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews). En la arquitectura del modelo, se utilizaron Embeddings y celdas de tipo LSTM.

## Desafío 6: Q&A Chatbot (Embeddings + LSTM)
#### [desafio6-bot_qa.ipynb](./desafio6-bot_qa.ipynb)
<a href="https://colab.research.google.com/drive/1xqrxCWw0TikMjh6DFdiqAm-_jC491nlP?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" height=22.5></a>

En este trabajo se entrena un mini Q&A chatbot para responder preguntas de usuario en ingles. Para esto se utilizan datos disponibles de [Covai](https://convai.io/).
El dataset puede ser descargado en este [link](http://convai.io/data/). El modelo propuesto tiene una arquitectura tipo encoder-decoder utilizando Embeddings y celdas tipo LSTM. Para el entrenamiento, la arquitectura propuesta fue la siguiente:

Dado que en la inferencia se necesita en primer lugar que el encoder reciba toda la secuencia de entrada para generar el estado interno, se tiene que utilizar por separado el encoder y el decoder. Esto se muestra en las siguientes imagenes:

