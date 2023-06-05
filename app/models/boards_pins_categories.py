from .db import db, add_prefix_for_prod, environment, SCHEMA
from datetime import datetime, timedelta

boards_pins = db.Table(
    "boards_pins",
    db.Column(
        "pin_to_board",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("pins.id"))
    ),
    db.Column(
        "board_pinned",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("boards.id")),
    )
)

if environment == "production":
    boards_pins.schema = SCHEMA

board_categories = db.Table(
    "board_categories",
    db.Column(
        "board_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('boards.id')),
    ),
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('categories.id')),
    )
)

if environment == "production":
    board_categories.schema = SCHEMA

pin_categories = db.Table(
    "pin_categories",
    db.Column(
        "pin_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("pins.id")),
    ),
    db.Column(
        "category_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("categories.id"))
    )
)

if environment == "production":
    pin_categories.schema = SCHEMA


class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    private = db.Column(db.Boolean)
    cover_image = db.Column(db.String(255))
    description = db.Column(db.String(255))
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user = db.relationship('User', back_populates='boards')
    categories = db.relationship('Category', secondary= board_categories, back_populates='boards')
    pins_tagged = db.relationship('Pin', secondary=boards_pins, backref='board_pinned')

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'private': self.private,
            'cover_image': self.cover_image,
            'description': self.description,
            'owner_id': self.owner_id,
            'user': self.user.to_dict(),
            'categories': [category.to_dict() for category in self.categories],
            'pins': [pin.to_dict() for pin in self.pins_tagged],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class Pin(db.Model):
    __tablename__ = 'pins'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, (db.ForeignKey(add_prefix_for_prod('users.id'))), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    alt_text = db.Column(db.String(255))
    destination = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user = db.relationship('User', back_populates='pins')
    categories = db.relationship('Category', secondary=pin_categories, back_populates='pins')
    board_tagged = db.relationship('Board', secondary=boards_pins, backref='pinned_boards')

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'image': self.image,
            'title': self.title,
            'description': self.description,
            'alt_text': self.alt_text,
            'destination': self.destination,
            'categories': [category.to_dict() for category in self.categories],
            'boards_pinned_in': [board.name for board in self.board_tagged],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


    boards = db.relationship('Board', secondary='board_categories', back_populates='categories')
    pins = db.relationship('Pin', secondary='pin_categories', back_populates='categories')

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }