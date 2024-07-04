#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Returns hypermedia pagination info based on index and page_size
        """
        assert isinstance(index, int) and index >= 0, \
            "Index must be a non-negative integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        dataset = self.indexed_dataset()
        max_index = len(dataset) - 1

        assert index <= max_index,
        f"Index {index} out of range. Maximum index is {max_index}."

        start_index = index
        next_index = start_index + page_size

        data = [dataset[idx] for idx in range(start_index, min(
            next_index, max_index + 1))]

        return {
            "index": start_index,
            "next_index": next_index if next_index <= max_index else None,
            "page_size": len(data),
            "data": data
        }
