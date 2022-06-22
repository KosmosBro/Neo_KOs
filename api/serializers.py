from rest_framework import serializers

from main.models import Company, Category, Contact, Branch


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class CompanySerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    contact = ContactSerializer(many=True)
    branch = BranchSerializer(many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'descriptions', 'category', 'contact', 'branch']

    def create(self, validated_data):
        create_category = validated_data.pop('category')
        create_contact = validated_data.pop('contact')
        create_branch = validated_data.pop('branch')
        company = Company.objects.create(**validated_data)

        for category in create_category:
            Category.objects.create(company=company, **category)

        for contact in create_contact:
            Contact.objects.create(company=company, **contact)

        for branch in create_branch:
            Branch.objects.create(company=company, **branch)
        return company

