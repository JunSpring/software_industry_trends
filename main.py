import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

it_util_index = pd.read_csv("data\\IT_활용지수_총괄표_20211212172442.csv")
it_production = pd.read_csv("data\\1-1-1. SW 생산 현황 (연도별).csv")
it_export = pd.read_csv("data\\1-2-1. SW 수출 현황 (연도별).csv")
it_corporation = pd.read_csv("data\\1-4-1. SW기업 현황.csv")
it_new_corporation = pd.read_csv("data\\1-4-3. SW신설법인 현황.csv")

it_util_index["산업내 IT활용지수"] = (it_util_index["농림어업"] + it_util_index["광업"] + it_util_index["제조업"] + it_util_index[
    "전기/가스업"] + it_util_index["원료재생/환경복원업"] + it_util_index["건설업"] + it_util_index["도소매업"] + it_util_index["운수업"] + \
                               it_util_index["숙박/음식점업"] + it_util_index["출판/방송/정보통신업"] + it_util_index["금융/보험업"] + \
                               it_util_index["부동산/임대업"] + it_util_index["전문 과학/기술서비스업"] + it_util_index["사업서비스업"] + \
                               it_util_index["기타 서비스업"]) / 15

it_new_corporation["소프트웨어 법인"] = it_new_corporation["ICT 서비스"] + it_new_corporation["기기"] + it_new_corporation["SW"]

plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

ax = plt.gca()
it_production.plot(kind='line', x='연도', y='패키지SW', ax=ax)
it_production.plot(kind='line', x='연도', y='IT서비스', ax=ax)
it_production.plot(kind='line', x='연도', y='게임SW', ax=ax)
plt.title("SW 생산 현황")
it_util_index.plot(kind='bar', x='연도', y='산업내 IT활용지수')
plt.title("산업내 IT활용지수")
plt.show()

ax = plt.gca()
it_export.plot(kind='line', x='연도', y='패키지SW', ax=ax)
it_export.plot(kind='line', x='연도', y='IT서비스', ax=ax)
it_export.plot(kind='line', x='연도', y='게임SW', ax=ax)
plt.title("SW 수출 현황")
it_util_index.plot(kind='bar', x='연도', y='산업내 IT활용지수')
plt.title("산업내 IT활용지수")
plt.show()

ax = plt.gca()
it_corporation.plot(kind='line', x='연도', y='패키지SW', ax=ax)
it_corporation.plot(kind='line', x='연도', y='IT서비스', ax=ax)
it_corporation.plot(kind='line', x='연도', y='게임SW', ax=ax)
plt.title("SW 기업 현황")
it_util_index.plot(kind='bar', x='연도', y='산업내 IT활용지수')
plt.title("산업내 IT활용지수")
plt.show()

it_new_corporation.plot(kind='line', x='연도', y='소프트웨어 법인')
plt.title("신SW 사업 추진 현황")
it_util_index.plot(kind='bar', x='연도', y='산업내 IT활용지수')
plt.title("산업내 IT활용지수")
plt.show()
