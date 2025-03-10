    
import json
from abc import ABC
from typing import List
from pipeline.models.general import DataSource
import concurrent.futures


class BaseImporter(): 
    DATA_SOURCES: List[str] = []

    @classmethod
    def import_data_sources(cls):
        if len(cls.DATA_SOURCES) >= 1:
            with concurrent.futures.ThreadPoolExecutor(len(cls.DATA_SOURCES)) as executor:
                future_to_url = {executor.submit(cls._import_data_source, url): url for url in cls.DATA_SOURCES}
                for future in concurrent.futures.as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        data = future.result()
                    except Exception as exc:
                        print('%r generated an exception: %s' % (url, exc))
                    else:
                        print('Data was imported successfully!')    
    
        elif len(cls.DATA_SOURCES) == 1:
            cls._import_data_source(cls.DATA_SOURCES[0])
        else:
            raise ValueError("cls.DATA_SOURCES defined")

    @classmethod
    def _import_data_source(cls, filename):
        with open(filename) as f:
            data_sources = json.loads(f.read())
        for data_source in data_sources:
            dataset, created = DataSource.objects.update_or_create(name=data_source.pop("name"), defaults={**data_source})
            print("dataset", dataset)