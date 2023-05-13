import os
from langchain.document_loaders import PyPDFLoader
from langchain.llms import Cohere
from langchain import PromptTemplate, LLMChain

COHERE_API_KEY = "o7QBUQ3Lvnn1yeIUdu3WuGuEP1lgGTwea9FsMx3b"

# loader = PyPDFLoader("./ZI_WEI_resume.pdf")
# pages = loader.load_and_split()

# resume = """This is a string that contains the resume. I need you to eliminate blank spaces between letters in a word so the string makes sense and is semantically correct.
# You will return the processed string. Resume: """

# for page in pages:
#     resume += page.page_content

template = """
Assistant will take in a raw text string as input, and output a grammatically and semantically correct version of the input text, with all unnecessary white space removed.

raw text string: {resume}
"""

prompt = PromptTemplate(
    input_variables=["resume"], 
    template=template
)
llm=Cohere(cohere_api_key=COHERE_API_KEY)
chain = LLMChain(llm=llm, prompt=prompt)
output = chain.predict(resume=resume)
print(output)