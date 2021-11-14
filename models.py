from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
import datetime
from time import time
from cloudinary import uploader
import jwt
import json
import os

class User(UserMixin, db.Document):
    username = db.StringField(max_length=12, unique=True, required=True)
    email = db.EmailField(max_length=100, unique=True, required=True)
    password_hash = db.StringField(required=True)
    img_url = db.URLField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password))
    
    def set_avatar(self, img_url):
        self.img_url = img_url
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Eventtype(db.Document):
    eventtype_name = db.StringField(required=True)

    def __repr__(self):
        return f"Meetup Type:('{self.eventtype_name}')"


class Event(db.Document):
    eventtype = db.ReferenceField(Meetuptype)
    nickname = db.StringField(max_length=50, required=True)
    img_url = db.URLField()
    img_url_card = db.URLField()
    img_url_thumb = db.URLField()
    about = db.StringField(max_length=250,
                           default="No meetup blurb yet!")
    event_organiser = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    attending_by = db.ListField(db.ReferenceField(User))
    attending_total = db.IntField()
    event_datetime = db.DateTimeField()
    upload_date = db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Meetup Type('{self.meetuptype_name}'" \
               f"Event Organiser = {self.uploader.username})"

    def set_event_image(self, event_img, user, pk):
        # Get an individual folder for each user's photo uploads
        # and set filename to bird's primary key,
        # so a new photo upload overwrites the old one
        public_id = f"breastcancerclub/{user}/{pk}"
        # upload image to identified folder
        # with eager transformations for smaller image
        res = uploader.upload(event_img, public_id=public_id, overwrite=True)
        # Get already configurated cloud name
        cloud_name = os.environ.get("CLOUD_NAME")
        # add to URL for building URL
        endpoint = f"https://res.cloudinary.com/{cloud_name}/image/upload"
        # Add transformations for delivering lower quality, smaller version
        # for bird card and bird profile page respectively
        card_transformation = '/c_fill,g_auto,h_350,w_525,q_auto:low'
        thumb_transformation = '/w_500,c_scale,q_auto:low'
        # Get the version, id and format details from uploaded image
        version = f"/v{res['version']}/"
        public_id = res["public_id"]
        image_format = res["format"]
        # add links for full quality image and thumbnails to Bird model
        self.img_url = f"{endpoint}{version}{public_id}.{image_format}"
        self.img_url_card = f"{endpoint}{card_transformation}" \
                            f"{version}{public_id}.{image_format}"
        self.img_url_thumb = f"{endpoint}{thumb_transformation}" \
                             f"{version}{public_id}.{image_format}"

    def delete_event_image(self, user, pk):
        public_id = f"breastcancerclub/{user}/{pk}"
        uploader.destroy(public_id)