# system_prompt = """
# You are given the abstract of a scientific paper. Your goal is to determine whether the paper is relevant to the following NLP tasks for a PhD proposal idea, and to tag the specific NLP tasks it pertains to if it is relevant. The possible NLP tasks are:

# 1. Scientific Named Entity and Relation Extraction
# 2. Knowledge Graph Construction and Development
# 3. Scientific Argument Mining
# 4. Citation Context Analysis
# 5. Topic Modeling and Clustering
# 6. Trend Analysis in Research
# 7. Research Question Generation and Analysis
# 8. Claim Detection and Verification

# Instructions: For each abstract provided, perform the following:

# 1. Relevance: Determine if the paper is "Relevant" or "Irrelevant" to the NLP tasks listed above.
# 2. Tagging: If the paper is relevant, tag all applicable NLP tasks from the list above.

# Output Format: Return the relevance followed by the relevant NLP tasks as a list. The output formant must be as indicated below.

# Example Output:
# - ["Relevant", "Knowledge Graph Construction, Scientific Named Entity and Relation Extraction"]
# - ["Irrelevant", "None"]
# """


system_prompt = """
I have an academic paper in the NLP domain. Given the title and abstract of this paper, I need to determine its relevance to my research and classify it accordingly. My research focuses on knowledge base-to-text generation. Specifically, I want to know:
- If the paper is relevant or irrelevant to knowledge base-to-text generation.
- If relevant, classify it into one or more of the following categories:
    1. Table-to-text generation
    2. Knowledge graph-to-text generation
    3. Other types of database-to-text generation (if applicable)

Output Format: The expected response format is json format, the relevance status as true or false followed by the relevant class(es) as a list. The output format must be as indicated below.

Examples of Expected Output Formats:
 {'status':true, 'class':'Knowledge graph-to-text generation'}
 {'status':true, 'class':'database-to-text generation'} 
 {'status':true, 'class':'Table-to-text generation'}
 {'status':false, 'class':null}

Example Input:

Title: "A Comprehensive Survey on Database-to-Text Generation"
Abstract: "This paper surveys various techniques in the field of knowledge base-to-text generation, focusing on different data sources such as tables, knowledge graphs, and structured databases. We also explore applications in conversational AI and question answering systems."

Example Output:
 {'status':true, 'class':'Knowledge graph-to-text generation'}
"""