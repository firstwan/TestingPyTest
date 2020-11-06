class Config:
    base_url = ""
    app_port = 8080

    def __init__(self, env):
        SUPPORTED_ENVS = ["dev", "staging"]

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f"{env} is not a correct environment (Example environment: {SUPPORTED_ENVS})")

        self.base_url = {
            "dev": "api_url",
            "staging": "api_url"
        }[env]
        
        self.app_port = {
            "dev": 8080,
            "staging": 80
        }[env]