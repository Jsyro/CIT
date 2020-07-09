from pipeline.models import (
    Court,
    Hospital,
    EconomicProject,
    NaturalResourceProject,
    ServiceBCLocation,
    School,
    Clinic,
    Community,
    FirstResponder
)


CSV_RESOURCES = {
    'communities': {
        'csv_path': 'data/COMMUNITIES_V2.csv',
        'model': Community,
    },
    'first_responders': {
        'csv_path': 'data/FRST_RSPND.csv',
        'model': FirstResponder,
    }
}


DATABC_RESOURCES = {
    'hospitals': {
        'resource_id': '5ff82cf4-0448-4063-804a-7321f0f2b4c6',
        'model': Hospital,
    },
    'natural_resource_projects': {
        'resource_id': '2b69cc4b-4076-4272-a5a0-1c731455e063',
        'model': NaturalResourceProject
    },
    'economic_projects': {
        'resource_id': 'b12cd4cc-b58b-4079-b630-a20b6df58e8d',
        'model': EconomicProject,
    },
    'servicebc_locations': {
        'resource_id': 'c7cc9297-220c-4d6c-a9a7-72d0680b2f74',
        'model': ServiceBCLocation
    },
    'schools': {
        'resource_id': '5832eff2-3380-435e-911b-5ada41c1d30b',
        'model': School,
    },
    'clinics': {
        'resource_id': '3ca6b086-c92b-4654-ae82-ff5723d00611',
        'model': Clinic
    },
    'courts': {
        'resource_id': '23aa0b75-2715-4ccb-9a36-9a608450dc2d',
        'model': Court
    }
}
