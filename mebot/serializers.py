
from rest_framework import serializers
from .models import TelegramUser, Update, UserState, Membership, Admin
class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('chat_id', 'username', 'first_name', 'last_name')


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('chat_id', 'username', 'first_name', 'last_name')

class UpdateSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = Update
        fields = ('message_id', 'text', 'photo', 'callback_query_id', 'data', 'user', 'created_at')

class UserStateSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = UserState
        fields = ('user', 'state', 'step')

class MembershipSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = Membership
        fields = ('user', 'member')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('chat_id',)


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ('chat_id', 'username', 'first_name', 'last_name')

class UpdateSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = Update
        fields = ('message_id', 'text', 'photo', 'callback_query_id', 'data', 'user', 'created_at')

class UserStateSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = UserState
        fields = ('user', 'state', 'step')

class MembershipSerializer(serializers.ModelSerializer):
    user = TelegramUserSerializer(read_only=True)
    class Meta:
        model = Membership
        fields = ('user', 'member')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('chat_id',)
