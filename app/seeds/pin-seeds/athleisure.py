
from datetime import datetime
from app.models import db, Pin, environment, SCHEMA, User, Category

user1 = User.query.get(1)
user2 = User.query.get(2)
user3 = User.query.get(3)
athleisure = Category.query.filter(Category.name == "Athleisure").one()

pin1 = Pin(
    title="ASRV Sportswear Gym Outfit",
    image="https://threadterest.s3.us-east-2.amazonaws.com/ASRV+Sportswear+Gym+Outfit.jpeg",
    user=user1,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)


pin2 = Pin(
    title="Bodybuilding & Fitness Men's Cotton Printed Tank Top",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Bodybuilding+_+Fitness+Men_s+Cotton+Printed+Tank+Top.jpeg",
    destination="https://vivinch.com/bodybuilding-fitness-mens-cotton-printed-tank-top?attribute_pa_cb5feb1b7314637725a2e7=white-red-letter&attribute_pa_6f6cb72d544962fa333e2e=xl",
    user=user1,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin3 = Pin(
    image="https://threadterest.s3.us-east-2.amazonaws.com/bradley.jpeg",
    user=user2,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin4 = Pin(
    title="Curved Hem Patchwork Stringer",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Curved+Hem+Patchwork+Stringer.jpeg",
    user=user2,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin5 = Pin(
    title="Gym Workout Sleeveless Tank Top",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Gym+Workout+Sleeveless+Tank+Top.jpeg",
    description="Sleeveless tank top. Made out of cotton.",
    user=user3,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin6 = Pin(
    title="Men's Casual Light Green Sports Suit",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Men_s+Casual+Light+Green+Sports+Suit.jpeg",
    description="Sport suit ready to be worn in the gym.",
    user=user3,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin7 = Pin(
    title="Men's Training Gear",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Men_s+Training+Gear.jpeg",
    description="Great gear to train in. Check out the site!",
    user=user3,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin8 = Pin(
    title="Men's White T-Shirt",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Men_s+White+T-Shirt.jpeg",
    user=user3,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)
    db.session.add(pin8)

    db.session.commit()

pin9 = Pin(
    title="Muscular Men's Gym & Fitness Tank Top",
    image="https://threadterest.s3.us-east-2.amazonaws.com/Muscular+Men_s+Gym+_+Fitness+Tank+Top.jpeg",
     user=user3,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin10 = Pin(
    title="New Men's Casual Solid Color Short Sleeve",
    image="https://threadterest.s3.us-east-2.amazonaws.com/New+Men_s+Casual+Solid+Color+Short+Sleeve.jpeg",
    user=user2,
    categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

pin11 = Pin(
    title="No Pain No Gain Mens Hooded Tank Top",
    image="https://threadterest.s3.us-east-2.amazonaws.com/No+Pain+No+Gain+Mens+Hooded+Tank+Top.jpeg",
    description="Material: cotton, Fabric: Broadcloth, Collar: O-Neck",
    destination="https://vivinch.com/no-pain-no-gain-mens-hooded-gym-fitness-tank-top",
    user=user2,
     categories=[athleisure],
    created_at=datetime.now(),
    updated_at=datetime.now()
)

    pin12 = Pin(
        title="Oakland Fleece Sweatpants",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Oakland+Fleece+Sweatpants+.webp",
        description="Your global online store that delivers latest fashion apparel for you! We have dresses, tops, blouses and shoes for girls and ladies. Thousands of products in different styles are waiting for you!",
        destination="https://www.vsmeestore.com/products/oakland-fleece-sweatpants?variant=bc26778f-f1b1-49cf-ad6a-eb3bff2f92ec&pp=0&epik=dj0yJnU9U005RkZQUkRELVpoMlhPWW1iTTJzTnJwdWVfN1d0cnkmcD0xJm49ak5xYUptNVdGbmtjTVVMM0owbkJtQSZ0PUFBQUFBR1I1WDdr",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin12)

    db.session.commit()

    pin13 = Pin(
        title="Swoltastic Gym Rashguard Shirt",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Swoltastic+Gym+Rashguard+Shirt.jpeg",
        description="Awesome spandex shirt. Great for your evening workout.",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin13)

    db.session.commit()

    pin14 = Pin(
        title="Back Poses | Motivate",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Back+Poses+_+Motivate.jpeg",
        description="Killer back workout!",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin14)

    db.session.commit()

    pin15 = Pin(
        title="Gym | Focus | Motivation",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Gym+_+Focus+_+Motivation.jpeg",
        description="Hope you all have a good day! Get motivated!",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin15)

    db.session.commit()

    pin16 = Pin(
        title="Gym Shark spandex top and bottom",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Gym+Shark+spandex+top+and+bottom+.jpeg",
        description="Look good to feel good inside",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin16)

    db.session.commit()

    pin17 = Pin(
        title="Color Block Tee and Leggings",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Color+Block+Tee+and+Leggings.jpeg",
        user=user2,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin17)

    db.session.commit()

    pin18 = Pin(
        title="High-Rise 7/8 Good Karma 2-Pocket Leggings",
        image="https://threadterest.s3.us-east-2.amazonaws.com/High-Rise+7_8+Good+Karma+2-Pocket+Leggings.jpeg",
        description="Free shipping. Get yours today!",
        destination="https://www.freepeople.com/shop/high-rise-7-8-good-karma-2-pocket-leggings/?color=041&epik=dj0yJnU9UkhlbmVjNUhsOHNWT1AxZW5iUUhKeWc4aWJOcEljZ1UmcD0wJm49SndYQ0RGWW5TUHIxdjAtZzdfQVJKdyZ0PUFBQUFBR1I1WVBv&size=XS%2FS&utm_campaign=2023-06-01&utm_content=High-Rise_7%2F8_Good_Karma_2-Pocket_Leggings&utm_medium=unpaid_social&utm_source=Pinterest&utm_term=pinterest_shopping&type=REGULAR&quantity=1",
        user=user1,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin18)

    db.session.commit()

    pin19 = Pin(
        title="Gym Shot",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Gym+Shot.jpeg",
        description="We don't skip leg day!",
        user=user1,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin19)

    db.session.commit()

    pin21 = Pin(
        title="Pearled Ivory Leggings",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Pearled+Ivory+Leggings.jpg",
        user=user1,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin21)

    db.session.commit()

    pin22 = Pin(
        title="Karma Leggings",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Karma+Leggings.jpeg",
        user=user1,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin22)

    db.session.commit()

    pin23 = Pin(
        title="Say Cheese",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Say+Cheese.jpeg",
        description="Posing for the gym fam. Check out the gear.",
        user=user3,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin23)

    db.session.commit()


    pin24 = Pin(
        title="If They Can Do It",
        image="https://threadterest.s3.us-east-2.amazonaws.com/If+They+Can+Do+It.jpeg",
        description="We all know that Western society is facing a catastrophic health crisis. The solution is easier than you might think . . .",
        user=user3,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin24)

    db.session.commit()

    pin25 = Pin(
        title="Top and Shorts",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Top+and+Shorts.JPEG",
        description="Great top and shorts. Very comfy",
        user=user3,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin25)

    db.session.commit()

    pin26 = Pin(
        title="Silver Metallic Sports Bra",
        image="https://threadterest.s3.us-east-2.amazonaws.com/Silver+Metallic+Sports+Bra.jpeg",
        user=user3,
        categories=[athleisure],
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db.session.add(pin26)

    db.session.commit()


def undo_pins():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pins RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pins"))

    db.session.commit()