define config.skip_delay = 75


define config.keymap['auto'] = None

define config.keymap['space'] = None
define config.keymap['rollback'] = None
define config.keymap['return'] = None
#define config.keymap['skip'] = None
define config.keymap['show_menu'] = None
define config.keymap['menu'] = None

define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]
image beaver = Movie(play="video/beaver.webm",loop=False)
label splashscreen:
    # громкость по умолчанию
    python:
        # при первом запуске
        if not persistent.set_volumes:
            persistent.set_volumes = True
            # музыку потише
            _preferences.volumes['music'] = .5
            _preferences.volumes['sfx'] = .5
            # игра на весь экран
            _preferences.fullscreen = True
    return
# The script of the game goes in this file.


# Declare characters used by this game. 20520610 The color argument colorizes the
# name of the character.
# $ Zeil = Character('Zeil', color="#E03B8B")
image i_lao sad_right=At('lao_sad_right',sprite_highlight('lao'))
image i_lao sad_left =At('lao_sad_left',sprite_highlight('lao'))

image i_lao thinking=At('lao_thinking',sprite_highlight('lao'))
image i_lao young=At('lao_young',sprite_highlight('lao'))

image i_samurai neutral_right=At('samurai_neutral_right',sprite_highlight('samurai'))
image i_samurai neutral_left=At('samurai_neutral_left',sprite_highlight('samurai'))

image i_nhi smile_right=At('nhi_smile_right',sprite_highlight('nhi'))
image i_nhi smile_left=At('nhi_smile_left',sprite_highlight('nhi'))
image i_nhi smile_right_vr=At('nhi_smile_right_vr',sprite_highlight('nhi'))
image i_nhi smile_right_pixcel=At('nhi_smile_right_pixcel',sprite_highlight('nhi'))

image i_nhi angry_left=At('nhi_angry_left',sprite_highlight('nhi'))
image i_nhi shock_right=At('nhi_shock_right',sprite_highlight('nhi'))
image i_nhi shock_right_pixcel=At('nhi_shock_right_pixcel',sprite_highlight('nhi'))
image i_nhi shock_right2=At('nhi_shock_right2',sprite_highlight('nhi'))

image i_lao serious_right=At('lao_serious_right',sprite_highlight('lao'))
image i_lao serious_left=At('lao_serious_left',sprite_highlight('lao'))
image i_lao serious_left_pixcel=At('lao_serious_left_pixcel',sprite_highlight('lao'))
image i_lao serious_left_vr=At('lao_serious_left_vr',sprite_highlight('lao'))


define character_lao=Character('Lao',image='i_lao',callback=name_callback,cb_name='lao', color="#563be0")
define character_samurai=Character('Samurai',image='i_samurai neutral_left',callback=name_callback,cb_name='samurai', color="#cd1313")
define character_nhi=Character('Nhi',image='i_nhi',callback=name_callback,cb_name='nhi', color="#e03bc2")
# The game start here:
screen stop_scr():
    key "dismiss" action [[]]
init python:
    # Định nghĩa một hàm để tắt click trong quá trình transition
    def disable_click():
        renpy.transition(allow_click=False)
label start:
    
    #$ renpy.movie_cutscene("video/videolao.ogg")
    # play movie "video/videolao.webm" loop

    #show i_lao young at center
    #character_lao "I'm in front of an animated background!"
    #play movie "video/bocchi.ogv"  loop
    #show movie with dissolve
    #show i_lao young at center with dissolve
    # character_lao "I'm in front of an animated background2!"
    #  hide movie with dissolve
    #stop movie
    

    play music "medieval.mp3" fadein 2.0 volume 0.05
    "Hướng dẫn chơi: \nClick \"chuột trái\" để điều khiển, tiếp tục câu chuyện.\n Nhấn \"Esc\"  để mở setting."
    
    
    "Visual Novel là một loại tiểu thuyết tương tác với tính năng rõ rệt, thường sử dụng phong cách nghệ thuật của anime hoặc đôi khi là ảnh thật hay một số cảnh quay video. (Wikipedia) (click chuột để tiếp tục.)"

    "Visual Novel sau đây là một tác phẩm giả tưởng chứa đựng ngôn ngữ chỉ dành cho lứa tuổi 18 trở lên, khán giả hãy cân nhắc kỹ. Visual Novel thuộc thể loại Hài hước (Comedy), Tâm lý (Psychological), Triết học (Philosophy) và Lãng mạn (Romance)."
    "Chương 1: AT THE BOTTOM OF SOCIETY."
    "\"Hikikomori\" là hiện tượng những người tự giam mình trong căn phòng đơn lẻ, từ chối tham gia vào đời sống xã hội và hoạt động gia đình trong khoảng thời gian dài."
    "Trong năm 2022 ở Nhật Bản có khoảng 1,46 triệu người mắc hội chứng hikikomori."
    "Ngày 4 tháng 9 năm 2023."

    show i_lao young at center
    "Nguyễn Thù Lao là 1 chàng trai 21 tuổi, với ước mơ hoài bão trở thành một nhà phát triển game tài năng."
    character_lao "Cuối cùng mình cũng đã tốt nghiệp"
    hide i_lao young
    show boss
    with dissolve
    character_lao "Mình đã tìm được một công ty công nghệ lớn."
    hide boss
    
    show i_lao young at center
    with dissolve
    character_lao "Chắc chắc sự nghiệp sẽ trơn tru, con đường thăng tiến sẽ rộng mở."
    scene bg room dark
    with dissolve

    "5 năm sau."
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    show i_lao sad_right
    character_lao "Đời như bu*i."
    "Lao, 26 tuổi đã trở thành 1 ông chú lúc nào không hay!"
    scene black
    show chatgpt
    "Lao đã bị đuổi việc sau khi làm cho công ty công nghệ \"3 chữ\" được 4 năm."
    scene bg room dark
    show i_lao sad_right
    character_lao "Có lẽ mình nên ra ngoài đi nhậu để xả stress."
    play music "medieval.mp3" fadein 2.0 volume 0.05
    scene bg quan nhau
    with slideright
    show i_lao sad_right
    character_lao "Bọn nó kêu 7 giờ mà 7 giờ 30 rồi đã thấy đâu."
    with dissolve
    character_samurai"Êêê, Bên này nè!"

    show i_samurai neutral_left at right
    with moveinright
    character_samurai "..."
    hide i_lao sad_right
    hide i_samurai neutral_left 
    show i_samurai neutral_left  at center
    " (Thằng này là Samurai 26 tuổi, bạn từ thời đại học của Lao, lý do nó được gọi là Samurai vì nó là wibu chúa, lúc nào cũng mặc đồ Nhật như trong phim samurai ngày xưa.)"
    hide samurai neutral
    show i_lao sad_right
    show i_samurai neutral_left at right
    character_samurai "Mấy hôm nay thế nào rồi?"
    character_lao "Như bu*i."
    character_samurai "Kể tao nghe xem nào"
    character_lao "Tao đã gửi CV cho hơn 97 công ty và vẫn chưa được apply. Hôm nay có lẽ là lần thứ 100 tao có ý định nhảy l*u."
    character_samurai "Bình tĩnh nào bro. Tao nghe cái ý định mày TU TU nhiều rồi mà thấy có bao giờ làm đâu."
    character_samurai "Tao thất nghiệp hơn 4 năm nay rồi mà tao có bao giờ làm đâu."
    character_lao "Mày có công việc ở nhà mày rồi, còn tao thì cạp đất mà ăn đây. Tao không muốn trở thành gánh nặng của gia đình nữa. Tao không muốn trở thành hikikomori."
    
    character_samurai "Vậy đi làm part-time đi. Mấy công việc kiểu như làm quầy thu ngân hoặc chạy bàn thì sao?"
    character_lao "Cái con người hướng nội như tao mà đi làm part-time thì chắc nổ tung mất."
    hide i_lao sad_right
    hide i_samurai neutral_left
    show beaver at truecenter
    with dissolve
    character_lao "\"Wo you wo ziji de yuanze, wo buxiang yibeizi rang ren cai zai jiaoxia, ni yiwei wo shi chou yaofan de?, wo dengle san nian, jiu xiang deng yige jihui, wo yao zheng yi kouqi, bushi xiang zhengming wo liaobuqi, wo shi yao gaosu renjia, wo shiqu de dongxi, wo yiding yao na huilai\""
    scene bg quan nhau
    show i_lao sad_right
    show i_samurai neutral_left at right
    character_samurai "Không hiểu gì nhưng nghe thấm vãi."
    character_samurai "Có lẽ mày nên đi khám tâm lý đi."
    character_lao "Tao đi khám rồi đấy chứ."
    character_samurai "Bác sĩ bảo sao?"
    character_lao "Bác sĩ bảo tao bị Rối loạn trầm cảm, Khủng hoảng lo âu, Khủng hoảng căn tín (Identity crisis), Khả năng giao tiếp kém, Rối loạn giấc ngủ, Khủng hoảng lo âu, Sống tách biệt với thế giới, Khủng hoảng hiện sinh (Existential crisis), stress lâu dài,..."
    character_samurai "Vãi cả l*n, mày lặp lại \"Khủng hoảng lo âu\" 2 lần đấy."
    character_samurai "Tao có cách này, sao mày không thử tưởng tượng mày là người hướng ngoại và hành động như họ xem."
    character_lao "Hành động như người hướng ngoại á?"
    
    character_samurai "Thử tưởng tượng mình là 1 diễn viên nổi tiếng xem. Mày hay xem Phê Phim nên chắc rõ cái này lắm mà."
    character_lao "Diễn viên à."
    scene bg matrix
    with pixellate 
    play music "matrix.mp3" fadein 1.0 volume 0.2
    "..."
    scene bg titanic
    with pixellate 
    play music "titanic.mp3" fadein 1.0 volume 0.2
    "..."
    scene bg quan nhau
    with pixellate 
    show i_lao sad_right
    show i_samurai neutral_left at right
    play music "medieval.mp3" fadein 1.0 volume 0.05
    character_lao "Kịch bản ấy đẹp tiếc là nó không xảy ra, tao có học Sân khấu điện ảnh đâu."
    character_lao "Cứ thế này tao trở thành zombie mất."
    
    character_samurai "Đừng bi quan nữa bro. "

    character_samurai "Tao có cái này cho bro."
    scene bg doraemon
    play sound "audio/doraemon_sound.mp3" volume 0.05
    character_samurai "Danh thiếp Tư vấn tâm lý miễn phí."
    label choices:
    
    "Lao sẽ nhận tấm danh thiếp?"
