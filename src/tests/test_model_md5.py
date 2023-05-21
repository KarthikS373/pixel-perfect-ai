def test_load_model():
    from src.plugins import InteractiveSeg
    from src.model_manager import ModelManager

    interactive_seg_model = InteractiveSeg('vit_l', 'cpu')

    models = [
        "lama",
        "ldm",
        "zits",
        "mat",
        "fcf",
        "manga",
    ]
    for m in models:
        ModelManager(
            name=m,
            device="cpu",
            no_half=False,
            hf_access_token="",
            disable_nsfw=False,
            sd_cpu_textencoder=True,
            sd_run_local=True,
            local_files_only=True,
            cpu_offload=True,
            enable_xformers=False,
        )

