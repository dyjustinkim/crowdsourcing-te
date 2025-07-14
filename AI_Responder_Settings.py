low_temp, med_temp, high_temp = 0.5, 1, 1.5
low_token_limit = "\nPlease limit EACH individual answer to a MAXIMUM of 100 tokens. "
med_token_limit = "\nPlease limit EACH individual answer to a MAXIMUM of 200 tokens. "
model_nano = "gpt-4.1-nano"
model_mini = "gpt-4.1-mini"
mturk_autism_demographics = """In a demographic survey, 70% of MTurk workers indicated they had some experience with autism in their personal or professional life. 40% indicated they regularly interacted with someone with autism. 
When asked to self-rate their own knowledge about autism, 65% indicated they knew a little, 29% indicated they knew a lot, and 6% indicated they knew nothing. """
mturk_autism_assign = """
Reflecting real-life demographics, simulate the responses of 1 worker with high knowledge and experience with autism, 1 with some knowledge and high experience with autism,
2 with some knowledge and experience with autism, and 1 with low knowledge and experience with autism.
"""
medium_mturk_detail = """MTurk workers are people who have been remotely hired to answer numerous small-scale online tasks. In this experiment, workers were paid $0.2.
The average age of MTurk workers was 33.4 years and 51% were female. The majority of workers (76%) were from the US.
Each worker should answer independently and may show variability, uncertainty, or minor mistakes like real human annotators. """
high_mturk_detail = medium_mturk_detail + """Also, simulate the important fact that MTurk workers typically seek to complete many tasks to earn money, 
and thus will often provide shorter, direct answers to tasks.
If providing the solution to a problem, MTurk answers are also often practical, structured, and actionable.
Additionally, 50% 0f the time, MTurk workers will include excerpts from their own experience in their answer for support and reliability. """
example_answer = """
Try to replicate the style and content of the below example MTurk answer:

'I've been in your situation! I used to have terrible anxiety and when a place started getting too crowded, I couldn't wait to leave. 
I tackled it with school dances by taking a couple friends with me who understood my situation. That way, I was able to dance with my own friends, 
talk with them, and they helped me to feel secure. They could also walk outside with me if I needed a break and I didn't have to stand out there and be alone. 
Worst case scenario, I would text/call someone to come get me! You don't have to completely immerse yourself here you're not comfortable. Take baby steps.' 
"""


def ai_responder_settings(name, temp = 1, token_limit = med_token_limit, model = model_mini, 
                          autism_information = mturk_autism_demographics, mturk_detail = medium_mturk_detail, example = ""):
    settings = {
        "setting_name": name,
        "temp": temp,
        "token_limit": token_limit,
        "model": model,
        "additional_information": autism_information + mturk_detail + example
    }
    return settings

default_setting = ai_responder_settings(name="Default setting")
low_temp_setting = ai_responder_settings(name = "Low temperature setting", temp = low_temp)
high_temp_setting = ai_responder_settings(name = "High temperature setting", temp = high_temp)
low_token_limit_setting = ai_responder_settings(name = "Low token limit setting", token_limit=low_token_limit)
no_token_limit_setting = ai_responder_settings(name = "No token limit setting", token_limit="")
model_nano_setting = ai_responder_settings(name = "Model GPT-4.1-nano setting", model = model_nano)
no_detail_setting = ai_responder_settings(name = "No details setting", autism_information = "", mturk_detail = "")
high_detail_setting = ai_responder_settings(name = "High details setting", mturk_detail = high_mturk_detail)
autism_assign_setting = ai_responder_settings(name = "Autism expertise assignment setting", autism_information = mturk_autism_assign)
example_answer_setting = ai_responder_settings(name = "Example answer setting", example=example_answer)

responder_settings = [default_setting, low_temp_setting, high_temp_setting, low_token_limit_setting, no_token_limit_setting, 
                      model_nano_setting, no_detail_setting, high_detail_setting, autism_assign_setting, example_answer_setting]