menu:
    "Nhận":
        jump choices1_a
    "Không nhận":
        jump choices1_b
label choices1_a:

    jump choices1_common

label choices1_b:
    character_samurai "Cứ nhận đi bro."
    jump choices1_common
label choices1_common:
    scene bg quan nhau
    show i_samurai neutral_left at right
    show i_lao sad_right
    
    character_lao "Bây giờ tao phải làm gì?"
    character_samurai "Cứ gọi tới số đó hoặc tới địa chỉ ghi trên đó là được. Tao cũng hay đến nhóm này để chia sẻ hội chứng chuunibyou của tao mà."
    hide i_lao sad_right
    show i_lao serious_right
    character_lao "Okay, thanks bro. Có 1 thằng như mày đời đáng sống hơn hẳn."
    character_samurai "No problem bro. Tao luôn ở bên mày mà. Giờ thì uống tới bến đi."
    scene bg black
    
    "Chương 2: THE DESCENT OF THE ANGEL"
    scene bg introduce_lao
    with dissolve
    "Giới thiệu background nhân vật chính của câu chuyện."
    scene bg introduce_samurai
    with dissolve
    "Giới thiệu background nhân vật bạn thân của nhân vật chính."
    with dissolve 
    scene bg next day
    with dissolve 
    pause (1.0)
    "Ngày hôm sau."
    scene bg street
    with dissolve
    show i_lao sad_right
    ""
    character_lao "(chắc là ở quanh đây thôi.)"
    character_lao "(Ah! Đây rồi, đúng địa chỉ này rồi.)"
    show i_lao sad_left
    character_lao "(Có nên vào không nhỉ? Ngại quá chắc không vào đâu.)"
    show i_lao sad_right
    character_lao "(Nhưng mà đã mất công đến đây rồi, phải vào thôi.)"
    show i_lao sad_left
    character_lao "(Nhưng mà ngại lắm, chắc phải về thôi.)"
    show i_nhi smile_left at right
    with moveinright
    character_nhi "A-Anooo..., cho hỏi!"
    show i_lao serious_right
    character_lao "(...)"
    stop music fadeout 1.0
    play music "wedding.mp3" fadein 1.0 volume 0.2
    scene bg wedding
    with pixellate 
    pause (2.0)
    "(*hình ảnh trong trí tưởng tượng cộng với nhạc nền đám cưới epic)"
    scene bg adam
    with pixellate 
    "(*vẫn là hình ảnh trong trí tưởng tượng.)"
    scene bg street
    with pixellate 
    stop music fadeout 1.0
    play music "medieval.mp3" fadein 1.0 volume 0.05
    show i_lao serious_right
    show i_nhi smile_left at right
    character_lao "(Một mỹ nữ, không biết nên bắt chuyện như thế nào đây?)"
    character_lao "Ây da, không biết quý cô nương đây nhờ ta có việc gì?"
    character_nhi "Hihi...(Lấy tay che miệng) anh đang có việc với phòng khám của tôi à?"
    character_lao "À không, tôi chỉ đi ngang qua thôi."
    character_nhi "Thật không? tôi nhìn thấy anh đứng đây hơn 5 phút rồi đấy."
    character_nhi "Đã tới đây rồi sao không vào đi, anh trông có vẻ cần một chuyên gia đấy."
    character_lao "Thì ra quý cô là một chuyên gia, cho hỏi quý cô là chuyên gia trong lĩnh vực gì?"
    character_nhi "Chuyên gia phẫu thuật trái tim."
    character_nhi "Thôi! hãy vào đi."
    play sound "audio/footstep.mp3"
    show i_nhi smile_left at left with MoveTransition(2.0)
    hide i_nhi smile_left
    with moveoutleft
    show i_lao serious_left
    character_lao "(Mùi hương thơm kỳ lạ. Chắc cô ấy dùng dầu gội đắt tiền.)"
    character_lao "(Một cô nàng kỳ lạ. Cứ như thể cô ta nhìn thấu trái tim của mình vậy.)"
    hide i_lao serious_left
    scene bg clinic-lobby
    with dissolve
    show i_samurai neutral_right at left
    with dissolve
    show i_lao serious_left at right
    with moveinright
    show i_nhi smile_left at right
    with moveinright
    show i_nhi smile_left at center with MoveTransition(1.0)
    
    character_nhi "(...)"

    
    character_samurai "Đến rồi à! Tưởng mày không đến chứ."
    character_lao "Mày tới đây để làm gì?"
    character_samurai "Có thằng đệ nhờ tao chỉ cách đánh con boss Abysswalker trong Dark Souls ấy mà, nó đang ngồi ghế ôm mặt kia kìa."
    character_samurai "À! chào chị Nhi! Cảm ơn chị vì con giới thiệu con game hôm qua, nó đỉnh kout thật sự."
    character_lao "(Mình tưởng cô ấy nhỏ tuổi hơn mình chứ?)"
    character_lao "Khoan đã, chị à? Cho hỏi chị bao nhiêu tuổi vậy?"
    hide i_nhi smile_left
    show i_nhi smile_right
    character_nhi "À! thật ra chị mới hai mươi chí..."
    character_samurai "Chị ta ba mươi b** nồi bánh trưng rồi..."
    hide i_nhi smile_right
    show i_nhi angry_left
    character_nhi "..."
    character_samurai "À~~"
    play sound "audio/nigerundayo.mp3"
    show i_samurai neutral_right at right with MoveTransition(0.8)
    hide i_samurai neutral_right
    with moveoutright
    character_samurai "Chạy!"
    "Bài học rút ra: đừng bao giờ nói về vấn đề tuổi tác trước mặt phụ nữ..."
    character_lao "(Tuổi tác không quan trọng.)"
    character_lao "(Tuổi tác chỉ là những con số.)"
    hide i_nhi angry_left
    show i_nhi smile_right
    character_nhi "Chỗ này ồn ào quá, hay là vào văn phòng của chị đi."


    scene bg office
    with dissolve
    show i_nhi smile_right at left
    with dissolve
    show i_lao serious_left
    with dissolve
    character_lao "(Ôi! Lần đầu tiên mình ở phòng riêng với 1 người phụ nữ xinh đẹp. Không biết chị ấy nghĩ sao về mình?)"

    stop music fadeout 1.0
    play music "calm.mp3" fadein 1.0 volume 0.2

    character_nhi "Gần đây cậu có tiếp xúc với nhiều người không?"
    character_lao "À không! Dạo gần đây em chỉ gặp mỗi thằng Samurai thôi."
    character_lao "Những người xung quanh em trừ Samurai ra toàn những kẻ vô cảm."
    character_nhi "Cậu không có anh chị hay bố mẹ để trò chuyện à?"
    character_lao "Bố mẹ thì ở xa, nhưng dù thế họ cũng không bao giờ lắng nghe đâu."
    character_nhi "Bậc làm cha làm mẹ nào mà lại như thế? Giống bố mẹ chị, đúng là bậc phụ huynh châu Á chuẩn mực."
    

    character_nhi "Cậu đã từng trải qua một sự kiện trong quá khứ và bị nó ám ảnh đến bây giờ?"
    character_lao "Sự kiện ám ảnh trong quá khứ?"
    scene bg bloody_black_white 
    pause 0.01
    scene bg office
    show i_nhi smile_right at left
    show i_lao serious_left
    character_lao "À! Có! Đã từng."
    character_nhi "Cậu thường làm gì vào thời gian rảnh rỗi?"
    character_lao "Em làm gì vào lúc rãnh rỗi à?"
    scene bg cinema
    character_lao "Khi stress em thường đến rạp phim xả hơi, quên đi những muộn phiền cuộc sống, em thường chọn những bộ phim ít người xem để không phải ăn cơm chó."
    scene bg computer
    character_lao "Đến tối em ngồi lại code dự án game đang làm dở 1 mình, nếu stress quá thì em chơi Dark Souls, chơi 1 thời gian thì nhận ra là nó lại khiến em tramcam nên lại code tiếp, tạo thành một vòng lặp không hồi kết."
    scene bg office
    show i_nhi smile_right at left
    show i_lao serious_left
   
    character_nhi "Cậu có cảm thấy thiếu động lực và cảm thấy mệt mỏi với mọi thứ không?"
    character_lao "Đúng rồi!"
    character_nhi "Cậu có cảm thấy dễ cáu gắt, bực mình, có nhiều cảm xúc tiêu cực không?"
    character_lao "Cái này thì không có cáu gắt, chỉ có nhiều cảm xúc tiêu cực."
    character_nhi "Có phải cậu đang bắt đầu mất những đam mê và đang tìm lại những đam mê khác?"
    character_lao "Đúng rồi! Sao chị biết hay vậy?"
    character_nhi "Những người bị tram cam thường mất khả năng tận hưởng những hoạt động trước đây mang lại niềm vui và đam mê."
    character_nhi "Trước đây chị mất đi đam mê về thiết kế, design, giờ thì chị có đam mê sưu tập mô hình."
    character_lao "Thật trùng hơp, em cũng có sở thích sưu tập mô hình."
    character_nhi "Thế à! Em sưu tập dòng mô hình gì vậy? Gundam? Nendroid? Chị thì thích sưu tập mô hình quân sự."
    character_lao "(Chẳng lẽ lại nói ra mình sưu tập mô hình NSFW)"
    character_lao "À! Em sưu tập tầm vài chục con mô hình Gundam dòng High Grade thôi, thỉnh thoảng có vài con Master Grade."
    character_nhi "Wào. Chị thì chỉ mới thử lắp Gundam gần đây thôi nên hơi fail, chưa được một con HG nào cả."
    character_nhi "Em có thể chỉ cho chị cách lắp được không? Hẹn cuối tuần sang nhà chị đi."
    character_lao "(Sao chị ta có thể rủ người mới quen về nhà được chứ? Chẳng lẽ đây là Bành Trướng Lãnh Địa của đối thủ? Mình phải trả lời sao đây?)"

    "Lao sẽ trả lời như thế nào?"
