## Рекомендательная система из курса по машинному обучению образовательной платформы Karpov Courses
        
### Задача

Даны три таблицы с данными: о постах, о пользователях, о действиях пользователей с постами.    
Необходимо разработать сервис с использованием FastAPI, который дает рекомендации из 5 постов для условного пользователя по id.    
Предполагается, что пользователь поставит лайк хотя бы одному из рекомендуемых постов.    
Модель машинного обучения, используемая сервисом, оценивается по метрике Hitrate@5 и должна пройти порог в  0.57.

### Решение

1. Из трех таблиц путем обработки признаков получил: две таблицы для работы сервиса и таблицу для обучения модели. Признак с текстом обработал отдельно с помощью предобученной модели bert.   
2. Для работы сервиса обучил модель catboost.    
3. Чтобы провести оценку по метрике Hitrate@5, написал алгоритм с учетом формулы, указанной в задании. Модель прошла необходимый порог.   
4. Создал сервис, который использует две таблицы с обработанными признаками и обученную модель.    
5. Работа сервиса проверил в программе Postman.   
Сервис работает, используя подходящую по качеству модель, поэтому задание можно считать выполненным.   
### Описание файлов

>__app.py__ - приложение с рекомендательным сервисом    
__bert_embeddings.pt__ - эмбеддинги обработанных текстов    
__catboost_model__ - обученная модель catboost    
__main.ipynb__ - описание признаков, их обработка, обучение модели и результат ее работы    
__requirements.txt__ - список используемых библиотек    
__schema.py__ - форма ответа сервиса    
__text_to_embeddings.ipynb__ - обработка текстов    

### Библиотеки

<div id="badges">
  <img src="https://img.shields.io/badge/pandas-black?style=for-the-badge&logo=pandas"/>
  <img src="https://img.shields.io/badge/numpy-black?style=for-the-badge&logo=numpy"/>
  <img src="https://img.shields.io/badge/sqlalchemy-black?style=for-the-badge&logo=sqlalchemy"/>
  <img src="https://img.shields.io/badge/sklearn-black?style=for-the-badge&logo=scikit-learn"/>
  <img src="https://img.shields.io/badge/pytorch-black?style=for-the-badge&logo=pytorch"/>
  <img src="https://img.shields.io/badge/catboost-black?style=for-the-badge&logo=catboost"/>
  <img src="https://img.shields.io/badge/fastapi-black?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/pydantic-black?style=for-the-badge&logo=pydantic"/>
  <img src="https://img.shields.io/badge/uvicorn-black?style=for-the-badge&logo=uvicorn"/>
</div>
