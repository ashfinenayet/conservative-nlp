import twint
import pandas
import nest_asyncio
nest_asyncio.apply()

config = twint.Config()
config.Username = "MattWalshBlog"
config.Limit = 20#running search
config.Format = "Tweet id: {id} | Username: {username} | Date: {date} | Time: {time} | Tweet: {tweet}"


twint.run.Search(config)