menu:
    "Tới nhà chị ấy.":
        jump choices3_a
    "Mời chị ấy vào Lãnh Địa (nhà của mình)" :
        jump choices3_b

label choices3_a:

    character_lao "Cuối tuần em rảnh ạ. Chị có bộ dụng cụ 3 món cơ bản chưa ạ?"
    character_nhi "Cái đó là gì vậy?"
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    play sound "audio/huh.mp3" volume 0.5
    scene bg question
    hide i_nhi smile_right
    show lao_thinking
    character_lao "Huh?"
    hide lao_thinking
    show nhi_thinking
    character_nhi "Hả?"
    hide nhi_thinking
    scene bg office
    show i_nhi smile_right at left
    show i_lao serious_left at center
    character_lao "..."
    character_lao "Bộ tool gồm kìm để tách nhựa, nhíp để dán decal và nhám để làm mịn bề mặt nhựa."
    character_lao "Thế từ trước đến giờ chị dùng gì để lắp mô hình?"
    character_nhi "À... chị dùng đồ cắt móng tay."
    character_lao "Thế thì mô hình tan nát mất. Để em mang qua cho chị vậy."
    character_nhi "Cảm ơn em. Nhờ em vậy."
    character_lao "(Hèn gì đã ba mươi b** tuổi rồi chị ta vẫn ế.)"
    scene bg clinic-lobby
    with dissolve
    show i_nhi smile_right
    with dissolve
    show i_lao serious_left at right
    with dissolve
    character_nhi "Nếu cậu có vướng mắc gì trong lòng nữa thì hãy cứ đến đây. Chị trực ở đây 24/7."
    character_lao "À vâng. Hẹn chị cuối tuần."
    character_nhi "Người mạnh mẽ đến đâu cũng có lúc cần sự giúp đỡ. Thật ra thì tất cả mọi người đều cô đơn, kể cả chị, chỉ là ta cho phép bản thân ta nghĩ rằng ta cô đơn hay không thôi."
    character_nhi "Nỗi cô đơn là một điều đáng sợ, đôi khi nỗi cô đơn cũng có vẻ đẹp của nó. Nhưng nếu ở đó lâu quá nó không còn đẹp nữa vì vẻ đẹp thường rất ngắn. "
    character_lao "Cái gì vậy chị? Triết học à?"
    character_nhi "Triết học đấy. Rồi cậu sẽ hiểu thôi."
    scene

    scene bg room dark
    with dissolve
    show i_lao sad_left
    character_lao "Những lời của chị ấy nghĩa là sao nhỉ? Thôi nghĩ nhiều chi cho mệt ngủ thôi."
    scene bg black
    "Chương 3: I Really Want to Stay at Your House"
    scene bg introduce_nhi
    "Giới thiệu nhân vật nữ chính."
    scene bg 3 days later
    with dissolve
    "3 ngày sau."
    scene bg street
    show i_lao serious_left
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    character_lao " (Theo địa chỉ chị ấy cho thì nhà chị ấy hình như là ở quanh đây.)"
    show i_nhi smile_right at left
    with moveinleft
    character_lao "(Ah! Chị ấy đây rồi!)"
    character_nhi " Cậu đến sớm vậy? Mời vào nhà chị."
    scene bg clinic-empty
    show i_lao serious_left
    with dissolve
    show i_nhi smile_right at left
    with dissolve
    character_lao "Vậy ra nhà của chị cũng là nơi chị làm việc."
    character_nhi "Vậy cho đỡ tốn tiền thuê nhà. Thời buổi thị trường kinh tế khó khăn mà."
    hide i_lao serious_left
    scene bg nhi-room
    show i_lao serious_left
    with dissolve
    show i_nhi smile_right at left
    with dissolve
    character_nhi "Đây là phòng của chị."
    scene bg question
    hide i_nhi smile_right
    show lao_thinking
    character_lao "(Huh?)"
    hide lao_thinking
    scene bg nhi-room
    show i_lao serious_left
    show i_nhi smile_right at left
    character_lao "Cho em hỏi là chị bao nhiêu tuổi rồi vậy?"
    character_nhi "Ba mươi b**. Em hỏi để làm gì?"
    character_lao "À không có gì?"
    character_lao "(Cứ tưởng chị ta sinh trước thời bao cấp.)"
    character_lao "Cho em hỏi được không? Sao chị thích sưu tập mô hình quân đội vậy?"
    character_nhi "Chắc là vì chị thích những thứ hoài niệm."
    character_nhi "À, xem nè."
    scene bg coins
    with dissolve
    character_nhi "Tađaaa! Bộ sưu tập xu của chị. Mất 7 năm để sưu tập đấy, Có đủ từ thời Quang Trung, Đông Dương đến năm 2003 dù còn thiếu vài xu. Cậu thấy thế nào?"
    scene bg nhi-room
    show i_lao serious_left
    show i_nhi smile_right at left
    character_lao "(Ấn tượng thật nhưng mình không biết nên khen hay nên chê nữa cứ như chị ta sống ở thế kỷ khác vậy.)"
    character_lao "(Phải làm sao đây, kỹ năng social của mình gần như bằng không phải nói với chị ta như thế nào?)"
    character_lao "(Nếu khen thì chị ta sẽ sống mãi ở thời đồ đá mất, còn nếu chê thì sợ chị ta tự ái.)"
    character_lao "(Đừng overthinking nữa tôi ơi, phải nói như thế nào đây?)"
