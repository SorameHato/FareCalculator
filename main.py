

print(u'\u001b[38;5;51mSeolbin\u001b[0mRapidEx \u001b[38;5;33m운임 계산기\u001b[0m\nCopyright 2011-2023 \u001b[38;5;45mSky\u001b[38;5;57mWare\u001b[0m, \u001b[38;5;51m하늘토끼\u001b[0m(\u001b[38;5;39mghwls030306@s-r.ze.am\u001b[0m) All \u001b[38;5;219mRights\u001b[0m Reserved.\n데이터를 불러오고 있는 중입니다...\n기준 OS\n\t우유나라 35 \u001b[38;5;34msame \u001b[0m(Super Advanced Millenium Edition) \u001b[38;5;27mGawr Gura \u001b[0mEdition for kiosk system 64-bit,\n\t우유나라 36 \u001b[38;5;34mame \u001b[38;5;208mP\u001b[38;5;220ml\u001b[38;5;40mu\u001b[38;5;33ms\u001b[0m! (Advanced Millenium Edition Enhanced Version) for kiosk&industrial system 64-bit,\n\t우유나라 37 \u001b[38;5;57mMilkyway\u001b[38;5;231mSnowflake\u001b[0m 모든 버전 64-bit\n기준 SCI-TVM 버전 : SNX:H:B:*:2023030406:0017')

print('기동 준비 완료\n')
while(True):
    print(u'조회하실 노선의 코드를 입력하여 주십시오. [\u001b[38;5;40m시온어반(통합) \u001b[38;5;213m1090\u001b[38;5;40m, 치노시온 \u001b[38;5;213m205\u001b[38;5;40m, 계산 및 종료 \u001b[38;5;213mQ 또는 0\u001b[0m]')
    route = input('노선 코드 : ')
    if (route == 'q' or route == 'Q' or route == '0'):
        break
    else:
        pass