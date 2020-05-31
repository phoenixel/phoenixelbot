import discord
import datetime
from discord.ext import commands








client=discord.Client()
token='Njk2OTU5MDQ3MDQ3NDQ2NTkw.XowT0A.hhR4qQDtIWSma0T5AYapHT-1JMg'
@client.event
async def on_ready():
    print('----------------------------------------------------------------------------')
    print(f'| Client ID: {client.user.id}                                             |')
    print(f'| Client Name: {client.user.name}                                                       |')
    print(f'| Client Token: {str(token)} |')
    print('----------------------------------------------------------------------------\n\n=========================================\n\n')
    print(discord.__version__)
    print('피닉셀봇 부팅 완료.')
    
@client.event


async def on_message(message):
    if message.author.bot:
        return None
    if message.content=='마크하실?':
        await message.channel.send('난 봇이어서 마크를 못해. 파란트롤한테 부탁해봐') # 마크 안함.

        
    if message.content=='찐':
        await message.channel.send('응 자기소개')


    if message.content=='Wls':
        await message.channel.send('응 자기소개쥬?')


    if message.content=='삼도수군통제사':
        await message.channel.send('와! 삼도수군통제사! 우리의 킹갓제네럴엠페러캡짱 이순신 장군님도 지내셨던 직책이죠! 킹갓제네럴엠페러캡짱 이순신 장군님을 모르시는건 아니죠? 모른다고?||~~매국노시키~~||')

    if message.content.startswith=='씨발':
        await message.delete()
        await message.channel.send('어허 나쁜말')

    if message.content.startswith=='존나':
        await message.delete()
        await message.channel.send('어허 나쁜말')

    
    if message.content.startswith=='좆까':
        await message.delete()
        await message.channel.send('어허 나쁜말')

    
    if message.content.startswith=='꺼져':
        await message.delete()
        await message.channel.send('어허 나쁜말')
        
    if message.content.startswith=='샒':
        await message.delete()
        await message.channel.send('어허 나쁜말')
        
    if message.content.startswith=='fuck':
        await message.delete()
        await message.channel.send('어허 나쁜말')
        
    if message.content.startswith=='^^l발':
        await message.delete()
        await message.channel.send('어허 나쁜말')
    

    if message.content.startswith('ㅗ'):
        await message.delete()
        await message.channel.send('어허 나쁜말')
    
    if message.content.startswith('cuss'):
        guild = message.guild
        await guild.create_text_channel('cuss')
        
    if message.content.startswith('ct'):
        global ticketNumber
        ticketNumber = str(ticketNumber)
        name = 'ETC.'
        guild = message.guild
        category = discord.utils.get(guild.categories, name=name)
        ticketNumber = int(ticketNumber) + 1

        await guild.create_text_channel(f'Ticket-{ticketNumber}', category=category)

    if message.content.startswith('피닉셀?'):
        try:
            if message.content=='피닉셀? 자기소개해':
                await message.channel.send('내가 파란 트롤의 부계인줄 알고 있는 사람들이 있겠지만 나는 그 사람이 아니야. 난 봇이라구.') #자기소개

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!') #짐을 부름. 하지만 짐은 절대 대답 안함.

                
            if message.content=='피닉셀? 소레이 어때?':
                await message.channel.send('싫어.') #소레이

                
            if message.content=='피닉셀? 하돌 어때?':
                await message.channel.send('djfljlajlad')  #하돌

                
            if message.content=='피닉셀? 태롤 어때?':
                await message.channel.send('불쌍한 녀석이지.') #태준

                
            if message.content=='피닉셀? 픽셀 어때?':
                await message.channel.send('내 주인놈 말하는 건가? 대체적으로 마음에 들지만 썩 마음에 들지 않는 구석이 있단 말이지...') #나

                
            if message.content=='피닉셀? 륵마 어때?':
                await message.channel.send('-빨-')#정우

                
            if message.content=='피닉셀? 미육이 어때?':
                await message.channel.send('형제였으면 좋겠어. 저런 대단한 녀석을 만든 주인이라면 내 주인보다 훨 나을 테니까.')#미육

                
            if message.content=='피닉셀? 크시 어때?':
                await message.channel.send('질투가 많이 나지. 애들이 "크시야 크시야" 거리는데 아닐 리가.')#크시

                
            if message.content=='피닉셀? 짐 어때?':
                await message.channel.send('짐? 그 짐? 내 친구 짐? 별로. 내 형이지만 하나부터 열까지 마음에 안 들어. 하는 짓이라곤 대화에 끼어드는 거지.')#짐

                
            if message.content=='피닉셀? 징징이 어때?':
                await message.channel.send('참 유용한 녀석이야. 말이 안통하는게 흠이지만...')#징징이

                
            if message.content=='피닉셀? 꺼져':
                await message.channel.send('픽셀한테 컴 끄라고 해.')

                
            if message.content=='피닉셀? 사랑해':
                await message.channel.send('우웩, 브로맨스는 사양할게. 그런 이야기는 크시한테나 하라구.')

                
            if message.content=='피닉셀? 음악 틀어줘':
                await message.channel.send('짐도 말했지? 못한다고. 나도 못해. 이 주인놈은 만들 수 있는게 뭐지.')

                
            if message.content=='피닉셀? 이스터에그':
                await message.delete()
                await message.author.send('짐!')

                
            if message.content=='피닉셀? 안녕':
                await message.channel.send('미안하지만 난 안녕하지 못해.')

                
            if message.content=='피닉셀? 3n':
                await message.channel.send('돈슨, NC, 넷마블.')

                
            if message.content=='피닉셀? 임베드 테스트':
                embed = discord.Embed(title="제목", description="설명", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다
                await message.channel.send("이게 임베드라는 거야.", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니



                
            if message.content=='피닉셀? 태준':
                await message.channel.send('@태준빠아악#5462 ')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                await message.channel.send('@태준빠아악#5462 !')
                
                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 자기소개해':
                await message.channel.send('내가 파란 트롤의 부계인줄 알고 있는 사람들이 있겠지만 나는 그 사람이 아니야. 난 봇이라구.')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 저리가':
                await message.channel.send('그건 짐한테나 하는 이야기 아니었어?')

                
            if message.content=='피닉셀? 바보':
                await message.channel.send('멍청이.')

                
            if message.content=='피닉셀? 어그로':
                await message.channel.send('미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..')

                
            if message.content=='피닉셀? 유튜브채널':
                await message.channel.send('https://www.youtube.com/channel/UCug2sX3RAFaWxPjRjf2u63g')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 자기소개해':
                await message.channel.send('내가 파란 트롤의 부계인줄 알고 있는 사람들이 있겠지만 나는 그 사람이 아니야. 난 봇이라구.')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 짐 좀 불러봐':
                await message.channel.send('짐!')

                
            if message.content=='피닉셀? 뭐해?':
                await message.channel.send('아무것도.')


   


           

       

                





        except:
            print('에러가 발생하였습니다') 
client.run(token)

