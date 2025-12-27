import time
import ollama

def test_model(model_name: str='gemma3:1b', question: str = 'Introduce Walmart.'):
    response = ollama.chat(
        model_name,
        messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content':  question}
    ], options={
        'keep_alive': True
    })

    print(response['message']['content'])


if __name__ == "__main__":
    start_time = time.time()   
    model_name = 'gemma3:1b'
    question = 'Where is Plano TX.'
    test_model(model_name, question)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    # model_name = 'gpt-oss:20b'
    # test_model(model_name)
    # end_time = time.time()
    # print(f"Time taken: {end_time - start_time} seconds")