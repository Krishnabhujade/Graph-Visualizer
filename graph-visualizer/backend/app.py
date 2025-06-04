from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.graph_logic import bfs


app = FastAPI()

class Edge(BaseModel):
    source: str
    target: str

class GraphRequest(BaseModel):
    nodes: List[str]
    edges: List[Edge]
    start: str

@app.post("/bfs")
def bfs_endpoint(data: GraphRequest):
    order = bfs(data.nodes, [e.dict() for e in data.edges], data.start)
    return {"order": order}
