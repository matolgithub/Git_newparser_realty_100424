import cianparser
from pprint import pprint

# moscow_parser = cianparser.CianParser(location="Москва")
# data = moscow_parser.get_flats(deal_type="sale", rooms=(1, 2), with_saving_csv=True,
#                                additional_settings={"start_page": 1, "end_page": 2})
#
# pprint(data[:2])

kaluga_flat_parser = cianparser.CianParser(location="Калуга")
data = kaluga_flat_parser.get_flats(deal_type="sale", rooms=(1, 2, "studio"), with_saving_csv=True,
                                    additional_settings={"start_page": 1, "end_page": 2,
                                                         "sort_by": "creation_data_from_newer_to_older"})
pprint(data[:3])
