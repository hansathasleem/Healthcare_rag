from app.config import CHUNK_SIZE, CHUNK_OVERLAP
def overlapchunking(data,chunkingsize,overlap):
    chunked = []

    for i in range(0,len(data),chunkingsize-overlap):
        text = " ".join(data[i:i+chunkingsize])
        chunked.append(text)
    return chunked

