from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
import os

OUT='assets/모세종_이력서.pdf'
PHOTO='assets/증명사진.jpg'
W,H=A4

FONT='/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
BOLD='/usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf'
MONO='/usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf'
pdfmetrics.registerFont(TTFont('NBG', FONT))
pdfmetrics.registerFont(TTFont('NBG-B', BOLD))
pdfmetrics.registerFont(TTFont('MONO', MONO))

NAVY=HexColor('#1C3266')
PURPLE=HexColor('#6257FF')
PURPLE2=HexColor('#7A6BFF')
LAV=HexColor('#F2EFFF')
SIDE=HexColor('#F5F7FB')
BORDER=HexColor('#D8E0EB')
TEXT=HexColor('#182234')
MUTED=HexColor('#68758A')
LIGHTTXT=HexColor('#8792A6')
WHITE=white

c=canvas.Canvas(OUT, pagesize=A4)
c.setTitle('모세종 - Python FastAPI 기반 AI 서비스 백엔드 개발자')
c.setAuthor('모세종')

def ypdf(top): return H-top

def rr(x, top, w, h, r=10, fill=WHITE, stroke=BORDER, sw=0.8):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(sw)
    c.roundRect(x, H-top-h, w, h, r, fill=1, stroke=1)

def text(x, top, s, size, font='NBG', color=TEXT, align='left'):
    c.setFillColor(color); c.setFont(font,size)
    yy=H-top-size
    if align=='right': c.drawRightString(x, yy, s)
    elif align=='center': c.drawCentredString(x, yy, s)
    else: c.drawString(x, yy, s)

def line_wrap(s, font, size, maxw):
    out=[]; cur=''
    for ch in s:
        test=cur+ch
        if stringWidth(test,font,size)<=maxw:
            cur=test
        else:
            if cur: out.append(cur.rstrip())
            cur=ch.lstrip() if ch==' ' else ch
    if cur: out.append(cur.rstrip())
    return out

def para(x, top, s, size, maxw, leading=None, font='NBG', color=TEXT, max_lines=None):
    if leading is None: leading=size*1.35
    lines=line_wrap(s,font,size,maxw)
    if max_lines: lines=lines[:max_lines]
    for i,ln in enumerate(lines): text(x, top+i*leading, ln, size, font, color)
    return len(lines)*leading

def section_title(x, top, label):
    c.setFillColor(PURPLE)
    c.roundRect(x, H-top-16, 4.2, 16, 2.1, fill=1, stroke=0)
    text(x+11, top-1, label, 13.4, 'NBG-B', TEXT)

def chip(x, top, w, label, active=False):
    fill=WHITE
    stroke=PURPLE if active else BORDER
    color=PURPLE if active else MUTED
    rr(x, top, w, 18, 9, fill, stroke, 0.8)
    text(x+w/2, top+4.2, label, 6.9, 'NBG', color, 'center')

def tagbar(x, top, w, s, size=7.0):
    c.setFillColor(LAV); c.roundRect(x, H-top-20, w, 20, 10, fill=1, stroke=0)
    text(x+10, top+5.2, s, size, 'NBG-B', PURPLE)

def resultbar(x, top, w, s, size=6.9):
    c.setFillColor(LAV); c.roundRect(x, H-top-18, w, 18, 9, fill=1, stroke=0)
    text(x+10, top+4.5, s, size, 'NBG-B', PURPLE)

def bullet(x, top, s, size, maxw, color=TEXT):
    c.setFillColor(PURPLE); c.circle(x+2.2, H-top-4.2, 1.6, fill=1, stroke=0)
    para(x+10, top, s, size, maxw-10, leading=size*1.27, color=color)

