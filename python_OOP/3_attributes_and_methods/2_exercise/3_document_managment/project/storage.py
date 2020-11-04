from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def _get_category(self, category_id: int):
        return [c for c in self.categories if c.id == category_id][0]

    def _get_topic(self, topic_id: int):
        return [t for t in self.topics if t.id == topic_id][0]

    def _get_document(self, document_id: int):
        return [d for d in self.documents if d.id == document_id][0]

    def edit_category(self, category_id: int, new_name: str):
        Storage._get_category(self, category_id).edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        Storage._get_topic(self, topic_id).edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        Storage._get_document(self, document_id).edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories.remove(Storage._get_category(self, category_id))

    def delete_topic(self, topic_id: int):
        self.topics.remove(Storage._get_topic(self, topic_id))

    def delete_document(self, document_id: int):
        self.documents.remove(Storage._get_document(self, document_id))

    def get_document(self, document_id: int):
        return Storage._get_document(self, document_id)

    def __repr__(self):
        return '\n'.join(repr(d) for d in self.documents)
