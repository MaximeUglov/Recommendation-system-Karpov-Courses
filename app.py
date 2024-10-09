from typing import List
from fastapi import FastAPI
from schema import PostGet
import pandas as pd
from catboost import CatBoostClassifier

app = FastAPI()

conn_url = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

def load_features() -> pd.DataFrame: # функция для загрузки двух таблиц с фичами и таблицы с постами
    users = pd.read_sql("""SELECT * FROM maximeuglov_feature_user_lesson_22""", conn_url)# с фичами для пользователей
    posts = pd.read_sql("""SELECT * FROM maximeuglov_feature_post_lesson_22""", conn_url) # с фичами для постов
    post_text = pd.read_sql("""SELECT * FROM public.post_text_df""", conn_url) # первоначальная таблица с постами
    return users, posts, post_text

def load_viewed_posts(id): # функция для загрузки просмотренных пользователем постов из сервера
    viewed_posts = pd.read_sql(f"""SELECT post_id
                                         FROM public.feed_data
                                         WHERE user_id = {id} AND action = 'view'
                                """, conn_url)
    return viewed_posts

def get_recommended_posts(id: int, limit=5) -> List[PostGet]: # основная функция рекомендует посты по id пользователя
    user = users[users['user_id']==id].drop(['user_id'], axis=1) # берем фичи для одного пользователя по id
    viewed_posts = load_viewed_posts(id) # берем посты, которые пользователь уже смотрел
    unviewed_posts = posts[~post_id.isin(viewed_posts['post_id'])] # и убираем их из всех постов
    data = pd.merge(user, unviewed_posts, how='cross') # к фичам пользователя добавляем фичи несмотренных постов
    data['preds'] = model.predict_proba(data)[:, 1] # делаем предсказание на вероятность лайка
    data['post_id'] = post_id # возвращаем id постов
    list_rec = list(data.sort_values(by='preds', ascending=False).head(limit)['post_id']) # сортируем и берем самые вероятные
    return [PostGet(**{"id": i,
                       "text": post_text[post_text['post_id'] == i]['text'].values[0],
                       "topic": post_text[post_text['post_id'] == i]['topic'].values[0]
    }) for i in list_rec] # возвращаем по форме из первоначальной таблицы post_text

users, posts, post_text = load_features() # загружаем таблицы
post_id = posts['post_id'] # сохраняем id постов 
posts = posts.drop(['post_id'], axis=1) # и убираем их из фичей
model = CatBoostClassifier().load_model("catboost_model") # загружаем модель 

@app.get("/post/recommendations/{id}", response_model=List[PostGet]) 
def recommended_posts(id: int, limit=5) -> List[PostGet]:
    return get_recommended_posts(id, limit)
