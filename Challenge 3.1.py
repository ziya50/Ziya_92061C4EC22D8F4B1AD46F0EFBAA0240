def linear_search_product(product_list, target_product):
    # Initialize an empty list to store indices of occurrences
    indices = []

    # Iterate through the product_list
    for index, product in enumerate(product_list):
        if product == target_product:
            # If the current product matches the target, append its index to the list
            indices.append(index)

    return indices

# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal","shoes"]
target = "shoes"
result = linear_search_product(products, target)
print(result)