c.setFillColor(NAVY); c.rect(0,H-112,W,112,fill=1,stroke=0)
c.saveState()
try: c.setFillAlpha(0.08)
except: pass
c.setFillColor(HexColor('#2B4279')); c.circle(510,H-28,72,fill=1,stroke=0); c.setFillColor(HexColor('#263D72')); c.circle(438,H-4,44,fill=1,stroke=0)
c.restoreState()
text(34,24,'모세종',25,'NBG-B',WHITE)
text(34,56,'Python · FastAPI 기반 AI 서비스 백엔드 개발자',11.9,'NBG-B',WHITE)
text(34,79,'약 9년의 물류·운영 현장 경험을 바탕으로 문제를 데이터 흐름으로 정리하고,',7.6,'NBG',HexColor('#E8EDF9'))
text(34,90,'Python/FastAPI 기반 API·DB·AI 기능을 실제 서비스로 연결합니다.',7.6,'NBG',HexColor('#E8EDF9'))
rr(492,20,72,80,10,WHITE,WHITE,0)
img=ImageReader(PHOTO)
c.drawImage(img,496,H-96,64,72,preserveAspectRatio=True,anchor='c',mask='auto')
contact_top=121
items=[('1995.08.24',34,0),('010-5413-4635',135,0),('ahtpwhd95@gmail.com',252,1),('GitHub · mosejong',388,0),('Web Resume',512,0)]
for i,(s,x,is_mono) in enumerate(items):
    if i>0:
        c.setStrokeColor(HexColor('#DCE2EA')); c.setLineWidth(0.6); c.line(x-15,H-contact_top-2,x-15,H-contact_top-14)
    text(x,contact_top,s,7.8,'NBG',HexColor('#57657A'))
c.linkURL('https://github.com/mosejong',(388,H-contact_top-13,485,H-contact_top+2),relative=0,thickness=0)
c.linkURL('https://mosejong.github.io/mosejong/resume.html',(512,H-contact_top-13,568,H-contact_top+2),relative=0,thickness=0)

cards=[('8년 9개월','물류·운영 현장 경력'),('우수수료생','이스트캠프 KDT AI Human 4기'),('대상','최종 프로젝트 · 나의 진로 아카데미아'),('최우수상','1차 프로젝트 · SchoolBridge')]
x0=34; gap=9; cardw=(W-68-gap*3)/4
for i,(a,b) in enumerate(cards):
    x=x0+i*(cardw+gap); rr(x,145,cardw,43,10,WHITE,BORDER,0.8)
    text(x+12,154,a,11.6,'NBG-B',PURPLE)
    text(x+12,172,b,6.6,'NBG',MUTED)

left_x=34; left_w=190; gap_col=14; right_x=left_x+left_w+gap_col; right_w=W-right_x-34
main_top=204; main_bottom=690
rr(left_x,main_top,left_w,main_bottom-main_top,14,SIDE,BORDER,0.8)
section_title(left_x+14,219,'Profile')
text(left_x+15,255,'현장 경험을 가진 경력전환형 개발자',8.7,'NBG-B',TEXT)
text(left_x+15,279,'문제를 요구사항과 데이터 흐름으로 정리하고,',7.7,'NBG',MUTED)
text(left_x+15,289.2,'AI 기능이 실제 서비스에서 안정적으로 동작하도록',7.7,'NBG',MUTED)
text(left_x+15,299.4,'API·DB·테스트·배포까지 연결합니다.',7.7,'NBG',MUTED)
section_title(left_x+14,336,'Education')
rr(left_x+15,369,left_w-30,76,10,WHITE,BORDER,0.7)
text(left_x+27,379,'이스트소프트 K-Digital Training',8.8,'NBG-B',TEXT)
text(left_x+27,400,'AI Human 4기 · 800시간',7.5,'NBG',MUTED)
text(left_x+27,417,'2026.03 - 2026.07',7.3,'NBG',MUTED)
text(left_x+27,428,'우수수료생',7.8,'NBG-B',PURPLE)
rr(left_x+15,453,left_w-30,44,10,WHITE,BORDER,0.7)
text(left_x+27,463,'진건고등학교',8.5,'NBG-B',TEXT)
text(left_x+27,481,'졸업',7.4,'NBG',MUTED)
section_title(left_x+14,514,'Core Stack')
chipw=49.5; chipgap=6.5; sx=left_x+15
chip_rows=[[('Python',1),('FastAPI',1),('REST API',1)],[('PostgreSQL',0),('pgvector',0),('Redis',0)],[('Docker',0),('Nginx',0),('GitHub Actions',0)],[('pytest',0),('RAG',0),('TTS',0)]]
for r,row in enumerate(chip_rows):
    y=543+r*25
    for j,(lab,act) in enumerate(row):
        w=chipw if lab!='GitHub Actions' else 58
        x=sx+j*(chipw+chipgap)
        if lab=='GitHub Actions': x=sx+2*(chipw+chipgap)-4
        chip(x,y,w,lab,bool(act))

