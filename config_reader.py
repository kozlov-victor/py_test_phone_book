
PICKLE_SERIALIZER_TYPE = 'pickle'
JSON_SERIALIZER_TYPE = 'json'
CSV_SERIALIZER_TYPE = 'csv'


def resolve_serializers():
    try:
        with open('config.conf', 'rt') as f:
            serializer_type = f.readline()
            if serializer_type == PICKLE_SERIALIZER_TYPE:
                import serializer.pickle_serializer as module
                return module.load, module.save
            elif serializer_type == JSON_SERIALIZER_TYPE:
                import serializer.json_serializer as module
                return module.load, module.save
            elif serializer_type == CSV_SERIALIZER_TYPE:
                import serializer.csv_serializer as module
                return module.load, module.save
            else:
                raise ValueError('wrong serializer type')
    except Exception as e:
        print('data base loading error: ', e)