import time
import json
import requests

def test_model(model_name: str='gemma3:12b', question: str = 'Explain what is KV cache in LLMs.'):
    url = "http://192.168.0.6:11434/api/generate"
    data = {
        "model": model_name,
        "prompt": question
    }

    response = requests.post(url, json=data, stream=True)
    for line in response.iter_lines():
        if line:
            obj = json.loads(line.decode('utf-8'))
            if 'response' in obj:
                print(obj['response'], end='', flush=True)


if __name__ == "__main__":  
    start_time = time.time()
    model_name = 'gemma3:12b'
    test_model(model_name)
    end_time = time.time()
    print("-" * 40)
    print(f"\n\n Time taken: {end_time - start_time} seconds")