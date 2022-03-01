from django.shortcuts import render
from rest_framework.views import APIView
from.models import Content
from common.common import CommonResponse, SuccessResponse, SuccessResponseWithData, ErrorResponse



# Create your views here.



class Main(APIView):
    def post(self, request):
        category = request.data.get('category')
        ##컨텐츠ID값 , subject , map
        contents = Content.objects.filter(category=category).order_by('-id')
        ContentList = []
        for i in contents:
            ContentList.append(dict(
                subject=i.subject,
                category=i.category,
                nickname=i.nickname,
                latitude=i.latitude,
                longitude=i.longitude,
            ))
        return SuccessResponseWithData(dict(Contents=ContentList))



class Create(APIView):
    def post(self, request):
        nickname = 'session'
        subject = request.data.get('subject')
        content = request.data.get('content')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        category = request.data.get('category')
        #파일과 이미지는 if문에서 처리
        Content.objects.create(
            nickname=nickname,
            subject=subject,
            content=content,
            category=category,
            latitude=latitude,
            longitude=longitude
        )
        return SuccessResponse()



class Detail(APIView):
    def post(self, request):
        contentId = request.data.get('contentId')
        detailContent = Content.objects.filter(id=contentId)
        ContentDetail = []
        for i in detailContent:
            ContentDetail.append(dict(
                subject=i.subject,
                content=i.content,
                category=i.category,
                image=i.image,
                nickname=i.nickname,
                latitude=i.latitude,
                longitude=i.longitude,
                createDate=i.createDate
            ))
        return SuccessResponseWithData(dict(ContentDetail=ContentDetail))

