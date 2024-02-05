from transformers import T5ForConditionalGeneration, T5Tokenizer

def generate_explanation(answer, context, question):
    model_name = "t5-small"  # Choose the T5 variant here
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Prepare input text in T5 format
    input_text = f"answer: {answer} context: {context} question: {question}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate explanation using the model
    output = model.generate(input_ids, max_length=100, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode the generated explanation
    explanation = tokenizer.decode(output[0], skip_special_tokens=True)

    return explanation

# Example usage
context = "The Hubble Space Telescope has provided stunning images of distant galaxies and nebulae."
question = "What is the Hubble Space Telescope known for?"
answer = "providing stunning images of cosmos."

explanation = generate_explanation(answer, context, question)
print("Explanation:", explanation)
