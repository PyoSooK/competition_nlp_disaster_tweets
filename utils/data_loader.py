import pandas as pd
import os

def load_and_validate_data(file_path):
    """
    주어진 경로에서 CSV 파일을 로드하고 유효성을 검사합니다.
    """
    if not os.path.exists(file_path):
        print(f"❌ 오류: 파일을 찾을 수 없습니다. 경로를 확인해 주세요: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        print(f"✅ 성공: 파일 '{os.path.basename(file_path)}'을 성공적으로 불러왔습니다.")
        print("--- 데이터 미리보기 ---")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ 오류: 데이터 로드 중 예상치 못한 에러 발생: {e}")
        return None