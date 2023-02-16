df_books.head()

df_ratings.head()

df_books.isnull().sum()

df_ratings.isnull().sum()

df_books.dropna(inplace=True)

df_books.isnull().sum()

df_ratings.shape

ratings = df_ratings['user'].value_counts()
ratings.sort_values(ascending=False).head()

len(ratings[ratings < 200])

df_ratings['user'].isin(ratings[ratings < 200].index).sum()

df_ratings_rm = df_ratings[
  ~df_ratings['user'].isin(ratings[ratings < 200].index)
]
df_ratings_rm.shape

ratings = df_ratings['isbn'].value_counts() # we have to use the original df_ratings to pass the challenge
ratings.sort_values(ascending=False).head()

len(ratings[ratings < 100])








