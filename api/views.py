from rest_framework.decorators import api_view
from rest_framework.response import Response
from embeddings.search import run_search


@api_view(['GET', 'POST'])
def semantic_search(request):
    # Accept GET ?query= OR POST {"query": "..."}
    query = request.GET.get('query') or request.data.get('query')

    if not query:
        return Response({"error": "query parameter required"}, status=400)

    results = run_search(query)
    return Response(results)
