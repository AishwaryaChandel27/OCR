import os
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from accelerate import init_empty_weights, dispatch_model

def load_model():
    # Use empty weights for offloading if needed
    with init_empty_weights():
        model = Qwen2VLForConditionalGeneration.from_pretrained(
            "Qwen/Qwen2-VL-2B-Instruct",
            torch_dtype="auto",  # Automatically determine the appropriate dtype
            device_map="auto"  # Set device map to automatically allocate resources
        )

    # Tie weights if necessary
    model.tie_weights()

    # Initialize the processor
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

    # Offload the model to disk instead of using dispatch_model directly
    model = dispatch_model(model, device_map='disk_offload')

    return model, processor
