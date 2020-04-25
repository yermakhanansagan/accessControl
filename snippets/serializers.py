from rest_framework import serializers
from snippets.models import History, Access, Employees, Device, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeesDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Employees
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['id', 'student_id', 'name', 'surname', 'department', 'position', 'check_in', 'check_out']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'