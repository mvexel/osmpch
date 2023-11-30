from osmpch.models.changeset import Changeset


class BaseWriter:
    def write_changeset(self, changesets: list[Changeset]):
        raise NotImplementedError("This method needs to be implemented by a subclass")

    def close(self):
        raise NotImplementedError("This method needs to be implemented by a subclass")
