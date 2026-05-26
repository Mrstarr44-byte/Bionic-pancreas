from app import create_app, db
from app.models import User, MealPreset

app = create_app()

def seed_database():
    with app.app_context():
        # Check if database is already seeded
        existing_user = db.session.execute(db.select(User)).scalars().first()
        existing_meal = db.session.execute(db.select(MealPreset)).scalars().first()

        if existing_user or existing_meal:
            print("Veritabanı zaten dolu, seed atlanıyor.")
            return

        # Create Test User
        test_user = User(
            username="testuser",
            email="test@example.com"
        )
        test_user.set_password("123456")
        db.session.add(test_user)

        # Create Meal Presets
        meals = [
            MealPreset(
                name_tr="Beyaz Pilav", name_en="White Rice",
                carb_per_serving=45.0, gi_value=73, category="Ana Yemek"
            ),
            MealPreset(
                name_tr="Makarna", name_en="Pasta",
                carb_per_serving=40.0, gi_value=50, category="Ana Yemek"
            ),
            MealPreset(
                name_tr="Elma", name_en="Apple",
                carb_per_serving=14.0, gi_value=36, category="Meyve"
            ),
            MealPreset(
                name_tr="Sütlaç", name_en="Rice Pudding",
                carb_per_serving=35.0, gi_value=60, category="Tatlı"
            ),
            MealPreset(
                name_tr="Kola", name_en="Cola",
                carb_per_serving=39.0, gi_value=63, category="İçecek"
            ),
            MealPreset(
                name_tr="Beyaz Ekmek", name_en="White Bread",
                carb_per_serving=15.0, gi_value=75, category="Fırın"
            ),
            MealPreset(
                name_tr="Tavuk Göğsü", name_en="Chicken Breast",
                carb_per_serving=0.0, gi_value=0, category="Protein"
            ),
            MealPreset(
                name_tr="Patates Kızartması", name_en="French Fries",
                carb_per_serving=50.0, gi_value=75, category="Atıştırmalık"
            )
        ]

        db.session.add_all(meals)
        db.session.commit()
        
        print(f"Seed işlemi tamamlandı: 1 kullanıcı, {len(meals)} yemek eklendi.")

if __name__ == "__main__":
    seed_database()
