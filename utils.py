import os
import torch
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from accelerate import init_empty_weights, dispatch_model

def load_model():
    # Use empty weights for offloading if needed
    with init_empty_weights():
        model = Qwen2VLForConditionalGeneration.from_pretrained(
            "Qwen/Qwen2-VL-2B-Instruct",
            torch_dtype="auto",
            device_map="auto"  # Set device map to automatically allocate resources
        )

    # Tie weights if necessary
    model.tie_weights()

    # Initialize the processor
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

    # Use disk offload for the model
    model = dispatch_model(model, device_map='disk_offload')

    return model, processor

def extract_text_from_image(image_url, model, processor):
    # Prepare messages with an image
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_url,
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ]

    # Preparation for inference
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)  # Make sure this function is defined

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )

    # Move inputs to the correct device
    inputs = inputs.to("cuda" if torch.cuda.is_available() else "cpu")

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [
        out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]

    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )

    return output_text
