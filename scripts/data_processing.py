from data_processing import extract_data, transform_data, load_data




#  variables MongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27018


# Configuration pour Station 1
DATABASE_STATION1 = 'data_station1'
COLLECTION_STATION1 = 'station1'
STATION1_URL = 'https://airqino-api.magentalab.it/v3/getStationHourlyAvg/90'

# Configuration pour Station 2
DATABASE_STATION2 = 'data_station2'
COLLECTION_STATION2 = 'station2'
STATION2_URL = 'https://airqino-api.magentalab.it/v3/getStationHourlyAvg/12908'


# STATION 1
print("################### DEBUT DE LA STATION 1 ########################")

    d = extract_data(STATION1_URL)
    data_f = transform_data(d)
    load_data(data_f, MONGO_HOST, MONGO_PORT, DATABASE_STATION1, COLLECTION_STATION1)
    st.success("Opération réussie pour la Station 1")

# STATION 2
print("################### DEBUT DE LA STATION 2 ########################")

    d = extract_data(STATION2_URL)
    data_f = transform_data(d)
    load_data(data_f, MONGO_HOST, MONGO_PORT, DATABASE_STATION2, COLLECTION_STATION2)
print("#################### FIN #######################")
