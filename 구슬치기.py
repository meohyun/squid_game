import random
import time

running = True
my_bead = 10
computer_bead = 10
attack_turn = True



#  선공,후공 정하기
print("구슬치기 게임을 시작하겠습니다.")

# time.sleep(2)

print("시작하기에 앞서 가위바위보로 순서를 정하겠습니다.")

# time.sleep(2)


# 가위바위보 

while running:
    # 가위바위보
    rsp = input("무엇을 내시겠습니까?(가위,바위,보 중 선택): ")
    Rsp = ['가위','바위','보']
    Rsp_choice = random.sample(Rsp,1)
    F_L = ['선공' , '후공']
    computer_choice = random.sample(F_L,1)


    if rsp == Rsp_choice[0]:
        print("비겼으므로 다시 내주세요.")
        continue

    if rsp == '가위' and Rsp_choice[0] == '보':
        my_choice = input("이겼습니다. 선공,후공 중 하나를 선택해주세요 : ")
    

    if rsp == '가위' and Rsp_choice[0] == '바위':
        print("졌습니다. 컴퓨터가 선,후공중 정합니다.")
        time.sleep(2)
        print(f" 컴퓨터가 {computer_choice[0]}입니다.")
        

    if rsp == '바위' and Rsp_choice[0] == '가위':
        my_choice = input("이겼습니다. 선공,후공 중 하나를 선택해주세요 : ")
       

    if rsp == '바위' and Rsp_choice[0] == '보':
        print("졌습니다. 컴퓨터가 선,후공중 정합니다.")
        time.sleep(2)
        print(f"컴퓨터가 {computer_choice[0]}입니다.")
        

    if rsp == '보' and Rsp_choice[0] == '바위':
        my_choice = input("이겼습니다. 선공,후공 중 하나를 선택해주세요 : ")
        

    if rsp == '보' and Rsp_choice[0] == '가위':
        print("졌습니다. 컴퓨터가 선,후공중 정합니다.")
        time.sleep(2)
        print(f"컴퓨터가 {computer_choice[0]}입니다.")
       
    break    

# 구슬치기 룰 설명

print()

print("구슬치기의 룰을 설명하겠습니다.")

print()
print()
print(""" 
각 플레이어들은 10개씩의 구슬을 가지고 시작합니다.
선공인 플레이어가 구슬을 몇개 움켜쥘지 정합니다. 
그리고 후공인 플레이어가 자신의 구슬을 배팅합니다. 그 다음 구슬의 갯수가 홀인지 짝인지 말합니다.
맞추게되면 배팅한 갯수만큼 상대의 구슬을 후공인 플레이어가 가지고 틀리게되면 선공인 플레이어가 갖습니다.
한 사람이 모든 구슬을 잃을 경우 게임은 종료되며 20개의 구슬을 가진 플레이어가 승리합니다.
    """)

# 구슬치기

