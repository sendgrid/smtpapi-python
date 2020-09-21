import json
import decimal


class _CustomJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        # Provide a fallback to the default encoder if we haven't implemented
        # special support for the object's class
        return super(_CustomJSONEncoder, self).default(o)


class SMTPAPIHeader(object):

    def __init__(self):
        self.data = {}

    def add_to(self, to):
        if 'to' not in self.data:
            self.data['to'] = []
        if type(to) is list:
            self.data['to'] += to
        else:
            self.data['to'].append(to)

    def set_tos(self, tos):
        self.data['to'] = tos

    def add_substitution(self, key, value):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        if key not in self.data['sub']:
            self.data['sub'][key] = []
        self.data['sub'][key].append(value)

    def set_substitutions(self, subs):
        self.data['sub'] = subs

    def _add_key_value(self, index, key, value):
        if index not in self.data:
            self.data[index] = {}
        self.data[index][key] = value

    def _add_key(self, index, key):
        if index not in self.data:
            self.data[index] = []
        self.data[index].append(key)

    def add_unique_arg(self, key, value):
        self._add_key_value('unique_args', key, value)

    def set_unique_args(self, value):
        self.data['unique_args'] = value

    def add_category(self, category):
        self._add_key('category', category)

    def set_categories(self, category):
        self.data['category'] = category

    def add_section(self, key, section):
        self._add_key_value('section', key, section)

    def set_sections(self, value):
        self.data['section'] = value

    def add_send_each_at(self, time):
        self._add_key('send_each_at', time)

    def set_send_each_at(self, time):
        self.data['send_each_at'] = time

    def set_send_at(self, time):
        self.data['send_at'] = time

    def add_filter(self, app, setting, val):
        if 'filters' not in self.data:
            self.data['filters'] = {}
        if app not in self.data['filters']:
            self.data['filters'][app] = {}
        if 'settings' not in self.data['filters'][app]:
            self.data['filters'][app]['settings'] = {}
        self.data['filters'][app]['settings'][setting] = val

    def set_asm_group_id(self, value):
        if not bool(value):
            self.data['asm_group_id'] = {}
        else:
            self.data['asm_group_id'] = value

    def set_ip_pool(self, value):
        if bool(value):
            self.data['ip_pool'] = value
        else:
            self.data['ip_pool'] = {}

    def json_string(self):
        result = {}
        for key in self.data.keys():
            if self.data[key] != [] and self.data[key] != {}:
                result[key] = self.data[key]
        return json.dumps(result, cls=_CustomJSONEncoder)
