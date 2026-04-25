def generate_hashtag(s):
    s = "".join(word.capitalize() for word in s.split())
    if not s or len(s) > 139:
        return False
    return f'#{s}'