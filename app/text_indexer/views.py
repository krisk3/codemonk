from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .models import Paragraph, Word
from .serializers import TextSerializer, WordSerializer
import uuid


class AddTextView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=TextSerializer)
    def post(self, request, *args, **kwargs):
        serializer = TextSerializer(data=request.data)

        if serializer.is_valid():

            text_data = serializer.validated_data['text']
            paragraphs = [p.strip() for p in text_data.split('\n\n') if p.strip()]

            unique_id = str(uuid.uuid4().hex)[:8]
            unique_id = unique_id.replace("-", "_")

            for idx, paragraph_text in enumerate(paragraphs, start=1):
                uid = f"{unique_id}-{idx}"
                paragraph_instance = Paragraph.objects.create(uid=uid, paragraph=paragraph_text)

                words = paragraph_text.lower().split()
                for word in words:
                    Word.objects.create(word=word, paragraph_word=paragraph_instance)

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchWordView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(responses=WordSerializer)
    def post(self, request, *args, **kwargs):
        serializer = WordSerializer(data=request.data)

        if serializer.is_valid():
            search_word = serializer.validated_data['word']
            search_word = search_word.lower()
            word_queryset = Word.objects.filter(word=search_word)[:10]
            print(type(search_word))
            result_paragraphs = []
            print(word_queryset)
            for i in word_queryset:
                paragraph_obj = Paragraph.objects.get(id=i.paragraph_word.id)
                result_paragraphs.append({
                    'uid': paragraph_obj.uid,
                    'paragraph': paragraph_obj.paragraph,
                })

            return Response(result_paragraphs, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
