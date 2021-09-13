
from django.db import models
from django.db.models import fields
import graphene

from graphene_django import DjangoObjectType
from .models import Test,Test2

class TestType(DjangoObjectType):
    class Meta:
        model=Test
        field=("id","name")
class Test2Type(DjangoObjectType):
    class Meta:
        model=Test2
        fields=("id","test_id","name")
    

class Query(graphene.ObjectType):
    allTest=graphene.List(TestType)
    testvar=graphene.String()
    allTest2=graphene.List(Test2Type)
    oneTest2=graphene.Field(Test2Type,id=graphene.Int())
    def resolve_oneTest2(root,info,id):
        return Test2.objects.get(id=id)
    def resolve_allTest2(root,info):
        
        return Test2.objects.all()
    def resolve_testvar(root,info):
        return "sdvsdv"
    def resolve_allTest(root,info):
        return Test.objects.all()
class TestMutations(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
    test=graphene.Field(TestType)
    @classmethod
    def mutate(cls,root,info,name):
        test=Test()
        test.name=name
        test.save()
        return TestMutations(test=test)
class Test2Mutations(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        test_id=graphene.ID()
    test1=graphene.Field(Test2Type)
    @classmethod
    def mutate(cls,root,info,name,test_id):

        test=Test2()
        test.name=name
        test.test_id=Test.objects.get(id=test_id)
        test.save()
        return Test2Mutations(test1=test)
class Mutation(graphene.ObjectType):
    save_test=TestMutations.Field()
    save_test2=Test2Mutations.Field()
sc=graphene.Schema(query=Query,mutation=Mutation)
