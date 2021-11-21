from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
