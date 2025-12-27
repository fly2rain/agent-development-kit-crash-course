from litellm import completion

response = completion(
    model="ollama/llama3.2:latest",
    messages=[{"role": "user", "content": "what is the climat in Plano TX"}],
    api_base="http://localhost:11434",
    stream=True,
)

for chunk in response:
    if "choices" in chunk:
        delta = chunk["choices"][0].get("delta", {})
        if "content" in delta:
            print(delta["content"], end="", flush=True)