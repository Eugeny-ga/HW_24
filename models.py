from marshmallow import Schema, fields, validate

valid_commands = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')

class RequestSchema(Schema):
    cmd1 = fields.Str(required=True, validate=validate.OneOf(valid_commands))
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True, validate=validate.OneOf(valid_commands))
    value2 = fields.Str(required=True)
    file_name = fields.Str(required=True)

