
class SearchHandle:
    """
    IndexHandle is an iterator class and returns iterator instances on query results from Elastic Search
    """

    def __init__(self, indexName, type, query, filters):
        self.indexName = indexName
        self.type = type
        self.query = query
        self.filters = filters
        self.numDocuments = 0
        # self.results is a list of all documents returned
        self.results = self.search(query, filters)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.numDocuments:
            self.n += 1
            return self.results[self.n - 1]
        else:
            raise StopIteration

    def search(self, query, filters):
        """
        search query based on options in the filters
        Returns the whole document as a dictionary
        """
        self.numDocuments = 2
        return ["hello", "world"]


def main():
    obj = SearchHandle("apple", "fruits", "arb", "152")
    for i in obj:
        print(i)
if __name__ == "__main__":
    main()
