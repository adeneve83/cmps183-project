# -*- coding: utf-8 -*-

db.define_table('user_info', Field('name'), Field('birth_date'), Field('shipping_address'), Field('email'))
db.define_table('posts',
                Field('title', requires=IS_NOT_EMPTY()),
                Field('author'),
                Field('interests'),
                Field('offers'),
                Field('image', 'upload'),
                Field('time_stamp','datetime')),
