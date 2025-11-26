import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY
print(stripe.api_key)


def create_stripe_product(product):
    """Функция для создания продукта (курса/урока) в страйп"""

    product = stripe.Product.create(name=product)
    return product.id


def create_stripe_price(amount, product_id):
    """Создание цены в страцп"""

    price = stripe.Price.create(
        currency="rub", unit_amount=int(amount * 100), product=product_id
    )
    return price.id


def create_stripe_session(price_id):
    """Создание сессии в страйп"""

    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url


def get_stripe_payment_status(session_id):
    """Получение статуса платежа"""

    session = stripe.checkout.Session.retrieve(session_id)
    return session.payment_status
