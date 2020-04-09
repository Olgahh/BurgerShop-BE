from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import (UserCreateSerializer,FoodListSerializer, FoodDetailSerializer)
from rest_framework.permissions import AllowAny,IsAuthenticated
# from rest_framework.filters import SearchFilter, OrderingFilters
# from .permissions import IsStaffOrUser
from .models import Food

# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

class FoodListView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer
    permission_classes = [AllowAny,]
    # filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name']


class FoodDetailView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'food_id'
    permission_classes = [AllowAny]


# class FoodCreateView(CreateAPIView):
#     serializer_class = FoodCreateSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         typeobj = Type.objects.get(id=self.kwargs.get("food_id"))
#         serializer.save(user=self.request.user, type=typeobj)

# class FoodUpdateView(RetrieveUpdateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodUpdateSerializer
#     permission_classes = [IsAuthenticated,IsStaffOrUser]
#     lookup_field = 'id'
#     lookup_url_kwarg = 'food_id'