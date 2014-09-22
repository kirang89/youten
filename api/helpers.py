from datetime import datetime


class Serializer(object):
    """Mixin for retrieving public fields of SQLAlchemy models
    in json-compatible format"""
    __public__ = None

    def get_dict(self, exclude=(), extra=()):
        "Returns model's PUBLIC data for jsonify"
        data = {}
        keys = self._sa_instance_state.attrs.items()
        public = self.__public__ + extra if self.__public__ else extra
        for k, field in keys:
            if public and k not in public: continue
            if k in exclude: continue
            value = self._serialize(field.value)
            if value:
                data[k] = value
        return data

    @classmethod
    def _serialize(cls, value, follow_fk=False):
        if isinstance(value, datetime):
            ret = value.isoformat()
        elif hasattr(value, '__iter__'):
            ret = [cls._serialize(v) for v in value]
        elif Serializer in value.__class__.__bases__:
            ret = value.get_public()
        else:
            ret = value
        return ret
