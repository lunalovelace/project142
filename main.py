import streamlit as st

# ตั้งค่าหน้าเว็บไซต์
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ตกแต่งด้วย CSS Custom Style

st.markdown("""
<style>
    /* ปรับแต่งส่วนหัวข้อหลัก */
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #FAFAFA;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    /* ปรับแต่งกรอบ Code / Terminal Output */
    div[data-baseweb="code"] {
        border-radius: 10px;
        border: 1px solid #333333;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    /* แต่งภาพโปสเตอร์ + เอฟเฟกต์ซูมเวลานำเมาส์ไปชี้ */
    img {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        transition: transform 0.3s ease-in-out;
    }
    img:hover {
        transform: scale(1.04);
    }
    /* แต่งปุ่มกดให้มีมิติ */
    div.stButton > button {
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
    }
    /* แต่งแถบ Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161920;
        border-right: 1px solid #2d3139;
    }
</style>
""", unsafe_allow_html=True)



#-------------------------------------------


# ==========================================
# MOVIE RECOMMENDATION SYSTEM
# ==========================================
movie = [
    {
        "title": "The Conjuring",
        "genre": "Horror",
        "rating": 7.5,
        "duration": 112,
        "synopsis": "เรื่องราวของสองสามีภรรยาผู้เชี่ยวชาญเรื่องสืบสวนสิ่งเหนือธรรมชาติ ที่ต้องเข้าไปช่วยเหลือครอบครัวหนึ่งในบ้านฟาร์มที่ถูกวิญญาณร้ายตามหลอกหลอน",
        "poster": "https://www.themoviedb.org/t/p/w1280/wVYREutTvI2tmxr6ujrHT704wGF.jpg"
    },
    {        
        "title": "Resident Evil",
        "genre": "Horror",
        "rating": 7.6,
        "duration": 94,
        "synopsis": "ไวรัสซอมบี้มรณะระบาดทั่วแล็บใต้ดิน ทางรอดเดียวคือต้องฝ่าดงอสูรกายออกไปให้ได้",
        "poster": "https://www.themoviedb.org/t/p/w1280/i7UyjfPio0VFHB9rBUZSFyhOoM8.jpg"
    },
    {
        "title": "IT",
        "genre": "Horror",
        "rating": 7.3,
        "duration": 135,
        "synopsis": "เมื่อเด็กๆ ในเมืองเริ่มหายตัวไปอย่างไร้ร่องรอย กลุ่มเด็กปีศาจจึงต้องเผชิญหน้ากับความกลัวสูงสุดในรูปร่างของตัวตลกมรณะ",
        "poster": "https://www.themoviedb.org/t/p/w1280/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg"
    },
    {
        "title": "Blackrooms",
        "genre": "Horror",
        "rating": 6.7,
        "duration": 126,
        "synopsis": "เมื่อมิติปริศนาไร้ทางออกกลายเป็นกับดัก ทุกห้องซ่อนความกลัวและความลับที่พร้อมจะกลืนกินคุณ",
        "poster": "https://www.themoviedb.org/t/p/w1280/rhGx6E3qRNMgj3i5su2oukNHwIQ.jpg"
    },
    {
        "title": "Util Dawn",
        "genre": "Horror",
        "rating": 5.7,
        "duration": 103,
        "synopsis": "8 เพื่อนรักกับคืนสยองบนภูเขาหิมะ ทุกการตัดสินใจมีชีวิตเป็นเดิมพัน คุณจะรอดชีวิตไปจนถึงรุ่งเช้าได้หรือไม่",
        "poster": "https://www.themoviedb.org/t/p/w1280/bLY5yN4MKVynZ2HMZWElTOGBgBe.jpg"
    },
    {
        "title": "The Nun",
        "genre": "Horror",
        "rating": 5.4,
        "duration": 96,
        "synopsis": "จุดเริ่มต้นแห่งความกลัวในจักรวาลคอนจูริ่ง เมื่อแม่ชีสาวต้องสืบหาความจริงในอารามลึกลับที่ซ่อนความแค้นของปีศาจเอาไว้",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Five Nights at Freddy's 2",
        "genre": "Horror",
        "rating": 5.1,
        "duration": 104,
        "synopsis": "ฝันร้ายระลอกใหม่ในร้านพซซ่าเมื่อเหล่าหุ่นมาสคอตกลับมาพร้อมความโหดร้ายที่ยิ่งกว่าเดิม",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Barbarian",
        "genre": "Horror",
        "rating": 7.0,
        "duration": 102,
        "synopsis": "อย่าจองบ้านพักกับคนแปลกหน้า... เพราะสิ่งที่ซ่อนอยู่ใต้บ้านหลังนี้ น่ากลัวเกินกว่าที่คุณจะจินตนาการได้",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Wednesday",
        "genre": "Horror",
        "rating": 8.0,
        "duration": 105,
        "synopsis": "เรื่องราวสุดลึกลับ ตลกร้าย และเต็มไปด้วยปริศนาฆาตกรรมของลูกสาวคนโตแห่งครอบครัวแอดดัมส์ในโรงเรียนเนเวอร์มอร์",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Talk to me",
        "genre": "Horror",
        "rating": 7.1,
        "duration": 95,
        "synopsis": "แค่มือสตาฟฟ์หนึ่งข้างกับคำพูดไม่กี่คำ ก็เปิดประตูเชื่อมวิญญาณได้... แต่เมื่อลองเล่นกับผี ผลลัพธ์อาจถอยหลังกลับไม่ได้อีกเลย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Tarot",
        "genre": "Horror",
        "rating": 4.8,
        "duration": 92,
        "synopsis": "อย่าใช้ไพ่ยิปซีของคนอื่น! เมื่อการทำนายดวงชะตากลายเป็นคำแช่งมรณะที่ไล่ล่าทีละคน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Ring",
        "genre": "Horror",
        "rating": 7.1,
        "duration": 115,
        "synopsis": "ม้วนเทปปริศนาที่ใครได้ดูจะต้องตายภายใน 7 วัน เว้นแต่คุณจะหาทางส่งต่อความกลัวนี้ไปให้คนอื่น",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Smile",
        "genre": "Horror",
        "rating": 6.5,
        "duration": 115,
        "synopsis": "เมื่อคุณเห็นรอยยิ้มที่ชวนขนหัวลุก นั่นคือสัญญาณเตือนว่าคำสาปสยองกำลังจะมาเอาชีวิตคุณ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Exorcist",
        "genre": "Horror",
        "rating": 8.1,
        "duration": 122,
        "synopsis": "ตำนานความหนาวยกกระดูก เมื่อเด็กหญิงบริสุทธิ์ถูกปีศาจร้ายเข้าสิง และพิธีกรรมไล่ผีคือทางรอดเดียว",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Sinister",
        "genre": "Horror",
        "rating": 6.8,
        "duration": 110,
        "synopsis": "ม้วนฟิล์มสยองที่พบในบ้านใหม่ นำไปสู่ปริศนาฆาตกรรมยกครัวและปีศาจสิงสู่ที่จ้องจับตาดูเด็กๆ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Get Out",
        "genre": "Horror",
        "rating": 7.8,
        "duration": 104,
        "synopsis": "การเดินทางไปเยี่ยมครอบครัวแฟนสาวต่างเชื้อชาติ ที่เริ่มต้นด้วยความอบอุ่น แต่กลับนำไปสู่ฝันร้ายสุดสยองที่คาดไม่ถึง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Insidious",
        "genre": "Horror",
        "rating": 6.8,
        "duration": 103,
        "synopsis": "เมื่อลูกชายเข้าสู่สภาวะโคม่าปริศนา ครอบครัวจึงพบว่าวิญญาณของเขาหลุดไปอยู่ในมิติด้านมืดและถูกสิ่งเร้นลับจ้องจะสิงร่าง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Tomb Raider",
        "genre": "Action",
        "rating": 6.3,
        "duration": 119,
        "synopsis": "การผจญภัยครั้งแรกของ ลาร่า โครฟต์ กับการออกตามหาร่องรอยพ่อที่หายสาบสูญ สู่เกาะปริศนาสุดอันตราย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Avengers:Endgame",
        "genre": "Action",
        "rating": 8.4,
        "duration": 181,
        "synopsis": "บทสรุปแห่งมหาสงครามจักรวาล เมื่อเหล่าฮีโร่ที่เหลือรอดต้องทุ่มเทสุดชีวิตเพื่อย้อนเวลาและกอบกู้ทุกสิ่งที่สูญเสียไป",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Sprider-Man:Brand New Day",
        "genre": "Action",
        "rating": 8.0,
        "duration": 145,
        "synopsis": "การเริ่มต้นใหม่ของไอ้แมงมุมในเส้นทางสายฮีโร่ เมื่อเขาต้องเผชิญกับบททดสอบและศัตรูระลอกใหม่โดยไร้ผู้คนจดจำ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Ghost Rider",
        "genre": "Action",
        "rating": 5.3,
        "duration": 110,
        "synopsis": "ยอมขายดวงวิญญาณให้ปีศาจ เพื่อแลกกับพลังเพลิงมัจจุราชสายพันธุ์ซิ่ง กลางคืนล่าวิญญาณบาปลงขุมนรก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Superman",
        "genre": "Action",
        "rating": 7.0,
        "duration": 129,
        "synopsis": "บุรุษเหล็กผู้มาจากดาวดวงอื่น กับภารกิจแบกรับหวังของมนุษยชาติและปกป้องโลกใบนี้จากภัยมรณะ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Suicide Squad",
        "genre": "Action",
        "rating": 5.9,
        "duration": 123,
        "synopsis": "เมื่อโลกต้องพึ่งพาเหล่าตัวร้ายสายฮาร์ดคอร์ รวมทีมวายร้ายสุดบ้าคลั่งออกทำภารกิจเสี่ยงตายแลกอิสรภาพ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Batman",
        "genre": "Action",
        "rating": 7.5,
        "duration": 126,
        "synopsis": "อัศวินรัตติกาลแห่งเมืองโกธแธม ผู้ออกล่าความยุติธรรมในเงามืดเพื่อกำจัดอาชญากรรมที่กัดกินเมือง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Fast&Furious",
        "genre": "Action",
        "rating": 6.5,
        "duration": 107,
        "synopsis": "เร็ว...แรงทะลุนรก! มหาศึกสายเลือดและสนามแข่งที่เปลี่ยนกลุ่มคนซิ่งให้กลายเป็นครอบครัวสุดแกร่ง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "John Wick",
        "genre": "Action",
        "rating": 7.5,
        "duration": 101,
        "synopsis": "อย่าปลุกสัญชาตญาณนักฆ่า! เมื่ออดีตมือสังหารระดับตำนานต้องกลับมาคิดบัญชีเลือดเพราะสุนัขตัวเดียว",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Deadpool",
        "genre": "Action",
        "rating": 8.0,
        "duration": 108,
        "synopsis": "ฮีโร่สายฮา ปากเสีย และไม่มีวันตาย ออกตามล่าคนที่ทำลายชีวิตเขาเพื่อแก้แค้นให้สุดติ่ง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Jurassic World",
        "genre": "Action",
        "rating": 6.9,
        "duration": 124,
        "synopsis": "สวนสนุกไดโนเสาร์ระดับโลกเปิดบริการอีกครั้ง แต่เมื่อสายพันธุ์พันธุกรรมโหดหลุดออกมา ความบันเทิงจึงกลายเป็นมหันตภัย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "No Time To Die",
        "genre": "Action",
        "rating": 7.3,
        "duration": 164,
        "synopsis": "ภารกิจสุดท้ายของ เจมส์ บอนด์ 007 กับการเผชิญหน้ากับศัตรูตัวฉกาจที่มีเทคโนโลยีฆ่าล้างเผ่าพันธุ์",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "No Body",
        "genre": "Action",
        "rating": 7.4,
        "duration": 92,
        "synopsis": "อย่าตัดสินคนจากภายนอก! เมื่อชายธรรมดาหัวหน้าครอบครัวปลดล็อกอดีตมือสังหารโหดเพื่อปกป้องคนที่เขารัก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Alita",
        "genre": "Action",
        "rating": 7.3,
        "duration": 122,
        "synopsis": "ไซบอร์กสาวผู้สูญเสียความทรงจำ ออกค้นหาตัวตนที่แท้จริงพร้อมปลุกสัญชาตญาณนักสู้สุดแข็งแกร่ง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "2012",
        "genre": "Action",
        "rating": 5.9,
        "duration": 158,
        "synopsis": "วันสิ้นโลกตามคำทำนายโบราณ เมื่อภัยธรรมชาติถล่มล้างมวลมนุษยชาติ ทางรอดเดียวคือการดิ้นรนเอาชีวิตรอด",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Frozen",
        "genre": "Animation",
        "rating": 7.4,
        "duration": 102,
        "synopsis": "การเดินทางสุดมหัศจรรย์ของสองพี่น้องเพื่อปลดล็อกคำสาปหิมะและตามหาความรักที่แท้จริง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Toy Story",
        "genre": "Animation",
        "rating": 8.3,
        "duration": 81,
        "synopsis": "เรื่องราวความผูกพันและมิตรภาพสุดน่ารักของเหล่าของเล่นที่จะมีชีวิตขึ้นมาเมื่อมนุษย์ไม่อยู่",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Coraline",
        "genre": "Animation",
        "rating": 7.8,
        "duration": 100,
        "synopsis": "ปลดล็อกประตูสู่โลกขนานสุดสมบูรณ์แบบ ที่ซ่อนความจริงอันน่าขนลุกไว้ใต้ความอบอุ่น",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Cars",
        "genre": "Animation",
        "rating": 7.3,
        "duration": 116,
        "synopsis": "รถแข่งสุดผยองที่ต้องมาติดอยู่ในเมืองเล็กๆ และได้เรียนรู้ว่าชัยชนะที่แท้จริงไม่ได้อยู่แค่ที่เส้นชัย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Elemental",
        "genre": "Animation",
        "rating": 7.0,
        "duration": 101,
        "synopsis": "เรื่องราวความรักและความแตกต่างในเมืองแห่งธาตุ ที่ซึ่ง ดิน น้ำ ลม และไฟ มาอาศัยอยู่ร่วมกัน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Kang Fu Panda",
        "genre": "Animation",
        "rating": 7.6,
        "duration": 92,
        "synopsis": "แพนด้าอ้วนต้มก๋วยเตี๋ยว โชคชะตาพลิกผันให้กลายเป็นนักรบมังกรผู้ปกป้องยุทธภพ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Boss Baby",
        "genre": "Animation",
        "rating": 6.3,
        "duration": 97,
        "synopsis": "ทารกใส่สูทผูกไทพร้อมภารกิจลับระดับโลก ที่เปลี่ยนชีวิตพี่ชายตัวน้อยไปตลอดกาล",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Good Dinosaur",
        "genre": "Animation",
        "rating": 6.7,
        "duration": 93,
        "synopsis": "ถ้าอุกกาบาตไม่เคยชนโลก มิตรภาพข้ามสายพันธุ์ระหว่างไดโนเสาร์ขี้กลัวกับเด็กมนุษย์จึงเริ่มขึ้น",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "How to Trian Your Dragon",
        "genre": "Animation",
        "rating": 7.7,
        "duration": 125,
        "synopsis": "มิตรภาพอันไกลเกินเอื้อนระหว่างเด็กหนุ่มไวกิ้งกับมังกรไร้พิษภัย ที่จะเปลี่ยนโลกของพวกเขาทั้งสองไปตลอดกาล",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Monsters, Inc.",
        "genre": "Animation",
        "rating": 8.1,
        "duration": 92,
        "synopsis": "พลังงานไฟฟ้าของเมืองได้มาจากเสียงกรีดร้องของเด็กๆ จนกระทั่งมีเด็กหลงเข้ามาในโลกของสัตว์ประหลาด",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Corpse Bride",
        "genre": "Animation",
        "rating": 7.4,
        "duration": 77,
        "synopsis": "ชายหนุ่มผู้โชคร้ายสวมแหวนแต่งงานผิดนิ้ว จนถูกดึงลงสู่โลกหลังความตายโดยเจ้าสาวศพแสนสวย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Tangled",
        "genre": "Animation",
        "rating": 7.7,
        "duration": 100,
        "synopsis": "เจ้าหญิงผมยาวกับจอมขโมยสุดแสบ ออกเดินทางตามหาแสงประทีปปริศนาในวันเกิด",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Moster House",
        "genre": "Animation",
        "rating": 6.7,
        "duration": 91,
        "synopsis": "บ้านหลังเก่าตรงข้ามถนนไม่ใช่แค่บ้านธรรมดา แต่มันคืออสูรกายที่มีชีวิตและจ้องจะกลืนกินทุกคน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Minions",
        "genre": "Animation",
        "rating": 6.4,
        "duration": 91,
        "synopsis": "การตามหาเจ้านายวายร้ายคนใหม่ของเหล่าตัวเหลืองสุดป่วน ก่อนที่เผ่าพันธุ์ของพวกมันจะหมดความหมาย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Ice Age",
        "genre": "Animation",
        "rating": 6.5,
        "duration": 81,
        "synopsis": "การเดินทางของสามแก๊งสัตว์ต่างสายพันธุ์ เพื่อพาเด็กมนุษย์กลับบ้านท่ามกลางยุคน้ำแข็ง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Luca",
        "genre": "Animation",
        "rating": 7.4,
        "duration": 95,
        "synopsis": "ความลับสุดยอดของอสูรกายทะเลตัวน้อยที่อยากขึ้นมาสัมผัสโลกบนบก และมิตรภาพฤดูร้อนในอิตาลี",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Finding Dory",
        "genre": "Animation",
        "rating": 7.0,
        "duration": 106,
        "synopsis": "ปลาขี้ลืมออกเดินทางข้ามมหาสมุทรเพื่อตามหาครอบครัวที่สูญหาย พร้อมความทรงจำที่ค่อยๆ คืนกลับมา",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Zootopia",
        "genre": "Animation",
        "rating": 8.0,
        "duration": 166,
        "synopsis": "กระต่ายตำรวจตัวน้อยกับจิ้งจอกต้มตุ๋น จับมือกันไขคดีปริศนาในเมืองใหญ่ของสัตว์มหานคร",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Lilo & Stitch",
        "genre": "Animation",
        "rating": 6.7,
        "duration": 108,
        "synopsis": "เมื่อเอเลี่ยนตัวป่วนหลบหนีมายังโลก ความรักและคำว่า 'โอฮานะ' จึงเปลี่ยนอสูรกายให้กลายเป็นครอบครัว",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Moana",
        "genre": "Animation",
        "rating": 7.6,
        "duration": 107,
        "synopsis": "สาวน้อยแห่งเกาะแปซิฟิก ออกแล่นเรือข้ามมหาสมุทรตามหาเทพมาวอิ เพื่อกู้วิกฤตบ้านเกิด",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Planes",
        "genre": "Animation",
        "rating": 5.7,
        "duration": 92,
        "synopsis": "เครื่องบินพ่นยาทำเกษตรกรรมผู้กลัวความสูง แต่มีความฝันอยากลงแข่งบินรอบโลก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Turbo",
        "genre": "Animation",
        "rating": 6.4,
        "duration": 96,
        "synopsis": "หอยทากสายสปีดที่ฝันอยากเป็นนักแข่ง และได้รับพลังพิเศษจนได้ลงสนามแข่งระดับโลก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Beauty And The Beast",
        "genre": "Animation",
        "rating": 7.1,
        "duration": 130,
        "synopsis": "ตำนานความรักเหนือกาลเวลา ของหญิงสาวผู้จิตใจดีกับอสูรกายในปราสาทต้องคำสาป",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "La La Land",
        "genre": "Romance",
        "rating": 8.0,
        "duration": 128,
        "synopsis": "บทเพลงแห่งความฝัน ความรัก และการไล่ตามความทะเยอทะยานในเมืองแห่งดวงดาว",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Bridgerton",
        "genre": "Romance",
        "rating": 7.5,
        "duration": 60,
        "synopsis": "เรื่องราวความรัก ชนชั้น และข่าวฉาวสุดแซ่บของตระกูลบริดเจอร์ตันในสังคมไฮโซยุครีเจนซี่",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "10 Things I hate about you",
        "genre": "Romance",
        "rating": 7.4,
        "duration": 97,
        "synopsis": "จากแผนการจีบสาวสุดแสบเพื่อผลประโยชน์ กลับกลายเป็นความรักจริงใจที่ซ่อนอยู่ใต้ความเกลียดชัง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Call Me by Your Name",
        "genre": "Romance",
        "rating": 7.8,
        "duration": 132,
        "synopsis": "ความทรงจำรักฤดูร้อนอันแสนงดงาม ชั่วคราว แต่จะติดอยู่ในใจไปตลอดชีวิต",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Notebook",
        "genre": "Romance",
        "rating": 7.8,
        "duration": 123,
        "synopsis": "ตำนานรักปักใจข้ามกาลเวลาและชนชั้น ที่ผ่านพ้นทั้งอุปสรรค สงคราม และโรคร้าย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Nothing Hill",
        "genre": "Romance",
        "rating": 7.2,
        "duration": 124,
        "synopsis": "เมื่อซูเปอร์สตาร์สาวระดับโลก หลงรักเจ้าของร้านหนังสือธรรมดาๆ ในเมืองเล็ก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Titanic",
        "genre": "Romance",
        "rating": 8.0,
        "duration": 194,
        "synopsis": "ตำนานรักแท้เหนือกาลเวลา ของชายหนุ่มไร้พกกับหญิงสาวสูงศักดิ์ บนเรือมรณะที่ไม่มีวันจม",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Romeo&Juliet",
        "genre": "Romance",
        "rating": 6.7,
        "duration": 120,
        "synopsis": "โศกนาฏกรรมความรักอันอมตะของสองสายเลือดที่ไม่ถูกกัน แต่หัวใจกลับผูกพันเกินกว่าจะแยกจาก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "500 Days of Summer",
        "genre": "Romance",
        "rating": 7.6,
        "duration": 95,
        "synopsis": "เรื่องราวความรัก 500 วันที่ไม่ใช่เรื่องรักหวานชวนฝัน แต่คือบทเรียนชีวิตที่จะเปลี่ยนมุมมองของคุณ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "After",
        "genre": "Romance",
        "rating": 5.3,
        "duration": 105,
        "synopsis": "เด็กสาวผู้เรียบร้อยและมีอนาคตไกล ต้องเผชิญกับบทเรียนความรักสุดทรมานและเร่าร้อนเมื่อพบกับชายหนุ่มสายลุยสุดอันตราย",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Test",
        "genre": "Romance",
        "rating": 2.9,
        "duration": 80,
        "synopsis": "บททดสอบหัวใจและความสัมพันธ์ ที่จะพิสูจน์ว่าความรักของพวกเขาแข็งแกร่งพอจะผ่านมันไปได้หรือไม่",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Throught my Window",
        "genre": "Romance",
        "rating": 5.5,
        "duration": 116,
        "synopsis": "การแอบมอง neighbor สุดหล่อผ่านหน้าต่าง นำไปสู่ความสัมพันธ์แสนเร่าร้อนเกินกว่าจะถอนตัว",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Last Summer",
        "genre": "Romance",
        "rating": 5.6,
        "duration": 110,
        "synopsis": "ฤดูร้อนสุดท้ายก่อนก้าวเข้าสู่วิทยาลัย ช่วงเวลาแห่งการไขว่คว้าความฝัน ความรัก และการค้นพบตัวเอง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "One of Them Days",
        "genre": "Comedy",
        "rating": 6.5,
        "duration": 97,
        "synopsis": "เมื่อสองเพื่อนซี้ต้องหาเงินจ่ายค่าเช่าบ้านให้ทันก่อนสิ้นวัน ความวายป่วงและมหกรรมดิ้นรนสุดติ่งจึงเริ่มต้นขึ้น",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Death At a Funeral",
        "genre": "Comedy",
        "rating": 7.3,
        "duration": 90,
        "synopsis": "พิธีศพสุดอลหม่าน เมื่อความลับสุดพิสดารของผู้ตายถูกเปิดเผย ท่ามกลางความวุ่นวายของเหล่าญาติป่วน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Wolf of Wall Street",
        "genre": "Comedy",
        "rating": 8.2,
        "duration": 180,
        "synopsis": "ชีวิตสุดเหวี่ยง เงินทอง ความโลภ และความวินาศสันตโรของโบรกเกอร์หุ้นระดับตำนาน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Nice Guys",
        "genre": "Comedy",
        "rating": 7.4,
        "duration": 116,
        "synopsis": "สองนักสืบต่างขั้ว สายลุยสุดโหดกับสายปอดแหก ต้องจับมือกันไขคดีคดีคนหายสุดป่วนในยุค 70s",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "21 Jump Street",
        "genre": "Comedy",
        "rating": 7.2,
        "duration": 109,
        "synopsis": "สองตำรวจหน้าใหม่สุดห่วย ต้องปลอมตัวเป็นนักเรียนไฮสคูลเพื่อแฝงตัวเข้าไปแฉขบวนการค้ายา",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "HarryPotter&the Philosospher's stone",
        "genre": "Fantasy",
        "rating": 7.7,
        "duration": 152,
        "synopsis": "ก้าวแรกสู่โลกเวทมนตร์ของเด็กชายผู้รอดชีวิต กับการออกตามหาปริศนาศิลาอาถรรพ์",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Lord of the Rings Trilogy",
        "genre": "Fantasy",
        "rating": 8.9,
        "duration": 178,
        "synopsis": "มหากาพย์การเดินทางของฮอบบิทตัวน้อยเพื่อทำลายแหวนครองภพและปกป้องมัชฌิมโลก",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Avatar",
        "genre": "Fantasy",
        "rating": 7.9,
        "duration": 162,
        "synopsis": "การผจญภัยสุดตระการตาบนดาวแพนดอร่า ที่ซึ่งชายคนหนึ่งต้องเลือกระหว่างหน้าที่และความรักต่อโลกใบใหม่",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Alice in Wonderland",
        "genre": "Fantasy",
        "rating": 6.4,
        "duration": 108,
        "synopsis": "พลัดตกสู่อุโมงค์กระต่าย เข้าสู่แดนมหัศจรรย์สุดเพี้ยนที่ทุกสิ่งเป็นไปได้และไม่มีใครเหมือนเดิม",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Maleficient",
        "genre": "Fantasy",
        "rating": 6.9,
        "duration": 97,
        "synopsis": "เบื้องหลังตำนานที่ไม่เคยถูกบอกเล่า ของนางฟ้าปีศาจผู้ถูกทรยศจนหัวใจกลายเป็นหิน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Peter Pan",
        "genre": "Fantasy",
        "rating": 6.8,
        "duration": 113,
        "synopsis": "บินสู่เนเวอร์แลนด์ ดินแดนแห่งจินตนาการและการผจญภัยอันไม่มีวันแก่ชรา",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Pan's Labyrinth",
        "genre": "Fantasy",
        "rating": 8.2,
        "duration": 119,
        "synopsis": "เทพนิยายสายมืดท่ามกลางสงคราม เมื่อเด็กหญิงตัวน้อยต้องผ่านบททดสอบสุดสยองใน เขาวงกตปริศนา",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Wonka",
        "genre": "Fantasy",
        "rating": 6.9,
        "duration": 117,
        "synopsis": "จุดเริ่มต้นก่อนจะมาเป็นโรงงานช็อกโกแลตสุดอัศจรรย์ กับความฝันสุดยิ่งใหญ่ของ วิลลี่ วองก้า",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Wicked",
        "genre": "Fantasy",
        "rating": 7.3,
        "duration": 160,
        "synopsis": "เรื่องราวความสัมพันธ์อันลึกซึ้งที่ไม่เคยเปิดเผย ของสองแม่มดแห่งดินแดนออส ก่อนที่โลกจะรู้จักพวกเธอ",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Vampire Twilight",
        "genre": "Fantasy",
        "rating": 5.4,
        "duration": 122,
        "synopsis": "เมื่อรักแรกของเธอคือแวมไพร์ ความรักระหว่างมนุษย์กับอมนุษย์ที่ต้องแลกด้วยอันตรายถึงชีวิต",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Halloween",
        "genre": "Thriller",
        "rating": 7.7,
        "duration": 91,
        "synopsis": "การกลับมาของเพชฌฆาตหน้าหน้ากากมัจจุราช ไมเคิล ไมเออร์ส และการเผชิญหน้าครั้งสุดท้ายที่สะสมความแค้นมากว่า 40 ปี",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Terrifier",
        "genre": "Thriller",
        "rating": 5.5,
        "duration": 85,
        "synopsis": "อาร์ต เดอะ คลวน์ ตัวตลกโหดกระหายเลือด ออกไล่ล่าฆ่าเหยื่ออย่างวิปริตและสยดสยองไร้ความปรานีในคืนฮาโลวีน",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "You",
        "genre": "Thriller",
        "rating": 7.6,
        "duration": 45,
        "synopsis": "เมื่อความรักกลายเป็นการเสพติดและสะกดรอย... ชายหนุ่มเสน่ห์แรงผู้ทำทุกอย่างเพื่อได้ครอบครองคนที่เขาหลงใหล",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Shark Frenzy",
        "genre": "Thriller",
        "rating": 2.6,
        "duration": 82,
        "synopsis": "เรืออับปางกลางมหาสมุทร ฝูงฉลามขาวคลั่งล้อมรอบ... การดิ้นรนเอาชีวิตรอดของกลุ่มคนที่ต้องหนีจากการเป็นอาหารทะเล",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Saw",
        "genre": "Thriller",
        "rating": 7.6,
        "duration": 103,
        "synopsis": "คุณจะยอมแลกอวัยวะชิ้นไหนเพื่อรักษาชีวิต? เกมแค้นทรมานสุดโหดจากจิ๊กซอว์ที่จะทดสอบสัญชาตญาณการเอาชีวิตรอด",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "The Strangers:Pray at Nighy",
        "genre": "Thriller",
        "rating": 5.3,
        "duration": 85,
        "synopsis": "ครอบครัวที่มาพักผ่อนในสวนรถบ้าน ต้องเผชิญกับ 3 ฆาตกรสวมหน้ากากปริศนาที่ออกล่าอย่างไร้เหตุผล",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Texas Chainsaw Massacre",
        "genre": "Thriller",
        "rating": 4.7,
        "duration": 83,
        "synopsis": "เสียงเลื่อยยนต์กรีดร้องลั่นบ้านทรงไทยลุยฝุ่น เมื่อฆาตกรหน้าหนังมนุษย์ เลธเธอร์เฟซ ออกไล่ล่าเหยื่ออย่างโหดเหี้ยม",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Ready or Not",
        "genre": "Thriller",
        "rating": 6.9,
        "duration": 95,
        "synopsis": "เจ้าสาวแสนสวยต้องลงเล่นเกมซ่อนหาในคืนวันแต่งงาน... แต่กฎคือครอบครัวสามีต้องฆ่าเธอให้ได้ก่อนรุ่งเช้า",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    },
    {
        "title": "Thanks Giving",
        "genre": "Thriller",
        "rating": 6.2,
        "duration": 107,
        "synopsis": "หลังเหตุการณ์วุ่นวายในวันแบล็กไฟรเดย์ ฆาตกรในชุดหน้ากากพิลกริมก็ออกสับเหยื่อทีละคนเพื่อจัดงานเลี้ยงวันขอบคุณพระเจ้าสุดสยอง",
        "poster": "https://via.placeholder.com/500x750?text=No+Poster"
    }
]


