from mcp.server.fastmcp import FastMCP
from pydantic import Field
import json
from mcp.server.fastmcp.prompts import base
mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc
@mcp.tool(name="read_doc", description="Read the contents of a document.")
def read_document(doc_id:str=Field(description="The ID of the document to read"))->str:
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]

# TODO: Write a tool to edit a doc
@mcp.tool(name="edit_doc", description="Edit the contents of a document.")
def edit_document(doc_id:str=Field(description="The ID of the document to edit"),
                   old_value:str=Field(description="The current content of the document"), 
                   new_value:str=Field(description="The updated content of the document")):
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    docs[doc_id]=docs[doc_id].replace(old_value, new_value)

    
# TODO: Write a resource to return all doc id's
@mcp.resource("docs://documents",mime_type="application/json",name="list_docs", description="List all document IDs.")
def list_docs()->list[str]:
    return list(docs.keys())
# TODO: Write a resource to return the contents of a particular doc
@mcp.resource("docs://documents/{doc_id}",mime_type="text/plain",name="get_doc", description="Get the contents of a document by ID.")
def fetch_doc(doc_id:str=Field(description="The ID of the document to retrieve"))->str:
    if doc_id not in docs:
        raise ValueError(f"Document with ID '{doc_id}' not found.")
    return docs[doc_id]
# TODO: Write a prompt to rewrite a doc in markdown format
@mcp.prompt(name="format_to_markdown",description="Rewrite a document in markdown format.")
def format_to_markdown(doc_id:str=Field(description="The ID of the document to format"),)->list[base.Message]:
    prompt = f"""
    Your goal is to reformat a document to be written with markdown syntax.
    The id of the document you need to reformat is:
    <document id>
    {doc_id}
    </document id>
    Add in headers, bullet points, tables, etc as necessary. Feel free to add in extra formatting.
    Use the 'edit_document' tool to edit the document. After the document has been reformatted..."""
    return [base.UserMessage(prompt)]

# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
