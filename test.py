import twint
import pandas

pundits = ["benshapiro", "MattWalshBlog", "RealCandaceO", "RubinReport"]

t = twint.Config()
t.Search = "from:@MattWalshBlog"

t.Store_object = True
t.Store_csv = True
t.Output = 'matt.csv'
t.Limit = 1000 

twint.run.Search(t)

