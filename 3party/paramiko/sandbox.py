def get_sandbox_host():
    if hostname := os.getenv("SSH_SANDBOX_HOST"):
        return hostname
    raise ValueError("Please set SSH_SANDBOX_HOST env var")
