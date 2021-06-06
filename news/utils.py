class MyMixin(object):
    mixin_proc = ''

    def get_proc(self):
        return self.mixin_proc.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()