from django.http import JsonResponse, HttpResponse
from decimal import Decimal
import csv
from .models import Product


def get_products(request):
    def clean_price(price_str):
        # # Remove currency symbol and comma characters
        # price_str = price_str.replace('₹', '').replace(',', '')
        # return Decimal(price_str)

        # Remove currency symbol and comma characters
        price_str = price_str.replace('₹', '').replace(',', '')

        try:
            return Decimal(price_str)
        except (ValueError, TypeError):
            # Handle invalid or missing values, return a default value or None if appropriate
            return None


    def clean_discount(discount_str):
        # Remove percentage symbol
        discount_str = discount_str.replace('%', '')
        return Decimal(discount_str)


    def clean_rating_count(rating_count):
        # Remove currency symbol and comma characters
        rating_count = rating_count.replace(',', '')
        return Decimal(rating_count)


    def import_data_from_csv():
        with open('/home/raj/Downloads/Dhruv-Surani/archive/Project/crud/amazon.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row if present

            for row in reader:
                try:
                    # Assuming the CSV file has columns: name, price, description
                    product_id = row[0]
                    product_name = row[1]
                    category = row[2]
                    discounted_price = clean_price(row[3])
                    actual_price = clean_price(row[4])
                    discount_percentage = clean_discount(row[5])
                    rating = Decimal(row[6])
                    rating_count = clean_rating_count(row[7])
                    about_product = row[8]
                    user_id = row[9]
                    user_name = row[10]
                    review_id = row[11]
                    review_title = row[12]
                    review_content = row[13]
                    img_link = row[14]
                    product_link = row[15]

                    product = Product.objects.create(
                        product_id=product_id,
                        product_name=product_name,
                        category=category,
                        discounted_price=discounted_price,
                        actual_price=actual_price,
                        discount_percentage=discount_percentage,
                        rating=rating,
                        rating_count=rating_count,
                        about_product=about_product,
                        img_link=img_link,
                    )
                    product.save()
                except Exception as e:
                    print(f"Error processing row: {row}")
                    print(f"Error message: {str(e)}")


    # Call the function and pass the path to your CSV file
    import_data_from_csv()

    return HttpResponse("done")