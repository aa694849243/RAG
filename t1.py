from langchain.embeddings import HuggingFaceBgeEmbeddings
# model_name = "moka-ai/m3e-base"
# model_kwargs = {'device': 'cuda'}
# encode_kwargs = {'normalize_embeddings': True} # set True to compute cosine similarity
# cache_folder='models/m3'
# model = HuggingFaceBgeEmbeddings(
#     model_name=model_name,
#     model_kwargs=model_kwargs,
#     encode_kwargs=encode_kwargs,
#     query_instruction="为这个句子生成表示以用于检索相关文章：",
#     cache_folder=cache_folder
# )
# model.query_instruction = "为这个句子生成表示以用于检索相关文章："
from transformers import AutoTokenizer, AutoModel,AutoConfig
cache_dir='models/chat'
model_config = AutoConfig.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True,cache_dir=cache_dir)
model_config.save_pretrained(cache_dir+'config')
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True,cache_dir=cache_dir)
# model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True,cache_dir=cache_dir).half().cuda()
# tokenizer.save_pretrained(cache_dir+'token')
# model.save_pretrained(cache_dir)
# from pathlib import Path


# cache_dir = Path('models/chat')
# # model_path = cache_dir + '/THUDM/chatglm3-6b'

# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True,cache_dir=cache_dir)
# model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True,local_files_only=True,catch_dir=cache_dir).half().cuda()
...