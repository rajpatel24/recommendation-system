import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import TruncatedSVD
# %matplotlib inline
plt.style.use("ggplot")


def recommended_product_based_on_history(last_purchase_id):
    amazon_ratings = pd.read_csv('crud/amazon.csv')
    amazon_ratings = amazon_ratings.dropna()

    amazon_ratings1 = amazon_ratings.head(10000)
    # Remove rows with invalid values
    amazon_ratings1 = amazon_ratings1[~amazon_ratings1['rating'].str.contains('\|')]

    # Convert the 'rating' column to float
    amazon_ratings1['rating'] = amazon_ratings1['rating'].astype(float)

    ratings_utility_matrix = amazon_ratings1.pivot_table(values='rating', index='user_id', columns='product_id', fill_value=0)
    X = ratings_utility_matrix.T
    X1 = X
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)
    # i = 'B0073QGKAS'
    i = last_purchase_id
    print("index ->>", i)
    product_names = list(X.index)
    product_ID = product_names.index(i)
    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.90])
    Recommend.remove(i)
    print(Recommend[0:5])
    return Recommend[0:5]
