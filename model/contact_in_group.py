from sys import maxsize


class ContactInGroup:
    def __init__(self, id=None, group_id=None, group_name=None):
        self.id = id
        self.group_id = group_id
        self.group_name = group_name

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.group_id, self.group_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.group_id is None or other.group_id is None or self.group_id == other.group_id

    def id_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
