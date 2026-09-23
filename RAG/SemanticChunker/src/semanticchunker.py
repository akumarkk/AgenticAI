import matplotlib.pyplot as plt
import numpy as np
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

# Sample Document
sample_text = """
Retrieval-Augmented Generation (RAG) optimizes LLM responses using external knowledge bases.
Traditional chunking methods split text based on character or token counts.
However, fixed-size chunking often cuts sentences in half or breaks semantic context.

Semantic chunking solves this by analyzing sentence embeddings.
It measures cosine distance between adjacent sentences and identifies topic shifts.
When the semantic distance exceeds a threshold, a new chunk boundary is created.

Machine learning models require clean, well-formatted training data.
Overfitting occurs when a model learns noise instead of actual patterns in data.
Regularization techniques like L1 and L2 help prevent overfitting during model training.

Neural networks consist of input, hidden, and output layers.
Backpropagation updates weights based on calculated loss values.
"""

# Initialize Local Ollama Embedding Model
# Replace model with "llama3.2" if you explicitly prefer it over nomic-embed-text
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# ------------------------------------------------------------------
# Experiment 1: Percentile Thresholding
# Splits where distance > 80th percentile threshold across the document.
# ------------------------------------------------------------------
percentile_chunker = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=80.0
)
percentile_docs = percentile_chunker.create_documents([sample_text])

print(f"=== Percentile (80th) Chunks: {len(percentile_docs)} ===")
for i, doc in enumerate(percentile_docs):
    print(f"--- Chunk {i+1} ---\n{doc.page_content.strip()}\n")

# ------------------------------------------------------------------
# Experiment 2: Standard Deviation Thresholding
# Splits when distance > (mean + 1.5 * std_dev).
# ------------------------------------------------------------------
std_chunker = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.5
)
std_docs = std_chunker.create_documents([sample_text])

print(f"=== Standard Deviation (1.5) Chunks: {len(std_docs)} ===")
for i, doc in enumerate(std_docs):
    print(f"--- Chunk {i+1} ---\n{doc.page_content.strip()}\n")

# ------------------------------------------------------------------
# Experiment 3: Interquartile Range (IQR) Thresholding
# Splits when distance > (Q3 + 1.5 * IQR).
# ------------------------------------------------------------------
iqr_chunker = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="interquartile",
    breakpoint_threshold_amount=1.5
)
iqr_docs = iqr_chunker.create_documents([sample_text])

print(f"=== Interquartile Range (1.5) Chunks: {len(iqr_docs)} ===")
for i, doc in enumerate(iqr_docs):
    print(f"--- Chunk {i+1} ---\n{doc.page_content.strip()}\n")