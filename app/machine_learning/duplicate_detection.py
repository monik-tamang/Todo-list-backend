import math


# process the data as required
def preprocessing_data(text):

    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace("_", " ")

    punctuation = '''!()[]{};:'"\,<>./?@#$%^&*~'''
    clean_text = ''

    for char in text:
        if char not in punctuation:
            clean_text += char
            
    words = clean_text.split()

    stopwords = [
        "the", "a", "an", "in", "on", "at", "of", "for", "to", "and", "up", "with", "from"
    ]

    filtered_words = []
    for word in words:
        if word not in stopwords:
            filtered_words.append(word)

    stemmed_words = []
    for word in filtered_words:
        if word.endswith("ing") and len(word) > 4:
            word = word[:-3]
        elif word.endswith('ied'):
            word[:-3] + 'y'
        elif word.endswith("ed") and len(word) > 3:
            word = word[:-2]
        elif word.endswith("s") and len(word) > 3:
            word = word[:-1]
        stemmed_words.append(word)

    return ' '.join(stemmed_words)


# convert text to vector form
def task_to_vector(task, vocab):
    words = task.split()
    return [words.count(word) for word in vocab]


# cosine_similarity
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    magnitide1 = math.sqrt(sum(a*a for a in vec1))
    magnitide2 = math.sqrt(sum(b*b for b in vec2))

    if magnitide1 == 0 or magnitide2 == 0:
        return  0.0
    
    return dot_product/ (magnitide1 * magnitide2)


# check duplicate or not
def is_duplicate(new_task: str, tasks: list[str], threshold: float = 0.8):
    processed_tasks = [preprocessing_data(task) for task in tasks]
    processed_new_task = preprocessing_data(new_task)

    vocab = sorted(set(" ". join(processed_tasks + [processed_new_task]).split()))

    tasks_vector = [task_to_vector(task, vocab) for task in processed_tasks]
    new_task_vector = task_to_vector(processed_new_task, vocab)

    similaritites = [cosine_similarity(new_task_vector, task_vector) for task_vector in tasks_vector]

    if any(sim >= threshold for sim in similaritites):
        max_index = similaritites.index(max(similaritites))
        return True, tasks[max_index]

    return False, None