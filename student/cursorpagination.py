from rest_framework.pagination import CursorPagination


class CursorPage(CursorPagination):
    page_size = 5
    cursor_query_param = "query"
    ordering = ['id', 'name']
    ordering = '__all__'
