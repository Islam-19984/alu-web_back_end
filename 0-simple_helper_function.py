#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Function to calculate start and end index for pagination.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Return:
    Tuple: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
