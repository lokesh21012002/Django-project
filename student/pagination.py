from rest_framework.pagination import PageNumberPagination


class PageClass(PageNumberPagination):
    page_size = 5
    max_page_size = 5
    page_query_param = "search"