# ==========================================
# HELPER FUNCTION FOR UI DISPLAY
# ==========================================
def display_movie_on_web(name, genre_movie, rating, duration, synopsis, poster):
    col_img, col_detail = st.columns([1, 3])
    with col_img:
        st.image(poster, use_column_width=True)
    with col_detail:
        st.subheader(name)
        st.write(f"**Genre:** {genre_movie} | **Rating:** ⭐ {rating} | **Duration:** ⏱️ {duration} minutes")
        st.write(f"**Synopsis:** {synopsis}")
    st.divider()

# ==========================================
# FUNCTION 1 : MAIN MENU #check
# ==========================================
def show_menu():
    st.sidebar.header("MAIN MENU")
    
    # รวมข้อความทั้งหมดให้อยู่ในรูปแบบเดียวกัน
    menu_text = (
        "==========================================\n"
        "       MOVIE RECOMMENDATION SYSTEM\n"
        "==========================================\n"
        "1. Find a Movie\n"
        "2. Show All Movies\n"
        "3. Show Highest-Rated Movies\n"
        "4. Show Movies by Genre\n"
        "5. Exit\n"
        "=========================================="
    )
    

    st.code(menu_text, language=None)

# ==========================================
# FUNCTION 2 : CHOOSE GENRE
# ==========================================
def choose_genre():
    choice = st.selectbox(
        "Choose genre:",
        ["1. Horror", "2. Action", "3. Animation", "4. Romance", "5. Comedy", "6. Fantasy", "7. Thriller"]
)
    if "1" in choice:
        genre = "Horror"
    elif "2" in choice:
        genre = "Action"
    elif "3" in choice:
        genre = "Animation"
    elif "4" in choice:
        genre = "Romance"
    elif "5" in choice:
        genre = "Comedy"
    elif "6" in choice:
        genre = "Fantasy"
    elif "7" in choice:
        genre = "Thriller"
    else:
        genre = "Wrong"
    return genre

