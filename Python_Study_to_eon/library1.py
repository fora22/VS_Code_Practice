import os
import sys
import library2

folder1 = os.path.dirname(os.path.abspath(__file__))
folder2 = os.path.join(folder1,'input.txt')
f = open(folder2,'r')
library = f.readlines()

class user:
    
    def __init__(self):
        self.librarypro_clss = library2.librarypro()

        
    
    def menu(self):                   # 메뉴 생성 
        print("1. 도서 추가하기")
        print("2. 도서 검색하기")
        print("3. 도서정보 수정하기")
        print("4. 도서 삭제하기")
        print("5. 도서목록 출력하기")
        print("6. 도서 저장하기")
        print("7. 프로그램 종료하기")

    def sub_menu(self,library):               # 사용자에게 숫자 입력받음
        self.menu()
        check1 = int(input("메뉴를 선택하세요 : "))        # 입력받은 숫자 check1에 저장

        if check1 ==1:
            self.librarypro_clss.menu1(library)
            # 사용자가 1 입력시 library2에 있는 도서추가 클라스 실행
            
            self.sub_menu(library)
        
        elif check1 ==2:
            self.librarypro_clss.menu2(library)
            # 사용자가 2 입력시 library2에 있는 도서검색 클라스 실행
            
            self.sub_menu(library)
        
        elif check1 ==3:
            self.librarypro_clss.menu3(library)
            # 사용자가 3 입력시 library2에 있는 도서수정 클라스 실행
        
            self.sub_menu(library)
        
        elif check1 ==4:
            self.librarypro_clss.menu4(library)
            # 사용자가 4 입력시 library2에 있는 도서삭제 클라스 실행
        
            self.sub_menu(library)
        
        elif check1 ==5:
            self.librarypro_clss.menu5(library)
            # 사용자가 5입력시 library2에 있는 도서목록 클라스 실행
        
            self.sub_menu(library)
        
        elif check1 ==6:
            self.librarypro_clss.menu6(library)
            # 사용자가 6 입력시 library2에 있는 도서저장 클라스 실행
        
            self.sub_menu(library)
        
        elif check1 ==7:
            self.librarypro_clss.menu7(library)
            # 사용자가 7 입력시 프로그램 종료
            
            print("프로그램을 마칩니다.")
        
        else:
            print("실행 불가능")
            # 그 외 숫자 받을시 프로그램 오류

a=user()
a.sub_menu(library)