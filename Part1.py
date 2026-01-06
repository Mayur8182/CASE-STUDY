@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        #  Safe JSON handling
        data = request.get_json()
        if not data:
            return {"error": "Invalid JSON"}, 400

        # Field validation
        required = ['name', 'sku', 'price', 'warehouse_id', 'initial_quantity']
        for field in required:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        if data['price'] <= 0:
            return {"error": "Price must be positive"}, 400

        if data['initial_quantity'] < 0:
            return {"error": "Quantity cannot be negative"}, 400

        # Create objects
        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=data['price'],
            warehouse_id=data['warehouse_id']
        )

        inventory = Inventory(
            product=product,   #  Relationship usage
            warehouse_id=data['warehouse_id'],
            quantity=data['initial_quantity']
        )

        # Single transaction
        db.session.add_all([product, inventory])
        db.session.commit()

        return {
            "message": "Product created successfully",
            "product_id": product.id
        }, 201

    except Exception as e:
        #  Rollback on failure
        db.session.rollback()
        return {"error": str(e)}, 500
