2. 김종원,이창재,홍성대,한승진 4명을 순서대로 사원번호를 부여하여 결과를 딕셔너리 형태로 출력하라.
  - 사원번호 리스트 = [NM001, NM002, NM003, NM004]
  - 결과 예시 : {김종원: NM001, ... }
  


def main():
    name = ['dolbam','ianlee','sdhong','john']
    nums = ['NM001','NM002','NM003','NM004']
    result = {}
    for i in name:
        for j in nums:
            if not j in result.values():
                result[i] = j
                continue
    print result

if __name__ == '__main__':
    main()