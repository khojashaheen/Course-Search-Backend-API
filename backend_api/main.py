from fastapi import FastAPI
from fastapi.responses import JSONResponse
from elasticsearch import Elasticsearch

app= FastAPI()


es = Elasticsearch(hosts=[{"host":"elasticsearch", "port":9200}])


@app.get("/")
async def read_root():
    return {"message":"Hello, this is FastAPI app"}

@app.get("/search/{index}")
async def search_index(index: str, query:str):
    try:
        result = es.search(index=index, body={"query":{"match":{"article_content_first_4_graph":query}}})
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error":str(e)}, status_code=500)