# ==========================================
# FUNCTION 3 : GET MINIMUM RATING #check
# ==========================================
def get_min_rating():
    st.write("\nRating should be between 0 and 10")
    rating = st.slider("Enter minimum rating :",0.0, 10.0, 7.0, 0.1)
    if rating < 0:
        rating = 0
    elif rating > 10:
        rating = 10
    return rating

# ==========================================
# FUNCTION 4 : GET MAXIMUM DURATION #check
# ==========================================
def get_max_duration():
    duration = st.number_input("Maximum duration (minutes):", min_value=1, value=150)
    if duration < 1:
        duration = 1
    return duration

# ==========================================
# FUNCTION 5 : FIND MOVIES #check
# ==========================================
def find_movies(movie_list, genre, min_rating, max_duration):
    found = 0
    for m in movie_list:
        name = m["title"]
        genre_movie = m["genre"]
        rating = m["rating"]
        duration = m["duration"]
        synopsis = m["synopsis"]
        poster = m["poster"]

        if genre_movie == genre:
            if rating >= min_rating:
                if duration <= max_duration:
                    display_movie_on_web(name, genre_movie, rating, duration, synopsis, poster)
                    found = found + 1
    return found

# ==========================================
# FUNCTION 6 : DISPLAY RESULT#check
# ==========================================
def display_result(found):
    if found == 0:
        st.warning("\nNo movies found.")
        st.warning("Please try different conditions.")
    else:
        print("\n==========================================")
        print("             MOVIE RESULTS")
        print("==========================================")
        st.success(f"Found {found} movie(s).")

