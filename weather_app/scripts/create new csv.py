def translate(string):
    from deep_translator import GoogleTranslator

    return GoogleTranslator(source='en', target='ru').translate(string)


# def get_city(city):
#     import requests
#     appid = '485c72e0e02b8ec897e58e082634c89d'
#
#     url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid=' + appid
#     try:
#         return requests.get(url.format(city)).json()[0]['local_names']['ru']
#     except:
#         from deep_translator import GoogleTranslator
#
#         return GoogleTranslator(source='en', target='ru').translate(city)


if __name__ == '__main__':
    import pandas as pd

    # from tqdm import tqdm
    #
    # from pandarallel import pandarallel

    # tqdm.pandas()
    # pandarallel.initialize(progress_bar=True)

    df = pd.read_csv('../owm_city_list.csv', sep=',', low_memory=False)
    df = df.drop(columns=[
        'owm_city_id',
        # 'owm_city_name',
        'owm_latitude',
        'owm_longitude',
        'owm_country',
        'locality_short',
        'locality_long',
        'admin_level_1_short',
        'admin_level_1_long',
        'admin_level_2_short',
        'admin_level_2_long',
        'admin_level_3_short',
        'admin_level_3_long',
        'admin_level_4_short',
        'admin_level_4_long',
        'admin_level_5_short',
        'admin_level_5_long',
        # 'country_short',
        # 'country_long',
        'postal_code'])

    df.rename(columns={'owm_city_name': 'city',
                       'country_long': 'country'}, inplace=True)
    # df['city'] = df['city'].parallel_apply(get_city)

    # df = df.drop(columns=['city_ascii'])
    df.to_excel('../all_cities.xlsx', index=False)
    df.to_csv('../all_cities.csv', index=False, encoding='utf-8')
