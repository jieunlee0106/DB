1. 학습한 내용
    -is_valid(raise_exception=True)
        view 함수에서 에러를 표현 할 때 return 을 따로 만들 필요 없이 유효성 검사에서 에러를 표현 하는 코드를 학습했습니다.
    - many=True
        데이터를 리스트로 받아올 때는 many=True 를 적용 
    - serializer = serializers.ReviewSerializer(review, data=request.data, partial=True)
        "PUT" 를 실행 할 때 partial=True 를 하게되면 , 원하는 항목만 수정할 수 있게됩니다.
        
    
2. 어려웠던 부분과 느낀 점
    혼자서 학습을 할 때는 깃에 올라와있는 코드를 바탕으로 필요한 추가 코드를 작성해가는 식으로 학습을 했습니다. 이게 습관이 되다보니, 이번프로젝트를 하며 백지상태에서 처음부터 코드를 작성하는데 어려움을 느꼈습니다. 
    앞으로 웹을 학습할 때는 바닐라 코딩으로 작성할 수 있도록 연습해야될 것 같습니다. 
    