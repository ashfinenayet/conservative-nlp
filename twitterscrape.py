import twint
import pandas

pundits = ["benshapiro", "MattWalshBlog", "RealCandaceO", "RubinReport"]

def scrape_by_pundit(conservative):
    config = twint.Config()
    config.Username = conservative
    
    config.Limit = 1000#running search
       
    config.Store_csv = True
    config.Output = f'{conservative}.csv'
    print(conservative)


    twint.run.Search(config)

for conservatives in pundits:
    scrape_by_pundit(conservatives)