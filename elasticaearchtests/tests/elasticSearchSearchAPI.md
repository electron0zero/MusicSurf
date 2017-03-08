## ElasticSearch Search API:

-    POST /hello/helloworld/1
    {
    "user":"rajdeep",
    "type":"human"
    }
    POST /hello/helloworld/2
    {
    "user":"archan",
    "type":"human"
    }
    POST /hello/helloworld/3
    {
    "user":"mainak",
    "type":"human"
    }
    POST /hello/helloworld/4
    {
    "user":"watson",
    "type":"machine"
    }
    POST /hello/helloworld/5
    {
    "user":"greg",
    "type":"machine"
    }
    GET /hello/_search
    {
    "query":
    {
        "bool":
        {
        "should":[
            {
            "match":{
                "user":"archan and greg and mainak are nice humans"
            }
            },
            {
            "match":{
                "type":"archan and greg and mainak are nice humans"
            }
            }
            ]
        
        }
        
        }
    }
    }
