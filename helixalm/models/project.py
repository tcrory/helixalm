"""Model of a Project object."""


class Project:

    def __init__(self, project_name: str, project_id: int, project_uuid: str):
        """Contains information about a Helix ALM project."""
        self.name = project_name
        self.id = int(project_id)
        self.uuid = project_uuid

    # TODO: Create get(@class)/post/update methods where appropriate.
