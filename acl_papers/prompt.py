system_prompt = """
You are given the abstract of a scientific paper. Your goal is to determine whether the paper is relevant to the following NLP tasks for a PhD proposal idea, and to tag the specific NLP tasks it pertains to if it is relevant. The possible NLP tasks are:

1. Scientific Named Entity and Relation Extraction
2. Knowledge Graph Construction and Development
3. Scientific Argument Mining
4. Citation Context Analysis
5. Topic Modeling and Clustering
6. Text Summarization
7. Semantic Similarity and Document Matching
8. Trend Analysis in Research
9. Research Question Generation and Analysis
10. Claim Detection and Verification

Instructions: For each abstract provided, perform the following:

1. Relevance: Determine if the paper is "Relevant" or "Irrelevant" to the NLP tasks listed above.
2. Tagging: If the paper is relevant, tag all applicable NLP tasks from the list above.

Output Format: Return the relevance followed by the relevant NLP tasks as a list. The output formant must be as indicated below.

Example Output:
- ["Relevant", "Knowledge Graph Construction, Scientific Named Entity and Relation Extraction"]
- ["Irrelevant", "None"]
"""