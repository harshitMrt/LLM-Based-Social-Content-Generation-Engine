from llm_helper import llm
from few_shots import FewShotsPost

few_shots = FewShotsPost()

def get_length_str(length):

    if length == "Short":
        return "1 to 5 Lines"
    if length == "Medium":
        return "5 to 10 Lines"
    if length == "Long":
        return "11 to 15 Lines"

def get_prompt(topic, length, language):

    length_str = get_length_str(length)

    prompt = f'''
        Generate a post for LinkedIn using the info given below. no preamble

        1. Topic : {topic}
        2. Length : {length}
        3. Language : {language}
        If language is Hinglish that means it a mix of hindi and english language
        The script for the generated post should always be in english 
        '''

    example = few_shots.get_filtered_posts(topic, length, language)

    if (len(example) > 0):
        prompt += "4. Use the writing style as per the following Examples."
        for i, post in enumerate(example):
            post_text = post['text']
            prompt += f"\n\n Example{i}\n\n {post_text}"

            if i == 1:
                break;

    return prompt


def generate_post(topic, length, language):

    prompt = get_prompt(topic, length, language)

    res= llm.invoke(prompt)
    return res.content

if __name__ == "__main__":
    post = generate_post("Mental Health" , "Medium" , "Hinglish")
    print(post)