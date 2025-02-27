from rest_framework import viewsets
from .models import Feedback, Convite
from .serializers import ConviteSerializer,FeedbackSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ConviteViewSet(viewsets.ModelViewSet):
    queryset = Convite.objects.all()
    serializer_class = ConviteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(userRemetente=self.request.user.member)

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