menu:
    "Tuyệt vời! Sugoi! Kỳ công quá! 10 điểm không có nhưng.":
        jump choices4_a
    "Năm 2028 rồi, em nghĩ là chị nên có sở thích khác. Mấy cái này chỉ dành cho mấy ông cụ thôi." :
        jump choices4_b
    "Cái này không nằm trong lĩnh vực của em nên em không thể nhận xét được.":

        jump choices4_c

label choices4_a:
    character_nhi "Thế à! Cảm ơn em nhé, ít ai hiểu được sở thích của chị lắm."
    jump choices4_common
label choices4_b:
    character_nhi "Thế à! Chị cũng nghĩ là mình có sở thích hơi khác người. Nhưng mà xem nè."
    jump choices4_common
label choices4_c:
    character_nhi "Thế à! Anyway, check this out..."
    jump choices4_common
label choices4_common:
    character_lao "Đây...đây là!"
    play music "Aerial.mp3" volume 0.05
    scene bg aerial1
    character_nhi "Đúng vậy đây chính là: Ma nữ sao Thủy Full Mechanics 1/100 XVX-016 Gundam Aerial đến từ Bandai, Mobile Suit mạnh nhất series The Witch from Mercury."
    scene bg aerial2
    character_lao "Tuyệt vời! Lại còn là hàng chính hãng nữa. Chị tự ráp à?"
    scene bg aerial3
    character_nhi "Chị nhờ shop ráp hộ."
    scene bg nhi-room_aerial
   
    show i_lao serious_left

    show i_nhi smile_right at left
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    character_nhi "Chị mới tậu 1 em SD Calibarn nhưng mà trình độ lắp vẫn còn kém quá."
    character_lao "Không sao. Cứ để em lo."
    scene bg 8 hours later
    "(Thế là họ cùng nhau ráp gunđàm trong 8 tiếng...)"
    scene bg calibarn
    character_nhi "Xong rồi!"
    scene bg nhi-room_calibarn
   
    show i_nhi smile_right at  left

    show i_lao serious_left at center

    character_lao "Thật sự thì đã rất lâu rồi em mới có khoảng thời gian tận hưởng lắp ráp như thế này, cứ như là em đã tìm lại niềm vui lắp gundam vậy."
    character_nhi "Phải không! Khi chia sẻ điều mình yêu thích với người khác, ta sẽ yêu thích công việc đó hơn."
    character_nhi "Để cảm ơn cậu, chị sẽ tặng cậu một món quà, giờ cậu hãy nhắm mắt lại đi."
    character_lao "Sao phải nhắm mắt lại?"
    character_nhi "Cứ nhắm mắt lại đi."
    scene bg black
    character_lao "..."
    show i_lao serious_left_pixcel at center
    character_lao "Đây là đâu?"
    with dissolve
    show i_nhi smile_right_pixcel at  left
    with moveinleft
   
    character_nhi "chúng ta đang ở trong tiềm thức của cậu."
    character_nhi "Chị sử dụng một thiết bị của Neuralink, dùng để trị liệu và chia sẻ giấc mơ. Chị cũng đeo một cái và chia sẻ giấc mơ với cậu."
    character_lao "Vậy là chị Inception em à?"
    character_nhi "Inception là gì?"
    character_lao "Nó có an toàn không vậy?"
    character_nhi "Chị sử dụng nó nhiều rồi nên không sao đâu."
    character_nhi "Chị không chuốc thuốc cậu đâu. Thiết bị này không hề khoá các dây thần kinh như trong Sword Art Online nên chỉ việc nghĩ rằng mình tỉnh lại là sẽ dậy thôi."
    character_nhi "Cậu làm thử xem?"
    scene bg nhi-room
    show i_nhi smile_right_vr at  left

    show i_lao serious_left_vr at center
    character_lao "Về lại thực tại rồi!"
    character_nhi "Rất an toàn phải không? Có 1 điểm trừ là thiết bị này cắm điện trực tiếp vào ổ điện, nếu đang dive mà vẫn cúp điện thì sẽ bị kẹt trong giấc mơ đến khi có điện, may mà ở khu này ít bị cúp điện."
    character_nhi "Cậu muốn dive tiếp không? Việc điều trị bằng thiết bị này sẽ hiệu quả hơn rất nhiều đấy."