# ==========================================
# FUNCTION 7 : SHOW ALL MOVIES#check
# ==========================================
def show_all_movies(movie_list):
    st.subheader("ALL MOVIES")
    number = 1

for m in movie_list:
        name = m["title"]
        genre_movie = m["genre"]
        rating = m["rating"]
        duration = m["duration"]
        synopsis = m["synopsis"]
        poster = m["poster"]

        st.write(f"### {number}.")
        display_movie_on_web(name, genre_movie, rating, duration, synopsis, poster)
        number = number + 1

# ==========================================
# FUNCTION 8 : FIND HIGHEST RATING#check
# ==========================================
def find_highest_rating(movie_list):
    highest = movie_list[0]["rating"]
    for m in movie_list:
        rating = m["rating"]
        if rating > highest:
            highest = rating
    return highest

# ==========================================
# FUNCTION 9 : SHOW HIGHEST-RATED MOVIES#check 
# ==========================================
def show_highest_rated(movie_list):
    highest = find_highest_rating(movie_list)
    st.subheader(f"HIGHEST-RATED MOVIES (⭐ {highest})")

    for m in movie_list:
        name = m["title"]
        genre_movie = m["genre"]
        rating = m["rating"]
        duration = m["duration"]
        synopsis = m["synopsis"]
        poster = m["poster"]

        if rating == highest:
            display_movie_on_web(name, genre_movie, rating, duration, synopsis, poster)
            
