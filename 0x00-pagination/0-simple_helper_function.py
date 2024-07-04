#!/usr/bin/env python3
"""
Helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Finding the index range with pagination
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return start_idx, end_idx
