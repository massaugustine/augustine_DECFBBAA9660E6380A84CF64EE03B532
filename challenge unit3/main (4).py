def LinearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices

# Example usage:
products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = LinearSearchProduct(products, target)
target2 = 'apple'
result2 = LinearSearchProduct(products, target2)
print(result)
print(result2)