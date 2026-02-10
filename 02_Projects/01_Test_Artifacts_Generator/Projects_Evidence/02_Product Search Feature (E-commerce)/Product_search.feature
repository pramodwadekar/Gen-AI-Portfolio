Feature: Product Search
Search products by name with filtering

Scenario: Search products by name
Given the user is on the search page
When the user searches for a product by name
Then the search results should display all products matching the search term

Scenario: Search products by partial name
Given the user is on the search page
When the user searches for a product by partial name
Then the search results should display all products with names containing the search term

Scenario: Filter search results by category
Given the user is on the search page
When the user searches for a product by name and filters by category
Then the search results should display only products matching the search term and category

Scenario: Filter search results by price range
Given the user is on the search page
When the user searches for a product by name and filters by price range
Then the search results should display only products matching the search term and price range

Scenario: Filter search results by category and price range
Given the user is on the search page
When the user searches for a product by name and filters by category and price range
Then the search results should display only products matching the search term, category, and price range

Scenario: No products found
Given the user is on the search page
When the user searches for a product by name that does not exist
Then the search results should display a 'No products found' message