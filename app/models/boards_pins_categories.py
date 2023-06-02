from .db import db, add_prefix_for_prod
from datetime import datetime, timedelta

boards_pins = db.Table(
    "boards_pins",
    db.Column(
        "pin_to_board",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey("pins.id")),
        primary_key=True
    ),
    db.Column(
        "board_pinned",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey("boards.id")),
        primary_key=True
    )
)

board_categories = db.Table(
    "board_categories",
    db.Column(
        "board_id",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey('boards.id')),
        primary_key=True
    ),
    db.Column(
        "category_id",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey('categories.id')),
        primary_key=True
    )
)

pin_categories = db.Table(
    "pin_categories",
    db.Column(
        "pin_id",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey("pins.id")),
        primary_key=True
    ),
    db.Column(
        "category_id",
        db.Integer,
        add_prefix_for_prod(db.ForeignKey("categories.id"))
    )
)


class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    private = db.Column(db.Boolean, nullable=False)
    cover_image = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, add_prefix_for_prod(db.ForeignKey('users.id')), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user = db.relationship('User', back_populates='boards')
    categories = db.relationship('Category', secondary= board_categories, back_populates='boards')



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'private': self.private,
            'cover_image': self.cover_image,
            'description': self.description,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Pin(db.Model):
    __tablename__ = 'pins'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, add_prefix_for_prod(db.ForeignKey('users.id')), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    alt_text = db.Column(db.String(255))
    destination = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    owner = db.relationship('User', back_populates='pins')
    categories = db.relationship('Category', secondary=pin_categories, back_populates='pins')
    board_tagged = db.relationship('Board', secondary=boards_pins, backref='pinned_boards')

    def to_dict(self):
        return {
            'id': self.id,
            'board_id': self.board_id,
            'owner_id': self.owner_id,
            'image': self.image,
            'title': self.title,
            'description': self.description,
            'alt_text': self.alt_text,
            'destination': self.destination,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


    boards = db.relationship('Board', secondary='board_categories', back_populates='categories')
    pins = db.relationship('Pin', secondary='pin_categories', back_populates='categories')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
