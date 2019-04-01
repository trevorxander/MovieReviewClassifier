import re
punct_space = re.compile('[^a-zA-Z ] ')
space_punct = re.compile(' [^a-zA-Z ]')
punct = re.compile('[^a-zA-Z ]')

def remove_non_alpha(text):
    processed = text
    processed = re.sub(punct_space, ' ', processed)
    processed = re.sub(space_punct, ' ', processed)
    processed = re.sub(punct, '', processed)
    return processed
