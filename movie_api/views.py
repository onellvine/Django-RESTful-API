from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import  IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import SysUser, Movie, Comment
from .serializers import RegisterUserSerializer, SysUserSerializer, MovieSerializer, CommentSerializer


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)

        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                print(new_user)
                return Response(status=status.HTTP_201_CREATED)

        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# initial entry point
@api_view(['GET'])
def apiOverView(request):
    endpoints = {
        'movie_api',
        'movie_api/users',
        'movie_api/users/add',
        'movie_api/user/<int:id>/detail',
        'movie_api/movies',
        'movie_api/movies/add',
        'movie_api/movie/<int:id>/detail',
        'movie_api/comments',
        'movie_api/comments/add',
        'movie_api/comment/<int:id>/detail',
        'movie_api/cat/movies',
        'movie_api/cat/series',
    }
    return Response(endpoints)


@api_view(['GET'])
def moviesCategory(request, cat):
    movies = Movie.objects.filter(category=cat)
    serializer = MovieSerializer(movies, many=True)

    return Response(serializer.data)
    

class SysUserCreate(generics.ListCreateAPIView):
    queryset = SysUser.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [IsAdminUser]

class SysUserList(generics.ListAPIView):
    queryset = SysUser.objects.all()
    serializer_class = SysUserSerializer
    permission_classes = [AllowAny]

class SysUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SysUser.objects.all()
    serializer_class = SysUserSerializer
    permission_classes = [IsAdminUser]


class MovieCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    lookup_field = "id"
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]


class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]    

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]