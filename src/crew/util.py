def calculate_costs(crew_usage_metrics, model_input_price, model_output_price, unit_of_tokens):
    """
    Calculate the costs based on crew usage metrics and token pricing.

    Parameters:
    crew_usage_metrics (dict): A dictionary containing the usage metrics with the keys:
        - 'total_tokens': Total number of tokens used.
        - 'prompt_tokens': Number of tokens used for input prompts.
        - 'completion_tokens': Number of tokens used for completions.
        - 'successful_requests': Number of successful requests made.
    model_input_price (float): Cost per unit of input tokens.
    model_output_price (float): Cost per unit of output tokens.
    unit_of_tokens (int): The number of tokens per unit cost (e.g., per 1000 tokens).

    Returns:
    dict: A dictionary with the calculated costs:
        - 'total_cost': Total cost of the usage.
        - 'input_cost': Cost of the input tokens.
        - 'output_cost': Cost of the output tokens.
    """
    
    prompt_tokens = crew_usage_metrics.get('prompt_tokens')
    completion_tokens = crew_usage_metrics.get('completion_tokens')
    
    input_cost = (prompt_tokens / unit_of_tokens) * model_input_price
    output_cost = (completion_tokens / unit_of_tokens) * model_output_price
    total_cost = input_cost + output_cost
    
    return {
        'total_cost': total_cost,
        'input_cost': input_cost,
        'output_cost': output_cost
    }