import datetime
from langchain_core.tools import tool

@tool
def get_current_date() -> str:
    """
    Gets today's date.
    """
    today = datetime.date.today()
    return today.strftime('%Y/%m/%d')