# ==========================================
# FUNCTION 10 : SHOW MOVIES BY GENRE
# ==========================================
def show_movies_by_genre(movie_list):
    genre = choose_genre()
    if genre == "Wrong":
        st.error("\nInvalid genre.")
    else:
         if st.button("Show Movies"):
            st.subheader("MOVIE RESULTS")
            found = 0

            for m in movie_list:
                name = m["title"]
                genre_movie = m["genre"]
                rating = m["rating"]
                duration = m["duration"]
                synopsis = m["synopsis"]
                poster = m["poster"]

                if genre_movie == genre:
                    display_movie_on_web(name, genre_movie, rating, duration, synopsis, poster)
                   
                    found = found + 1

            if found == 0:
                st.warning("No movies found.")

# ==========================================
# FUNCTION 11 : FIND MOVIE MENU
# ==========================================

def find_movie_menu(movie_list):

    st.subheader("FIND A MOVIE")

    genre = choose_genre()

    if genre == "Wrong":

        st.error("Invalid genre.")

    else:

        min_rating = get_min_rating()

        max_duration = get_max_duration()

        if st.button("Search Movies"):
            st.subheader("MOVIE RESULTS")
            found = find_movies(
                movie_list,
                genre,
                min_rating,
                max_duration
            )
            display_result(found)

# ==========================================
# FUNCTION 12 : SHOW INFORMATION
# ==========================================

def show_information():
    st.title("🎬 MOVIE RECOMMENDATION SYSTEM")
    st.write("This program helps users find movies based on genre, rating and duration.")
    
    with st.expander("ℹ️ Show Program Technical Info"):
        st.write("The program uses:")
        st.write("- List")
        st.write("- If / Elif / Else")
        st.write("- For Loop")
        st.write("- User-defined Functions")


# ==========================================
# WEB UI (STREAMLIT) - มาแทน while running
# ==========================================

show_information()
show_menu()

choice = st.sidebar.radio(
    "📌 Select Option (1-4):",
    [
        "1. Find a Movie",
        "2. Show All Movies",
        "3. Show Highest-Rated Movies",
        "4. Show Movies by Genre"
    ]
)

st.divider()

if "1" in choice:
    find_movie_menu(movie)
elif "2" in choice:
    show_all_movies(movie)
elif "3" in choice:
    show_highest_rated(movie)
elif "4" in choice:
    show_movies_by_genre(movie)
