import uuid

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []  # เก็บออบเจกต์ Product ทั้งหมดของร้าน

    def addingItemsToCart(self, customer, product, quantity):
        """เพิ่มสินค้าและจำนวนลง cart ของลูกค้า"""
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        customer.cart.append({"product": product, "quantity": quantity})
        print(f"Added to cart: {product.name} x {quantity}")

    def checkOut(self, customer):
        """ประมวลผลตะกร้าสินค้า: คำนวณราคารวม สร้าง order_id บันทึกลง past_orders แล้วล้าง cart"""
        if not customer.cart:
            print("Cart is empty!")
            return None
        total_price = sum(item["product"].price * item["quantity"] for item in customer.cart)
        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "items": [{"name": it["product"].name, "price": it["product"].price, "quantity": it["quantity"]}
                      for it in customer.cart],
            "total": total_price
        }
        customer.past_orders.append(order)
        customer.cart.clear()
        print(f"Order placed! Order ID: {order_id}, Total: {total_price}")
        return order_id

    def orderTracking(self, customer, order_id):
        """ค้นหา order จาก past_orders ของลูกค้าด้วย order_id แล้วแสดงรายละเอียด"""
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print("Order found:")
                print(f"Order ID: {order['order_id']}")
                print("Items:")
                for it in order["items"]:
                    print(f"- {it['name']} x {it['quantity']} @ {it['price']}")
                print(f"Total: {order['total']}")
                return order
        print("Order not found.")
        return None

class Product:
    def __init__(self, name, description, price, online_shop):
        self.name = name
        self.description = description
        self.price = float(price)
        self.online_shop = online_shop  # อ้างอิงร้านเจ้าของสินค้า
        # เพิ่มสินค้าเข้าคลังของร้านโดยอัตโนมัติ (สะดวกตอนทดสอบ)
        if online_shop is not None:
            online_shop.products.append(self)

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []        # รายการที่ยังไม่ชำระเงิน
        self.past_orders = [] # ประวัติคำสั่งซื้อที่สำเร็จ

if __name__ == "__main__":
    # ตัวอย่างการทดสอบ
    # shop = OnlineShop("Gadget World", "www.gadgetworld.com")
    # prod1 = Product("Gaming Mouse Pro X", "High-end gaming mouse", 1500, shop)
    # prod2 = Product("Mechanical Keyboard Z", "RGB mechanical keyboard", 3500, shop)
    # customer = Customer("John Doe", "john@example.com", "123 Street")
    # shop.addingItemsToCart(customer, prod1, 2)
    # shop.addingItemsToCart(customer, prod2, 1)
    # oid = shop.checkOut(customer)
    # if oid:
    #     shop.orderTracking(customer, oid)
    pass
