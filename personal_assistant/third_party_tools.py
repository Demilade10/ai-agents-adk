import wikipediaapi

def get_wikipedia_summary(query: str) -> str:
    """
    Provides historical, cultural, and background information about a landmark, city, or concept.

    Args:
        query: The topic or landmark to look up on Wikipedia (e.g., "Kyoto", "Eiffel Tower").

    Returns:
        A text summary from Wikipedia, or an error message if not found.
    """
    wiki = wikipediaapi.Wikipedia(
        user_agent="PersonalAssistantAgent/1.0 (contact@example.com)",
        language="en"
    )
    
    page = wiki.page(query)
    
    if page.exists():
        return page.summary[:3000]
    
    # If exact page isn't found, try stripping extra keywords
    main_topic = query.replace("history", "").replace("culture", "").strip()
    page_retry = wiki.page(main_topic)
    
    if page_retry.exists():
        return page_retry.summary[:3000]
        
    return f"No detailed Wikipedia article found for '{query}'."