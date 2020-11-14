## metis_project_4
### NLP on biology paper abstracts

For this project I collected ~330,000 English-language abstracts from PubMed using NCBI's EUtilities API. The abstracts were linked to the Mesh term "Cell Physiological Processes" and the search terms "signaling" or "pathway", and the organism was restricted to human. 

## [*PubMed EUtilities*](https://github.com/Beth526/metis_project_4/blob/main/Eutilities_queries.py)

### Tools used:
- Spacy
- Gensim
- Scikit-learn
- SciSpacy

I used Spacy for document tokenization, with stop word removal and lemmitization. SciSpacy's en_ner_bionlp13cg_md for named entity linking and Spacy's entity chunking were both really helpful in this project. I ended up using only the tokens that SciSpacy tagged as "GENE OR GENE PRODUCT" for topic modeling, which included most gene and protein names, as well as many small molecules which was actually useful in this application. However, sometimes there are a lot of different names, abbreviations, and hypenation patterns for the same protein. SciSpacy does have an entity-linking tool, but that tool annotes all biology and medical terms, and it was too challenging at the time to extract only genes from that list. 

## [*NMF Topic Modeling Notebook*](https://github.com/Beth526/metis_project_4/blob/main/Proj_4.ipynb)

I tried topic modeling of the gene/gene product tokens with LSA, LDA and NMF, and NMF produced the best results in terms of interpretibility and recognizable topics. I found 25 latent topics, then used K-means clustering to find 30 clusters, this last step seperated out some closely related pathways like Wnt and Tgf-B. There was one large group, about 20k documents, that contained a lot of reactive oxygen species and aging-related genes. The figure below is a tSNE plot of the cluster centers, and the circle sizes represent the cluster sizes.
### NMF cluster tSNE
![NMF tSNE](https://github.com/Beth526/metis_project_4/blob/main/nmf_clusters.jpg)

## [*Word2Vec Model and Document Centroid Notebook*](https://github.com/Beth526/metis_project_4/blob/main/Project4_Word2Vec.ipynb)

Next, I tried making a small Word2Vec model from the abstract corpus. It was a CBOW model with a window size of 5 and a vector size of 30. This small model was only 25Mb in size but I think it had captured some really nice relationships between biological terms because the corpus was so specific. It is also available under Pickled Files.

![Receptor Ligand Pair Embeddings](https://github.com/Beth526/metis_project_4/blob/main/receptor_ligand_embeddings.jpg)

![Kinase Cascade Pair Embeddings](https://github.com/Beth526/metis_project_4/blob/main/kinase_embeddings.jpg)

I used word vectors to calculate a centroid for each document's gene/gene product tokens (normalized sum of the gene/gene product token word vectors). I clustered the document centroids with K-means, and it was able to capture many more nuanced but still recognizable pathways. Interestingly it also clustered out the junk documents that not abstracts but only author lists and instition locations, which I wasn't aware were in the corpus.
### Word2Vec Centroid tSNE
![Word2Vec Centroid tSNE](https://github.com/Beth526/metis_project_4/blob/main/w2v_cluster.jpg)

## [*Final PDF Presentation*](https://github.com/Beth526/metis_project_4/blob/main/Metis%20Project%204.pdf)
