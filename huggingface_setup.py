from huggingface_hub import HfApi

hub_api = HfApi()
hub_api.create_tag("youliangtan/so100_strawberry_grape", tag="_version_", repo_type="dataset")
