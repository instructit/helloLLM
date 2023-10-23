# LLM Playground

## Instructions

Create a virtual environment

```python
# Run the following in an empty directory to create a virtual environment
# On Windows
python -m venv venv
.\venv\Scripts\activate.ps1

# On Apple
python3 -m venv venv 
source venv/bin/activate
```

Run following command to install

```python
pip install openllm
```

```python
pip install -r requirements.txt
```

```python
# Uses pytorch for the backend
openllm start dolly-v2 --model-id databricks/dolly-v2-3b --backend pt
```
