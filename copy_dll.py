import shutil
import os
import re

def copy_files(file_list, destination_folder):
    # 파일 목록을 특정 구분자로 분할하여 파일 이름 리스트를 생성 (\n, \r, \t)
    files = re.split(r'[\n\r\t]+', file_list)

    # 각 파일을 대상으로 복사
    for file in files:
        # 파일 경로의 앞뒤 공백 제거
        file = file.strip()
        # 파일이 존재하는지 확인
        if os.path.isfile(file):
            try:
                shutil.copy(file, destination_folder)
                print(f"Copied: {file} to {destination_folder}")
            except Exception as e:
                print(f"Failed to copy {file}: {e}")
        else:
            print(f"File does not exist: {file}")

# 파일 목록 문자열 (예시)
file_list = """C:\\example1.dll
C:\\example2.dll"""

# 복사할 대상 폴더 경로
destination_folder = "C:\\example_folder"

if __name__ == "__main__":
    # 파일을 복사하는 함수 호출
    copy_files(file_list, destination_folder)
