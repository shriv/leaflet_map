import pandas as pd

fixit_df = pd.read_csv('~/Documents/remutaka-ct-analysis/qgis-mapping/Trapline Repairs - Sheet1.tsv', sep='\t')

fixit_df.dtypes

fixit_df['trap_code'] = (fixit_df['Trap Number']
                          .astype(str)
                          .apply(lambda x : x.strip().upper())
                          .apply(lambda x : x.replace('0', 'O'))
                          .apply(lambda x : x.replace('#', '-')) )

fixit_df['date'] = pd.to_datetime(fixit_df['Date Reported'], errors='coerce')

loc_df = pd.read_csv('~/Documents/remutaka-ct-analysis/qgis-mapping/amalgamated_coordinates.csv', header=None)

loc_df.columns = ['trap_code', 'easting', 'northing', 'lon', 'lat']

loc_df.head()

joined_df = pd.merge(fixit_df, loc_df, how = 'left')
recent_df = joined_df.query('date > "2019-01-01"')

missing_trap_locs = (joined_df[joined_df['easting']
                    .isnull()]['Trap Number']
                    .drop_duplicates())

joined_df.to_csv('~/Documents/remutaka-ct-analysis/qgis-mapping/joined_data.csv')

recent_df.to_csv('~/Documents/remutaka-ct-analysis/qgis-mapping/joined_data_2019.csv')

fixit_df.shape
