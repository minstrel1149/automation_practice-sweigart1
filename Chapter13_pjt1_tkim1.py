import openpyxl
# 데이터 형태의 엑셀이므로 pandas를 활용하여 쉽게 구현
import pandas as pd
from pathlib import Path

p1 = Path.cwd() / 'attachments'
p2 = Path.cwd() / 'result_attachments'

# pandas의 read_excel() 함수 사용
censusDf = pd.read_excel(p1 / 'censuspopdata.xlsx')

# POP2010열을 정수로 형변환하고 groupby 활용
resultDf = (censusDf
.assign(POP2010=lambda df: df['POP2010'].astype(int))
.groupby(['State', 'County'], as_index=False)[['POP2010']]
.sum()
)

# engine=''으로 xlsxwriter 대신 openpyxl 이용
xlsxwriter = pd.ExcelWriter(p2 / 'resultcensuspotdata.xlsx', engine='openpyxl')
# index=False 필수 -> index를 안 넣도록
resultDf.to_excel(xlsxwriter, sheet_name='Sheet1', index=False)
xlsxwriter.close()