menu:
    "Tiếp tục dive.":
        jump choices5_a
    "Có lẽ thiết bị này vẫn quá nguy hiểm." :
        jump choices5_b
label choices5_a:
    character_nhi "Có thế chứ! Vậy tiếp tục nào."
    jump choicescredit_common
label choices5_b:
    character_nhi "Vậy à, chị cũng không muốn đẩy nhanh tiến độ."

    jump choicescredit_common

label choices3_b:
    character_lao "(Đến nhà của gái chơi thì hay đấy nhưng...)"
    scene bg daga kotowaru
    character_lao "(TA TỪ CHỐI!)"
    character_lao "(Đã là một Gigachad thì không được để cám dỗ lôi kéo.)"
    character_lao "(Không được để bản thân rơi vào Lãnh Địa của người khác!)"
    character_lao "(Phải triển khai lãnh địa của mình!)"
    scene bg domain expansion
    play sound "audio/Ryoiki Tenkai.mp3" volume 0.5
    character_lao "(Bành Trướng Lãnh Địa: THỈNH NƯƠNG TỬ NHẬP PHỦ / UKE JYOSHI NIUFU!)"
    scene bg office
    show i_nhi smile_right at left
    show i_lao serious_left
    character_lao "Hay chị sang nhà em để lắp cho dễ?"
    character_nhi "Được đấy, hôm đó chị sẽ mang theo bộ kit đang ráp dở."
    scene bg clinic-lobby
    with dissolve
    show i_nhi smile_right
    with dissolve
    show i_lao serious_left at right
    with dissolve
    character_nhi "Nếu cậu có vướng mắc gì trong lòng nữa thì hãy cứ đến đây. Chị trực ở đây 24/7."
    character_lao "À vâng. Hẹn chị cuối tuần."
    character_nhi " Nỗi cô đơn là một điều đáng sợ, đôi khi nỗi cô đơn cũng có vẻ đẹp của nó. Nhưng nếu ở đó lâu quá nó không còn đẹp nữa vì vẻ đẹp thường rất ngắn. Thật ra thì tất cả mọi người đều cô đơn, kể cả chị, chỉ là ta cho phép bản thân ta nghĩ rằng ta cô đơn hay không thôi."
    character_lao "Cái gì vậy chị? Triết học à?"
    character_nhi "Triết học đấy. Rồi cậu sẽ hiểu thôi."
    scene

    scene bg room dark
    with dissolve
    show i_lao sad_left
    character_lao "Những lời của chị ấy nghĩa là sao nhỉ? Thôi nghĩ nhiều chi cho mệt ngủ thôi."
    scene bg black
    "Chương 3: I Really Want to Stay at Your House"
    scene bg introduce_nhi
    "Giới thiệu nhân vật nữ chính."
    scene bg 3 days later
    with dissolve
    "3 ngày sau."
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    scene bg room light
    with dissolve
    show i_lao sad_right
    character_lao "Aiss chết tiệt! ngủ quên mất rồi. Còn 5 giây nữa là đến giờ hẹn rồi. Phải dọn phòng mới được."
    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("bg room", 999999999999999,
        ("beer", 950, 735, _("Gối Hatsune Miku dài 40x1m ruột bông - 320.000đ")),
        ("elf", 111, 560, _("Makima Bunny BiCute FuRyu Studio 1/6 - 520.000đ")),
        ("flowers", 700, 481, _("Yamato Dragon Studio 1/4 recast - 1.099.000đ ")),
        ("skull", 1813, 161, _("Gundam Girl Max Milk Studio 1/6 - 6.850.000đ")),
        ("sprite", 355, 318, _("manga Metamorphosis - Samurai tặng")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=False,
        # включаем подсказки
        hint=True,
        # включаем подсветку предмета при наведении
        hover=brightness(.05),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Cần phải thu thập 5 món đồ NSFW\n Trước khi Nhi đến nhà."

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if hf_return == 0:
        centered "{size=+24}Thành công!"
    else:
        centered "{size=+24}GAME OVER\nĐồ vật còn lại:  [hf_return]."

    $ hf_hide()
    scene bg room
    show i_lao serious_left
    with dissolve
    character_lao "Đã xong."
    scene bg street-vn
    with dissolve
    show i_nhi smile_right at  left
    with dissolve
    character_nhi "Alo! Chị tới rồi đây!"
    show i_lao serious_left at right
    with moveinright
    character_lao "À! Mời chị vào nhà."
    scene bg room
    with dissolve
    show i_nhi smile_right at  left
    with dissolve
    show i_lao serious_left at center
    with dissolve
    character_lao "Cho hỏi hôm nay là ngày nghỉ mà sao chị vẫn mang áo phòng thí nghiệm?"
    character_nhi "Đây là thường phục của chị đó."
    show nhi_eye at right
    character_nhi "Uwaah, Đây lẽ nào là ..."
    play music "ibo.mp3" fadein 2.0 volume 0.05
    scene bg barbatos1
    character_lao "Đúng vậy đây chính là: Acquy sao Hoả Full Mechanics 1/100 ASWG08 Gundam Barbatos Lupus Rex Garage kit Custom Build đến từ Zero Labs Studio."
    scene bg barbatos2
    character_lao "Form cuối cùng của Gundam Barbatos: đã cùng Mikazuki August chiến đấu chống lại Gjallarhorn trong trận triến cuối cùng trên Hoả tinh. Mobile Suit đc thiết kế để phù hớp với phong cách chiến đấu tàn bạo của Mika."
    scene bg barbatos3
    character_nhi "Quá là đỉnh kout! Fantastic! Wonderful! Significant! Magnificent! Outstanding! Class of Titans! đây là World Class! Em này bao nhiêu vậy?"
    
    play music "calm.mp3" fadein 1.0 volume 0.2
    scene bg room_barbatos
    show i_lao serious_left at center
    show i_nhi shock_right2 at  left
    character_lao " **.599.0000đ tính cả tiền sơn, bay mất ** tháng lương của em đấy. Do chính tay em mất 2 năm để sơn độ chế. Cỗ máy mà mọi thằng con trai đều ao ước. Cố máy phá huỷ ví tiền của mọi thằng đàn ông."
    character_nhi "Chị cũng muốn có 1 em Acquy sao hoả Full Mechanics 1/100 ASWG08 Gandamu Barubatosu Rupusu Rekusu Garage kit Custom Build đến từ Zero Labs Studio từ lâu rồi nhưng đây là lần đầu tiên thấy ở ngoài đời."
    character_lao "Sao chị không sắm 1 em?"
    character_nhi "Chị cũng muốn lắm nhưng mà chị không biết lắp, đến cả Hight Grade chị cũng chưa lắp nổi, chị mới chỉ lắp được ở cấp độ Entry Grade thôi."
    character_nhi "Vả lại ngày trước chị cũng chỉ biết mua ở hàng chính hãng chứ chẳng biết cách mua hàng lậu."
    character_nhi "Đến giờ chị chỉ mới sắm được 1 em FM Aerial do shop lắp sẵn thôi."
    character_lao "FM Aerial à? Chị cũng có máu mặt trong giới gunpla đấy."
    hide i_nhi shock_right2
    show i_nhi smile_right at left
    character_nhi "Có vẻ như hai ta hiểu nhau hơn rồi đấy."
    scene bg 8 hours later
    "(Thế là họ cùng nhau ráp gunđàm trong 8 tiếng...)"
    scene bg calibarn
    character_nhi "Xong rồi! SD Gundam Calibarn phù thuỷ sao Thuỷ."
    scene bg room_calibarn
   
    show i_nhi smile_right at  left

    show i_lao serious_left at center

    character_lao "Thật sự thì đã rất lâu rồi em mới có khoảng thời gian tận hưởng lắp ráp như thế này, cứ như là em đã tìm lại niềm vui lắp gundam vậy."
    character_nhi "Phải không! Khi chia sẻ điều mình yêu thích với người khác, ta sẽ yêu thích công việc đó hơn."
    character_nhi "Để cảm ơn cậu, chị sẽ cho cậu một bất ngờ, giờ cậu hãy nhắm mắt lại đi."
    character_lao "Sao phải nhắm mắt lại?"
    character_nhi "Cứ nhắm mắt lại đi."
    scene bg black
    character_lao "..."
    show i_lao serious_left_pixcel at center
    character_lao "Đây là đâu?"
    with dissolve
    show i_nhi smile_right_pixcel at  left
    with moveinleft
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    character_nhi "chúng ta đang ở trong tiềm thức của cậu."
    character_nhi "Chị sử dụng một thiết bị của Neuralink, dùng để trị liệu và chia sẻ giấc mơ. Chị cũng đeo một cái và chia sẻ giấc mơ với cậu."
    character_lao "Vậy là chị Inception em à?"
    character_nhi "Inception là gì?"
    character_lao "Nó có an toàn không vậy?"
    character_nhi "Chị sử dụng nó nhiều rồi nên không sao đâu."
    character_nhi "Chị không chuốc thuốc cậu đâu. Thiết bị này không hề khoá các dây thần kinh như trong Sword Art Online nên chỉ việc nghĩ rằng mình tỉnh lại là sẽ dậy thôi."
    character_nhi "Cậu làm thử xem?"
    character_lao "... Vẫn không dậy được."
    character_nhi "Lạ thật, chị cũng không dậy được."
    character_nhi "Có phải khu này hay cúp điện không?"
    character_lao "Đúng rồi. Mới hôm qua cũng cúp điện."

    show i_nhi shock_right_pixcel
    character_nhi "Thôi ăn l*n rồi, quả đúng là cúp vô địch thế giới. Nếu đang hoạt động mà thiết bị cúp điện thì ta sẽ bị kẹt ở đây đến khi có điện."
    character_nhi "Nhưng 5 phút ở ngoài đời bằng 1 tiếng ở đây. Tức là nếu cúp điện 1 tiếng thì ta sẽ kẹt ở đây 12 tiếng, nếu cúp điện 1 ngày thì ta sẽ kẹt ở đây 12 ngày."
    play sound "audio/huh.mp3" volume 0.5
    play music "SPECIALZ.mp3" volume 0.2
    hide i_nhi shock_right_pixcel
    show lao_thinking
    character_lao "Hả?"
    hide lao_thinking
    show nhi_thinking
    play sound "audio/huh.mp3" volume 0.5
    character_nhi "Hả?"
 
    hide nhi_thinking
    show i_nhi smile_right_pixcel at left
    show i_lao serious_left_pixcel at center
    character_nhi "..."
    play music "dizzy.mp3" fadein 2.0 volume 0.05
    character_lao "Vậy là giống Inception rồi."
    character_nhi "Inception là cái gì vậy? Mà đây không phải lần đầu chị gặp tình huống này. Sẵn có thời gian ta cùng xem qua từng mảng ký ức của cậu vậy."
    character_nhi "Ở trong thế giới này ta có thể tái hiện lại mọi khoảng khắc quan trọng trong cuộc đời cậu. Nếu cậu có những gì riếng tư thì có thể không chia sẻ cũng được."
    character_nhi "Nhưng chúng ta phải tìm tới gốc rễ của những vướng mắc của cậu để cậu trở nên tốt hơn, để phát triển và cải thiện bản thân."
    character_nhi "Nào! Bắt đầu với ký ức thời cấp 3."
    scene bg yamero
    character_lao "YAMEROOOOOOOOOOOOO!!!"
    character_lao "Dừng lại đi! Panic Attackkkkkkk!"
    character_lao "Đó là những ký ức trauma nhất của emmmmmm!"
    jump choicescredit_common

label choicescredit_common:
    play music "Saihate no Bukun Uta.mp3" fadein 1.0 volume 0.2
    scene bg room dark
    with dissolve
    "Đã hết phần Demo, nếu bạn muốn tiếp tục theo dõi câu chuyện của Lao từ Hikikomori tiến hoá lên người bình thường. Hãy ủng hộ nhà phát triển. Mọi sự đóng góp đều đáng trân trọng °˖✧◝(⁰▿⁰)◜✧˖°"
    "Bài hát Ending là một bài hát rất hay nghe rất thấm nhưng ít được người biết đến, nhặt được trên Youtube khi đang tìm soundtrack cho game, dù nhà phát triển game học tiếng Nhật nhưng cũng không rõ bài hát nói về điều gì."
    "Bài hát có tên là  Saihate no Bukun Uta, hát bởi Robina Goodfellow (CV- Suzuki Eri)"
    "Visual Novel này được thực hiện dựa trên trải nghiệm cá nhân và lấy ý tưởng từ các bộ phim nổi tiếng như Good Will Hunting (1997), Lost in Translation (2003), Welcome to the N.H.K (2006), Castaway on the Moon (2009), The Garden of Words (2013), Passengers(2016), Bocchi the Rock! (2022)"
    "Credits:\nDirector Huy Hà\nStory by Nguyễn Cương Lĩnh\nCostume Designer Nguyễn Cương Lĩnh\nEditor Nguyễn Cương Lĩnh"
    "Artist Nguyễn Cương Lĩnh with the help of AI and Riyo's artstyle\nScript by Nguyễn Cương Lĩnh\nCharacter Development by Nguyễn Cương Lĩnh\nGame Designer Nguyễn Cương Lĩnh"
    "Tester:  Huy Hà, Cương Lĩnh 2004, Lý Hải Đăng, thầy Phúc Toàn, Phan Quốc Cường, Hoshi Visual Novel fanpage, Yuzusoft Vietnam Fanclub."
    scene bg lao_fact
    with dissolve
    "Một vài fact về nhân vật để làm tăng chiều sâu cho câu chuyện: Lao là một người yêu thiên nhiên, thích leo núi, thám hiểm vì thế mà hình thành nên tính cách ít giao tiếp từ đó thường thu mình lại và ít tham gia các hoạt động xã hội. "
    "Tính cách của Lao là kết hợp giữa tích cách hướng nội của Bocchi và vẻ nam tính lành mạnh của Bear Grylls. Đây là nhân vật giống tích cách của người làm ra tựa game này nhất. Nhân vật Lao là tôi tưởng tượng ra bản thân trong tương lai."
    scene bg samurai_fact
    with dissolve
    "Samurai là kiểu nhân vật bạn thân mà các nhân vật nam chính anime thường có, luôn ở bên hỗ trợ cho nam chính dù loser vãi cả ra, là 1 wingman chính hiệu."
    "Samurai xem Lao như một người em cần phải bảo vệ, giống như Gyro Zeppeli đối với Johnny Joestar trong Jojo part 7, anh cũng mang tính cách lầy lội và sự nam tính độc hại của Barney Stinson."
    scene bg nhi_fact
    with dissolve
    "Nhi là nhân vật được xây dựng phức tạp nhất, cô là người có khả năng làm chủ tâm lý của bản thân trong mọi tình huống, cô không dùng kỹ năng này để làm diễn viên mà sử dụng nó giúp đỡ người khác, những người bất ổn."
    "Nhi là một người luôn mang nụ cười bí hiểm của Makima, có sở thích kỳ lạ như Hannibal và là người có tài năng như Gen Asagiri trong Dr.Stone. Nếu đóng vai phản diện thì Nhi sẽ diễn tròn vai."
    "Tôi cố gắng xây dựng nhân vật Nhi và nhân vật Lao là 2 con người đối lập nhau, cả 2 đều hướng nội nhưng Nhi tận hưởng điều đó, enjoy cảm giác ở một mình, còn Lao hướng nội vì số phận đưa đẩy."
    scene bg room dark
    with dissolve
    " Nhật ký phát triển: Nếu bạn đọc được những dòng này có nghĩa là tôi vẫn còn sống và tựa game này đã đến được tay bạn, còn nếu bạn không đọc được những dòng này có nghĩa là tựa game này không đến được tay bạn và tôi đã ngủm cùng với chính đam mê của tôi."
    "Nhật ký phát triển: Ngày 2/12/2023 Lên ý tưởng, kịch bản phát triển."
    "Nhật ký phát triển: Ngày 4/12/2023 Tìm ra phần mềm Ren'py và học cách sử dụng phần mềm này để phát triển."
    "Nhật ký phát triển: Ngày 6/12/2023 Học cách thêm âm nhạc vào game. Sửa lại kịch bản"
    "Nhật ký phát triển: Ngày 8/12/2023 Xem Bocchi the rock để lấy ý tưởng."
    "Nhật ký phát triển: Ngày 10/12/2023 Học cách thêm transition, animation."
    "Nhật ký phát triển: Ngày 14/12/2023 đưa ra bản demo 1.0 cho các đàn em và đàn anh chơi thử để nhận về review."
    "Nhật ký phát triển: Ngày 16/12/2023 sửa lại vài lỗi mà đàn em đề xuất và cải thiện UI, vẫn giữ phiên bản game là demo 1.0 vì không thay đổi nội dung."
    "Nhật ký phát triển: Ngày 18/12/2023 nhờ thầy Toàn chơi thử bản demo 1.0."
    "Nhật ký phát triển: Ngày 20/12/2023 nhờ thầy Tuấn Anh và Thầy Kiệt chơi thử bản demo 1.0."
    "Nhật ký phát triển: Ngày 24/12/2023 dành ra cả 1 ngày để tìm hiểu sâu về phát triển nhân vật, tâm lý nhân vật và từ đó sửa lại tâm lý của bản thân."
    "Nhật ký phát triển: Ngày 26/1/2024 Xem Good Will Hunting để lấy ý tưởng câu chuyện."
    "Nhật ký phát triển: Ngày 28/1/2024 Chơi Phoenix Wright để lấy ý tưởng."
    "Nhật ký phát triển: Ngày 30/12/2023 gửi thầy Tuấn Anh ý tưởng và thuật toán mẫu của game."
    "Nhật ký phát triển: Ngày 2/1/2024 lên ý tưởng cho chương 2."
    "Nhật ký phát triển: Ngày 4/1/2023 xem Cast Away On the Moon 1 lần nữa để lấy ý tưởng"
    "Nhật ký phát triện: Ngày 6/1/2023 Vừa code vừa nghe sách nói Khu vườn ngôn từ để hiểu hơn về sự cô đơn."
    "Nhật ký phát triển: Ngày 8/1/2024 Vừa code vừa nghe về Chủ nghĩa khắc kỷ trên spiderum dể hiểu hơn về phát triển bản thân."
    "Nhật ký phát triển: Ngày 10/1/2024 xem Social Network (2010) không vì lý do gì"
    "Nhật ký phát triển: Ngày 12/1/2024 Nhận ra mình rơi vào Dev Hell và lấy lại tinh thần"
    "Nhật ký phát triển: Ngày 14/1/2024 chưa hoàn thành code chương 2 nhưng trong đầu đã nghĩ ra kịch bản chương 3."
    "Nhật ký phát triển: Ngày 16/1/2024 làm minigame cho chương 3."
    "Nhật ký phát triển: Ngày 18/1/2024 hoàn thành minigame."
    "Nhật ký phát triển: Ngày 20/1/2024 xem Bocchi the Rock 1 lần nữa để lấy ý tưởng"
    "Nhật ký phát triển: Ngày 22/1/2024 Xem Chainsaw man để lấy ý tưởng về nhân vật nữ chính"
    "Nhật ký phát triển: Ngày 24/1/2024 Xem Blade Runner 2049 (2017) và Drive (2011) để lấy ý tưởng."
    "Nhật ký phát triển: Ngày 26/1/2024 Xem Cyberpunk: Edgrunner 1 lần nữa để lấy ý tưởng về nhân vật nữ chính."
    "Nhật ký phát triển: Ngày 28/1/2024 thêm soundtrack, vì không tốt nghiệp học viện âm nhạc nên tôi thêm nhạc phiêu lưu cho giống các game rpg ngày xưa. dù gì cũng là hành trình phiêu lưu phát triển bản thân."
    "Nhật ký phát triển: Ngày 30/1/2024 Nhận ra mình rơi vào Dev Hell 1 lần nữa."
    "Nhật ký phát triển: Ngày 2/2/2024 Cố gắng thêm thông điệp nhân văn nhưng sợ làm lời thoại thiếu tự nhiên và mất đi sự tinh tế nên có lẽ là để cho chương 4."
    "Nhật ký phát triển :Ngày 4/2/2024 Hoàn thiện chương 3"
    "Nhật ký phát triển: Ngày 6/2/2024 Gửi cho tester chơi thử"
    "Hướng phát triển tương lai:\nThêm tiếng Anh và tiếng Nhật.\nTìm artist cho game."
    "Thêm copyright cho game.\nChỉnh lại toàn bộ game để không bị đánh bản quyền.\nKịch bản chương 4: đi sâu vào tiềm thức nhân vật Lao, tìm hiểu quá khứ, mục đích sống."
    play music "medieval.mp3" fadein 2.0 volume 0.05
    scene 1
    "Reference 1: Tôi bị ấn tượng bởi phong cách nghệ thuật của Ishida Sui (tác giả của manga Tokyo Ghouls) nên tạo 1 bức tranh của Nhi khi còn trẻ bằng AI"
    scene 2
    "Reference 2: Tôi muốn nhân vật Nhi sẽ tương tác với nhân vật chính như cách Lucy tương tác với David trong Cyberpunk Edgerunners, cả 2 đều cứu rỗi lẫn nhau, cùng nhau vượt qua hoạn nạn."
    scene 3
    "Reference 3: Vì tôi rất yêu thích phong cách độc lạ Jojo pose của tác giả Hirohiko Araki nên tôi tạo 1 Jojo pose cho Nhi tư thế của tượng David, của nghệ nhân Michelangelo, một trong những tác phẩm nghệ thuật nổi tiếng nhất trong lịch sử, đại diện cho sự hoàn hảo và sức mạnh của con người."
    scene 4
    "Reference 4: Tôi muốn ở Main Title có phong cách 3D nên tôi đã bỏ ra 35 đô để mua Honey Select 2 trên Steam để tạo 1 model 3D của Nhi. Vừa để ủng hộ nhà phát triển game và bài trừ nạn tải game lậu."
    scene 5
    "Reference 5: Ở đây tôi dùng 1 model AI nhặt được trên mạng, vì có nhiều cảnh Nhi đút tay vào túi áo rồi nên tôi muốn tạo 1 cảnh Nhi pose dáng để thể hiện tính cách cá tính. Để có thể cho AI vẽ bàn tay thật sự rất khó, phải sử dụng nhiều model và LoRa."
    scene 6
    "Reference 6: Để thể hiện nội tâm phức tạp cho Nhi tôi đã dùng nhiều model AI manga để tạo 1 phiên bản Nhi trưởng thành."
    scene 7
    "Reference 7: Nhi là 1 Gen Y, tức là những người sinh vào những năm 90s vì vậy tôi muốn tạo 1 phiên bản Nhi mang phong cách retro 90s."
    scene 8
    "Reference 8: Đây không phải là art tạo từ AI mà từ một tác giả có tên là JuheePark."
    scene 9
    "Reference 9: Tôi bức ảnh này như một hình tượng thiên thần đến cứu rỗi cuộc sống tẻ nhạt của nhân vật chính."
    scene 10
    "Reference 10: Meme về con hải ly Trung Quốc nổi rần rần trên Tiktok, meme được chế từ một cảnh trong phim Anh hùng bản sắc (1986)."
    scene 11
    "Reference 11: Anime Oshi no Ko nổi tiếng trong giới wibu năm 2023 và bải hát chủ đề mang tên Idol do YOASOBI thực hiện."
    scene 12
    "Reference 12: Tái hiện lại cảnh Dorêmon lấy ra bảo bối thần kỳ."
    scene 13
    "Reference 13: bức tranh nổi tiếng The Creation of Adam (1511), bức tranh tả cảnh Chúa ban sự sống cho Adam, giống như Nhi mang sự sống cho tâm hồn nhân vật chính."
    scene 14
    "Reference 14: Cảnh này gồm 3 meme, Padoru nhưng mà là cô gái nghiện rượu Kikuri Hiroi, Shinji ôm mặt và Doomer Guy"
    scene 16
    "Reference 16: Phân cảnh nổi tiếng trong phim Tội phạm nhân bản 2049 (2017)."
    scene 17
    "Reference 17: Câu nói này trích từ một đoạn trong stream của Dũng CT vào năm 2021. link của đoạn đó: youtu.be/B5wQhGkR4VI?si=uxs5j962AdP4HZnE&t=4164"
    scene 18
    "Reference 18: Vì nhà không có nhiều mô hình quân đội nên tôi xin cái ảnh của user Reddit có tên là 18 Glass_Definition_222 để làm ảnh nền cho đoạn này."
    scene 19
    "Reference 19: Đây là bộ xu Việt Nam qua các thời kỳ mà tôi sưu tập, tôi vẫn còn bộ coin Nhật Bản và các nước trên thế giới."
    scene 20
    "Reference 20: Mô hình lắp ráp FM Gundam Aerial chính hãng từ Bandai giá 1.200.000đ phát hành tháng 4/2023."
    scene 21
    "Reference 21: Mô hình lắp ráp SD Gundam Calibarn chính hãng từ Bandai giá 355.000đ phát hành tháng 7/2024."
    scene 22
    "Reference 22: Reference về phim Kẻ đánh cắp giấc mơ (2010) đạt 4 giải Oscar của Christopher Nolan."
    scene 23
    "Reference 23: ảnh lấy từ kính Vrorbit Theater 2D/3D 2K VR Headset ORBTHEATER B&H vì trông giống NerveGear trong Sword Art Online."
    scene 24
    "Reference 24: meme DAGA KOTOWARU trong anime Jojo part 4 nổi rần rần ở Nhật Bản."
    scene 25
    "Reference 25: \"Triển khai lãnh địa\", \"Bành trướng lãng địa\" hay \"Lĩnh vực triển khai\" do nhân vật Sukuna thi triển trong anime Chú thuật Hồi chiến.4 "
    scene 26
    "Reference 26: Màn chơi này nhặt từ code của 1 anh người Nga để thực hiện được. Trong hình gồm có mô hình Son Goku, bộ manga tôi yêu thích nhất Berserk (1987), mô hình Gojira (2014), mô hình Fourarms."
    scene 27
    "Reference 27: Mô hình các nhân vật nữ nhưng mà là NSFW (Not Safe for work): Makima trong Chainsawman, Yamato trong One Piece, Hatsune Miku, XXXG-01W Wing Gundam nhưng mà là nữ và 1 cuốn manga H*ntai huyền thoại Metamorphosis. "
    scene 28
    "Reference 28: Mô hình Gundam Barbatos Lupus Rex từ anime Mobile suit Gunda Iron-Blooded Orphans (2015)."
    play sound "audio/tachaicuathudam.mp3" volume 0.07
    scene 29
    play sound "audio/tranthanh.mp3" volume 0.09
    "Ở đoạn thoại này tôi dùng đoạn Trấn Thành sử dùng từ vựng tiếng Anh trong chương trình The Masked Singer."
    scene bg room dark
    scene black
    "Tất cả các refrences trên là những pop culture mà tôi lớn lên cùng và còn nhiều references khác rải rác trong game như Dark Souls, nShop, SpongeBob,...."
    stop music fadeout 5.0
    ""