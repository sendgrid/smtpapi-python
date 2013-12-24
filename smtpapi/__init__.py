try:
    import json
except ImportError:
    import simplejson as json


class SMTPAPIHeader(object):
    def __init__(self):
        self.data = {}

    def add_substitution(self, key, value):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        self.data[key].append(value)

    def set_substitution(self, key, value):
        if 'sub' not in self.data:
            self.data['sub'] = {}
        if type(value) is str:
            self.data[key] = [val]
        elif type(value) is list:
            self.data[key] = value

    def add_unique_args(self, key, value):
        if 'unique_args' not in self.data:
            self.data['unique_args'] = {}
        self.data['unique_args'][key] = value

    def set_unique_args(self, value):
        if type(val) is dict:
            self.data['unique_args'] = value

    def add_category(self, category):
        if 'category' not in self.data:
            self.data['category'] = []
        self.data['category'].append(category)

    def set_category(self, category):
        self.data['category'] = category

    def add_section(self, key, section):
        if 'section' not in self.data:
            self.data['section'] = {}
        self.data['section'][key] = section

    def set_section(self, value):
        self.data['section'] = value

    def add_filter(self, app, setting, val):
        if 'filters' not in self.data:
            self.data['filters'] = {}
        if app not in self.data['filters']:
            self.data['filters'][app] = {}
        if 'settings' not in self.data['filters'][app]:
            self.data['filters'][app]['settings'] = {}
        self.data['filters'][app]['settings'][setting] = val

    def api_header_as_json(self):
        return json.dumps(self.data)

