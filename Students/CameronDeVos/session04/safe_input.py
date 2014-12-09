

def safe_input(prompt):
    try:
        response = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return unicode(response)
