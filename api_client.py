from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()
api.competition_download_files("walmart-recruiting-store-sales-forecasting", path="./data")