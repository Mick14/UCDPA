#real world data
#import daftlistings

import pandas as pd
#import seaborn as sns
#from daftlistings import *


file = pd.read_csv(r"C:\Users\Mick\Downloads\daft_ie_v1.csv")
print(file.head())







# daft = Daft()
# listings = daft.search(max_pages=1)
#
# #Write - will create a file if the specified file does not exist
# file = open("search.txt", "w")
# file.writelines(listings)

    #fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

#for listing in listings:
    # print(listing.title)
    # print(listing.price)
    # print(listing.daft_link)


#daft.set_location(Location.DUBLIN)
#daft.set_search_type(SearchType.RESIDENTIAL_RENT)
#daft.set_property_type(PropertyType.APARTMENT)