CARD_UP=1.0
def cu(v): return v-CARD_UP
section_title(right_x,219,'Projects')
x=right_x; y=252; w=right_w; h=124
rr(x,y,w,h,14,WHITE,HexColor('#C9C2FF'),1.2)
text(x+16,cu(y+12),'나의 진로 아카데미아',10.8,'NBG-B',TEXT)
text(x+w-16,cu(y+13),'Reporting · Data Pipeline',7.2,'NBG-B',PURPLE,'right')
text(x+16,cu(y+33),'2026.07.06 - 07.31 · 6인 팀 · KDT Final Project',7.1,'NBG',MUTED)
tagbar(x+16,cu(y+49),w-32,'담당 · 직무/NCS 데이터 구조화 · 개인화 추천 근거 · PDF 리포트 · 커리어넷 API · CI',6.8)
bullet(x+16,cu(y+77),'AI 상담·가상 직무 체험 기록을 근거 기반 진로 리포트로 연결',6.9,w-32)
bullet(x+16,cu(y+91),'역량 레이더·AI 해석·근거 각주·공개 직업정보를 PDF 리포트로 구현',6.9,w-32)
resultbar(x+16,cu(y+104),w-32,'Project-wide · 직무군 38 · 세부직업 204 · 시나리오 37 · pytest 564 · 직무 오염률 12.5% -> 0%',6.45)
y=383; h=108
rr(x,y,w,h,14,WHITE,BORDER,0.9)
text(x+16,cu(y+12),'SchoolBridge',10.5,'NBG-B',TEXT)
text(x+w-16,cu(y+13),'Translation · TTS Pipeline',7.2,'NBG-B',PURPLE,'right')
text(x+16,cu(y+32),'2026.04.24 - 05.13 · 5인 팀 · 1차 프로젝트 최우수상',7.0,'NBG',MUTED)
tagbar(x+16,cu(y+47),w-32,'담당 · NLLB 8개 언어 · 학교 Glossary · 핵심정보 보존 · Edge-TTS · 실기기 E2E',6.9)
bullet(x+16,cu(y+75),'핵심정보 보존·학교 Glossary 검수로 오역을 보정하고 FastAPI/TTS 흐름 연결',7.0,w-32)
resultbar(x+16,cu(y+88),w-32,'Result · 번역 품질 39.0 -> 89.6 · pytest 27 · Android 실기기 E2E',6.6)
row_y=498; row_h=122; inner_gap=10; half=(w-inner_gap)/2
rr(x,row_y,half,row_h,13,WHITE,BORDER,0.9)
text(x+14,cu(row_y+11),'Rainbow Bridge',9.8,'NBG-B',TEXT)
text(x+14,cu(row_y+29),'Team Lead · Backend',6.8,'NBG-B',PURPLE)
text(x+14,cu(row_y+45),'2026.06.02 - 06.19 · 6인 팀',6.8,'NBG',MUTED)
para(x+14,cu(row_y+61),'담당 · API 통합 · 일정 조율 · 배포 · 안전성 평가',6.6,half-28,8.3,'NBG-B',PURPLE,2)
para(x+14,cu(row_y+84),'AI 메시지·TTS·영상·미션·리포트 흐름 통합',6.7,half-28,8.4,'NBG',TEXT,1)
resultbar(x+14,cu(row_y+98),half-28,'팀 전체 · 골든셋 39 -> 289 · 고위험 미탐 0',6.2)
x2=x+half+inner_gap
rr(x2,row_y,half,row_h,13,WHITE,BORDER,0.9)
text(x2+14,cu(row_y+11),'공공조달 기반 물류 거점 분석',9.1,'NBG-B',TEXT)
text(x2+14,cu(row_y+29),'Solo · Data Pipeline',6.7,'NBG-B',PURPLE)
text(x2+14,cu(row_y+45),'2026.05.13 - 07.21 · 1인 프로젝트',6.8,'NBG',MUTED)
text(x2+14,cu(row_y+61),'담당 · 수집/정제 · 지표 설계 · 분류 · AI 해석',6.4,'NBG-B',PURPLE)
text(x2+14,cu(row_y+72),'Streamlit 대시보드 전체 수행',6.4,'NBG-B',PURPLE)
text(x2+14,cu(row_y+87),'입찰 10만 · 계약 3.8만 · 급식 73.4만건 분석',6.7,'NBG',TEXT)
resultbar(x2+14,cu(row_y+99),half-28,'공공조달 AI 경진대회 · 대면심사 진출',6.3)
hi_y=626; hi_h=62
rr(x,hi_y,w,hi_h,13,WHITE,BORDER,0.9)
text(x+16,cu(hi_y+10),'How I Work',10.4,'NBG-B',TEXT)
text(x+w-16,cu(hi_y+12),'Problem -> Design -> Build -> Verify',7.2,'NBG-B',PURPLE,'right')
text(x+16,cu(hi_y+31),'정상 흐름뿐 아니라 실패 케이스와 운영 제약까지 함께 설계합니다.',7.0,'NBG',MUTED)
text(x+16,cu(hi_y+43),'테스트와 정량 지표로 개선 전후를 검증합니다.',7.0,'NBG',MUTED)
career_y=704
section_title(34,career_y,'Career · 주요 경력')
text(W-34,career_y+2,'기타 자동차부품 물류·운영 경력 포함 · 총 경력 8년 9개월',6.7,'NBG',MUTED,'right')
cy=730; cw=(W-68-10)/2; ch=88
for idx,(company,date,role,desc) in enumerate([('(주)정우금속이엔지','2021.02.22 - 2026.01.30','물류팀 · 대리','입출고·재고·납기·사무/전산 운영. 월 재고손실률 10% 이상 문제를 보고하고 관리 체계를 개선해 5% 미만 안정화에 기여.'),('(주)미래부품','2017.06.05 - 2020.01.02','구매팀 · 대리','매입·발주·재고·지역별 납품 담당. 팀장 공석 기간 업무를 대행하며 재고·매입 보고서 작성과 데이터 분석 수행.')]):
    cx=34+idx*(cw+10)
    rr(cx,cy,cw,ch,12,WHITE,BORDER,0.9)
    text(cx+14,cy+12,company,9.6,'NBG-B',TEXT)
    text(cx+cw-14,cy+13,date,6.8,'NBG',MUTED,'right')
    text(cx+14,cy+33,role,7.5,'NBG-B',PURPLE)
    para(cx+14,cy+53,desc,6.9,cw-28,8.6,'NBG',TEXT,3)
text(W-34,828,'Updated 2026.08 · 상세 역할·근거·코드는 GitHub에서 확인할 수 있습니다.',6.0,'NBG',HexColor('#9AA5B5'),'right')
c.showPage(); c.save()
print(OUT)
