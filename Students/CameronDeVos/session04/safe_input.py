

def safe_input(prompt):
    """Return None when response to prompt is EOFError or KeyboardInterrupt"""
    try:
        response = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return unicode(response)
