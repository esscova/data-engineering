from extract_products import products
from extract_users import users


def transform_data():
    return {
        'products': products,
        'users': users
    }

if __name__ == '__main__':
    print(transform_data())