import csv

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.core.exceptions import FieldDoesNotExist

from pipeline.models import (
    Community,
)


def import_data_into_model(resource_type, model_class, data):

    Model = model_class

    for row in data:
        print("row", row)
        try:
            point = Point(
                float(row[Model.LONGITUDE_FIELD]),
                float(row[Model.LATITUDE_FIELD]),
                srid=3005
            )
        except TypeError:
            print("Skipping error:", row[Model.NAME_FIELD], "has no geometry!")
            continue
        closest_community = Community.objects.annotate(
            distance=Distance('point', point)
        ).order_by('distance').first()

        # containing_subdiv = CensusSubdivision.objects.get(geom__contains=point)
        instance = Model.objects.get_or_create(
            name=row[Model.NAME_FIELD],
            point=point,
            location_type=resource_type,
            community=closest_community
        )[0]

        for field_name, field_value in row.items():
            # loop over fields, and if the field exists
            # on the model, import this field
            if isinstance(field_value, str):
                try:
                    field_value = field_value[:Model._meta.get_field(field_name.lower()).max_length]
                except FieldDoesNotExist:
                    pass
            setattr(instance, field_name.lower(), field_value)


def read_csv(csv_path):
    data = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print("data", reader)

        # for row in reader:
        #     print("here", row)

    return data
