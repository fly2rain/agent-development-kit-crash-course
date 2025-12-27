from ollama import Client

def test_model(
    model_name: str='gemma3:12b',
    question: str='Introduce Walmart.',
    host: str='http://192.168.0.6:11434'
):
    client = Client(host=host)
    response = client.chat(
        model=model_name,
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': question}
        ],
        options={'keep_alive': True}
    )
    print(response['message']['content'])


if __name__ == "__main__":
    test_model()
