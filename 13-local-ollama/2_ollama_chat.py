import time
import ollama



def test_model(model_name: str='gemma3:1b'):
    response = ollama.chat(model=model_name, messages=[
        {'role': 'user', 'content': 'Explain what is KV cache in LLMs.'}
    ], options={
        'temperature': 0.7,
        'num_predict': 200,
        'top_p': 0.9
    })

    print("*" * 100)
    print(model_name)        
    print(response['message']['content'])


if __name__ == "__main__":
    start_time = time.time()
    model_name = 'gemma3:1b'
    test_model(model_name)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    # model_name = 'gpt-oss:20b'
    # test_model(model_name) 