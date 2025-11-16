def FirstLayerDMM(query):
    """
    Decision Making Model - analyzes the query and returns appropriate actions.
    """
    query = query.lower()
    actions = []

    # Open/close applications
    if "open" in query:
        if "youtube" in query:
            actions.append("open youtube")
        elif "chrome" in query or "browser" in query:
            actions.append("open chrome")
        elif "camera" in query:
            actions.append("open camera")
        else:
            app_name = query.replace("open", "").strip()
            actions.append(f"open {app_name}")

    if "close" in query:
        app_name = query.replace("close", "").strip()
        actions.append(f"close {app_name}")

    # Play music/videos
    if "play" in query:
        if "youtube" in query:
            song = query.replace("play", "").replace("on youtube", "").strip()
            actions.append(f"play {song}")
        else:
            actions.append(f"play {query.replace('play', '').strip()}")

    # Search functionality
    if "search" in query or "google" in query or "find" in query:
        if "google" in query:
            search_term = query.replace("search", "").replace("google", "").replace("for", "").strip()
            actions.append(f"google search {search_term}")
        elif "youtube" in query:
            search_term = query.replace("search", "").replace("youtube", "").replace("for", "").strip()
            actions.append(f"youtube search {search_term}")
        else:
            search_term = query.replace("search", "").replace("for", "").strip()
            actions.append(f"search {search_term}")

    # Camera and photos
    if "camera" in query or "photo" in query or "picture" in query:
        if "take" in query or "click" in query:
            actions.append("take photo")
        else:
            actions.append("open camera")

    # Image generation
    if "generate" in query and "image" in query:
        prompt = query.replace("generate", "").replace("image", "").replace("of", "").strip()
        actions.append(f"generate image {prompt}")

    # General conversation
    if not actions:
        actions.append(f"general {query}")

    return actions
