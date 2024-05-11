import os
from django.conf import settings
import requests
from prod.models import Product
from prod.models import Image
from django.db import models

def fetch_and_store_products():
    api_url = "https://dummyjson.com/products?skip=0&limit=100"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        products = data.get('products', [])
        for product_data in products:
            product_id = product_data['id']
            # Check if the product already exists
            if Product.objects.filter(id=product_id).exists():
                print(f"Product {product_id} already exists. Skipping...")
                continue  
            product = Product(
                id=product_data['id'],
                title=product_data['title'],
                description=product_data['description'],
                price=product_data['price'],
                discountPercentage=product_data['discountPercentage'],
                rating=product_data['rating'],
                stock=product_data['stock'],
                brand=product_data['brand'],
                category=product_data['category'],
                thumbnail=product_data['thumbnail'],
                # Add other fields as needed
            )
            product.save()
            
            # Fetch and save images associated with the product
            images_data = product_data.get('images', [])
            for image_url in images_data:
                # Create and save Image instances
                image = Image(product=product,image=image_url)
                image.save()
                # Associate the Image instance with the Product instance
                product.images.add(image)
            # images_data = product_data.get('images', [])
            # for image_url in images_data:
            #     image, _ = Image.objects.get_or_create(url=image_url)
            #     product.images.add(image)
        print("Products stored successfully.")
    else:
        print("Failed to fetch products from the API.")

    images_data = product_data.get('images', [])



def remove_duplicate_images():
    # Find duplicate images based on URL
    duplicate_image_urls = (Image.objects.values('image')
                                        .annotate(count=models.Count('image'))
                                        .filter(count__gt=1)
                                        .values_list('image', flat=True))

    # Keep track of which images to delete
    images_to_delete = []

    # Iterate over duplicate image URLs
    for image_url in duplicate_image_urls:
        # Find all instances of the duplicate image
        duplicate_images = Image.objects.filter(image=image_url)

        # Keep the first image and mark others for deletion
        first_image = duplicate_images.first()
        images_to_delete.extend(duplicate_images[1:])

    # Delete duplicate images
    Image.objects.filter(id__in=[i.id for i in images_to_delete]).delete()
    print("Duplicate images removed successfully.")
if __name__=="__main__":
    fetch_and_store_products()