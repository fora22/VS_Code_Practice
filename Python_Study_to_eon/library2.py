import os
import sys

    
class librarypro:

    def menu1(self,library):
       
        print("추가하고자하는 도서의 정보를 입력하세요. 순서는 제목 저자 발행년도 출판사 카테고리 입니다.")     
        self.book1 = str(input("입력 : "))
        self.Addbook = self.book1.split()
        print(self.Addbook)
        print("제목 : %s 저자 : %s 발행년도 : %s 출판사 : %s 카테고리 : %s" %(self.Addbook[0],self.Addbook[1],self.Addbook[2],self.Addbook[3],self.Addbook[4]))
        check = int(input("저장하시려면 1을 눌러주세요. 다른 것을 누르면 취소됩니다.\n입력 : "))
        if check == 1:
            library.append(self.book1+'\n')
            print("도서가 추가되었습니다.")      
        else:
            print("취소되었습니다.")
        return library
       
    def menu2(self,library):
        find = str(input("검색하고자하는 도서를 입력하세요.\n입력 : "))
        for i in range(0,len(library),1):        # 배열 검사해서
            if find in library[i]:        # 배열에서 입력된 도서 찾으면 출력
                print(library[i])        
            else:
                print("검색되지 않습니다.")
        print("도서 검색이 완료되었습니다.\n")
        return library

    def menu3(self,library):
        for i in range(len(library)):           # 책 목록 보여주고
            print(i)
            print(library[i])
        num = int(input("번호를 입력해주세요.\n입력 : "))         # 수정할 번호를 입력받음
        library[num] = str(input("수정할 책정보를 입력하세요. 순서는 제목 저자 발행년도 출판사 카테고리 입니다.\n입력 : "))
        print("수정되었습니다.")
        return library


    def menu4(self,library):              
        for i in range(len(library)):           # 책 목록 보여주고
            print(i)
            print(library[i])
        num = int(input("삭제할 책 번호를 입력하세요.\n입력 : "))       # 삭제할 번호를 입력받음
        library.pop(num)                 # 입력된 숫자에 해당되는 정보 pop해줌
        print("삭제되었습니다.")
        return library

    def menu5(self,library):
        print ("현재 책 목록은 다음과 같습니다.")
        print (library)          #library에 있는 정보 출력
    
    def menu6(self,library):
        Save1 = ''.join(library)
        folder1 = os.path.dirname(os.path.abspath(__file__))
        folder2 = os.path.join(folder1,'input.txt')
        wr = open(folder2,'w')
        wr.write(Save1)
        wr.close
        print("저장되었습니다.")

    def menu7(self,library):
        Save2 = ''.join(library)
        folder1 = os.path.dirname(os.path.abspath(__file__))
        folder2 = os.path.join(folder1,'input.txt')
        wr = open(folder2,'w')
        wr.write(Save2)
        wr.close
        print("프로그램을 종료합니다.")
        sys.exit()