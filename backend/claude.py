import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

def extract_date_range(user_query):
    """
    Takes a natural language query and returns a date range
    
    Args:
        user_query (str): e.g., "the reign of Queen Elizabeth II"
    
    Returns:
        tuple: (start_year, end_year) or (None, None) if extraction fails
    """
    
    # Initialize the client
    client = anthropic.Anthropic(
        api_key=os.getenv('ANTHROPIC_API_KEY')
    )
    
    # Craft a prompt that will get Claude to return just the dates
    prompt = f"""Given this historical period or event: "{user_query}"
    
    Please respond with ONLY the start and end years in this exact format:
    START: [year]
    END: [year]
    
    If the event is ongoing, use the current year (2025) as the end.
    If you cannot determine specific years, respond with:
    START: None
    END: None"""
    
    try:
        message = client.messages.create(
            model="claude-3-sonnet-20241022",  # Note: correct model name
            max_tokens=100,  # We only need a short response
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Parse the response
        response_text = message.content[0].text
        
        # Extract years from the response
        # This is a simple parser - you might need to make it more robust
        lines = response_text.strip().split('\n')
        start_year = None
        end_year = None
        
        for line in lines:
            if line.startswith('START:'):
                try:
                    start_year = int(line.replace('START:', '').strip())
                except:
                    pass
            elif line.startswith('END:'):
                try:
                    end_year = int(line.replace('END:', '').strip())
                except:
                    pass
        
        return start_year, end_year
        
    except Exception as e:
        print(f"Error calling Claude API: {e}")
        return None, None

# Test function (remove this when importing into server.py)
if __name__ == "__main__":
    # Test the function
    test_queries = [
        "the reign of Queen Elizabeth II",
        "World War 2",
        "the Roman Empire"
    ]
    
    for query in test_queries:
        start, end = extract_date_range(query)
        print(f"Query: {query}")
        print(f"Result: {start} - {end}\n")