while running:
    nums = [1,2,3,4,5,6,7,8,9,10]
    computer_nums = random.sample(nums,1)
    choice = ['홀','짝']
    computer_choice_hz = random.sample(choice,1)
    
    # 구슬치기 선,후공에 따라 다름
    try :
        if my_choice == '선공':
            if attack_turn :
                my_choices = int(input("구슬의 갯수를 정해주세요(숫자만 입력) : "))
                
                print()

                
                if my_choices > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                
                print(f"""
당신은 {my_choices}개를 선택하셨습니다.
컴퓨터가 선택할 동안 기다려 주세요!
                """)
                time.sleep(2)

                print(f"""
컴퓨터의 선택은 {computer_choice_hz[0]} 입니다.
                """)

                # 홀 짝 맞는지 확인
                if my_choices % 2 == 0:
                    answer = '짝'
                else:
                    answer = '홀'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20
                        
                    print(f"""
컴퓨터가 맞췄습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
컴퓨터가 틀렸습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                attack_turn = False

            # 다음턴으로 넘어감.        
            else:
                my_selection = input("홀,짝 중 정해주세요 : ")
                print()
                
                if my_selection != '홀' and my_selection != '짝':
                    print("홀,짝만 입력해주세요.")
                    continue
                print()

                my_choice_2 = int(input("배팅할 구슬의 갯수를 정해주세요 : "))
                print()
                
                
                if my_choice_2 > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                print("컴퓨터가 구슬의 갯수를 정하는 중입니다. 기다려 주세요.")
                time.sleep(2)


                if int(computer_nums[0]) % 2 == 0:
                    answer = '짝'
                
                else:
                    answer = '홀'


                print(f"컴퓨터의 구슬은 {computer_nums[0]}개 였습니다.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 맞췄습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                
                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 틀렸습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                attack_turn = True


        if my_choice == '후공':
            if attack_turn:
                my_selection = input("홀,짝 중 정해주세요 : ")
                print()
                
                if my_selection != '홀' and my_selection != '짝':
                    print("홀,짝만 입력해주세요.")
                    continue
                print()

                my_choice_2 = int(input("배팅할 구슬의 갯수를 정해주세요 : "))
                print()
                
                
                if my_choice_2 > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                print("컴퓨터가 구슬의 갯수를 정하는 중입니다. 기다려 주세요.")
                time.sleep(2)

                if int(computer_nums[0]) % 2 == 0:
                    answer = '짝'
                
                else:
                    answer = '홀'

                print(f"컴퓨터의 구슬은 {computer_nums[0]}개 였습니다.")
                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 맞췄습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                

                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 틀렸습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)

                attack_turn = False
            
            # 턴이 바뀜
            else:
                my_choices = int(input("구슬의 갯수를 정해주세요(숫자만 입력) : "))
                
                print()

                
                if my_choices > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()
                
                if my_choices <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                
                print(f"""
당신은 {my_choices}개를 선택하셨습니다.
컴퓨터가 선택할 동안 기다려 주세요!
                """)
                time.sleep(2)

                print(f"""
컴퓨터의 선택은 {computer_choice_hz[0]} 입니다.
                """)

                # 홀 짝 맞는지 확인
                if my_choices % 2 == 0:
                    answer = '짝'
                else:
                    answer = '홀'
                

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20
                        
                    print(f"""
컴퓨터가 맞췄습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                

                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
컴퓨터가 틀렸습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                attack_turn = True

                

    except NameError:
        if computer_choice[0] == '선공':
            if attack_turn:
                my_selection = input("홀,짝 중 정해주세요 : ")
                print()
                
                if my_selection != '홀' and my_selection != '짝':
                    print("홀,짝만 입력해주세요.")
                    continue
                print()

                my_choice_2 = int(input("배팅할 구슬의 갯수를 정해주세요 : "))
                print()

                
                if my_choice_2 > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                print("컴퓨터가 구슬의 갯수를 정하는 중입니다. 기다려 주세요.")
                time.sleep(2)

            
                if int(computer_nums[0]) % 2 == 0:
                    answer = '짝'
                
                else:
                    answer = '홀'

                print(f"컴퓨터의 구슬은 {computer_nums[0]}개 였습니다.")

                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 맞췄습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)

                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 틀렸습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                attack_turn = False

            # 턴이 바뀜
            else:
                my_choices = int(input("구슬의 갯수를 정해주세요(숫자만 입력) : "))
            print()


            if my_choices > my_bead:
                print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                continue
            print()

            if my_choices <= 0 :
                print("0과 음수는 입력할 수 없습니다.")
                continue
            print()


            print(f"""
당신은 {my_choices}개를 선택하셨습니다.
컴퓨터가 선택할 동안 기다려 주세요!
            """)
            time.sleep(2)

            # 홀 짝 맞는지 확인
            if my_choices % 2 == 0:
                answer = '짝'
            else:
                answer = '홀'

            print(f"컴퓨터의 선택은 {computer_choice_hz[0]} 입니다.")

            time.sleep(2)

            if answer == computer_choice_hz[0]:
                my_bead -= computer_nums[0]
                computer_bead += computer_nums[0]

                # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                if my_bead < 0:
                    my_bead = 0
                if computer_bead < 0 :
                    computer_bead = 0
                if my_bead > 20:
                    my_bead = 20 
                if computer_bead > 20:
                    computer_bead = 20

                print(f"""
컴퓨터가 맞췄습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
""")

                
            else:
                my_bead += computer_nums[0]
                computer_bead -= computer_nums[0]

                # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                if my_bead < 0:
                    my_bead = 0
                if computer_bead < 0 :
                    computer_bead = 0
                if my_bead > 20:
                    my_bead = 20 
                if computer_bead > 20:
                    computer_bead = 20
                    
                print(f"""
컴퓨터가 틀렸습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
""")
                attack_turn = True


                
        if computer_choice[0] == '후공':
            if attack_turn:
                my_choices = int(input("구슬의 갯수를 정해주세요(숫자만 입력) : "))
                print()


                if my_choices > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()

                if my_choices <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()


                print(f"""
    당신은 {my_choices}개를 선택하셨습니다.
    컴퓨터가 선택할 동안 기다려 주세요!
                """)
                time.sleep(2)

                # 홀 짝 맞는지 확인
                if my_choices % 2 == 0:
                    answer = '짝'
                else:
                    answer = '홀'

                print(f"컴퓨터의 선택은 {computer_choice_hz[0]} 입니다.")

                time.sleep(2)

                if answer == computer_choice_hz[0]:
                    my_bead -= computer_nums[0]
                    computer_bead += computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
    컴퓨터가 맞췄습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
    당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
    """)

                    
                else:
                    my_bead += computer_nums[0]
                    computer_bead -= computer_nums[0]

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20
                        
                    print(f"""
    컴퓨터가 틀렸습니다. 컴퓨터가 배팅한 구슬은 {computer_nums[0]}개입니다. 
    당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
    """)
                attack_turn = False
            # 턴이 바뀜
            else:
                my_selection = input("홀,짝 중 정해주세요 : ")
                print()
                
                if my_selection != '홀' and my_selection != '짝':
                    print("홀,짝만 입력해주세요.")
                    continue
                print()

                my_choice_2 = int(input("배팅할 구슬의 갯수를 정해주세요 : "))
                print()

                
                if my_choice_2 > my_bead:
                    print("소유한 구슬의 갯수보다 많이 걸수 없습니다.")
                    continue
                print()

                if my_choice_2 <= 0 :
                    print("0과 음수는 입력할 수 없습니다.")
                    continue
                print()

                print("컴퓨터가 구슬의 갯수를 정하는 중입니다. 기다려 주세요.")
                time.sleep(2)

            
                if int(computer_nums[0]) % 2 == 0:
                    answer = '짝'
                
                else:
                    answer = '홀'

                print(f"컴퓨터의 구슬은 {computer_nums[0]}개 였습니다.")

                time.sleep(2)


                if answer == my_selection:
                    my_bead += my_choice_2
                    computer_bead -= my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 맞췄습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)

                
                else:
                    my_bead -= my_choice_2
                    computer_bead += my_choice_2

                    # 구슬의 개수가 음수 거나 20개 이상일 경우 초기화

                    if my_bead < 0:
                        my_bead = 0
                    if computer_bead < 0 :
                        computer_bead = 0
                    if my_bead > 20:
                        my_bead = 20 
                    if computer_bead > 20:
                        computer_bead = 20

                    print(f"""
당신이 틀렸습니다. 내가 배팅한 구슬은 {my_choice_2}개입니다. 
당신의 구슬의 갯수는 {my_bead}개입니다. 컴퓨터의 구슬의 갯수는 {computer_bead}개입니다.
                    """)
                attack_turn = True

                            
    # 게임 종료
    if my_bead <= 0:

        print("당신은 탈락입니다.")
        time.sleep(3)
        running = False
    
    if computer_bead <=0:
        print("당신의 승리입니다.")
        time.sleep(3)
        running = False

    
